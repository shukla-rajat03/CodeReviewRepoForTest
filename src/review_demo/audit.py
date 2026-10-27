from dataclasses import dataclass


@dataclass(frozen=True)
class AuditEntry:
    action: str
    subject_id: str


class AuditLog:
    def __init__(self):
        self.entries: list[AuditEntry] = []

    def write(self, action: str, subject_id: str) -> None:
        self.entries.append(AuditEntry(action=action, subject_id=subject_id))

