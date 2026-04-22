from datetime import datetime


def main() -> None:
    print("Today: ")
    print(datetime.now().strftime("%A"))
    


if __name__ == "__main__":
    main()
