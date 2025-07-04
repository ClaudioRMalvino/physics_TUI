from typing import Dict, List, Optional, Tuple
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition
from math import sin, cos, asin, tan, pi, sqrt

# Constants

g: float = 9.82  # gravitational acceleration on Earth [m/s^2]


class Chapter4(PhysicsChapter):
    """
    Chapter on two and three dimensional motion.
    """

    def __init__(self) -> None:
        super().__init__(
            "Motion in Two and Three Dimensions",
            "Study of motion in two and three dimensions.",
        )

        self.var_mapping: Dict[str, str] = {
            "v₀": "v_0",
            "t": "t",
            "x": "x",
            "y": "y",
            "v": "v_f",
            "θ": "theta",
        }

        self.equations: List[Equation] = [
            Equation(
                name="Position vector",
                formula="r(t) = x(t)𝐢̂ + y(t)𝐣̂ + z(t)𝐤̂",
                variables={},
            ),
            Equation(
                name="Displacement vector", formula="Δr = r(t₂) − r(t₁)", variables={}
            ),
            Equation(
                name="Velocity vector",
                formula="v(t) = lim(Δt→0) ((r(t + Δt) − r(t)) / Δt) = dr/dt",
                variables={"Δt": "Elapsed time (s)"},
            ),
            Equation(
                name="Velocity in terms of components",
                formula="v(t) = vₓ(t)𝐢̂ + vᵧ(t)𝐣̂ + v𝓏(t)𝐤̂",
                variables={},
            ),
            Equation(
                name="Velocity components",
                formula="vₓ = dx/dt, vᵧ = dy/dt, v𝓏 = dz/dt",
                variables={},
            ),
            Equation(
                name="Average velocity",
                formula="v_avg = (r(t₂) − r(t₁)) / (t₂ − t₁)",
                variables={},
            ),
            Equation(
                name="Instantaneous acceleration",
                formula="a(t) = lim(Δt→0) ((v(t + Δt) − v(t)) / Δt) = dv/dt",
                variables={},
            ),
            Equation(
                name="Acceleration components",
                formula="a(t) = (d²x/dt²)𝐢̂ + (d²y/dt²)𝐣̂ + (d²z/dt²)𝐤̂",
                variables={},
            ),
            Equation(
                name="Time of Flight",
                formula="T_tot = 2v₀sinθ / g",
                variables={
                    "v₀": "Initial velocity (m/s)",
                    "θ": "Launch angle (degrees)",
                },
                calculation=self.Calculate.time_of_flight,
            ),
            Equation(
                name="Trajectory",
                formula="y = (tanθ)x − (g / (2(v₀cosθ)²))x²",
                variables={
                    "θ": "Launch angle (degrees)",
                    "v₀": "Initial velocity (m/s)",
                    "x": "Position along he x-axis (m)",
                },
                calculation=self.Calculate.trajectory,
            ),
            Equation(
                name="Range",
                formula="R = (v₀²sin2θ) / g",
                variables={
                    "θ": "Launch angle (degrees)",
                    "v₀": "Initial velocity (m/2)",
                },
                calculation=self.Calculate.projectile_range,
            ),
            Equation(
                name="Centripetal acceleration",
                formula="a_c = v² / r",
                variables={"v": "Velocity (m/s)", "r": "Radius (m)"},
                calculation=self.Calculate.centripetal_accel,
            ),
            Equation(
                name="Position vector (uniform cirular motion)",
                formula="r(t) = A cos ωt 𝐢̂ + A sin ωt 𝐣̂",
                variables={
                    "A": "Amplitude (m)",
                    "ω": "Angular frequency (rads/s)",
                    "t": "time (s)",
                },
            ),
            Equation(
                name="Velocity vector (uniform cirular motion)",
                formula="v(t) = dr(t)/dt = −Aω sin ωt 𝐢̂ + Aω cos ωt 𝐣̂",
                variables={
                    "A": "Amplitude (m)",
                    "ω": "Angular frequency (rads/s)",
                    "t": "time (s)",
                },
            ),
            Equation(
                name="Acceleration vector (uniform circular motion)",
                formula="a(t) = dv(t)/dt = −Aω² cos ωt 𝐢̂ − Aω² sin ωt 𝐣̂",
                variables={
                    "A": "Amplitude (m)",
                    "ω": "Angular frequency (rads/s)",
                    "t": "time (s)",
                },
            ),
            Equation(
                name="Tangential acceleration", formula="a(c) = d|v|/dt", variables={}
            ),
            Equation(
                name="Total acceleration",
                formula="a(t) = a_c + a_T",
                variables={
                    "a(c)": "Centripetal acceleration (m/s²)",
                    "a(c)": "Tangential acceleration (m/s²)",
                },
            ),
            Equation(
                name="Position vector in frame",
                formula="r_PS = r_PS' + r_S'S",
                variables={
                    "r(PS')": "Position vector in frame S'",
                    "r(S'S)": "Position vector from the origin of S to the origin of S'",
                },
            ),
            Equation(
                name="Relative velocity equation (two reference frames)",
                formula="v_PS = v_PS' + v_S'S",
                variables={
                    "v(PS')": "Velocity vector in frame S'",
                    "v(S'S)": "Velocity vector between frames S and S'",
                },
            ),
            Equation(
                name="Relative velocity equation (more than two reference frames)",
                formula="v(PC) = v(PA) + v(AB) + v(B)",
                variables={
                    "v(PA)": "Relative velocity between points P and A",
                    "v(AB)": "Relative velocity between points A and B",
                    "v(BC)": "Relative velocity between points B and C",
                },
            ),
            Equation(
                name="Relative acceleration equation",
                formula="a(PS) = a(PS)' + a(S'S)",
                variables={
                    "a(PS)'": "Acceleration vector in frame S'",
                    "a(S'S)": "Acceleration vector between frames S and S'",
                },
            ),
        ]
        self.definitions: List[Definition] = [
            Definition(
                term="acceleration vector",
                meaning="Instantaneous acceleration found by taking \
                    the derivative of the velocity function with respect \
                    to time in unit vector notation.",
            ),
            Definition(
                term="angular frequency",
                meaning="ω, rate of change of an angle with which an object \
                    that is moving on a circular path.",
            ),
            Definition(
                term="centripetal acceleration",
                meaning="Component of acceleration of an object moving in a circle \
                    that is directed radially inward toward the center of the circle.",
            ),
            Definition(
                term="displacement vector",
                meaning="Vector from the initial position to a final position on \
                    a trajectory of a particle.",
            ),
            Definition(
                term="position vector",
                meaning="Vector from the origin of a chosen coordinate system \
                    to the position of a particle in two- or three-dimensional space.",
            ),
            Definition(
                term="projectile motion",
                meaning="Motion of an object subject only to the acceleration of gravity.",
            ),
            Definition(
                term="range",
                meaning="Maximum horizontal distance a projectile travels.",
            ),
            Definition(
                term="reference frame",
                meaning="Coordinate system in which the position, velocity, and acceleration \
                    of an object at rest or moving is measured.",
            ),
            Definition(
                term="relative velocity",
                meaning="Velocity of an object as observed from a particular reference frame, \
                    or the velocity of one reference frame with respect to another reference frame.",
            ),
            Definition(
                term="tangential acceleration",
                meaning="Magnitude of which is the time rate of change of speed. \
                    Its direction is tangent to the circle.",
            ),
            Definition(
                term="time of flight",
                meaning="Elapsed time a projectile is in the air.",
            ),
            Definition(
                term="total acceleration",
                meaning="Vector sum of centripetal and tangential accelerations.",
            ),
            Definition(
                term="trajectory", meaning="Path of a projectile through the air."
            ),
            Definition(
                term="velocity vector",
                meaning="Vector that gives the instantaneous speed and direction of a particle; \
                    tangent to the trajectory.",
            ),
        ]

    class Calculate:
        """
        Class holds methods to calculate equations in chapter 4.
        """

        @staticmethod
        def quadratic_eq(a: float, b: float, c: float) -> Optional[Tuple[float, float]]:
            """
            Function calculates the roots of a quadratic equation ax^2 + bx + c = 0
            accurately in all cases.

            Returns a tuple containing the two roots.
            """

            discriminant: float = b**2 - 4 * a * c

            if discriminant < 0:
                return None

            if b == 0 and c == 0:
                return (0.0, 0.0)

            # Choose the appropriate formula based on the sign of b
            if b >= 0:
                x1: float = (-b - sqrt(discriminant)) / (2 * a)
                x2: float = (2 * c) / (-b - sqrt(discriminant))
            else:
                x1: float = (2 * c) / (-b + sqrt(discriminant))
                x2: float = (-b + sqrt(discriminant)) / (2 * a)

            return (x1, x2)

        @staticmethod
        def time_of_flight(
            v_0: Optional[float] = None,
            theta: Optional[float] = None,
            t: Optional[float] = None,
        ) -> float:
            """
            Function calculates the time of flight of a projectile.
            Can also calculate for desired variable when arg == None and all
            other args have values.

            Args:
                v_0 (Optional[float], optional): initial velocity [m/s]. Defaults to None.
                theta (Optiona[float], optional): launch angle in degree. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """
            if theta is not None:
                # Converts degrees to radians
                theta_radians: float = theta * (pi / 180)
            else:
                raise ValueError(
                    "Cannot solve for theta with this equation. Yields complex numbers. \n Please input a value for theta."
                )

            if t is not None and t < 0:
                raise ValueError("Time cannot be a negative value")

            if v_0 is None:
                # Solves for v_0 (initial velocity)
                return (t * g) / (2.0 * sin(theta_radians))

            return (2 * v_0 * sin(theta_radians)) / g

        @staticmethod
        def trajectory(
            theta: Optional[float] = None,
            v_0: Optional[float] = None,
            x: Optional[float] = None,
            y: Optional[float] = None,
        ) -> float:
            """
            Function calculates the trajectory of a porjectile as function of
            theta, initial velocity, and position along the x axis.
            Can also calculate for desired variable when arg == None and all
            other args have values.

            Args:
                theta (Optional[float], optional): launch angle [degrees]_. Defaults to None.
                v_0 (Optional[float], optional): initial velocity [m/s]_. Defaults to None.
                x (Optional[float], optional): position  along the x-axis [m]. Defaults to None.
                y (Optional[float], optional): position  along the y-axis [m]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if theta is not None:
                # Converts degrees to radians
                theta_radian: float = theta * (pi / 180)
            else:
                raise ValueError(
                    "Cannot solve for theta with this equation. Please input a value for theta."
                )

            if v_0 is None:

                if y == 0:
                    raise ValueError("Division by zero is undefined")

                # Solves for v_0 (initial velocity)
                radicand: float = (g / 2) * (((-(x**2)) / y) + (x / tan(theta_radian)))

                if radicand < 0:
                    raise ValueError(
                        "Radicand cannot be negative. Outputs imaginary number."
                    )

                return sqrt(radicand) / cos(theta_radian)

            if x is None:

                raise ValueError(
                    "Cannot solve for x with this equation. Consider calculating the range."
                )

            if v_0 == 0 or theta == 90 or theta == 270:
                raise ValueError("Division by zero is undefined")

            return tan(theta_radian) * x - (
                (g / (2 * (v_0 * cos(theta_radian)) ** 2)) * (x**2)
            )

        @staticmethod
        def projectile_range(
            r_total: Optional[float] = None,
            v_0: Optional[float] = None,
            theta: Optional[float] = None,
        ) -> float:
            """
            Function calculates the range of a projectile as function of
            theta and initial velocity.
            Can also calculate for desired variable when arg == None and all
            other args have values.

            Args:
                r_total (Optional[float], optional): total range of the projectile. Defaults to None.
                v_0 (Optional[float], optional): initial. Defaults to None.
                theta (Optional[float], optional): theta. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if theta is not None:
                theta_radian: float = theta * (pi / 180.0)

            if v_0 == None:

                if theta == 0.0:
                    raise ValueError("Division by zero is undefined.")

                else:
                    # Solves for v_0
                    radicand: float = (r_total * g) / sin(2 * theta_radian)

                    if radicand < 0:
                        raise ValueError(
                            "Radicand cannot be negative. Outputs imaginary number."
                        )
                    return sqrt(radicand)

            if theta == None:

                if v_0 == 0.0:
                    raise ValueError("Division by zero is undefined.")

                argument: float = (r_total * g) / (v_0**2)

                if argument > 1:
                    raise ValueError(
                        "No real solution exists. Range too large for given velocity."
                    )
                if argument < 0:
                    raise ValueError("Range cannot be negative.")

                # Solves for theta
                return (asin(argument) / 2.0) * (180 / pi)

            return ((v_0**2) * sin(2 * theta_radian)) / g

        @staticmethod
        def centripetal_accel(
            accel: Optional[float] = None,
            velocity: Optional[float] = None,
            radius: Optional[float] = None,
        ) -> float:
            """
            Function calculates the centripetal acceleration of a projectile as function of
            velocity and radius.
            Can also calculate for desired variable when arg == None and all
            other args have values.

            Args:
                accel (Optional[float], optional): centripetal acceleration. Defaults to None.
                velocity (Optional[float], optional): velocity. Defaults to None.
                radius (Optional[float], optional): radius. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if radius <= 0:
                raise ValueError("Radius cannot be less than or equal to zero.")

            if velocity == None:
                radicand: float = accel * radius

                if radicand < 0:
                    raise ValueError(
                        "Radicand cannot be negative. Yields an imaginary number."
                    )

                return sqrt(radicand)

            if radius == None:

                if accel == 0:
                    raise ValueError("Division by zero is undefined.")

                return (velocity**2) / accel

            return (velocity**2) / radius
