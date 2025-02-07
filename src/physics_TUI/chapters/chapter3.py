from typing import Dict, List, Tuple, Optional
from math import sqrt
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition


class Chapter3(PhysicsChapter):
    """
    Chapter on one-dimensional motion.
    """

    def __init__(self) -> None:
        super().__init__("Motion Along a Straight Line", 
                         "Study of motion along one dimension.")

        self.equations: List[Equation] = [
            Equation(
                name="Displacement",
                formula="Δx = x - x₀",
                variables={
                    "x": "Final position",
                    "x₀": "Initial position",
                }
            ),
            Equation(
                name="Total Displacement",
                formula="Δx = ∑Δxᵢ",
                variables={
                    "Δxᵢ": "All steps taken"
                }
            ),
            Equation(
                name="Average velocity (constant acceleration)",
                formula="v = Δx/Δt = (x - xᵢ)/(t - tᵢ)",
                variables={
                    "Δx": "Displacement in direction",
                    "Δt": "Elapsed time"}
            ),
            Equation(
                name="Instantaneous velocity",
                formula="v(t) = dx(t)/dt",
                variables={}
            ),
            Equation(
                name="Average speed",
                formula="s = (Total distance)/(Elapsed time)",
                variables={}
            ),
            Equation(
                name="Instantaneous speed",
                formula="|v(t)|",
                variables={}
            ),
            Equation(
                name="Average acceleration",
                formula="a = Δv/Δt",
                variables={
                    "Δv": "Change in velocity",
                    "Δt": "Elapsed time"
                }
            ),
            Equation(
                name="Instantaneous acceleration",
                formula="a(t) = dv(t)/dt",
                variables={}
            ),
            Equation(
                name="Position from avg. velocity",
                formula="x(t) = x₀ + vt",
                variables={
                    "x₀": "Initial position",
                    "v": "Average velocity",
                    "t": "time"
                }
            ),
            Equation(
                name="Velocity from acceleration",
                formula="v(t) = v₀ + at",
                variables={
                    "v₀": "Initial velocity",
                    "a": "Acceleration"
                }
            ),
            Equation(
                name="Position from velocity and acceleration",
                formula="x(t) = x₀ + v₀t + (1/2)at²",
                variables={
                    "x₀": "Initial position",
                    "v₀": "Intiial velocity",
                    "t": "Time",
                    "a": "Acceleration"
                }
            ),
            Equation(
                name="Velocity from distance",
                formula="v² = v₀² + 2a(x - x₀)",
                variables={
                    "x": "Final position",
                    "x₀": "Initial position",
                    "v₀": "Intiial velocity",
                    "a": "Acceleration"
                    
                }
            ),
            Equation(
                name="Velocity of free fall",
                formula="v = v₀ - gt",
                variables={
                    "v₀": "Initial velocity",
                    "g": "Accelration due to gravity: 9.8 m/s",
                    "t": "Time"
                }
            ),
            Equation(
                name="Height of free fall",
                formula="y(t) = y₀ + v₀t - (1/2)gt²",
                variables={
                    "y₀": "Initial height",
                    "v₀": "Initial velocity",
                    "g": "Accelration due to gravity: 9.8 m/s",
                    "t": "Time"
                }
            ),
            Equation(
                name="Velocity of free fall from height",
                formula="v² = v₀² - 2g(y - y₀)",
                variables={
                    "y": "Final height",
                    "y₀": "Initial height",
                    "v₀": "Initial velocity",
                    "g": "Accelration due to gravity: 9.8 m/s",
                }
            ),
            Equation(
                name="Velocity from acceleration",
                formula="v(t) = ∫ a(t)dt + C₁",
                variables={}

            ),
            Equation(
                name="Position from velocity",
                formula="x(t) = ∫ V(t)dt + C₂",
                variables={}
            )
        ]

        self.definitions: List[Definition] = [
            Definition(
                term="acceleration due to gravity",
                meaning="acceleration of an object as a result of gravity"
            ),
            Definition(
                term="average acceleration",
                meaning="the rate of change in velocity; the change in velocity over time"
            ),
            Definition(
                term="average speed",
                meaning="the total distance traveled divided by elapsed time"
            ),
            Definition(
                term="average velocity",
                meaning="the displacement divided by the time over which displacement occurs under constant acceleration"      
            ),
            Definition(
                term="displacement",
                meaning="the change in position of an object"
            ),
            Definition(
                term="distance traveled",
                meaning="the total length of the path traveled between two positions"
            ),
            Definition(
                term="elapsed time",
                meaning="the difference between the ending time and the beginning time"
            ),
            Definition(
                term="free fall",
                meaning="the state of movement that results from gravitational force only"
            ),
            Definition(
                term="instantaneous acceleration",
                meaning="acceleration at a specific point in time"
            ),
            Definition(
                term="instantaneous speed",
                meaning="the absolute value of the instantaneous velocity"
            ),
            Definition(
                term="instantaneous velocity",
                meaning="the velocity at a specific instant or time point"
            ),
            Definition(
                term="kinematics",
                meaning="the description of motion through properties such as position, time, velocity, and acceleration"
            ),
            Definition(
                term="position",
                meaning="the location of an object at a particular time"
            ),
            Definition(
                term="total displacement",
                meaning="the sum of individual displacements over a given time period"
            ),
            Definition(
                term="two-body pursuit problem",
                meaning="a kinematics problem in which the unknowns are calculated by solving the kinematic equations simultaneously for two moving objects"
            )
        ]

    class Calculate:
        """ Class holds methods to calculate equations in Chapter 3 """

        @staticmethod
        def positionFromVelAndAcc( 
            x_0: Optional[float]=None,
            v_0: Optional[float]=None,
            t: Optional[float]=None,
            accel: Optional[float]=None,
            x_f: Optional[float]=None ) -> float:
            """
            Calculates position from velocity and acceleration.
            Can also calculate for desired variable when arg == None and all
            other args have values.

            Args:
                x_0 (float, optional): Initial position. Defaults to None.
                v_0 (float, optional): Initial velocity. Defaults to None.
                t (float, optional): Elapsed time. Defaults to None.
                accel (float, optional): Constant acceleration. Defaults to None.
                x_f (float, optional): Final position. Defaults to None.
            """
            def quadratic_eq(a: float, b: float, c: float) -> Optional[Tuple[float, float]]:
                """
                Function calculates the roots of a quadratic equation ax^2 + bx + c = 0
                accurately in all cases.

                Returns a tuple containing the two roots.
                """

                discriminant = b**2 - 4*a*c

                if discriminant < 0:
                    return None  

                # Choose the appropriate formula based on the sign of b
                if b >= 0:
                    x1 = (-b - sqrt(discriminant)) / (2*a)
                    x2 = (2*c) / (-b - sqrt(discriminant))
                else:
                    x1 = (2*c) / (-b + sqrt(discriminant))
                    x2 = (-b + sqrt(discriminant)) / (2*a)

                return (x1, x2)

            if x_0 is None and v_0 and t and accel and x_f: 
                return round(
                    x_f - (v_0 * t) - (0.5 * accel * (t**2)), 4)

            if v_0 is None and x_0 and t and accel and x_f:
                return round(
                    (x_f - x_0 - (0.5 * accel * (t**2)))/t, 4)

            if t is None and x_0 is not None \
                and v_0 is not None and accel is not None and x_f is not None:
                
                if accel == 0 and v_0 == 0:
                    raise ValueError("v₀ and a cannot both be equal to zero")

                c: float = x_0 - x_f
                b: float = v_0
                a: float = (0.5 * accel)
                roots = quadratic_eq(a, b, c)

                if roots[0] < 0: 
                    return round(roots[1], 4)
                if roots[1] < 0:
                    return round(roots[0], 4)

            if accel is None and x_0 and v_0 and t and x_f:
                return round(x_f - x_0 - (v_0 *t), 4)
            
            return round(
                (x_0 + (v_0 * t) + (0.5 * accel * (t**2))), 4)
