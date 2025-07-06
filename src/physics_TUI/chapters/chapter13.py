from typing import List, Optional, Dict
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition
from math import sqrt, cos, acos

# Global constants
G: float = 6.674E-11 # Newton's gravitational constant
c: float = 2.998E+8 # Speed of light in a vacuum

class Chapter13(PhysicsChapter):
    """
    Class Gravitation
    """

    def __init__(self) -> None:
        super().__init__("Gravitation")

        self.var_mapping: Dict[str, str] = {}

        self.equations: List[Equation] = [
            Equation(
                name="Newton's law of gravitation",
                formula="F₁₂ = G(m(1)m(2)/r²)r̂₁₂",
                variables={
                    "F₁₂": "Gravitational force between from object 1 \
                        on object 2 (N)",
                    "G": "Newton's gravitational constant:  6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² (constant)",
                    "m(1)": "Mass of object 1 (kg)",
                    "m(2)": "Mass of object 2 (kg)",
                    "r": "Distance between the centers of mass of m(1) to m(2) (m)",
                },
                calculation=self.Calculate.law_of_gravitation
            ),
            Equation(
                name="Acceleration due to gravity at the surface of a stellar body",
                formula="g = GM/r²",
                variables={
                    "g": "Acceleration due to gravity (m/s²)",
                    "G": "Newton's gravitational constant:  6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² (constant)",
                    "M": "Mass of the stellar body (kg)",
                    "r": "Radius of the stellar body (m)",
                },
                calculation=self.Calculate.gravitational_acceleration
            ),
            Equation(
                name="Gravitational potential energy beyond a stellar body",
                formula="U = -GMm/r",
                variables={
                    "U": "Gravitational potential energy (J)",
                    "G": "Newton's gravitational constant:  6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² (constant)",
                    "M": "Mass of the stellar body (kg)",
                    "m": "Mass of the object (kg)",
                    "r": "Distance from the center of mass of M to  m (m)"
                },
                calculation=self.Calculate.gravitational_potential
            ),
            Equation(
                name="Conservation of energy",
                formula="½mv(1)² - GMm/r(1) = ½mv(2)² - GMm/r(2)",
                variables={
                    "G": "Newton's gravitational constant:  6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² (constant)",
                    "m": "Mass of the object (kg)",
                    "M": "Mass of the stellar body (kg)",
                    "v(1)": "Velocity of object 1 (m/s)",
                    "v(2)": "Velocity of object 2 (m/s)",
                    "r(1)": "Distance from the center of mass M to m (m)",
                    "r(2)": "Distance from the center of mass M to m (m)",
                },
                calculation=self.Calculate.conservation_of_grav_energy
            ),
            Equation(
                name="Escape velocity",
                formula="v(esc) = √(2GM/R)",
                variables={
                    "V(esc)": "Escape velocity (m/s)",
                    "G": "Newton's gravitational constant:  6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² (constant)",
                    "M": "Mass of the stellar body (kg)",
                    "R": "Radius of the stellar body (m)"
                },
                calculation=self.Calculate.escape_velocity
            ),
            Equation(
                name="Orbital speed",
                formula="V(orbit) = √(GM/r)",
                variables={
                    "V(esc)": "Escape velocity (m/s)",
                    "G": "Newton's gravitational constant:  6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² (constant)",
                    "M": "Mass of the stellar body (kg)",
                    "r": "Altitude of the orbiting body (m)"
                },
                calculation=self.Calculate.orbital_velocity
            ),
            Equation(
                name="Orbital period",
                formula="T = 2π√(r³/GM)",
                variables={
                    "T": "Orbital period (s)",
                    "r": "Altitude of orbiting body (m)",
                    "G": "Newton's gravitational constant:  6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² (constant)",
                    "M": "Mass of the stellar body (kg)"
                },
                calculation=self.Calculate.orbital_period
            ),
            Equation(
                name="Energy in circular orbit",
                formula="E = K + U = -GmM/2r",
                variables={
                    "E": "Total energy of the systen (J)",
                    "r": "Distance between the center of mass of object M and m (m)",
                    "G": "Newton's gravitational constant:  6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² (constant)",
                    "M": "Mass of the stellar body (kg)",
                    "m": "Mass of the orbiting body (kg)"
                }
            ),
            Equation(
                name="Orbital equation",
                formula="a(1-e²)/r = 1 + ecosθ",
                variables={
                    "a": "Semi-major axis of the orbit",
                    "e": "Eccentricity of the orbit",
                    "r": "Distance from focus to object (m)",
                    "θ": "Angle from periapsis (rads)"
                },
                calculation=self.Calculate.orbital_equation
            ),
            Equation(
                name="Kepler's third law",
                formula="T² = (4π²/GM)a³",
                variables={
                    "T": "The orbital period of the stellar body (s)",
                    "a": "Semi-major axis of the orbit",
                    "G": "Newton's gravitational constant:  6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² (constant)",
                    "M": "Mass of the stellar body (kg)"
                },
                calculation=self.Calculate.keplers_third_law
            ),
            Equation(
                name="Schwarzschild radius",
                formula="R(S) = 2GM/c²",
                variables={
                    "R(S)": "Schwarzschild radius (m)",
                    "G": "Newton's gravitational constant:  6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² (constant)",
                    "M": "Mass of the stellar body (kg)",
                    "c": "Speed of light: 2.998 × 10⁸ m/s (constant) "
                },
                calculation=self.Calculate.schwarzschild_radius
            )
        ]

        self.definitions: List[Definition] = [
            Definition(
                term="action-at-a-distance force",
                meaning="type of force exerted without physical contact"
            ),
            Definition(
                term="aphelion",
                meaning="farthest point from the Sun of an orbiting body; the corresponding term for the Moon's farthest point from Earth is the apogee"
            ),
            Definition(
                term="apparent weight",
                meaning="reading of the weight of an object on a scale that does not account for acceleration"
            ),
            Definition(
                term="black hole",
                meaning="mass that becomes so dense, that it collapses in on itself, creating a singularity at the center surrounded by an event horizon"
            ),
            Definition(
                term="escape velocity",
                meaning="initial velocity an object needs to escape the gravitational pull of another; it is more accurately defined as the velocity of an object with zero total mechanical energy"
            ),
            Definition(
                term="event horizon",
                meaning="location of the Schwarzschild radius and is the location near a black hole from within which no object, even light, can escape"
            ),
            Definition(
                term="gravitational field",
                meaning="vector field that surrounds the mass creating the field; the field is represented by field lines, in which the direction of the field is tangent to the lines, and the magnitude (or field strength) is inversely proportional to the spacing of the lines; other masses respond to this field"
            ),
            Definition(
                term="gravitationally bound",
                meaning="two objects are gravitationally bound if their orbits are closed; gravitationally bound systems have a negative total mechanical energy"
            ),
            Definition(
                term="Kepler's first law",
                meaning="law stating that every planet moves along an ellipse, with the Sun located at a focus of the ellipse"
            ),
            Definition(
                term="Kepler's second law",
                meaning="law stating that a planet sweeps out equal areas in equal times, meaning it has a constant areal velocity"
            ),
            Definition(
                term="Kepler's third law",
                meaning="law stating that the square of the period is proportional to the cube of the semi-major axis of the orbit"
            ),
            Definition(
                term="neap tide",
                meaning="low tide created when the Moon and the Sun form a right triangle with Earth"
            ),
            Definition(
                term="neutron star",
                meaning="most compact object known—outside of a black hole itself"
            ),
            Definition(
                term="Newton's law of gravitation",
                meaning="every mass attracts every other mass with a force proportional to the product of their masses, inversely proportional to the square of the distance between them, and with direction along the line connecting the center of mass of each"
            ),
            Definition(
                term="non-Euclidean geometry",
                meaning="geometry of curved space, describing the relationships among angles and lines on the surface of a sphere, hyperboloid, etc."
            ),
            Definition(
                term="orbital period",
                meaning="time required for a satellite to complete one orbit"
            ),
            Definition(
                term="orbital speed",
                meaning="speed of a satellite in a circular orbit; it can also be used for the instantaneous speed for noncircular orbits in which the speed is not constant"
            ),
            Definition(
                term="perihelion",
                meaning="point of closest approach to the Sun of an orbiting body; the corresponding term for the Moon's closest approach to Earth is the perigee"
            ),
            Definition(
                term="principle of equivalence",
                meaning="part of the general theory of relativity, it states that there is no difference between free fall and being weightless, or a uniform gravitational field and uniform acceleration"
            ),
            Definition(
                term="Schwarzschild radius",
                meaning="critical radius (RS) such that if a mass were compressed to the extent that its radius becomes less than the Schwarzschild radius, then the mass will collapse to a singularity, and anything that passes inside that radius cannot escape"
            ),
            Definition(
                term="space-time",
                meaning="concept of space-time is that time is essentially another coordinate that is treated the same way as any individual spatial coordinate; in the equations that represent both special and general relativity, time appears in the same context as do the spatial coordinates"
            ),
            Definition(
                term="spring tide",
                meaning="high tide created when the Moon, the Sun, and Earth are along one line"
            ),
            Definition(
                term="theory of general relativity",
                meaning="Einstein's theory for gravitation and accelerated reference frames; in this theory, gravitation is the result of mass and energy distorting the space-time around it; it is also often referred to as Einstein's theory of gravity"
            ),
            Definition(
                term="tidal force",
                meaning="difference between the gravitational force at the center of a body and that at any other location on the body; the tidal force stretches the body"
            ),
            Definition(
                term="universal gravitational constant",
                meaning="constant representing the strength of the gravitational force, that is believed to be the same throughout the universe"
            ),
        ]

    class Calculate:
        """
        Class holds methods to calculate equations in Chapter 13
        """

        @staticmethod
        def law_of_gravtation(
            force_12: Optional[float]=None,
            mass_1: Optional[float]=None,
            mass_2: Optional[float]=None,
            distance: Optional[float]=None 
        ) -> float:
            """
            Function calculates the gravitational force between two bodies
            as a function of the two masses and the distance between their
            respective centers of mass. 
            Can also calculate for desired variable when arg == None
            and all other args have values.

            Args:
                force_12 (Optional[float], optional): gravitational force on object2 by object 1 [N]. Defaults to None.
                mass_1 (Optional[float], optional): mass of stellar body 1 [kg]. Defaults to None.
                mass_2 (Optional[float], optional): mass of stellar body 2 [kg]. Defaults to None.
                distance (Optional[float], optional): distance between the center of mass of both bodies [m]. Defaults to None.

            Raises:
                ValueError: "We are operating with massive objects.
                    Make sure all objects have a mass greater than zero
                ValueError: "Distance cannot be a negative value."
                ValueError: "Negative radicand yields a complex number. Check your values."

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if mass_1 is not None and mass_1 <= 0.0
            or mass_2 is not None and mass_2 <= 0.0:
                raise ValueError(
                    "We are operating with massive objects. \
                    Make sure all objects have a mass greater than zero."
                )
            
            if distance is not None and distance < 0.0:
                raise ValueError("Distance cannot be a negative value.")

            if mass_1 == None:

                # Calculates mass of object 1
                numerator: float = force_12 * (distance * distance)
                denominator: float = G * mass_2
                return numerator/denominator
            
            if mass_2 == None:

                # Calculates mass of object 2
                numerator: float = force_12 * (distance * distance)
                denominator: float = G * mass_1
                return numerator/denominator

            if distance == None:
                
                # Calculates the distance between two stellar bodies
                radicand: float = (G * mass_1 * mass_2) / force_12
                
                if radicand < 0:
                    raise ValueError("Negative radicand yields a complex number.\
                        Check your values.")
                
                return sqrt(radicand)
            
            return (G * mass_1 * mass_2) / (radius * radius)

        @staticmethod
        def gravitational_acceleration(
            g: Optional[float]=None,
            mass: Optional[float]=None,
            distance: Optional[float]=None
        ) -> float:
            """
            Function calculates the acceleration due to gravity of a stellar
            body as a function of its mass and the radius of the body. 
            Can also calculate for desired variable when arg == None
            and all other args have values.

            Args:
                g (Optional[float], optional): acceleration due to gravity [m/s²]. Defaults to None.
                mass (Optional[float], optional): mass of the stellar body [kg]. Defaults to None.
                distance (Optional[float], optional): radius of the stellar body [m]. Defaults to None.


            Raises:
                ValueError: "Distance cannot be a value that is less than or equal to zero."
                ValueError: "Distance cannot be a negative value."

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if distance is not None and distance <= 0.0:
                raise ValueError("Distance cannot be a value that is \
                    less than or equal to zero.")
            
            if mass == None:
                # Calculates the acceleration due to gravity
                return (g * (radius * radius)) / G
            
            if distance == None: 
                # Calculates the radius of the stellar body
                radicand: float = (G * mass) / g

                if radicand < 0.0:
                    raise ValueError("Distance cannot be a negative value.")
                
                return sqrt(radicand)
            
            return (G * mass) / (radius * radius)

        @staticmethod
        def gravitational_potential(
            potential_energy: Optional[float]=None,
            mass_body: Optional[float]=None,
            mass_object: Optional[float]=None,
            distance: Optional[float]=None
        ) -> float:
            """
            Function calculates the gravitational potential energy betweem 
            a stellar and an orbiting object as a function of both masses 
            and the distance between the center of mass of each object. 
            Can also calculate for desired variable when arg == None
            and all other args have values.

            Args:
                potential_energy (Optional[float], optional): gravitational potential energy [J]. Defaults to None.
                mass_body (Optional[float], optional): mass of stellar body [kg]. Defaults to None.
                mass_object (Optional[float], optional): mass of object [kg]. Defaults to None.
                distance (Optional[float], optional): distance between the two objects [m]. Defaults to None.

            Raises:
                ValueError: "Distance between the two bodies must be greater than zero."
                ValueError: "We are operating with massive objects. Make sure all objects have a mass greater than zero."
                ValueError: "Mass cannot be negative. Check your values."
                ValueError: "Distance cannot be negative. Check your values."

            Returns:
                float: _description_
            """

            if distance is not None and distance <= 0.0:
                raise ValueError("Distance between the two bodies must be \
                greater than zero.")
            
            if mass_body is not None and mass_body <= 0.0
            or mass_object is not None and mass_object <= 0.0:
                raise ValueError("We are operating with massive objects. \
                Make sure all objects have a mass greater than zero.")
            
            if mass_body == None:

                # Calculates the mass of the stellar body
                result: float = -(potential_energy * distance) / (G * mass_object)

                if result < 0.0:
                    raise ValueError("Mass cannot be negative. Check your values.")
                else:
                    return result
            
            if mass_object == None:

                # Calculates the mass of the orbiting object
                result: float = -(potential_energy * distance) / (G * mass_body)

                if result < 0.0:
                    raise ValueError("Mass cannot be negative. Check your values.")
                else:
                    return result   
            
            if distance == None:

                result: float = -(G * mass_body * mass_object) / potential_energy

                if result < 0.0:
                    raise ValueError("Distance cannot be negative. \
                        Check your values.")
                else:
                    return result  

            return -(G * mass_body * mass_object) / distance 

        @staticmethod
        def conservation_of_grav_energy(
            mass_object: Optional[float]=None,
            mass_body: Optional[float]=None,
            velocity_1: Optional[float]=None,
            velocity_2: Optional[float]=None,
            distance_1: Optional[float]=None,
            distance_2: Optional[float]=None
        ) -> float:
            """
            Function calculates the conservation of gravitational energy betweem 
            a stellar and an orbiting object as a function of both masses,
            the distance and velocitie at point 1 and point 2. 
            Can also calculate for desired variable when arg == None
            and all other args have values.

            Args:
                mass_object (Optional[float], optional): mass of orbiting object [kg]. Defaults to None.
                mass_body (Optional[float], optional): mass of stellar object [kg]. Defaults to None.
                velocity_1 (Optional[float], optional): velocity at moment 1 [m/s]. Defaults to None.
                velocity_2 (Optional[float], optional): velocity at moment 2 [m/s]. Defaults to None.
                distance_1 (Optional[float], optional): distance of center of mass 
                                                        from mass_body and mass_stellar at moment 1 [m]. Defaults to None.
                distance_2 (Optional[float], optional): distance of center of mass 
                                                        from mass_body and mass_stellar at moment 2 [m]. Defaults to None.

            Raises:
                ValueError: "Distance cannot be a negative value."
                ValueError: "We are operating with massive objects.
                            Make sure all objects have a mass greater than zero."
                ValueError: "Divison by zero is undefined."
                ValueError: "Mass of orbiting body cancels out and
                            cannot be determined."
                ValueError: "Negative radicand yields a complex number. Check your values."
                
                Returns:
                float: the result of whichever variable was left equal to None
            """
        if distance_1 is not None and distance_1 <= 0.0
        or distance_2 is not None and distance_2 <= 0.0:
            raise ValueError("Distance cannot be a negative value.")
        
        if mass_object is not None and mass_object <= 0.0
        or mass_body is not None and mass_body <= 0.0:
            raise ValueError(
                "We are operating with massive objects. \
                Make sure all objects have a mass greater than zero."
            )
        
        if mass_body == None:

            velocity_1_sq: float = velocity_1 * velocity_1 
            velocity_2_sq: float = velocity_2 * velocity_2 

            numerator: float = (0.5 ) * (velocity_1_sq - velocity_2_sq)
            denominator: float = G * (( -1 / distance_2 ) + (1 / distance_1))

            if denominator == 0.0:
                raise ValueError("Divison by zero is undefined.")
            
            return numerator / denominator
        
        if mass_object == None:
            raise ValueError("Mass of orbiting body cancels out and \
                cannot be determined.")

        if distance_2 == None:
            
            if velocity_1 == 0.0 or velocity_2 == 0.0:
                raise ValueError("Division by zero is undefined.")

            coeff: float = -(1.0 / G * mass_body * mass_object)
            term1: float = 0.5 * mass_object * (velocity_1 * velocity_1)
            term2: float = (G * mass_object * mass_body) / distance_1
            term3: float = 0.5 * mass_object * (velocity_2 * velocity_2)

            return coeff * (term1 - term2 - term3)
        
        if distance_1 == None:
            
            if velocity_1 == 0.0 or velocity_2 == 0.0:
                raise ValueError("Division by zero is undefined.")

            coeff: float = (1.0 / G * mass_body * mass_object)
            term1: float = 0.5 * mass_object * (velocity_1 * velocity_1)
            term2: float = (G * mass_object * mass_body) / distance_2
            term3: float = 0.5 * mass_object * (velocity_2 * velocity_2)

            return coeff * (term1 + term2 - term3)
        
        if velocity_1 == None:

            term1: float = (0.5) * mass_object * (velocity_2 * velocity_2)
            term2: float = (G * mass_body * mass_object) / distance_1
            term3: float = (G * mass_body * mass_object) / distance_2
            coeff: float = 2.0 / mass_object

            radicand: float = coeff * (term1 + term2 - term3)
            if radicand < 0.0:
                raise ValueError("Negative radicand yields a complex number. \
                    Check your values.")
            
            return sqrt(radicand)

        if velocity_1 == None:

            term1: float = (0.5) * mass_object * (velocity_1 * velocity_1)
            term2: float = (G * mass_body * mass_object) / distance_1
            term3: float = (G * mass_body * mass_object) / distance_2
            coeff: float = 2.0 / mass_object

            radicand: float = coeff * (term1 - term2 + term3)
            if radicand < 0.0:
                raise ValueError("Negative radicand yields a complex number. \
                    Check your values.")
            
            return sqrt(radicand)
        
        @staticmethod
        def escape_velocity(
            escape_vel: Optional[float]=None,
            mass_body: Optional[float]=None,
            radius: Optional[float]=None
        ) -> float:
            """
            Function calculates the escape velocity for a stellar body as a
            function of its mass and its radius.
            Can also calculate for desired variable when arg == None
            and all other args have values.

            Args:
                escape_vel (Optional[float], optional): escape velocity [m/s]. Defaults to None.
                mass_body (Optional[float], optional): mass of stellar body [kg]. Defaults to None.
                radius (Optional[float], optional): radius of stellar body. Defaults to None.

            Raises:
                ValueError: "We are operating with massive objects. Make sure all objects have a mass greater than zero."
                ValueError: "Radius of stellar body must be greater than zero."
                ValueError: "Negative square root yields a complex number. Check your values."
                ValueError: "Divison by zero is undefined."

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if mass_body is not None and mass_body <= 0:
                raise ValueError(
                "We are operating with massive objects. \
                Make sure all objects have a mass greater than zero."
            )

            if radius is not None and radius <= 0:
                raise ValueError("Radius of stellar body must be greater than zero.")

            if mass_body == None:

                # Calculates the mass of the stellar body
                if escape_vel < 0.0:
                    raise ValueError("Negative square root yields a complex number.\
                        Check your values.")

                return (sqrt(escape_vel) * radius) / (2.0 * G)
            
            if radius == None:
        
                if escape_vel < 0.0:
                    raise ValueError("Negative square root yields a complex number.\
                        Check your values.")

                 if escape_vel == 0.0:
                    raise ValueError("Divison by zero is undefined.")
                
                return (2.0 * G * mass_body) / sqrt(escape_vel)
            
            radicand: float = (2.0 * G * mass_body) / radius

            if radicand < 0.0: 
                raise ValueError("Negative square root yields a complex number.\
                        Check your values.")
            
            return sqrt(radicand)

        @staticmethod
        def orbital_velocicty(
            orbital_vel: Optional[float]=None,
            mass_body: Optional[float]=None,
            distance: Optional[float]=None,
        ) -> float:
            return 0.0
        
        @staticmethod
        def orbital_period(
            orbital_period: Optional[float]=None,
            distance: Optional[float]=None,
            mass_body: Optional[float]=None
        ) -> float:
            return 0.0
        
        @staticmethod
        def orbital_equation(
            semi_major_axis: Optional[float]=None,
            eccentricity: Optional[float]=None,
            distance: Optional[float]=None,
            theta: Optional[float]=None
        ) -> float:
            return 0.0
        
        @staticmethod
        def keplers_third_law(
            orbital_period: Optional[float]=None,
            semi_major_axis: Optional[float]=None,
            mass_body: Optional[float]=None
        ) -> float:
            return 0.0
        
        @staticmethod
        def schwarzschild_radius(
            shwarz_radius: Optional[float]=None,
            mass_body: Optional[float]=None,
        ) -> float: 
            return 0.0

                

