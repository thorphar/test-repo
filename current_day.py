from datetime import datetime


def get_current_day() -> str:
    """Return the current day of the week."""
    return datetime.now().strftime("%A")


def main() -> None:
    today = datetime.now()
    day_name = get_current_day()
    print(f"Today is {day_name} ({today:%Y-%m-%d}).")


if __name__ == "__main__":
    main()
