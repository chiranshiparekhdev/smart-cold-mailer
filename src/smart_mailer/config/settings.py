from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Settings:
    smtp_host: str
    smtp_port: int
    email_address: str
    email_password: str
    daily_email_limit: int
    delay_min_seconds: int
    delay_max_seconds: int
    contact_file: Path
    resume_file: Path
    log_file: Path


def load_settings() -> Settings:
    return Settings(
        smtp_host=os.getenv("SMTP_HOST", ""),
        smtp_port=int(os.getenv("SMTP_PORT", 587)),
        email_address=os.getenv("EMAIL_ADDRESS", ""),
        email_password=os.getenv("EMAIL_PASSWORD", ""),
        daily_email_limit=int(os.getenv("DAILY_EMAIL_LIMIT", 25)),
        delay_min_seconds=int(os.getenv("DELAY_MIN_SECONDS", 15)),
        delay_max_seconds=int(os.getenv("DELAY_MAX_SECONDS", 30)),
        contact_file=PROJECT_ROOT
        / os.getenv("CONTACT_FILE", "data/input/contacts.xlsx"),
        resume_file=PROJECT_ROOT
        / os.getenv("RESUME_FILE", "data/attachments/resume.pdf"),
        log_file=PROJECT_ROOT
        / os.getenv("LOG_FILE", "data/output/email_logs.csv"),
    )


settings = load_settings()
