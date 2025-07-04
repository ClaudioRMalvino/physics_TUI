from typing import List, Optional, Dict
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition
from math import sqrt, sin, asin, pi


class Chapter10(PhysicsChapter):
    """
    Chapter on Fixed-Axis Rotation
    """

    def __init__(self) -> None:
        super().__init__("Fixed-Axis Rotation")

        self.var_mapping: Dict[str, str] = {
            "θ": "theta",
            "s": "arc_length",
            "r": "radius",
            "v(t)": "tang_speed",
            "r": "radius",
            "ω": "angular_vel",
            "ω(ave)": "ave_angular_vel",
            "ω₀": "init_angular_vel",
            "ω(f)": "final_angular_vel",
            "θ(f)": "theta_final",
            "θ₀": "theta_init",
            "t": "time",
            "α": "const_angular_accel",
            "Δθ": "delta_theta",
            "K": "kinetic_energy",
            "I": "moment_inertia",
            "τ": "torque",
            "F": "force",
        }

        self.equations: List[Equation] = [
            Equation(
                name="Angular position",
                formula="θ = s/r",
                variables={
                    "θ": "Angular position (rads)",
                    "s": "Arc length (m)",
                    "r": "Radius (m)",
                },
                calculation=self.Calculate.angular_position,
            ),
            Equation(
                name="Angular velocity",
                formula="ω = lim(Δt→0) Δθ/Δt = dθ/dt",
                variables={
                    "ω": "Angular velocity (rads/s)",
                    "dθ/dt": "The change in angular position with respect to \
                        time.",
                },
            ),
            Equation(
                name="Tangential speed",
                formula="v(t) = rω",
                variables={
                    "v(t)": "Tangential speed (m/s)",
                    "r": "Radius (m)",
                    "ω": "Angular velocity (rads/s)",
                },
                calculation=self.Calculate.tangential_speed,
            ),
            Equation(
                name="Angular acceleration",
                formula="α = lim(Δt→0) Δω/Δt = dω/dt = d²θ/dt²",
                variables={
                    "α": "Angular acceleration (m/s²)",
                    "d²θ/dt²": "Second derivative of the angular position \
                        with respect to time.",
                },
            ),
            Equation(
                name="Tangential acceleration",
                formula="a(t) = rα",
                variables={
                    "a(t)": "Tangential acceleration (m/s²)",
                    "r": "Radius (m)",
                    "α": "Angular acceleration (rads/s²)",
                },
            ),
            Equation(
                name="Average angular velocity",
                formula="ω(ave) = (ω₀+ω(f))/2",
                variables={
                    "ω(ave)": "Average angular velocity (rad/s)",
                    "ω₀": "Initial angular velocity (rad/s)",
                    "ω(f)": "Final angular velocity (rad/s)",
                },
                calculation=self.Calculate.average_angular_vel,
            ),
            Equation(
                name="Angular displacement",
                formula="θ(f) = θ₀ + ω(ave)t",
                variables={
                    "θ(f)": "Final angular position (rads)",
                    "θ₀": "Initial angular position (rads)",
                    "ω(ave)": "Average angular velocity (rads/s)",
                    "t": "time (s)",
                },
                calculation=self.Calculate.angular_displacement,
            ),
            Equation(
                name="Angular velocity from constant angular acceleration",
                formula="ω(f) = ω₀ + αt",
                variables={
                    "ω(f)": "Final angular velocity (rads/s)",
                    "ω₀": "Initial angular velocity (rads/s)",
                    "α": "Constant angular velocity (rads/s²)",
                    "t": "time (s)",
                },
                calculation=self.Calculate.angular_vel_const_accel,
            ),
            Equation(
                name="Angular displacement from angular velocity and \
                    constant angular acceleration",
                formula="θ(f) = θ₀ + ω₀t + ½αt²",
                variables={
                    "θ(f)": "Final angular position (rads)",
                    "θ₀": "Initial angular position (rads)",
                    "ω₀": "Initial angular velocity (rads/s)",
                    "t": "time (s)",
                    "α": "Angular acceleration (rads/s²)",
                },
                calculation=self.Calculate.angular_displacement_const_accel,
            ),
            Equation(
                name="Change in angular velocity",
                formula="ω(f)² = ω₀² + 2α(Δθ)",
                variables={
                    "ω(f)": "Final angular velocity (rads/s)",
                    "ω₀": "Initial angular velocity (rads/s)",
                    "α": "Angular acceleration (rads/s²)",
                    "Δθ": "Change in angular position (rads)",
                },
                calculation=self.Calculate.change_angular_velocity,
            ),
            Equation(
                name="Total Acceleration",
                formula="a = a(c) + a(t)",
                variables={
                    "a": "Total acceleration (m/s²)",
                    "a(c)": "Centripetal acceleration (m/s²)",
                    "a(t)": "Tangential acceleration (m/s²)",
                },
            ),
            Equation(
                name="Rotational kinetic energy",
                formula="K = ½(∑ⱼ mⱼrⱼ²)ω²",
                variables={
                    "mⱼ": "Mass of the jth object (kg)",
                    "rⱼ": "Radial distance of the jth object (m)",
                    "ω": "Angular velocity (rads/s)",
                },
            ),
            Equation(
                name="Moment of inertia",
                formula="I = ∑ⱼ mⱼrⱼ²",
                variables={
                    "I": "Moment of inertia (kg⋅m²)",
                    "mⱼ": "Mass of the jth object (kg)",
                    "rⱼ": "Radial distance of the jth object (m)",
                },
            ),
            Equation(
                name="Rotational kinetic energy in terms of the moment of \
                    inertia of a rigid body",
                formula="K = ½Iω²",
                variables={
                    "K": "Kinetic energy (J)",
                    "I": "Moment of inertia of a rigid body (kg⋅m²)",
                    "ω": "Angular velocity (rads/s)",
                },
                calculation=self.Calculate.rotational_ke,
            ),
            Equation(
                name="Moment of inertia of a continuous object",
                formula="I = ∫rdm",
                variables={
                    "I": "Moment of inertia (kg⋅m²)",
                    "r": "Distance to the axis of rotation (m)",
                    "dm": "Infinitesimal change in mass (kg)",
                },
            ),
            Equation(
                name="Parallel-axis theorem",
                formula="I(parallel-axis) = I(center of mass) + md²",
                variables={
                    "I(parallel-axis)": "Moment of interia of an object \
                        about any axis parallel to the axis through the \
                        center of mass (kg⋅m²)",
                    "I(center of mass)": "Moment of inertia through the center of mass (kg⋅m²)",
                    "m": "Mass of the object (kg)",
                    "d": "Distance from an axis through the object's center of mass \
                        to a new axis (m)",
                },
            ),
            Equation(
                name="Moment of inertia of a compound object",
                formula="I(total) = ∑ᵢ Iᵢ",
                variables={
                    "I(total)": "Total moment of inertia (kg⋅m²)",
                    "∑ᵢ Iᵢ": "The sum of all moments of inertia within the system (kg⋅m²)",
                },
            ),
            Equation(
                name="Torque vector",
                formula="τ = r × F",
                variables={
                    "τ": "Torque (N⋅m)",
                    "r": "Length of the lever arm to the axis of rotation (m)",
                    "F": "The force applied onto the lever arm (N)",
                },
            ),
            Equation(
                name="Magnitude of torque",
                formula="|τ| = r⊥F = rFsinθ",
                variables={
                    "|τ|": "Magnitude of the applied torque (N⋅m)",
                    "r": "The distance from where the force is being applied \
                        and the axis of rotation (m)",
                    "F": "The applied force (N)",
                    "θ": "The angle of the applied force relative to r (rads)",
                },
                calculation=self.Calculate.magnitude_of_torque,
            ),
            Equation(
                name="Total torque",
                formula="τ(net) = ∑ᵢ|τᵢ|",
                variables={
                    "τ(net)": "Total torque in a system (N⋅m)",
                    "∑ᵢ|τᵢ|": "The sum of all discrete torque in the system (N⋅m)",
                },
            ),
            Equation(
                name="Newton's second law for rotation",
                formula="∑ᵢτᵢ = Iα",
                variables={
                    "∑ᵢτᵢ": "The sum of all torque force (N⋅m)",
                    "I": "Moment of inertia (kg⋅m²)",
                    "α": "Angular acceleration (rads/s²)",
                },
            ),
            Equation(
                name="Incremental work done by a torque",
                formula="dW = (∑ᵢ τᵢ) dθ",
                variables={
                    "dW": "Infinitesimal change of work (J)",
                    "(∑ᵢ τᵢ)": "The sum of all discrete torque in the system (N⋅m)",
                    "dθ": "Infinitesimal change in angular position (rads)",
                },
            ),
            Equation(
                name="Work-energy theorem",
                formula="W(AB) = K(B) - K(A)",
                variables={
                    "W(AB)": "The total work done in the system (J)",
                    "K(B)": "Kinetic energy at event/location B (J)",
                    "K(A)": "Kinetic energy at event/location A (J)",
                },
            ),
            Equation(
                name="Rotational work done by a net force",
                formula="W(AB) = ∫[θ(A) to θ(B)] (∑ᵢ τᵢ) dθ",
                variables={},
            ),
            Equation(
                name="Rotational power",
                formula="P = τω",
                variables={
                    "P": "Power generated by the system (J⋅s)",
                    "τ": "Applied torque in the system (N⋅m)",
                    "ω": "Angular velocity (m/s)",
                },
            ),
        ]

        self.definitions: List[Definition] = [
            Definition(
                term="angular acceleration",
                meaning="time rate of change of angular velocity",
            ),
            Definition(
                term="angular position",
                meaning="angle a body has rotated through in a fixed coordinate system",
            ),
            Definition(
                term="angular velocity",
                meaning="time rate of change of angular position",
            ),
            Definition(
                term="instantaneous angular acceleration",
                meaning="derivative of angular velocity with respect to time",
            ),
            Definition(
                term="instantaneous angular velocity",
                meaning="derivative of angular position with respect to time",
            ),
            Definition(
                term="kinematics of rotational motion",
                meaning="describes the relationships among rotation angle, angular velocity, angular acceleration, and time",
            ),
            Definition(
                term="lever arm",
                meaning="perpendicular distance from the line that the force vector lies on to a given axis",
            ),
            Definition(
                term="linear mass density",
                meaning="the mass per unit length λ of a one dimensional object",
            ),
            Definition(
                term="moment of inertia",
                meaning="rotational mass of rigid bodies that relates to how easy or hard it will be to change the angular velocity of the rotating rigid body",
            ),
            Definition(
                term="Newton's second law for rotation",
                meaning="sum of the torques on a rotating system equals its moment of inertia times its angular acceleration",
            ),
            Definition(
                term="parallel axis",
                meaning="axis of rotation that is parallel to an axis about which the moment of inertia of an object is known",
            ),
            Definition(
                term="parallel-axis theorem",
                meaning="if the moment of inertia is known for a given axis, it can be found for any axis parallel to it",
            ),
            Definition(
                term="rotational dynamics",
                meaning="analysis of rotational motion using the net torque and moment of inertia to find the angular acceleration",
            ),
            Definition(
                term="rotational kinetic energy",
                meaning="kinetic energy due to the rotation of an object; this is part of its total kinetic energy",
            ),
            Definition(
                term="rotational work",
                meaning="work done on a rigid body due to the sum of the torques integrated over the angle through which the body rotates",
            ),
            Definition(
                term="surface mass density",
                meaning="mass per unit area σ of a two dimensional object",
            ),
            Definition(
                term="torque",
                meaning="cross product of a force and a lever arm to a given axis",
            ),
            Definition(
                term="total linear acceleration",
                meaning="vector sum of the centripetal acceleration vector and the tangential acceleration vector",
            ),
        ]

    class Calculate:
        """
        Class holds methods to calculate equations in Chapter 10
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
        def angular_position(
            theta: Optional[float] = None,
            arc_length: Optional[float] = None,
            radius: Optional[float] = None,
        ) -> float:
            """
            Function calculates the angular position as a function ofarc length
            and radius.
            Can also calculate for desired variable when arg == None and all
            other args have values.

            Args:
                theta (Optional[float], optional): angular position [rads]. Defaults to None.
                arc_length (Optional[float], optional): arc length travered (m). Defaults to None.
                radius (Optional[float], optional): radius of rotation (m). Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if r is not None and r <= 0.0:
                raise ValueError(
                    "Radius of rotational trajectory cannot be \
                    less than or equal to zero."
                )

            if arc_length is not None and arc_length < 0:
                raise ValueError("An arc length cannot be a negative value.")

            if arc_length == None:
                # Calculates the arc length traversed
                return theta * radius

            if radius == None:

                if theta == 0.0:
                    raise ValueError("Division by zero is undefined.")

                # Calculates the radius
                return arc_length / theta

            return arc_length / radius

        @staticmethod
        def tangential_speed(
            tang_speed: Optional[float] = None,
            radius: Optional[float] = None,
            angular_vel: Optional[float] = None,
        ) -> float:
            """
            Function calculates the tangential speed as a function of angular
            velocity and radius.
            Can also calculate for desired variable when arg == None and all
            other args have values.

            Args:
                tang_speed (Optional[float], optional): tangential speed [m/s]. Defaults to None.
                radius (Optional[float], optional): radius of circular trajectory [m]. Defaults to None.
                omega (Optional[float], optional): angular velocity [rads/s]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if radius is not None and radius <= 0.0:
                raise ValueError("Radius must be greater than zero.")

            if radius == None:

                if omega == 0.0:
                    raise ValueError("Divison by zero is undefined.")

                # Calculates the radius
                return tang_speed / omega

            if omega == None:
                # Calculates angular velocity
                return tang_speed / omega

            # Calculates tengential speed
            return radius * omega

        @staticmethod
        def average_angular_vel(
            ave_angular_vel: Optional[float] = None,
            init_angular_vel: Optional[float] = None,
            final_angular_vel: Optional[float] = None,
        ) -> float:
            """
            Function calculates the average angular velocity as a function of
            angular initial angular velocity and final angular velocity.
            Can also calculate for desired variable when arg == None and all
            other args have values.

            Args:
                ave_angular_vel (Optional[float], optional): average angular velocity [rads/s]. Defaults to None.
                init_angular_vel (Optional[float], optional): initial angular velocity [rads/s]. Defaults to None.
                final_angular_vel (Optional[float], optional): final angular velocity [rads/s]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if init_angular_vel == None:
                # Calculates initial angular velocity
                return (2.0 * ave_angular_vel) - final_angular_vel

            if final_angular_vel == None:
                # Calculates final angular velocity
                return (2.0 * ave_angular_vel) - init_angular_vel

            return (init_angular_vel + final_angular_vel) / 2.0

        @staticmethod
        def angular_displacement(
            theta_final: Optional[float] = None,
            theta_init: Optional[float] = None,
            ave_angular_vel: Optional[float] = None,
            time: Optional[float] = None,
        ) -> float:
            """
            Function calculates the angular displacement as a function of
            initial theta, average angular velocity, and time.
            Can also calculate for desired variable when arg == None and all
            other args have values.

            Args:
                theta_final (Optional[float], optional): final angular position [rads]. Defaults to None.
                theta_init (Optional[float], optional): initial angular position [rads]. Defaults to None.
                ave_angular_vel (Optional[float], optional): average angular velocity [rads/s]. Defaults to None.
                time (Optional[float], optional): time [s]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """
            if time is not None and time < 0:
                raise ValueError("Time cannot be a negative value.")

            if theta_init == None:
                # Calculates initial angular position
                return theta_final - ave_angular_vel * time

            if ave_angular_vel == None:

                if time == 0.0:
                    raise ValueError("Division by zero is undefined.")
                # Calculates average angular velocity
                return (theta_final - theta_init) / time

            if time == None:

                if ave_angular_vel == 0.0:
                    raise ValueError("Division by zero is undefined.")
                return (theta_final - theta_init) / ave_angular_vel

            return theta_init + (ave_angular_vel * time)

        @staticmethod
        def angular_vel_const_accel(
            final_angular_vel: Optional[float] = None,
            init_angular_vel: Optional[float] = None,
            const_angular_accel: Optional[float] = None,
            time: Optional[float] = None,
        ) -> float:
            """
            Function calculates the angular velocity as a function
            of initial angular velocity, constant angular acceleration
            and time.
            Can also calculate for desired variable when arg == None
            and all other args have values.

            Args:
                final_angular_vel (Optional[float], optional): final angular velocity [rads/s]. Defaults to None.
                init_angular_vel (Optional[float], optional): initial angular velocity [rads/s]. Defaults to None.
                const_angular_accel (Optional[float], optional): constant angular accceleration [rads/s²]. Defaults to None.
                time (Optional[float], optional): time [s]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if time is not None and time < 0:
                raise ValueError("Time cannot be a negative value.")

            if init_angular_vel == None:
                # Calculates the initial angular velocity
                return final_angular_vel - (const_angular_accel * time)

            if const_angular_accel == None:

                if time == 0.0:
                    raise ValueError("Division by zero is undefined.")

                # Calculates the constant angular acceleration
                return (final_angular_vel - init_angular_vel) / time

            return init_angular_vel + (const_angular_accel * time)

        @staticmethod
        def angular_displacement_const_accel(
            theta_final: Optional[float] = None,
            theta_init: Optional[float] = None,
            init_angular_vel: Optional[float] = None,
            time: Optional[float] = None,
            const_angular_accel: Optional[float] = None,
        ) -> float:
            """
            Function calculates the angular displacement as a function
            of initial angular position, initial angular velocity,
            constant angular acceleration, and time.
            Can also calculate for desired variable when arg == None
            and all other args have values.

            Args:
                theta_final (Optional[float], optional): final angular position [rads]. Defaults to None.
                theta_init (Optional[float], optional): initial angular position [rads]. Defaults to None.
                init_angular_vel (Optional[float], optional): initial angular velocity [rads/s]. Defaults to None.
                time (Optional[float], optional): time [s]. Defaults to None.
                const_angular_accel (Optional[float], optional): constant angular accceleration [rads/s²]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if time is not None and time < 0:
                raise ValueError("Time cannot be a negative value.")

            if theta_init == None:
                # Calculates initial angular position
                return (
                    theta_final
                    - (init_angular_vel * time)
                    - (0.5 * const_angular_accel * (time * time))
                )

            if init_angular_vel == None:

                if time == 0.0:
                    raise ValueError("Division by zero is undefined.")

                return (
                    theta_final
                    - theta_init
                    - (0.5 * const_angular_accel * (time * time))
                ) / time

            if const_angular_accel == None:

                if time == 0.0:
                    raise ValueError("Division by zero is undefined.")

                # Calculates for constant angular acceleration
                return (theta_final - theta_init - (init_angular_vel * time)) * (
                    2.0 / (time * time)
                )

            if time is None:

                # Calculates for time
                c: float = theta_init - theta_final
                b: float = init_angular_vel
                a: float = 0.5 * const_angular_accel
                roots: Tuple[float, float] = Chapter10.Calculate.quadratic_eq(a, b, c)

                if roots is None:
                    raise ValueError("No real solution for time")

                # Return the non-negative root, preferring the smaller positive one
                valid_roots: List[float] = [r for r in roots if r >= 0]

                if not valid_roots:
                    raise ValueError("No positive time solution")

                return round(min(valid_roots), 4)

            return (
                theta_init
                + (init_angular_vel * time)
                + (0.5 * (const_angular_accel * (time * time)))
            )

        @staticmethod
        def change_angular_velocity(
            final_angular_vel: Optional[float] = None,
            init_angular_vel: Optional[float] = None,
            const_angular_accel: Optional[float] = None,
            delta_theta: Optional[float] = None,
        ) -> float:
            """
            Function calculates the change in angular velocity as a function
            of initial angular position, constant angular acceleration,
            and angular displacement.
            Can also calculate for desired variable when arg == None
            and all other args have values.

            Args:
                final_angular_vel (Optional[float], optional): final angular velocity [rads/s]. Defaults to None.
                init_angular_vel (Optional[float], optional): initial angular velocity [rads/s]. Defaults to None.
                const_angular_accel (Optional[float], optional): constant angular acceleration [rads/s²]. Defaults to None.
                delta_theta (Optional[float], optional): the change in angular position [rads]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if init_angular_vel == None:

                radicand: float = (final_angular_vel * final_angular_vel) - (
                    2 * const_angular_accel * delta_theta
                )
                if radicand < 0:
                    raise ValueError(
                        "A negative radicand yields a complex number.\
                        Check your values."
                    )

                # Calculates initial angular velocity
                return sqrt(radicand)

            if const_angular_accel == None:

                if delta_theta == 0.0:
                    raise ValueError("Divison by zero is undefined.")

                # Calculates the constant angular acceleration
                return (
                    (final_angular_vel * final_angular_vel)
                    - (init_angular_vel * init_angular_vel)
                ) / (2 * delta_theta)

            if delta_theta == None:

                if const_angular_accel == 0.0:
                    raise ValueError("Division by zero is undefined.")

                # Calculates the change in angular position
                return (
                    (final_angular_vel * final_angular_vel)
                    - (init_angular_vel * init_angular_vel)
                ) / (2 * delta_theta)

            radicand: float = (
                init_angular_vel * init_angular_vel
            ) + 2 * const_angular_accel * delta_theta

            if radicand < 0.0:
                raise ValueError(
                    "A negative radicand yields a complex number.\
                        Check your values."
                )

            return sqrt(radicand)

        @staticmethod
        def rotational_ke(
            kinetic_energy: Optional[float] = None,
            moment_inertia: Optional[float] = None,
            angular_vel: Optional[float] = None,
        ) -> float:
            """
            Function calculates the rotational kinetic energy as a function
            of the moment of inertia and angular velocity.
            Can also calculate for desired variable when arg == None
            and all other args have values.

            Args:
                kinetic_energy (Optional[float], optional): rotational kinetic energy [J]. Defaults to None.
                moment_inertia (Optional[float], optional): moment of inertia (kg⋅m²). Defaults to None.
                angular_vel (Optional[float], optional): angular velocity [rads/s]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if moment_inertia is not None and moment_inertia < 0.0:
                raise ValueError("The moment of inertia cannot be a negative value.")

            if moment_inertia == None:

                if angular_vel == 0.0:
                    raise ValueError("Divison by zero is undefined.")

                return (2.0 * kinetic_energy) / (angular_vel * angular_vel)

            if angular_vel == None:

                if moment_inertia == 0.0:
                    raise ValueError("Divison by zero is undefined.")

                radicand: float = (2.0 * kinetic_energy) / moment_inertia

                if radicand < 0:
                    raise ValueError(
                        "A negative radicand yields a complex number.\
                        Check your values."
                    )

                return sqrt(radicand)

            return 0.5 * moment_inertia * (angular_vel * angular_vel)

        @staticmethod
        def magnitude_of_torque(
            torque: Optional[float] = None,
            radius: Optional[float] = None,
            force: Optional[float] = None,
            theta: Optional[float] = None,
        ) -> float:
            """
            Function calculates the magnitude of torque as a function
            of the the distance from the axis of rotation to the applied
            force and the force.
            Can also calculate for desired variable when arg == None
            and all other args have values.

            Args:
                torque (Optional[float], optional): torque in the system [N⋅m]. Defaults to None.
                radius (Optional[float], optional): distance from axis of rotation to applied force [m]. Defaults to None.
                force (Optional[float], optional): applied force [N]. Defaults to None.
                theta (Optional[float], optional): angle between distance r and applied force [rads]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """
            if theta is not None:
                theta_radians: float = theta * (pi / 180.0)

            if radius is not None and radius <= 0.0:
                raise ValueError(
                    "The length of the center of axis to applied\
                    force cannot be less than or equal to zero."
                )

            if radius == None:
                # Calculates the distance r
                return torque / (force * sin(theta_radians))

            if force == None:
                # Calculates the force
                return torque / (radius * sin(theta_radians))

            if theta == None:

                if force == 0.0:
                    raise ValueError("Division by zero is undefined.")

                # Calculates theta
                argument: float = torque / (radius * force)
                return asin(argument) * (180 / pi)

            return radius * force * sin(theta_radians)
