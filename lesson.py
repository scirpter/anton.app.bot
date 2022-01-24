from typing import List
from trainer import Trainer


class Lesson:
    def __init__(self, lessonJson: dict):
        self.title: str = lessonJson.get("title")
        self.puid: str = lessonJson.get("puid")
        self.type: str = lessonJson.get("type")
        self.topic: str = lessonJson.get("parentTopic").get("title")
        self.block: str = lessonJson.get("parentBlock").get("title")
        self.trainersJson: List[Trainer] = lessonJson.get("trainers")
        self.trainers: List[Trainer] = []

    def solveAll(self):
        for trainer in self.trainersJson:
            trainer: Trainer = Trainer(trainer)
            trainer.solve()
            self.trainers.append(trainer)
        return self
