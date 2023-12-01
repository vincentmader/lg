from datetime import datetime as dt
from pathlib import Path
import os, sys

from termcolor import colored


PATH_TO_LOGS = Path("..", "logs")
COLOR = "green"

BOLD = "\033[1m"
NO_BOLD = "\033[0m"


if __name__ == "__main__":

    date = dt.now().strftime("%y-%m-%d")
    time = dt.now().strftime("%H:%M:%S")
    os.system('cls' if os.name == 'nt' else 'clear')
    welcome = BOLD + f"Date: {date}\nTime: {time}\n Log: " + NO_BOLD

    line = input(colored(welcome, COLOR))
    lines = [line]
    while True:
        if line.endswith(":q"):
            sys.exit()
        if line.endswith(":wq"):
            break
        lines.append(line)
        line = input("  >>  ")

    path = Path(PATH_TO_LOGS, f"{date}.org")
    os.makedirs(PATH_TO_LOGS, exist_ok=True)
    with open(path, 'a') as fp:
        content = f"\n\n* {date} {time}\n\n" + '\n'.join(lines)
        fp.write(content)

    n = len(content)
    print(colored(f"Wrote {n} characters to \"{path}\".", COLOR))
