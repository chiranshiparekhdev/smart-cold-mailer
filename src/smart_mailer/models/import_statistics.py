from dataclasses import dataclass

@dataclass(slots=True)
class ImportStatistics:
    total_rows: int
    valid_rows: int
    invalid_rows: int
    duplicates: int