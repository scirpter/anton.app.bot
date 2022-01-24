from trainertypes import TrainerTypes
from typing import Dict, List


class Trainer:
    def __init__(self, trainer: dict):
        self.rawType: str = trainer.get("trainer")
        self.type = [t for t in TrainerTypes if t.value == trainer.get("trainer")]
        self.type = self.rawType if not self.type else self.type[0]
        self.atoms: dict | list = trainer.get(
            "atoms"
        )  # type is always list for no-instruction-trainer ("content")
        self.instruction: str | None = trainer.get(
            "instruction"
        )  # dependant, some have instructions some dont.
        self.solutions = [{}]
        self.isNecessary: bool = True
        self.isUnknownType: bool = False

    def solve(self):
        if "content" in self.rawType:
            self.type = self.rawType
            self.isNecessary = False
            pass
        else:

            if (
                self.type == TrainerTypes.MULTIPLE_CHOICE
            ):  # safe to assume that MULTIPLE_CHOICE will always be solved.
                furtherInstruction = f"{self.atoms.get('a')} "
                for solution in self.atoms.get("b"):
                    if solution.startswith("++"):
                        self.solutions.append(
                            {
                                "furtherInstruction": furtherInstruction,
                                "solution": f"@blue:{solution[2:]}@green:".replace(
                                    "<b>", ""
                                ).replace("</b>", ""),
                            }
                        )

            elif (
                self.type == TrainerTypes.MULTIPLE_CHOICE_TEXT
            ):  # safe to assume that MULTIPLE_CHOICE_TEXT will always be solved.
                for atom in self.atoms:
                    if atom.get("a"):
                        furtherInstruction = f"{atom.get('a')} "
                        for solution in atom.get("b"):
                            if solution.startswith("++"):
                                self.solutions.append(
                                    {
                                        "furtherInstruction": furtherInstruction,
                                        "solution": f"@blue:{solution[2:]}@green:".replace(
                                            "<b>", ""
                                        ).replace(
                                            "</b>", ""
                                        ),
                                    }
                                )

            elif (
                self.type == TrainerTypes.GAP
            ):  # safe to assume that GAP will always be solved.
                partial = (
                    self.atoms.get("b")
                    .replace("<b>", "")
                    .replace("</b>", "")
                    .split(" ")
                )
                self.solutions.append(
                    {
                        "furtherInstruction": "",
                        "solution": " ".join(
                            [
                                f"{'@blue:' if word.startswith('((++') or '_' in word else '@green:'}{word.replace('((++', '').replace('_', ' ').replace('))', '').replace('((', '').replace('.', '@green:.')}"
                                for word in partial
                                if not word.endswith("))")
                            ]
                        ),
                    }
                )

            elif self.type == TrainerTypes.TABLE.value:
                self.internalType = TrainerTypes.TABLE.value

            else:
                self.type = self.rawType
                self.isUnknownType = True

        return self
