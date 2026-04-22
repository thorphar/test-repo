from datetime import datetime
import os
from pathlib import Path
import sys
import tkinter as tk


def get_current_day() -> str:
    """Return the current day of the week."""
    return datetime.now().strftime("%A")


def get_current_date() -> str:
    """Return the current date in ISO format."""
    return datetime.now().strftime("%Y-%m-%d")


def get_app_tag() -> str:
    """Return app tag from env or executable name, else 'unset'."""
    env_tag = os.getenv("APP_TAG")
    if env_tag:
        return env_tag

    if getattr(sys, "frozen", False):
        exe_name = Path(sys.executable).stem
        prefix = "current-day-app-"
        if exe_name.startswith(prefix):
            tag = exe_name[len(prefix) :]
            if tag:
                return tag

    return "unset"


def update_label(label: tk.Label) -> None:
    """Update the label with the current day and date."""
    day_name = get_current_day()
    date_value = get_current_date()
    app_tag = get_app_tag()
    label.config(text=f"Today is {day_name} ({date_value}) | Tag: {app_tag}")


def main() -> None:
    app_tag = get_app_tag()
    root = tk.Tk()
    root.title(f"Current Day App ({app_tag})")
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
