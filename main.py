from smart_mailer.config.settings import settings


def main():

    print("Smart Cold Mailer")

    print(
        f"Daily email limit: {settings.DAILY_EMAIL_LIMIT}"
    )


if __name__ == "__main__":
    main()