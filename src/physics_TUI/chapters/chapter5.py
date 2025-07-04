from typing import Dict, List, Optional
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition
from math import pi, cos, acos

# Constants

g: float = 9.82  # gravitational acceleration on Earth [m/s^2]


class Chapter5(PhysicsChapter):
    """
    Chapter on Newton's Laws of Motion.
    """

    def __init__(self) -> None:
        super().__init__("Newton's Laws of Motion")

        self.var_mapping: Dict[str, str] = {
            "N": "normal_F",
            "m": "mass",
            "θ": "theta",
            "F": "force",
            "k": "spring_const",
            "x": "displacement",
        }

        self.equations: List[Equation] = [
            Equation(
                name="Net external force",
                formula="F(net) = ∑F",
                variables={
                    "F": "Force vector, (N)",
                    "F(net)": "Sum of all force vectors (N)",
                },
            ),
            Equation(
                name="Newton's first law",
                formula="v = constant ⟺ F(Net) = 0",
                variables={
                    "v": "Velocity (m/s)",
                    "F(net)": "Sum of all force vectors (N)",
                },
            ),
            Equation(
                name="Newton's second law",
                formula="F(net) = ∑ma",
                variables={
                    "F(net)": "Sum of all force vectors",
                    "m": "Mass of the object (kg)",
                    "a": "Acceleration vector (m/s²)",
                },
            ),
            Equation(
                name="Newton's second law, component form",
                formula="∑Fₓ = maₓ, ∑Fᵧ = maᵧ, and ∑F𝓏 = ma𝓏",
                variables={
                    "m": "Mass of the object (kg)",
                    "aₓ": "X component of acceleration (m/s²)",
                    "aᵧ": "y component of acceleration (m/s²)",
                    "a𝓏": "z component of acceleration (m/s²)",
                },
            ),
            Equation(
                name="Newton's second law, momentum form",
                formula="F(net) = dp/dt = d(mv)/dt",
                variables={
                    "F(net)": "Sum of all force vectors (N)",
                    "p": "Time dependent momentum vector (kg⋅m/s)",
                    "d/dt": "First order derivative with respect to time",
                },
            ),
            Equation(
                name="Weight",
                formula="w = mg",
                variables={"w": "Weight (N)", "m": "Mass (kg)"},
            ),
            Equation(
                name="Newton's third law",
                formula="F(AB) = - F(BA)",
                variables={
                    "F(AB)": "Force acted upon B by A (N)",
                    "F(BA)": "Force acted upon A by B (N)",
                },
            ),
            Equation(
                name="Normal force (resting)",
                formula="N = mgcosθ",
                variables={
                    "N": "Normal force (N)",
                    "m": "Mass of the object (kg)",
                    "θ": "Angle between the normal vector and gravitational vector [radians]",
                },
                calculation=self.Calculate.normal_force,
            ),
            Equation(
                name="Hooke's Law",
                formula="F = -kx",
                variables={
                    "F": "Restorative force (N)",
                    "k": "Spring constant (kg/s²)",
                    "x": "Distance from point of equilibrium",
                },
                calculation=self.Calculate.hookes_law,
            ),
        ]

        self.definitions: List[Definition] = [
            Definition(
                term="dynamics",
                meaning="study of how forces affect the motion of objects and systems",
            ),
            Definition(
                term="external force",
                meaning="force acting on an object or system that originates outside \
                    of the object or system",
            ),
            Definition(
                term="force",
                meaning="push or pull on an object with a specific magnitude and direction; \
                    can be represented by vectors or expressed as a multiple of a standard force",
            ),
            Definition(
                term="free fall",
                meaning="situation in which the only force acting on an object is gravity",
            ),
            Definition(
                term="free-body diagram",
                meaning="sketch showing all external forces acting on an object or system; \
                    the system is represented by a single isolated point, and the forces are \
                    represented by vectors extending outward from that point",
            ),
            Definition(
                term="Hooke's law",
                meaning="in a spring, a restoring force proportional to and in the \
                    opposite direction of the imposed displacement",
            ),
            Definition(
                term="inertia",
                meaning="ability of an object to resist changes in its motion",
            ),
            Definition(
                term="inertial reference frame",
                meaning="reference frame moving at constant velocity relative to an \
                    inertial frame is also inertial; a reference frame accelerating relative \
                    to an inertial frame is not inertial",
            ),
            Definition(
                term="law of inertia", meaning="see Newton's first law of motion"
            ),
            Definition(
                term="net external force",
                meaning="vector sum of all external forces acting on an object or system; \
                    causes a mass to accelerate",
            ),
            Definition(
                term="newton",
                meaning="SI unit of force; 1 N is the force needed to accelerate an object \
                    with a mass of 1 kg at a rate of 1m/s²",
            ),
            Definition(
                term="Newton's first law of motion",
                meaning="body at rest remains at rest or, if in motion, remains in motion \
                    at constant velocity unless acted on by a net external force; also known \
                    as the law of inertia",
            ),
            Definition(
                term="Newton's second law of motion",
                meaning="acceleration of a system is directly proportional to and in the \
                    same direction as the net external force acting on the system and is \
                    inversely proportional to its mass",
            ),
            Definition(
                term="Newton's third law of motion",
                meaning="whenever one body exerts a force on a second body, the first body \
                    experiences a force that is equal in magnitude and opposite in direction \
                    to the force that it exerts",
            ),
            Definition(
                term="normal force",
                meaning="force supporting the weight of an object, or a load, that is \
                    perpendicular to the surface of contact between the load and its support; \
                    the surface applies this force to an object to support the weight of the object",
            ),
            Definition(
                term="tension",
                meaning="pulling force that acts along a stretched flexible connector, \
                    such as a rope or cable",
            ),
            Definition(
                term="thrust",
                meaning="reaction force that pushes a body forward in response to a backward force",
            ),
            Definition(
                term="weight",
                meaning="force due to gravity acting on an object of mass m",
            ),
        ]

    class Calculate:
        """
        Class holds methods to calculate equations in chapter 5.
        """

        # TO-DO: Decide which equations are needed and how best to calculate knowing
        # the typical problem which they are used to solve.

        @staticmethod
        def normal_force(
            normal_F: Optional[float] = None,
            mass: Optional[float] = None,
            theta: Optional[float] = None,
        ) -> float:
            """
            Function calculates the normal force of an object resting on a surface.
            Can also calculate for desired variable when arg == None and all other args
            have values.

            Args:
                normal_F (Optional[float], optional): normal force [N]. Defaults to None.
                mass (Optiona[float], optional): mass of the object [kg]. Defaults to None.
                theta (Optional[float], optional): angle between the normal force and gravitational force. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if mass is not None and mass < 0:
                raise ValueError("Mass cannot be negative.")

            if theta is not None:
                # Converts degrees to radians
                theta_radians: float = theta * (pi / 180)
            else:
                # Calculates for theta
                arg: float = normal_F / (mass * g)
                return acos(arg) * (180 / pi)

            if mass == None:

                if theta == 90.0 or theta == 270.0:
                    raise ValueError("Division by zero is undefined.")

                # Calculates for the mass
                result = normal_F / (g * cos(theta_radians))

                if result < 0:
                    raise ValueError("Mass cannot be negative.")
                else:
                    return result

            return mass * g * cos(theta_radians)

        @staticmethod
        def hookes_law(
            force: Optional[float] = None,
            spring_const: Optional[float] = None,
            displacement: Optional[float] = None,
        ) -> float:
            """
            Function calculates the restorative force of a spring system
            as a fuction of displacement and the spring constant.
            Can also calculate for desired variable when arg == None and all
            other args have values.

            Args:
                force (Optional[float], optional): restorative force [N]. Defaults to None.
                spring_const (Optional[float], optional): displacement [m]. Defaults to None.
                displacement (Optional[float], optional): spring constant [kg*m/s^2]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if spring_const is not None and spring_const < 0:
                raise ValueError("Spring constant (k) cannot be a negative value.")

            if spring_const == None:

                if displacement == 0:
                    raise ValueError("Divison by zero is undefined.")

                # Calculates the spring constant
                result = -force / displacement

                if result < 0:
                    raise ValueError(
                        "Spring constant cannot be negative. \
                        Consider the relation between the direction \
                        of displacment and the restorative force."
                    )

                return result

            if displacement == None:

                if spring_const == 0:
                    raise ValueError("Divison by zero is undefined.")

                # Calculates the displacement
                return -force / spring_const

            return -spring_const * displacement
