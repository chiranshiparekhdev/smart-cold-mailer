from dataclasses import dataclass, field
from smart_mailer.models.contact import Contact
from smart_mailer.models.import_error import ImportError
from smart_mailer.models.import_statistics import ImportStatistics

@dataclass(slots=True)
class ImportResult:
    contacts: list[Contact] = field(default_factory=list)
    errors: list[ImportError] = field(default_factory=list)
    statistics: list[ImportStatistics] = field(default_factory=list)