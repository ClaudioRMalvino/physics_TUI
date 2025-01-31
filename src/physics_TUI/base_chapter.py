from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Equation:
    """Class to represent a physics equation"""
    name: str
    formula: str
    variables: Dict[str, str]  # variable_name: description

@dataclass
class Definition:
    """Class to represent a physics definition"""
    term: str
    meaning: str


class PhysicsChapter:
    """Base class for all physics chapters"""
    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.equations: List[Equation] = []
        self.definitions: List[Definition] = []

    def get_equations(self) -> List[Equation]:
        return self.equations

    def get_definitions(self) -> List[Definition]:
        return self.definitions