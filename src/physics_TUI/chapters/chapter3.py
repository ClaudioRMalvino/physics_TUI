from typing import Dict, List
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

        def positionFromVelAndAcc(self, 
            x_0: float=None,
            v_0: float=None,
            t: float=None,
            accel: float=None,
            x_f: float=None
        ) -> float:
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

            if x_0 is None and v_0 and t and accel and x_f: 
                pass
            elif v_0 is None and x_0 and t and accel and x_f:
                pass
            elif t is None and x_0 and v_0 and accel and x_f:
                pass
            elif accel is None and x_0 and v_0 and t and x_f:
                pass
            else:
                return x_0 + (v_0*t) + (0.5 * accel * (t**2))
