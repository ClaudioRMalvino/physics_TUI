from typing import Dict, List
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition

class Chapter4(PhysicsChapter):
    """
    Chapter on two and three dimensional motion. 
    """

    def __init__(self) -> None:
        super().__init__("Motion in Two and Three Dimensions",
                    "Study of motion in two and three dimensions.")

        self.equations: List[Equation] = [
            Equation(
                name="Position vector",
                formula="r(t) = x(t)𝐢̂ + y(t)𝐣̂ + z(t)𝐤̂",
                variables={}
            ),
            Equation(
                name="Displacement vector",
                formula="Δr = r(t₂) − r(t₁)",
                variables={}
            ),
            Equation(
                name="Velocity vector",
                formula="v(t) = lim(Δt→0) [(r(t + Δt) − r(t)) / Δt] = dr/dt",
                variables={}
            ),
            Equation(
                name="Velocity in terms of components",
                formula="v(t) = vₓ(t)𝐢̂ + vᵧ(t)𝐣̂ + v𝓏(t)𝐤̂",
                variables={}
            ),
            Equation(
                name="Velocity components",
                formula="vₓ = dx/dt, vᵧ = dy/dt, v𝓏 = dz/dt",
                variables={}
            ),
            Equation(
                name="Average velocity",
                formula="v_avg = (r(t₂) − r(t₁)) / (t₂ − t₁)",
                variables={}
            ),
            Equation(
                name="Instantaneous acceleration",
                formula="a(t) = lim(Δt→0) [(v(t + Δt) − v(t)) / Δt] = dv/dt",
                variables={}
            ),
            Equation(
                name="Acceleration components",
                formula="a(t) = (d²x/dt²)𝐢̂ + (d²y/dt²)𝐣̂ + (d²z/dt²)𝐤̂",
                variables={}
            ),
            Equation(
                name="Time of Flight",
                formula="T_tot = 2v₀sinθ / g",
                variables={
                    "v₀": "Initial velocity",
                    "θ": "Launch angle",
                    "g": "Acceleration due to gravity"
                }
            ),
            Equation(
                name="Trajectory",
                formula="y = (tanθ)x − (g / (2(v₀cosθ)²))x²",
                variables={
                    "θ": "Launch angle",
                    "v₀": "Initial velocity",
                    "x": "Position along he x-axis",
                    "g": "Acceleartion due to gravity"
                }
            ),
            Equation(
                name="Range",
                formula="R = (v₀²sin2θ) / g",
                variables={
                    "θ": "Launch angle",
                    "v₀": "Initial velocity",
                    "g": "Acceleartion due to gravity"
                }
            ),
            Equation(
                name="Centripetal acceleration",
                formula="a_c = v² / r",
                variables={
                    "v": "Velocity",
                    "r": "Radius"
                }
            )
        ]
        self.definitions: List[Definition] = [
            Definition(
                term=" vector",
                meaning="Instantaneous acceleration found by taking \
                    the derivative of the velocity function with respect \
                    to time in unit vector notation."
            )
        ]