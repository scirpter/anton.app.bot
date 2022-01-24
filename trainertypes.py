from enum import Enum


class TrainerTypes(Enum):
    MULTIPLE_CHOICE = "multipleChoice"  # done
    GAP = "gap"  # done
    CONTENT = "content"  # unnecessary
    MULTIPLE_CHOICE_TEXT = "multipleChoiceText"  # done
    TABLE = "table"
    FIND_ALL = "findAll"
    DRAG_SORT = "dragSort"
