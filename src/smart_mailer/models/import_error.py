from dataclasses import dataclass

@dataclass(slots=True)
class ImportError:
    row_number: int
    field_name: str
    message: str
    invalid_value: str