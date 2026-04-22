from datetime import datetime
import tkinter as tk


def get_current_day() -> str:
    """Return the current day of the week."""
    return datetime.now().strftime("%A")


def get_current_date() -> str:
    """Return the current date in ISO format."""
    return datetime.now().strftime("%Y-%m-%d")


def update_label(label: tk.Label) -> None:
    """Update the label with the current day and date."""
    day_name = get_current_day()
    date_value = get_current_date()
    label.config(text=f"Today is {day_name} ({date_value}).")


def main() -> None:
    root = tk.Tk()
    root.title("Current Day App")
    root.geometry("360x140")

    day_label = tk.Label(root, text="Click the button to show today.")
    day_label.pack(pady=16)

    show_button = tk.Button(
        root,
        text="Show Current Day",
        command=lambda: update_label(day_label),
    )
    show_button.pack(pady=8)

    root.mainloop()


if __name__ == "__main__":
    main()
