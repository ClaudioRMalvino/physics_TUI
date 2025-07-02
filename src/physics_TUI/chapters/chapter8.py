from typing import List, Optional, Dict
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition

class Chapter8(PhysicsChapter):
    """
    Chapter on Potential Energy and Conservation of Energy
    """

    def __init__(self) -> None:
        super().__init__("Potential Energy and Conservation of Energy")

        self.var_mapping: Dict[str, str] = {}

        self.equations: List[Equation] = [
            Equation(
                name="Difference in gravitational potential energy",
                formula="ΔUαβ = Uβ − Uα = −Wαβ",
                variables={
                    "ΔUαβ": "Change in gravitational potential energy",
                    "Uβ": "Gravitational potential energy at final position",
                    "Uα": "Gravitational potential energy at final position",
                    "Wαβ": "Work done from point α to point β"
                }
            ),
            Equation(
                name="Conservation of Energy",
                formula="Wₙc,αβ = Δ(K + U)αβ = ΔEαβ",
                variables={
                    "0 = Wₙc,αβ": "Non-conservative work",
                    "Δ(K + U)αβ": "The sum of the changes in kinetic energy and potential energy \
                        from α to β.",
                    "ΔEαβ": "The change in energy of the system"
                }
            ),
            Equation(
                name="Work done by a conservative force along a closed path",
                formula="W(closed path) = ∫ F(cons) · dr = 0",
                variables={
                    "F(cons)": "Conservative force"
                }
            ),
            Equation(
                name="Condition for conservative forces in two dimensions",
                formula="(∂F(y)/∂x) = (∂F(x)/∂y)",
                variables={
                    "∂F_y/∂x": "Partial derivative of F(y) with respect to x",
                    "∂F(x)/∂y": "Partial derivative of F(x) with respect to y"
                }
            ),
            Equation(
                name="Conservative force is the negative derivative of the potential energy",
                formula="F(l) = -∂U/∂x(l)",
                variables={
                    "F(l)": "Conservative force",
                    "dU/dx(l)": "Derivative of F(l) with respect to x"
                }
            )
        ]

        self.definitions: List[Definition] = [
            Definition(
                term="conservative force",
                meaning="force that does work independent of path"
            ),
            Definition(
                term="conserved quantity",
                meaning="one that cannot be created or destroyed, but may be transformed between different forms of itself"
            ),
            Definition(
                term="energy conservation",
                meaning="total energy of an isolated system is constant"
            ),
            Definition(
                term="equilibrium point",
                meaning="position where the assumed conservative, net force on a particle, given by the slope of its potential energy curve, is zero"
            ),
            Definition(
                term="exact differential",
                meaning="is the total differential of a function and requires the use of partial derivatives if the function involves more than one dimension"
            ),
            Definition(
                term="mechanical energy",
                meaning="sum of the kinetic and potential energies"
            ),
            Definition(
                term="non-conservative force",
                meaning="force that does work that depends on path"
            ),
            Definition(
                term="non-renewable",
                meaning="energy source that is not renewable, but is depleted by human consumption"
            ),
            Definition(
                term="potential energy",
                meaning="function of position, energy possessed by an object relative to the system considered"
            ),
            Definition(
                term="potential energy diagram",
                meaning="graph of a particle's potential energy as a function of position" 
            ),
            Definition(
                term="potential energy difference",
                meaning="negative of the work done acting between two points in space"
            ),
            Definition(
                term="renewable",
                meaning="energy source that is replenished by natural processes, over human time scales"
            ),
            Definition(
                term="turning point",
                meaning="position where the velocity of a particle, in one-dimensional motion, changes sign"
            ),
        ]


