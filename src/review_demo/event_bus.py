from review_demo.contracts import PaymentCompletedEvent


class EventBus:
    def __init__(self):
        self.published: list[PaymentCompletedEvent] = []

    def publish(self, event: PaymentCompletedEvent) -> str:
        self.published.append(event)
        return f"event-{len(self.published)}"

