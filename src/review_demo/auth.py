class AuthorizationService:
    def __init__(self, account_owners: dict[str, str]):
        self._account_owners = account_owners

    def can_pay(self, user_id: str, account_id: str) -> bool:
        return self._account_owners.get(account_id) == user_id

    def can_refund(self, user_id: str, account_id: str) -> bool:
        return self._account_owners.get(account_id) == user_id

