from enum import IntEnum, auto
from typing import NewType

Username = NewType("Username", str)


class MessageKind(IntEnum):
    COMPUTER_SAYS_NO = auto()
    HELLO = auto()
    NO_HELLO = auto()
    LFG = auto()

    # Error responses
    MALFORMED = auto()
    TIMEOUT = auto()

    # Skills
    TRAIN_RANGED = auto()
