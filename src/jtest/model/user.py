from dataclasses import dataclass


@dataclass
class User:
    """ Dataclass representing user """

    id: int
    name: str
