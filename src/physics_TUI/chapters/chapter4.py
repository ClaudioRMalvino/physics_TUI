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
            ),
            Equation(
                name="Position vector (uniform cirular motion)",
                formula="r(t) = A cos ωt 𝐢̂ + A sin ωt 𝐣̂",
                variables= {
                    "A": "Amplitude",
                    "ω": "Angular frequency",
                    "t": "time"
                }
            ),
            Equation(
                name="Velocity vector (uniform cirular motion)",
                formula="v(t) = dr(t)/dt = −Aω sin ωt 𝐢̂ + Aω cos ωt 𝐣̂",
                variables={
                    "A": "Amplitude",
                    "ω": "Angular frequency",
                    "t": "time"
                }
            ),
            Equation(
                name="Acceleration vector (uniform circular motion)",
                formula="a(t) = dv(t)/dt = −Aω² cos ωt 𝐢̂ − Aω² sin ωt 𝐣̂",
                variables={
                    "A": "Amplitude",
                    "ω": "Angular frequency",
                    "t": "time"
                }
            ),
            Equation(
                name="Tangential acceleration",
                formula="a_T = d|v|/dt",
                variables={}
            ),
                        Equation(
                name="Total acceleration",
                formula="a(t) = a_c + a_T",
                variables={
                    "a_c": "Centripetal acceleration",
                    "a_T": "Tangential acceleration"
                }
            ),
            Equation(
                name="Position vector in frame",
                formula="r_PS = r_PS' + r_S'S",
                variables={
                    "r_PS'": "Position vector in frame S'",
                    "r_S'S": "Position vector from the origin of S to the origin of S'"
                }
            ),
            Equation(
                name="Relative velocity equation (two reference frames)",
                formula="v_PS = v_PS' + v_S'S",
                variables={
                    "v_PS'": "Velocity vector in frame S'",
                    "v_S'S": "Velocity vector between frames S and S'"
                }
            ),
            Equation(
                name="Relative velocity equation (more than two reference frames)",
                formula="v_PC = v_PA + v_AB + v_BC",
                variables={
                    "v_PA": "Relative velocity between points P and A",
                    "v_AB": "Relative velocity between points A and B",
                    "v_BC": "Relative velocity between points B and C"
                }
            ),
            Equation(
                name="Relative acceleration equation",
                formula="a_PS = a_PS' + a_S'S",
                variables={
                    "a_PS'": "Acceleration vector in frame S'",
                    "a_S'S": "Acceleration vector between frames S and S'"
                }
            )

        ]
        self.definitions: List[Definition] = [
            Definition(
                term="acceleration vector",
                meaning="Instantaneous acceleration found by taking \
                    the derivative of the velocity function with respect \
                    to time in unit vector notation."
            ),
                        Definition(
                term="angular frequency",
                meaning="ω, rate of change of an angle with which an object \
                    that is moving on a circular path."
            ),
            Definition(
                term="centripetal acceleration",
                meaning="Component of acceleration of an object moving in a circle \
                    that is directed radially inward toward the center of the circle."
            ),
            Definition(
                term="displacement vector",
                meaning="Vector from the initial position to a final position on \
                    a trajectory of a particle."
            ),
            Definition(
                term="position vector",
                meaning="Vector from the origin of a chosen coordinate system \
                    to the position of a particle in two- or three-dimensional space."
            ),
            Definition(
                term="projectile motion",
                meaning="Motion of an object subject only to the acceleration of gravity."
            ),
            Definition(
                term="range",
                meaning="Maximum horizontal distance a projectile travels."
            ),
            Definition(
                term="reference frame",
                meaning="Coordinate system in which the position, velocity, and acceleration \
                    of an object at rest or moving is measured."
            ),
            Definition(
                term="relative velocity",
                meaning="Velocity of an object as observed from a particular reference frame, \
                    or the velocity of one reference frame with respect to another reference frame."
            ),
            Definition(
                term="tangential acceleration",
                meaning="Magnitude of which is the time rate of change of speed. \
                    Its direction is tangent to the circle."
            ),
            Definition(
                term="time of flight",
                meaning="Elapsed time a projectile is in the air."
            ),
            Definition(
                term="total acceleration",
                meaning="Vector sum of centripetal and tangential accelerations."
            ),
            Definition(
                term="trajectory",
                meaning="Path of a projectile through the air."
            ),
            Definition(
                term="velocity vector",
                meaning="Vector that gives the instantaneous speed and direction of a particle; \
                    tangent to the trajectory."
            )
        ]