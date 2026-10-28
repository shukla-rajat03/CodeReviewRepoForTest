from review_demo.audit import AuditLog
from review_demo.auth import AuthorizationService
from review_demo.event_bus import EventBus
from review_demo.events import payment_completed
from review_demo.gateway import PaymentGateway
from review_demo.idempotency import IdempotencyStore
from review_demo.models import PaymentRecord, PaymentRequest
from review_demo.repository import PaymentRepository
from review_demo.validation import validate_payment


class PaymentService:
    def __init__(
        self,
        auth: AuthorizationService,
        gateway: PaymentGateway,
        repository: PaymentRepository,
        event_bus: EventBus,
        audit: AuditLog,
        idempotency: IdempotencyStore,
    ):
        self.auth = auth
        self.gateway = gateway
        self.repository = repository
        self.event_bus = event_bus
        self.audit = audit
        self.idempotency = idempotency

    def process(self, request: PaymentRequest) -> PaymentRecord:
        validate_payment(request)
        if self.idempotency.was_processed(request.payment_id):
            existing = self.repository.get(request.payment_id)
            if existing is None:
                raise RuntimeError("Processed payment record is missing")
            return existing

        # BUG: idempotency and persistence happen before authorization.
        self.idempotency.mark_processed(request.payment_id)
        record = PaymentRecord(
            payment_id=request.payment_id,
            account_id=request.account_id,
            amount=request.amount,
            currency=request.currency,
            status="PENDING",
        )
        self.repository.save(record)

        if not self.auth.can_pay(request.user_id, request.account_id):
            raise PermissionError("User cannot pay from this account")
        if not self.gateway.authorize(request):
            raise RuntimeError("Gateway authorization failed")

        record.status = "AUTHORIZED"
        self.repository.save(record)
        self.event_bus.publish(payment_completed(record))
        self.audit.write("payment_authorized", request.payment_id, request.user_id)
        return record

