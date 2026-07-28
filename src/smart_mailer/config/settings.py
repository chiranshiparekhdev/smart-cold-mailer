import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    SMTP_HOST = os.getenv("SMTP_HOST")

    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")

    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

    DAILY_EMAIL_LIMIT = int(
        os.getenv("DAILY_EMAIL_LIMIT", 25)
    )

    DELAY_MIN_SECONDS = int(
        os.getenv("DELAY_MIN_SECONDS", 15)
    )

    DELAY_MAX_SECONDS = int(
        os.getenv("DELAY_MAX_SECONDS", 30)
    )

    CONTACT_FILE = os.getenv(
        "CONTACT_FILE",
        "data/input/contacts.xlsx"
    )

    RESUME_FILE = os.getenv(
        "RESUME_FILE",
        "data/attachments/resume.pdf"
    )

    LOG_FILE = os.getenv(
        "LOG_FILE",
        "data/output/email_logs.csv"
    )


settings = Settings()