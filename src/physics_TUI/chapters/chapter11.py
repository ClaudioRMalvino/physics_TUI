from typing import List, Optional, Dict
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition
from math import sqrt, sin, asin, pi

# Global constant
g: float = 9.82  # Gravitational acceleration on Earth


class Chapter11(PhysicsChapter):
    """
    Chapter on Angular Momentum
    """

    def __init__(self) -> None:
        super.__init__("Angular Momentum")

        self.var_mapping: Dict[str, str] = {
            "a(CM)": "accel",
            "m": "mass",
            "M": "mass",
            "I(CM)": "moment_inertia",
            "I": "moment_inertia",
            "r": "radius",
            "θ": "theta",
            "L": "angular_momentum",
            "ω": "angular_vel",
            "ωₚ": "processional_ang_vel",
        }

        self.equations: List[Equation] = [
            Equation(
                name="Velocity of center of mass of rolling body",
                formula="v(CM) = Rω",
                variables={
                    "v(CM)": "Velocity of the center of mass (m/s)",
                    "R": "Radius of the rolling body (m)",
                    "ω": "Angular velocity about its axis (rads/s)",
                },
            ),
            Equation(
                name="Acceleration of center of mass of rolling body",
                formula="a(CM) = Rα",
                variables={
                    "a(CM)": "Acceleration of the center of mass (m/s²)",
                    "R": "Radius of the rolling body (m)",
                    "α": "Angular acceleration about its axis (rads/s²)",
                },
            ),
            Equation(
                name="Displacement of center of mass of rolling object",
                formula="d(CM) = Rθ",
                variables={
                    "d(CM)": "Displacement of cetner of mass (m)",
                    "R": "Radius of the rolling body (m)",
                    "θ": "Angular position of the center of mass (rads)",
                },
            ),
            Equation(
                name="Acceleration of an object rolling without slipping",
                formula="a(CM) = (mgsinθ)/(m+(I(CM)/r²))",
                variables={
                    "a(CM)": "Acceleration of the object (m/s²)",
                    "m": "Mass of the object (kg)",
                    "I(CM)": "Moment of inertia for the center of mass (kg⋅m²)",
                    "r": "radius of the object (m)",
                    "θ": "The angle between the normal force and gravitational force (rads)",
                },
                calculation=self.Calculate.accel_without_slipping,
            ),
            Equation(
                name="Angular momentum",
                formula="L = r × p",
                variables={
                    "L": "Angular momentum (J⋅s)",
                    "r": "Position vector of the object (m)",
                    "p": "Momentum vector of the object (kg⋅m/s)",
                },
            ),
            Equation(
                name="Derivative of angular momentum",
                formula="dL/dt = ∑τ",
                variables={},
            ),
            Equation(
                name="Angular momentum of a system of particles",
                formula="L = l₁ + l₂ + ... + l(N)",
                variables={},
            ),
            Equation(
                name="Angular momentum of a rotating rigid body",
                formula="L = Iω",
                variables={
                    "L": "Angular momentum (J⋅s)",
                    "I": "Moment of inertia (kg⋅m²)",
                    "ω": "Angular velocity (m/s)",
                },
                calculation=self.Calculate.ang_momentum_rigid_body,
            ),
            Equation(
                name="Conservation of angular momentum",
                formula="dL/dt = 0",
                variables={},
            ),
            Equation(
                name="Conservation of angular momentum",
                formula="L = l₁ + l₂ + ... + I(N) = constant",
                variables={},
            ),
            Equation(
                name="Processional angular velocity",
                formula="ωₚ = (rMg)/(Iω)",
                variables={
                    "ωₚ": "Processional angular velocity (m/s)",
                    "r": "Distance from center of mass and the pivot point (m)",
                    "M": "Mass of the rotating body (kg)",
                    "I": "Moment of inertia (kg⋅m²)",
                    "ω": "Angular velocity (rads/s)",
                },
                calculation=self.Calculate.processional_ang_vel,
            ),
        ]

        self.definitions: List[Definition] = [
            Definition(
                term="angular momentum",
                meaning="rotational analog of linear momentum, found by taking the product of moment of inertia and angular velocity",
            ),
            Definition(
                term="law of conservation of angular momentum",
                meaning="angular momentum is conserved, that is, the initial angular momentum is equal to the final angular momentum when no external torque is applied to the system",
            ),
            Definition(
                term="precession",
                meaning="circular motion of the pole of the axis of a spinning object around another axis due to a torque",
            ),
            Definition(
                term="rolling motion",
                meaning="combination of rotational and translational motion with or without slipping",
            ),
        ]

        class Calculate:
            """
            Class holds methods to calculate equations in Chapter 11
            """

            @staticmethod
            def accel_without_slipping(
                accel: Optional[float] = None,
                mass: Optional[float] = None,
                moment_inertia: Optional[float] = None,
                radius: Optional[float] = None,
                theta: Optional[float] = None,
            ) -> float:
                """
                Function calculates the acceleration of a rolling body
                without slipping as a function of its mass, moment of
                inertia, radius, and the normal force.
                Can also calculate for desired variable when arg == None and all
                other args have values.

                Args:
                    accel (Optional[float], optional): acceleration of the body [m/s²]. Defaults to None.
                    mass (Optional[float], optional): mass of the object [kg]. Defaults to None.
                    moment_inertia (Optional[float], optional): moment of inertia [kg⋅m²]. Defaults to None.
                    radius (Optional[float], optional): radius of the rolling body [m]. Defaults to None.
                    theta (Optional[float], optional): angle between normal force and gravity [rads]. Defaults to None.

                Returns:
                    float: the result of whichever variable was left equal to None
                """
                if theta is not None:
                    theta_radians: float = theta * (pi / 180.0)

                if mass is not None and mass <= 0.0:
                    raise ValueError(
                        "We are operating with massive objects. \
                        Make sure all objects have a mass greater than zero."
                    )

                if moment_inertia is not None and moment_inertia < 0.0:
                    raise ValueError(
                        "The moment of inertia cannot be a negative value."
                    )

                if radius is not None and radius <= 0.0:
                    raise ValueError("Radius cannot be less than or equal to zero.")

                if mass == None:
                    # Calculates the mass
                    numerator: float = (
                        (accel / (g * sin(theta_radians))) - 1.0
                    ) * moment_inertia

                    denominator: float = radius * radius

                    return numerator / denominator

                if moment_inertia == None:

                    if accel == 0.0:
                        raise ValueError("Division by zero is undefined.")

                    # Calculates the moment of inertia
                    terms: float = ((g * sin(theta_radians)) / accel) - 1.0
                    coefficient: float = mass * (radius * radius)

                    return terms * coefficient

                if radius == None:

                    if accel == 0.0:
                        raise ValueError("Division by zero is undefined.")

                    # Calculates the radius
                    denominator: float = (
                        ((g * sin(theta_radians)) / accel) - 1.0
                    ) * mass

                    radicand: float = moment_inertia / denominator

                    if radicand < 0:
                        raise ValueError(
                            "Negative radicand yields a complex number. \
                            Check your values."
                        )

                    return sqrt(radicand)

                if theta == None:

                    numerator: float = accel * (
                        mass + (moment_inertia / (radius * radius))
                    )

                    denominator: float = mass * g

                    argument: float = numerator / denominator

                    return asin(argument) * (180.0 / pi)

                numerator: float = mass * g * sin(theta_radians)
                denominator: float = mass + (moment_inertia / (radius * radius))

                return numerator / denominator

            @staticmethod
            def ang_momentum_rigid_body(
                angular_momentum: Optional[float] = None,
                moment_interia: Optional[float] = None,
                angular_vel: Optional[float] = None,
            ) -> float:
                """
                Function calculates the angular momentum of a rigid body
                as a function of the moment of inertia and the angular velocity.
                Can also calculate for desired variable when arg == None and all
                other args have values.

                Args:
                    angular_momentum (Optional[float], optional): angular momentum [J⋅s]. Defaults to None.
                    moment_interia (Optional[float], optional): moment of inertia [kg⋅m²]. Defaults to None.
                    angular_vel (Optional[float], optional): angular velocity [m/s]. Defaults to None.

                Returns:
                    float: the result of whichever variable was left equal to None
                """

                if moment_interia is not None and moment_interia < 0.0:
                    raise ValueError(
                        "The moment of inertia cannot be a negative value."
                    )

                if moment_interia == None:

                    if angular_vel == 0.0:
                        raise ValueError("Division by zero is undefined.")

                    # Calculates moment of inertia
                    return angular_momentum / angular_vel

                if angular_vel == 0.0:

                    if moment_interia == 0.0:
                        raise ValueError("Divison by zero is undefined.")

                    # Calculates angular velocity
                    return angular_momentum / moment_interia

                return moment_interia * angular_vel

            @staticmethod
            def processional_ang_vel(
                proccesional_ang_vel: Optional[float] = None,
                radius: Optional[float] = None,
                mass: Optional[float] = None,
                moment_inertia: Optional[float] = None,
                angular_vel: Optional[float] = None,
            ) -> float:
                """
                Function calculates the processional angular velocity
                of a rigid body as a function of the moment of inertia,
                mass of the object, distance from center of mass and the pivot
                point, and the angular velocity.
                Can also calculate for desired variable when arg == None and all
                other args have values.

                Args:
                    proccesional_ang_vel (Optional[float], optional): precessional angular velocity [rads/s]. Defaults to None.
                    radius (Optional[float], optional): distance from pivot point and center of mass [m]. Defaults to None.
                    mass (Optional[float], optional): mass of the body [m]. Defaults to None.
                    moment_inertia (Optional[float], optional): moment of inertia [kg⋅m²]. Defaults to None.
                    angular_vel (Optional[float], optional): angular velocity [rads/s]. Defaults to None.

                Returns:
                    float: the result of whichever variable was left equal to None
                """

                if mass is not None and mass <= 0.0:
                    raise ValueError(
                        "We are operating with massive objects. \
                        Make sure all objects have a mass greater than zero."
                    )

                if moment_inertia is not None and moment_inertia < 0.0:
                    raise ValueError(
                        "The moment of inertia cannot be a negative value."
                    )

                if radius is not None and radius <= 0.0:
                    raise ValueError("Radius cannot be less than or equal to zero.")

                if radius == None:

                    # Calculates the radius
                    numerator: float = moment_inertia * angular_vel
                    denominator: float = mass * g

                    return proccesional_ang_vel * (numerator / denominator)

                if mass == None:

                    # Calculates the mass
                    numerator: float = moment_inertia * angular_vel
                    denominator: float = radius * g

                    return proccesional_ang_vel * (numerator / denominator)

                if moment_inertia == None:

                    if angular_vel == 0.0 or proccesional_ang_vel == 0.0:
                        raise ValueError("Division by zero is undefined.")

                    # Calculates the moment of inertia
                    numerator: float = radius * mass * g
                    denominator: float = proccesional_ang_vel * angular_vel

                    return numerator / denominator

                if angular_vel == None:

                    if angular_vel == 0.0:
                        raise ValueError("Division by zero is undefined.")

                    # Calculates the angular velocity
                    numerator: float = radius * mass * g
                    denominator: float = proccesional_ang_vel * moment_inertia

                    return numerator / denominator

                if angular_vel == 0.0 or moment_inertia == 0.0:
                    raise ValueError("Division by zero is undefined.")

                numerator: float = radius * mass * g
                denominator: float = moment_inertia * angular_vel

                return numerator / denominator
