from typing import List, Optional, Dict
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition

class Chapter13(PhysicsChapter):
    """
    Class Gravitation
    """

    def __init__(self) -> None:
        super.__init__("Gravitation")

        self.var_mapping: Dict[str, str] = {}

        self.equations: List[Equation] = []

        self.definitions: List[Definition] = []

        class Calculate:
            """
            Class holds methods to calculate equations in Chapter 13
            """