from smart_mailer.contacts.contact_reader import ContactReader
from smart_mailer.models.contact import Contact
from pathlib import Path

class ExcelContactReader(ContactReader):
    
    def __init__(self, file_path: Path):
        self.file_path = file_path
    
    def read_contacts(self) -> list[Contact]:
        ...