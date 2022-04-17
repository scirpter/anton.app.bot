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
        self.cats: list = trainer.get(
            "cats"
        )  # a list of categories. only for DRAG_GROUP as far as i know.
        self.instruction: str | None = trainer.get(
            "instruction"
        )  # dependant, some have instructions some dont.
        self.solutions = [{}]
        self.isNecessary: bool = True
        self.isUnknownType: bool = False

    def solve(self) -> "Trainer":
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
                        sol = f"@blue:{solution[2:]}@green:".replace("<b>", "").replace(
                            "</b>", ""
                        )
                        self.solutions.append(
                            {
                                "furtherInstruction": furtherInstruction,
                                "solution": sol.replace("_", " "),
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
                                sol = f"@blue:{solution[2:]}@green:".replace(
                                    "<b>", ""
                                ).replace("</b>", "")
                                self.solutions.append(
                                    {
                                        "furtherInstruction": furtherInstruction,
                                        "solution": sol.replace("_", " "),
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
                sol = " ".join(
                    [
                        f"{'@blue:' if word.startswith('((++') or '_' in word else '@green:'}{word.replace('((++', '').replace('_', ' ').replace('))', '').replace('((', '').replace('.', '@green:.')}"
                        for word in partial
                        if not word.endswith("))")
                    ]
                )
                self.solutions.append(
                    {
                        "furtherInstruction": "",
                        "solution": sol.replace("_", " "),
                    }
                )

            elif self.type == TrainerTypes.GAP_MULTI:
                if type(self.atoms) == dict:
                    sol = " ".join(
                        [
                            f"{'@blue:' if word.startswith('((') else '@green:'}{word.replace('((', '').replace('))', '')}"
                            for word in self.atoms.get("b").split(" ")
                            if not word.startswith("--")
                        ]
                    )
                    self.solutions.append(
                        {
                            "furtherInstruction": "",
                            "solution": sol.replace("_", " "),
                        }
                    )
                elif type(self.atoms) == list:
                    for atom in self.atoms:
                        sol = " ".join(
                            [
                                f"{'@blue:' if word.startswith('((') else '@green:'}{word.replace('((', '').replace('))', '')}"
                                for word in atom.get("b").split(" ")
                                if not word.startswith("--")
                            ]
                        )
                        self.solutions.append(
                            {
                                "furtherInstruction": "",
                                "solution": sol.replace("_", " "),
                            }
                        )

            elif self.type == TrainerTypes.BUTTONS:
                if type(self.atoms) == list:
                    for atom in self.atoms:
                        if "++" in atom.get("b"):
                            sol = " ".join(
                                [
                                    f"{' @blue:' if word.startswith('++') else '@green:'}{word.replace('++', '')}"
                                    for word in atom.get("b").split(" ")
                                    if word.startswith("++")
                                ]
                            )
                            self.solutions.append(
                                {
                                    "furtherInstruction": atom.get("a")
                                    .replace("<b>", "")
                                    .replace("</b>", ""),
                                    "solution": sol.replace("_", " "),
                                }
                            )
                        else:
                            sol = " ".join([f" @blue:{atom.get('b')}"])
                            self.solutions.append(
                                {
                                    "furtherInstruction": atom.get("a")
                                    .replace("<b>", "")
                                    .replace("</b>", ""),
                                    "solution": sol.replace("_", " "),
                                }
                            )

            elif self.type == TrainerTypes.LIST_MATCH:
                ...  # https://content.anton.app/files/?fileId=level%2Fc-natdeu-9%2Ftopic-04-grammatik-satzlehre%2Fblock-01-satzglieder%2Flevel-03&etag=0958-7629

            elif self.type == TrainerTypes.FIND_WORDS_IN_TEXT:
                ...  # https://content.anton.app/files/?fileId=level%2Fc-natdeu-9%2Ftopic-04-grammatik-satzlehre%2Fblock-01-satzglieder%2Flevel-03&etag=0958-7629

            elif self.type == TrainerTypes.GRAVITY:
                ...  # https://anton.app/en_us/learn/deutsch-9-10-klasse/topic-04-grammatik-satzlehre/exercises-01-satzglieder/exercise-01/

            elif self.type == TrainerTypes.TABLE:
                ...  # https://anton.app/en_us/learn/deutsch-9-10-klasse/topic-04-grammatik-satzlehre/exercises-01-satzglieder/exercise-01/

            elif self.type == TrainerTypes.DRAG_GROUP:
                for atom in self.atoms:
                    sol = f" @blue:{self.cats[atom.get('cat')]} -> {atom.get('b')}"
                    self.solutions.append(
                        {
                            "furtherInstruction": self.instruction.get("text"),
                            "solution": sol.replace("_", " "),
                        }
                    )

            else:
                self.type = self.rawType
                self.isUnknownType = True

        return self
