from typing import List, Optional, Dict
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition

class Chapter11(PhysicsChapter):
    """
    Chapter on Angular Momentum
    """

    def __init__(self) -> None:
        super.__init__("Angular Momentum")

        self.var_mapping: Dict[str, str] = {}

        self.equations: List[Equation] = []

        self.definitions: List[Definition] = []

        class Calculate:
            """
            Class holds methods to calculate _summary_equations in Chapter 11
            """

