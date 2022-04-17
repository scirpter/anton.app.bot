from enum import Enum


class TrainerTypes(Enum):
    MULTIPLE_CHOICE = "multipleChoice"  # done
    GAP = "gap"  # done
    CONTENT = "content"  # unnecessary
    GAP_MULTI = "gapMulti"
    BUTTONS = "buttons"
    MULTIPLE_CHOICE_TEXT = "multipleChoiceText"  # done
    TABLE = "table"
    FIND_ALL = "findAll"
    DRAG_SORT = "dragSort"
    DRAG_GROUP = "dragGroup"
    FIND_WORDS_IN_TEXT = "findWordsInText"
    LIST_MATCH = "listMatch"
    GRAVITY = "gravity"
