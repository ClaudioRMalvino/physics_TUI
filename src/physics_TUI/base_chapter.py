from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional


@dataclass
class Equation:
    """Class to represent a physics equation"""
    name: str
    formula: str
    variables: Dict[str, str]  # variable_name: description
    calculation: Optional[Callable] = None  # optional reference to calculation function

@dataclass
class Definition:
    """Class to represent a physics definition"""
    term: str
    meaning: str



class PhysicsChapter:
    """Base class for all physics chapters"""
    def __init__(self, title: str, description: str = ""):
        self.title: str = title
        self.description: str = description
        self.equations: List[Equation] = []
        self.definitions: List[Definition] = []
        self.var_mapping: Dict[str, str] = {} 
    

    def get_equations(self) -> List[Equation]:
        """Returns the list of equations within the class"""
        return self.equations

    def get_definitions(self) -> List[Definition]:
        """Returns the list of definitions within the class"""
        return self.definitions

    def get_calculable_equations(self) -> List[Equation]:
        """Returns the list of equations that have calculation functions"""
        return [eq for eq in self.equations if eq.calculation is not None]
