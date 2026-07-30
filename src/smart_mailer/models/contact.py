from dataclasses import dataclass

@dataclass(slots=True)
class Contact:
    id: int
    name: str
    email: str
    title: str