from typing import List, Optional, Dict
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition

class Chapter9(PhysicsChapter):
    """
    Chapter on Linear Momentum and Collisions
    """

    def __init__(self) -> None:
        super().__init__("Linear Momentum and Collisions")

        self.var_mapping: Dict[str, str] = {}

        self.equations: List[Equation] = [
            Equation(
                name="Definiiton of momentum",
                formula="p = mv",
                variables={
                    "p": "Momentum (N*s)",
                    "m": "Mass of the object (kg)",
                    "velocity": "m/s)"
                }
            ),
            Equation(
                name="Impulse",
                formula="J = ∫(t₁ to t₂) F(t)dt  or  J = F(ave) Δt",
                variables={
                    "J": "Impulse (N*s)",
                    "F(t)": "Force as a function of time (N)",
                    "F(ave)": "Average velocity",
                    "Δt": "Elapsed time"
                }
            ),
            Equation(
                name="Impulse-momentum theorem",
                formula="J = Δp",
                variables={
                    "J": "Impulse (N*s)",
                    "Δp": "Change in momentum (N*s)",
                }
            ),
            Equation(
                name="Average force from momentum",
                formula="F = Δp/Δt",
                variables={
                    "F": "Average force (N)",
                    "Δp": "Change in momentum (N*s)",
                    "Δt": "Elapsed time (s)"
                }
            ),
            Equation(
                name="Instantaneous force from momentum",
                formula="F(t) = dp/dt",
                variables={
                    "F(t)": "Instantaneous force (N)",
                    "dp/dt": "The rate of change of momentum with respect \
                        to time (N)"
                }
            ),
            Equation(
                name="Conservation of momentum",
                formula="dp₁/dt + dp₂/dt = 0  or  p₁ + p₂ = constant",
                variables={
                    "p₁": "Momentum from the first object (N*s)",
                    "p₂": "Momentum from the second object (N*s)"
                }
            ),
            Equation(
                name="Generalized conservation of momentum",
                formula="∑(j=1 to N) pⱼ = constant",
                variables={
                    "∑(j=1 to N) pⱼ": "The sum of all momenta in the system"
                }
            ),
            Equation(
                name="Conservation of momentum in two dimensions",
                formula="p₁,ₓ = p₁,ᵢ,ₓ + p₂,ᵢ,ₓ, p₁,ᵧ = p₁,ᵢ,ᵧ + p₂,ᵢ,ᵧ",
            ),
            Equation(
                name="External forces",
                formula="F(ext) = ∑(j=1 to N) dp(j)/dt",
                variables={
                    "F(ext)": "External force (N)",
                    "∑(j=1 to N) dp(j)/dt": "The sum of all the rate of \
                        change of momenta with respect to time in the system"
                }
            ),
            Equation(
                name="Newton's second law for an extended object",
                formula="F = dp(CM)/dt",
                variables={
                    "F": "Force (N)",
                    "dp(CM)/dt": "Rate of change of momentum from the center \
                        of mass with respect to time"
                }
            ),
            Equation(
                name="Acceleration of the center of mass",
                formula="a(CM) = d²/dt² (1/M ∑(j=1 to N) m(j) r(j)) = 1/M ∑(j=1 to N) m(j) a(j)",
                variables={
                    "a(CM)": "Acceleration of the center of mass (m/s²)",
                    "M": "Total mass of the system (kg)",
                    "∑(j=1 to N) m(j) a(j)": "Sum of the product of mass and \
                        acceleration of each individual object in the system"
                }
            ),
            Equation(
                name="Position of the center of mass for a system of particles",
                formula="r(CM) = 1/M ∑(j=1 to N) m(j) r(j)",
                variables={
                    "r(CM)": "Position of the center of mass of the system (m)",
                    "M": "Total mass of the system",
                    "∑(j=1 to N) m(j) r(j)": "Sum of the product of mass and \
                        position of each object in the system"
                }
            ),
            Equation(
                name="Velocity of the center of mass",
                formula="v(CM) = d/dt (1/M ∑(j=1 to N) m_j r_j) \
                    = 1/M ∑(j=1 to N) m(j) v(j)",
                variables={
                    "v(CM)": "Velocity of the center of mass (m/s)",
                    "M": "Total mass of the system (m)",
                    "∑(j=1 to N) m(j) v(j)": "The sum of the product of mass \
                        and velocity of each object in the system"
                }
            ),
            Equation(
                name="Position of the center of mass of a continuous object",
                formula="r(CM) = 1/M ∫ r dm",
            ),
            Equation(
                name="Rocket equation",
                formula="Δv = u ln(m(i)/m)",
                varables={
                    "Δv": "Change of velocity obtained from loss of mass",
                    "u": "Velocity of the gas being exhausted from the rocket",
                    "m(i)": "Initial mass of the rocket (with fuel)",
                    "m": "Mass of the rocket after the fuel has been exhausted"
                }
            )
        ]

        self.definitions: List[Definition] = []
        
        class Calculate:
            """
            Class holds methods to calculate equations in Chapter 9
            """