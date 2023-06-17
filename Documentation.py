"""This script is used to generate the documentation for the Wheel of Fortune game."""

import os
import subprocess
import pydoc


def main():
    path = os.getcwd()
    print(path)
    # generate_documentation for game_board.py
    subprocess.run(['pydoc', r"C:\Users\sells\PycharmProjects\anthony_steve_wheel_of_fortune\Wheel_of_Fortune_using_run_screen.py"],
                         stdout=subprocess.PIPE, text=True)


if __name__ == "__main__":
    main()
