from datetime import datetime as dt
from pathlib import Path
import os

from termcolor import colored


PATH_TO_LOGS = Path("..", "logs")
COLOR = "green"


if __name__ == "__main__":

    date = dt.now().strftime("%Y-%m-%d")
    time = dt.now().strftime("%H:%M:%S")
    os.system('cls' if os.name == 'nt' else 'clear')
    welcome = f"Date: {date}\nTime:   {time}\nLog: "

    lines = [input(colored(welcome, COLOR))]
    while True:
        line = input(">> ")
        if line == ":wq":
            break
        lines.append(line)

    path = Path(PATH_TO_LOGS, f"{date}.org")
    os.makedirs(PATH_TO_LOGS, exist_ok=True)
    with open(path, 'a') as fp:
        content = f"\n\n* {date} {time}\n\n" + '\n'.join(lines)
        fp.write(content)

    n = len(content)
    print(colored(f"Wrote {n} characters to \"{path}\"", COLOR))
