from typing import List, Optional, Dict
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition

class Chapter10(PhysicsChapter):
    """
    Chapter on Fixed-Axis Rotation
    """

    def __init__(self) -> None:
        super().__init__("Fixed-Axis Rotation")

        self.var_mapping: Dict[str, str] = {}

        self.equations: List[Equation] = [
            Equation(
                name="Angular position",
                formula="θ = s/r",
                variables={
                    "θ": "Angular position (rads)",
                    "s": "Arc length (m)",
                    "r": "Radius (m)"
                },
                calculation=self.Calculate.angular_position
            ),
            Equation(
                name="Angular velocity",
                formula="ω = lim(Δt→0) Δθ/Δt = dθ/dt",
                variables={
                    "ω": "Angular velocity (rads/s)",
                    "dθ/dt": "The change in angular position with respect to \
                        time."
                }
            ),
            Equation(
                name="Tangential speed",
                formula="v(t) = rω",
                variables={
                    "v(t)": "Tangential speed (m/s)",
                    "r": "Radius (m)",
                    "ω": "Angular velocity (rads/s)"
                },
                calculation=self.Calculate.tangential_speed
            ),
            Equation(
                name="Angular acceleration",
                formula="α = lim(Δt→0) Δω/Δt = dω/dt = d²θ/dt²",
                variables={
                    "α": "Angular acceleration (m/s²)",
                    "d²θ/dt²": "Second derivative of the angular position \
                        with respect to time."
                }
            ),
            Equation(
                name="Tangential acceleration",
                formula="a(t) = rα",
                variables={
                    "a(t)": "Tangential acceleration (m/s²)",
                    "r": "Radius (m)",
                    "α": "Angular acceleration (rads/s²)"
                },
                calculation=self.Calculate.tangential_accel
            ),
            Equation(
                name="Average angular velocity",
                formula="ω(ave) = (ω₀+ω(f))/2",
                variables={
                    "ω(ave)": "Average angular velocity (rad/s)",
                    "ω₀": "Initial angular velocity (rad/s)",
                    "ω(f)": "Final angular velocity (rad/s)",
                },
                calculation=self.Calculate.average_angular_vel
            ),
            Equation(
                name="Angular displacement",
                formula="θ(f) = θ₀ + ω(ave)t",
                variables={
                    "θ(f)": "Final angular position (rads)",
                    "θ₀": "Initial angular position (rads)",
                    "ω(ave)": "Average angular velocity (rads/s)",
                    "t": "time (s)"
                },
                calculation=self.Calculate.angular_displacement
            ),
            Equation(
                name="Angular velocity from constant angular acceleration",
                formula="ω(f) = ω₀ + αt",
                variables={
                    "ω(f)": "Final angular velocity (rads/s)",
                    "ω₀": "Initial angular velocity (rads/s)",
                    "α": "Constant angular velocity (rads/s²)",
                    "t": "time (s)"
                },
                calculation=self.Calculate.angular_vel_const_accel
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
                    "α": "Angular acceleration (rads/s²)"
                },
                calculation=self.Calculate.angular_displacement_const_accel
            ),
            Equation(
                name="Change in angular velocity",
                formula="ω(f)² = ω₀² + 2α(Δθ)",
                variables={
                    "ω(f)": "Final angular velocity (rads/s)",
                    "ω₀": "Initial angular velocity (rads/s)",
                    "α": "Angular acceleration (rads/s²)",
                    "Δθ": "Change in angular position (rads)"
                },
                calculation=self.Calculate.change_angular_velocity
            ),
            Equation(
                name="Total Acceleration",
                formula="a = a(c) + a(t)",
                variables={
                    "a" : "Total acceleration (m/s²)",
                    "a(c)": "Centripetal acceleration (m/s²)",
                    "a(t)": "Tangential acceleration (m/s²)"
                }
            ),
            Equation(
                name="Rotational kinetic energy",
                formula="K = ½(∑ⱼ mⱼrⱼ²)ω²",
                variables={
                    "mⱼ": "Mass of the jth object (kg)",
                    "rⱼ": "Radial distance of the jth object (m)",
                    "ω": "Angular velocity (rads/s)"
                }
            ),
            Equation(
                name="Moment of inertia",
                formula="I = ∑ⱼ mⱼrⱼ²",
                variables={
                    "I": "Moment of inertia (kg⋅m²)",
                    "mⱼ": "Mass of the jth object (kg)",
                    "rⱼ": "Radial distance of the jth object (m)",
                }
            ),
            Equation(
                name="Rotational kinetic energy in terms of the moment of \
                    inertia of a rigid body",
                formula="K = ½Iω²",
                variables={
                    "K": "Kinetic energy (J)",
                    "I": "Moment of inertia of a rigid body (kg⋅m²)",
                    "ω²": "Angular velocity (rads/s)"
                },
                calculation=self.Calculate.rotational_ke
            ),
            Equation(
                name="Moment of inertia of a continuous object",
                formula="I = ∫rdm",
                variables={
                    "I": "Moment of inertia (kg⋅m²)",
                    "r": "Distance to the axis of rotation (m)",
                    "dm": "Infinitesimal change in mass (kg)"
                }
            ),
            Equation(
                name="Parallel-axis theorem",
                formula="I(parallel-axis) = I(center of mass) + md²",
                variables={
                    "I(parallel-axis)": "Moment of interia of an object \
                        about any axis parallel to the axis through the \
                        center of mass (kg⋅m²)",
                    "I(center of mass)":  "Moment of inertia through the center of mass (kg⋅m²)",
                    "m": "Mass of the object (kg)",
                    "d": "Distance from an axis through the object's center of mass \
                        to a new axis (m)"
                }
            ),
            Equation(
                name="Moment of inertia of a compound object",
                formula="I(total) = ∑ᵢ Iᵢ",
                variables={
                    "I(total)": "Total moment of inertia (kg⋅m²)",
                    "∑ᵢ Iᵢ": "The sum of all moments of inertia within the system (kg⋅m²)"
                }
            ),
            Equation(
                name="Torque vector",
                formula="τ = r × F",
                variables={
                    "τ": "Torque (N⋅m)",
                    "r": "Length of the lever arm to the axis of rotation (m)",
                    "F": "The force applied onto the lever arm (N)"
                }
            ),
            Equation(
                name="Magnitude of torque",
                formula="|τ| = r⊥F = rFsinθ",
                variables={
                    "|τ|": "Magnitude of the applied torque (N⋅m)",
                    "r": "The distance from where the force is being applied \
                        and the axis of rotation (m)",
                    "F": "The applied force (N)",
                    "θ": "The angle of the applied force relative to r (rads)"   
                },
                calculation=self.Calculate.magnitude_of_torque
            ),
            Equation(
                name="Total torque",
                formula="τ(net) = ∑ᵢ|τᵢ|",
                variables={
                    "τ(net)": "Total torque in a system (N⋅m)",
                    "∑ᵢ|τᵢ|": "The sum of all discrete torque in the system (N⋅m)"
                }
            ),
            Equation(
                name="Newton's second law for rotation",
                formula="∑ᵢτᵢ = Iα",
                variables={
                    "∑ᵢτᵢ": "The sum of all torque force (N⋅m)",
                    "I": "Moment of inertia (kg⋅m²)",
                    "α": "Angular acceleration (rads/s²)"
                }
            ),
            Equation(
                name="Incremental work done by a torque",
                formula="dW = (∑ᵢ τᵢ) dθ",
                variables={
                    "dW": "Infinitesimal change of work (J)",
                    "(∑ᵢ τᵢ)": "The sum of all discrete torque in the system (N⋅m)",
                    "dθ": "Infinitesimal change in angular position (rads)"
                }
            ),
            Equation(
                name="Work-energy theorem",
                formula="W(AB) = K(B) - K(A)",
                variables={
                    "W(AB)": "The total work done in the system (J)",
                    "K(B)": "Kinetic energy at event/location B (J)",
                    "K(A)": "Kinetic energy at event/location A (J)"
                }
            ),
            Equation(
                name="Rotational work done by a net force",
                formula="W(AB) = ∫[θ(A) to θ(B)] (∑ᵢ τᵢ) dθ"
            ),
            Equation(
                name="Rotational power",
                formula="P = τω",
                variables={
                    "P": "Power generated by the system (J⋅s)",
                    "τ": "Applied torque in the system (N⋅m)",
                    "ω": "Angular velocity (m/s)"
                }
            )
        ]

        self.definitions: List[Definition] = [
            Definition(
                term="angular acceleration",
                meaning="time rate of change of angular velocity"
            ),
            Definition(
                term="angular position", 
                meaning="angle a body has rotated through in a fixed coordinate system"
            ),
            Definition(
                term="angular velocity",
                meaning="time rate of change of angular position"
            ),
            Definition(
                term="instantaneous angular acceleration",
                meaning="derivative of angular velocity with respect to time"
            ),
            Definition(
                term="instantaneous angular velocity",
                meaning="derivative of angular position with respect to time"
            ),
            Definition(
                term="kinematics of rotational motion",
                meaning="describes the relationships among rotation angle, angular velocity, angular acceleration, and time"
            ),
            Definition(
                term="lever arm",
                meaning="perpendicular distance from the line that the force vector lies on to a given axis"
            ),
            Definition(
                term="linear mass density",
                meaning="the mass per unit length λ of a one dimensional object"
            ),
            Definition(
                term="moment of inertia",
                meaning="rotational mass of rigid bodies that relates to how easy or hard it will be to change the angular velocity of the rotating rigid body"
            ),
            Definition(
                term="Newton's second law for rotation",
                meaning="sum of the torques on a rotating system equals its moment of inertia times its angular acceleration"
            ),
            Definition(
                term="parallel axis",
                meaning="axis of rotation that is parallel to an axis about which the moment of inertia of an object is known"
            ),
            Definition(
                term="parallel-axis theorem",
                meaning="if the moment of inertia is known for a given axis, it can be found for any axis parallel to it"
            ),
            Definition(
                term="rotational dynamics",
                meaning="analysis of rotational motion using the net torque and moment of inertia to find the angular acceleration"
            ),
            Definition(
                term="rotational kinetic energy",
                meaning="kinetic energy due to the rotation of an object; this is part of its total kinetic energy"
            ),
            Definition(
                term="rotational work",
                meaning="work done on a rigid body due to the sum of the torques integrated over the angle through which the body rotates"
            ),
            Definition(
                term="surface mass density",
                meaning="mass per unit area σ of a two dimensional object"
            ),
            Definition(
                term="torque",
                meaning="cross product of a force and a lever arm to a given axis"
            ),
            Definition(
                term="total linear acceleration",
                meaning="vector sum of the centripetal acceleration vector and the tangential acceleration vector"
            ),
        ]

    class Calculate:
        """
        Class holds methods to calculate equations in Chapter 10
        """

        @staticmethod
        def angular_position(
            theta: Optional[float]=None,
            arc_length: Optional[float]=None,
            radius: Optional[float]=None
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
                raise ValueError("Radius of rotational trajectory cannot be \
                    less than or equal to zero.")

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
        
        @staticmethod
        def tangential_speed(
            tang_speed: Optional[float]=None,
            radius: Optional[float]=None,
            omega: Optional[float]=None
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
            ave_angular_vel: Optional[float]=None,
            init_angular_vel: Optional[float]=None,
            final_angular_vel: Optional[float]=None
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
            