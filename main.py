"""A anton.app autocompleter, coded in a brainfuck fashion.

@author: Nyaanity
"""


from requests import request
from lesson import Lesson
from datetime import datetime
import os


class Console:
    def __init__(self):
        pass

    @property
    def time(self) -> str:
        return datetime.now().strftime("%H:%M:%S")

    def toOsColor(self, value: int = 249) -> str:
        return f"\033[38;5;{value}m"

    def doClear(self) -> "Console":
        os.system("cls" if os.name == "nt" else "clear")
        return self

    def write(
        self, label: str, text: str, top_level_color: int = "@gray:"
    ) -> "Console":
        print(
            (
                (
                    f"{top_level_color}[{self.time}] "
                    f"[{label}] "
                    f"{text}{self.toOsColor()}"
                )
            )
            .replace("@red:", self.toOsColor(52))
            .replace("@gray:", self.toOsColor(242))
            .replace("@dark-green:", self.toOsColor(100))
            .replace("@green:", self.toOsColor(78))
            .replace("@yellow:", self.toOsColor(226))
            .replace("@blue:", self.toOsColor(33))
            .replace("@pink:", self.toOsColor(135))
        )
        return self

    def writeDeath(self, text: str, top_level_color: int = "@red:") -> "Console":
        print(
            (f"{top_level_color}{text}{self.toOsColor()}")
            .replace("@red:", self.toOsColor(52))
            .replace("@gray:", self.toOsColor(242))
            .replace("@dark-green:", self.toOsColor(100))
            .replace("@green:", self.toOsColor(78))
            .replace("@yellow:", self.toOsColor(226))
            .replace("@blue:", self.toOsColor(33))
            .replace("@pink:", self.toOsColor(135))
        )
        return self

    def inp(self, text: str, top_level_color: int = "@gray:") -> "Console":
        return input(
            (
                (
                    f"{top_level_color}[{self.time}] "
                    f"[Input] "
                    f"{text}{self.toOsColor()}"
                )
            )
            .replace("@red:", self.toOsColor(52))
            .replace("@gray:", self.toOsColor(242))
            .replace("@dark-green:", self.toOsColor(100))
            .replace("@green:", self.toOsColor(78))
            .replace("@yellow:", self.toOsColor(226))
            .replace("@blue:", self.toOsColor(33))
            .replace("@pink:", self.toOsColor(135))
        )


def main() -> None:
    while 1:
        lessonUrl = console.inp("Lesson URL: ", top_level_color="@pink:")
        try:
            req = request("GET", lessonUrl)
            lessonJson = req.json()
        except:
            console.write("Error", "Invalid URL. You might wanna grab the level URL from dev tools instead? Here, an example: https://content.anton.app/files/?fileId=level%2Fc-natdeu-9%2Ftopic-04-grammatik-satzlehre%2Fblock-01-satzglieder%2Flevel-03&etag=0958-7629", top_level_color="@red:")
            continue
        lesson: Lesson = Lesson(lessonJson)
        console.write(
            "Autocomplete",
            f"Found lesson @red:{lesson.puid} @gray:of type {lesson.type}: {lesson.title}. Topic: {lesson.topic}. Block: {lesson.block}.",
        )

        console.writeDeath(
            f"\n\n{'-'*5} LESSON RESULT ({lesson.puid}) {'-'*5}",
            top_level_color="@gray:",
        )
        solvedTrainers = lesson.solveAll().trainers
        for i in range(len(solvedTrainers)):
            if solvedTrainers[i].isUnknownType:
                console.writeDeath(
                    f"{i+1}) Can't solve trainer of unknown type {solvedTrainers[i].type}.",
                    top_level_color="@red:",
                )
            elif solvedTrainers[i].isNecessary:
                console.writeDeath(
                    f"{i+1}) {'     @green:     '.join(['{}{}'.format(package.get('furtherInstruction'), package.get('solution')) for package in solvedTrainers[i].solutions if package.get('solution')])}",
                    top_level_color="@green:",
                )
            else:
                console.writeDeath(
                    f"{i+1}) Unnecessary trainer of type {solvedTrainers[i].type} ignored.",
                    top_level_color="@red:",
                )
        console.writeDeath(
            f"{'-'*42}\n\n",
            top_level_color="@gray:",
        )


if __name__ == "__main__":
    console = Console()
    console.doClear()
    os.system("title anton.app@autocompleter")
    console.write("Init", "kekkin-anton.app-autocomplete @red:@0.0.1")
    main()
