from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition


class Chapter5(PhysicsChapter):
    """
    Chapter on Newton's Laws of Motion.
    """

    def __init__(self) -> None:
        super().__init__("Newton's Laws of Motion")

        # TO-DO: complete the map once all calculation methods have been developed
        self.var_mapping: Dict[str, str] = {}

        self.equations: List[Equation] = [
            Equation(
                name="Net external force",
                formula="F(net) = ∑F",
                variables={
                    "F": "Force vector [N]",
                    "F(net)": "Sum of all force vectors [N]",
                },
            ),
            Equation(
                name="Newton's first law",
                formula="v = constant ⟺ F(Net) = 0",
                variables={
                    "v": "Velocity [m/s]",
                    "F(net)": "Sum of all force vectors [N]",
                },
            ),
            Equation(
                name="Newton's second law",
                formula="F(net) = ∑ma",
                variables={
                    "F(net)": "Sum of all force vectors",
                    "m": "Mass of the object [kg]",
                    "a": "Acceleration vector [m/s²]",
                },
            ),
            Equation(
                name="Newton's second law, component form",
                formula="∑F(x) = ma(x), ∑F(y) = ma(y), and ∑F(z) = ma(z)",
                variables={
                    "m": "Mass of the object [kg]",
                    "a(x)": "X component of acceleration [m/s²]",
                    "a(y)": "y component of acceleration [m/s²]",
                    "a(z)": "z component of acceleration [m/s²]",
                },
            ),
            Equation(
                name="Newton's second law, momentum form",
                formula="F(net) = dp/dt = d(mv)/dt",
                variables={
                    "F(net)": "Sum of all force vectors [N]",
                    "p": "Time dependent momentum vector [kg⋅m/s]",
                    "d/dt": "First order derivative with respect to time",
                },
            ),
            Equation(
                name="Weight",
                formula="w = mg",
                variables={
                    "w": "Weight [N]",
                    "g": "Acceleration due to gravity [m/s²]",
                },
            ),
            Equation(
                name="Newton's third law",
                formula="F(AB) = - F(BA)",
                variables={
                    "F(AB)": "Force acted upon B by A [N]",
                    "F(BA)": "Force acted upon A by B [N]",
                },
            ),
            Equation(
                name="Normal force (resting)",
                formula="N = mgcosθ",
                variables={
                    "N": "Normal force [N]",
                    "m": "Mass of the object [kg]",
                    "g": "Acceleration due to gravity [m/s²]",
                    "θ": "Angle between the normal vector and gravitational vector [radians]",
                },
            ),
            Equation(
                name="Hooke's Law",
                formula="F = -kx",
                variables={
                    "F": "Restorative force [N]",
                    "k": "Spring constant [kg/s²]",
                    "x": "Distance from point of equilibrium",
                },
            ),
        ]

        definitions: List[Definition] = [
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