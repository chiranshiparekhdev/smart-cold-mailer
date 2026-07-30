from abc import ABC, abstractmethod
from smart_mailer.models.contact import Contact

class ContactReader(ABC):

    @abstractmethod
    def read_contacts(self) -> list[Contact]:
        ...