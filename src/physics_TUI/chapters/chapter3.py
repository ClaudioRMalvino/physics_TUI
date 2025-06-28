from typing import Dict, List, Tuple, Optional
from math import sqrt
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition

# Constant
g: float = -9.82  # gravitational acceleration on Earth [m/s^2]


class Chapter3(PhysicsChapter):
    """
    Chapter on one-dimensional motion.
    """

    def __init__(self) -> None:
        super().__init__(
            "Motion Along a Straight Line", "Study of motion along one dimension."
        )

        self.var_mapping: Dict[str, str] = {
            "x₀": "x_0",
            "v₀": "v_0",
            "t": "t",
            "a": "accel",
            "x": "x_f",
            "y₀": "y_0",
            "y": "y_f",
            "v": "v_f",
        }

        self.equations: List[Equation] = [
            Equation(
                name="Displacement",
                formula="Δx = x - x₀",
                variables={
                    "x": "Final position (m)",
                    "x₀": "Initial position (m)",
                },
            ),
            Equation(
                name="Total Displacement",
                formula="Δx = ∑Δxᵢ",
                variables={"Δxᵢ": "All steps taken"},
            ),
            Equation(
                name="Average velocity (constant acceleration)",
                formula="v = Δx/Δt = (x - xᵢ)/(t - tᵢ)",
                variables={"Δx": "Displacement in direction (m)", 
                "Δt": "Elapsed time (s)"
                },
            ),
            Equation(
                name="Instantaneous velocity", formula="v(t) = dx(t)/dt", variables={}
            ),
            Equation(
                name="Average speed",
                formula="s = (Total distance)/(Elapsed time)",
                variables={},
            ),
            Equation(name="Instantaneous speed", formula="|v(t)|", variables={}),
            Equation(
                name="Average acceleration",
                formula="a = Δv/Δt",
                variables={"Δv": "Change in velocity (m/s)", "Δt": "Elapsed time (s)"},
            ),
            Equation(
                name="Instantaneous acceleration",
                formula="a(t) = dv(t)/dt",
                variables={},
            ),
            Equation(
                name="Position from avg. velocity",
                formula="x(t) = x₀ + vt",
                variables={
                    "x₀": "Initial position (m)",
                    "v": "Average velocity (m/s)",
                    "t": "time (s)",
                },
            ),
            Equation(
                name="Velocity from acceleration",
                formula="v(t) = v₀ + at",
                variables={"v₀": "Initial velocity (m/s)", "a": "Acceleration (m/s²)"},
            ),
            Equation(
                name="Position from velocity and acceleration",
                formula="x(t) = x₀ + v₀t + (1/2)at²",
                variables={
                    "x₀": "Initial position (m)",
                    "v₀": "Intiial velocity (m/s)",
                    "t": "Time (s)",
                    "a": "Acceleration (m/s²)",
                    "x": "Final Position (m)",
                },
                calculation=self.Calculate.positionFromVelAndAcc,
            ),
            Equation(
                name="Velocity from distance",
                formula="v² = v₀² + 2a(x - x₀)",
                variables={
                    "x": "Final position (m)",
                    "x₀": "Initial position (m)",
                    "v₀": "Intiial velocity (m/s)",
                    "a": "Acceleration (m/s²)",
                    "v": "Final velocity (m/s)",
                },
                calculation=self.Calculate.velocityFromDistance,
            ),
            Equation(
                name="Velocity of free fall",
                formula="v = v₀ - gt",
                variables={
                    "v₀": "Initial velocity (m/s)",
                    "t": "Time (s)",
                },
            ),
            Equation(
                name="Height of free fall",
                formula="y(t) = y₀ + v₀t - (1/2)gt²",
                variables={
                    "y₀": "Initial height (m)",
                    "v₀": "Initial velocity (m/s)",
                    "t": "Time (s)",
                    "y": "Final Position (s)",
                },
                calculation=self.Calculate.heightOfFreeFall,
            ),
            Equation(
                name="Velocity of free fall from height",
                formula="v² = v₀² - 2g(y - y₀)",
                variables={
                    "y": "Final height (m)",
                    "y₀": "Initial height (m)",
                    "v₀": "Initial velocity (m/s)",
                    "v": "Final velocity (m/s)",
                },
                calculation=self.Calculate.velFreeFallFromHeight,
            ),
            Equation(
                name="Velocity from acceleration",
                formula="v(t) = ∫ a(t)dt + C₁",
                variables={},
            ),
            Equation(
                name="Position from velocity",
                formula="x(t) = ∫ V(t)dt + C₂",
                variables={},
            ),
        ]

        self.definitions: List[Definition] = [
            Definition(
                term="acceleration due to gravity",
                meaning="acceleration of an object as a result of gravity",
            ),
            Definition(
                term="average acceleration",
                meaning="the rate of change in velocity; the change in velocity over time",
            ),
            Definition(
                term="average speed",
                meaning="the total distance traveled divided by elapsed time",
            ),
            Definition(
                term="average velocity",
                meaning="the displacement divided by the time over which displacement occurs under constant acceleration",
            ),
            Definition(
                term="displacement", meaning="the change in position of an object"
            ),
            Definition(
                term="distance traveled",
                meaning="the total length of the path traveled between two positions",
            ),
            Definition(
                term="elapsed time",
                meaning="the difference between the ending time and the beginning time",
            ),
            Definition(
                term="free fall",
                meaning="the state of movement that results from gravitational force only",
            ),
            Definition(
                term="instantaneous acceleration",
                meaning="acceleration at a specific point in time",
            ),
            Definition(
                term="instantaneous speed",
                meaning="the absolute value of the instantaneous velocity",
            ),
            Definition(
                term="instantaneous velocity",
                meaning="the velocity at a specific instant or time point",
            ),
            Definition(
                term="kinematics",
                meaning="the description of motion through properties such as position, time, velocity, and acceleration",
            ),
            Definition(
                term="position",
                meaning="the location of an object at a particular time",
            ),
            Definition(
                term="total displacement",
                meaning="the sum of individual displacements over a given time period",
            ),
            Definition(
                term="two-body pursuit problem",
                meaning="a kinematics problem in which the unknowns are calculated by solving the kinematic equations simultaneously for two moving objects",
            ),
        ]

    class Calculate:
        """
        Class holds methods to calculate equations in Chapter 3
        """

        @staticmethod
        def quadratic_eq(a: float, b: float, c: float) -> Optional[Tuple[float, float]]:
            """
            Function calculates the roots of a quadratic equation ax^2 + bx + c = 0
            accurately in all cases.

            Returns a tuple containing the two roots.
            """

            discriminant: float = (b * b) - 4 * a * c

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
        def positionFromVelAndAcc(
            x_0: Optional[float] = None,
            v_0: Optional[float] = None,
            t: Optional[float] = None,
            accel: Optional[float] = None,
            x_f: Optional[float] = None,
        ) -> float:
            """
            Calculates position from velocity and acceleration.
            Can also calculate for desired variable when arg == None and all
            other args have values.

            Args:
                x_0 (float, optional): Initial position [m]. Defaults to None.
                v_0 (float, optional): Initial velocity [m/s]. Defaults to None.
                t (float, optional): Elapsed time [s]. Defaults to None.
                accel (float, optional): Constant acceleration [m/s^2]. Defaults to None.
                x_f (float, optional): Final position [m]. Defaults to None.
            """
            if t is not None and t < 0:
                raise ValueError("Time cannot be a negative value")

            if x_0 is None:
                # Solves for x_0 (initial position)
                return round(x_f - (v_0 * t) - (0.5 * accel * (t*t)), 4)

            if v_0 is None:
                if t == 0:
                    raise ValueError("Division by zero is undefined")
                    
                # Solves for v_0 (initial velocity)
                return round((x_f - x_0 - (0.5 * accel * (t * t))) / t, 4)

            if t is None:
                # Solves for t (elapsed time)
                if accel == 0 and v_0 == 0:
                    raise ValueError("v₀ and a cannot both be equal to zero")

                c: float = x_0 - x_f
                b: float = v_0
                a: float = 0.5 * accel
                roots: Tuple[float, float] = Chapter3.Calculate.quadratic_eq(a, b, c)

                if roots[0] < 0:
                    return round(roots[1], 4)
                if roots[1] < 0:
                    return round(roots[0], 4)

            if (
                accel is None
                and x_0 is not None
                and v_0 is not None
                and t is not None
                and x_f is not None
            ):
                if t == 0:
                    raise ValueError("Divison by zero is undefined.")

                return round( (x_f - x_0 - (v_0 * t) ) * (2 / (t * t)), 4)

            # Solves for x_f (final position)

            return round((x_0 + (v_0 * t) + (0.5 * accel * (t * t))), 4)

        @staticmethod
        def velocityFromDistance(
            x_0: Optional[float] = None,
            v_0: Optional[float] = None,
            accel: Optional[float] = None,
            x_f: Optional[float] = None,
            v_f: Optional[float] = None,
        ) -> float:
            """
            Calculates final velocity as a function of displacement, acceleration,
            and initial velocity.
            Can also calculate for desired variable when arg == None and all
            other args have values.

            Args:
                x_0 (Optional[float], optional): initial position [m]. Defaults to None.
                v_0 (Optional[float], optional): initial velocity [m/s]. Defaults to None.
                accel (Optional[float], optional): constant acceleration [m/s^2]. Defaults to None.
                x_f (Optional[float], optional): final position [m]. Defaults to None.
                v_f (Optional[float], optional): finasl velocity [m/s^2]. Defaults to None.

            Returns:
                float: value of whichever argument was left set to None.
            """
            if x_0 is None:
                # Solves for x_0 (initial position)

                if accel == 0:
                    raise ValueError("acceleration cannot be equal to zero")

                return round(-((((v_f * v_f) - (v_0 * v_0)) / (2 * accel)) - x_f), 4)

            if v_0 is None:
                # Solves for v_0 (initial velocity)
                discriminant: float = (v_f * v_f) - (2 * accel * (x_f - x_0))

                if discriminant < 0:
                    raise ValueError("The discriminant cannot be negative")

                return round(sqrt(discriminant), 4)

            if accel is None:
                # Solves for acceleration

                if x_f == 0 and x_0 == 0:
                    raise ValueError("x_f and x_0 cannot both be equal to zero")

                return round(((v_f * v_f) - (v_0 * v_0)) / (2 * (x_f - x_0)), 4)

            if x_f is None:
                # Solves for x_f (final position)

                if accel == 0:
                    raise ValueError("acceleration cannot be equal to zero")

                return round((((v_f*v_f) - (v_0*v_0)) / (2 * accel)) - x_0, 4)

            discriminant: float = (v_0*v_0) + 2 * accel * (x_f - x_0)

            if discriminant < 0:
                raise ValueError("The discriminant cannot be negative")

            # Returns v_f (final velocity)
            return round(sqrt(discriminant), 4)

        @staticmethod
        def heightOfFreeFall(
            y_0: Optional[float] = None,
            v_0: Optional[float] = None,
            t: Optional[float] = None,
            y_f: Optional[float] = None,
        ) -> float:
            """
            Calculates height as a function of time, initial velocity,
            and initial position.
            """
            if t is not None and t < 0:
                raise ValueError("Time cannot be a negative value")

            if y_0 is None:
                # Solves for y_0 (initial position)
                return round(y_f - (v_0 * t) - (0.5 * g * (t*t)), 4)

            elif v_0 is None:
                # Solves for v_0 (initial velocity)
                if t == 0:
                    raise ValueError("Cannot solve for v_0 when t=0")
                return round((y_f - y_0 - (0.5 * g * (t*tuple))) / t, 4)

            elif t is None:
                # Solves for t (elapsed time)
                c: float = y_0 - y_f
                b: float = v_0
                a: float = 0.5 * g
                roots: Tuple[float, float] = Chapter3.Calculate.quadratic_eq(a, b, c)

                if roots is None:
                    raise ValueError("No real solution for time")

                # Return the non-negative root, preferring the smaller positive one
                valid_roots: List[float] = [r for r in roots if r >= 0]

                if not valid_roots:
                    raise ValueError("No positive time solution")

                return round(min(valid_roots), 4)

            else:  # y_f is None
                # Solves for y_f (final position)
                return round(y_0 + (v_0 * t) + (0.5 * g * (t*t)), 4)

        @staticmethod
        def velFreeFallFromHeight(
            y_0: Optional[float] = None,
            v_0: Optional[float] = None,
            y_f: Optional[float] = None,
            v_f: Optional[float] = None,
        ) -> float:
            """Calculates final velocity as a function of displacement, acceleration,
            and initial velocity along the y-axis.
            Can also calculate for desired variable when arg == None and all
            other args have values.

            Args:
                y_0 (Optional[float], optional): initial height [m]. Defaults to None.
                v_0 (Optional[float], optional): initial velocity [m/s]. Defaults to None.
                y_f (Optional[float], optional): final height [m]. Defaults to None.
                v (Optional[float], optional): final velocity [m/s]. Defaults to None.

            Returns:
                float: value of whichever argument was left set to None.
            """
            if y_0 is None:
                # Solves for y_0 (initial height)

                return round(-((((v_f*v_f) - (v_0*v_0)) / (2 * g)) - y_f), 4)

            if v_0 is None:
                # Solves for v_0 (initial velocity)
                discriminant: float = (v_f*v_f) - (2 * g * (y_f - y_0))

                if discriminant < 0:
                    raise ValueError("The discriminant cannot be negative")

                return round(sqrt(discriminant), 4)

            if y_f is None:
                # Solves for y_f (final position)
                return round((((v_f*v_f) - (v_0*v_0)) / (2 * g)) - y_0, 4)

            discriminant: float = (v_0*v_0) + 2 * g * (y_f - y_0)

            if discriminant < 0:
                raise ValueError("The discriminant cannot be negative")

            # Returns v_f (final velocity)
            return round(sqrt(discriminant), 4)
