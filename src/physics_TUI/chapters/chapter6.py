from typing import Dict, List, Optional
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition
from math import sqrt, tan, atan, pi

# Global constant
g: float = 9.82 # gravitational acceleration on Earth [m/s^2]

class Chapter6(PhysicsChapter):
    """
    Chapter on Applications of Newton's Laws
    """

    def __init__(self) -> None:
        super().__init__("Applications of Newton's Laws")
        
        self.var_mapping: Dict[str, str] = {
            "m": "mass",
            "r": "radius",
            "F(c)": "centripetal_F",
            "v": "velocity",
            "ω": "angular_vel",
            "θ": "theta",
            "F(D)": "drag_F",
            "C": "drag_coeff",
            "ρ": "fluid_dens",
            "A": "area",
            "Fₛ": "drag_Fs",
            "η": "viscosity",
            "vₜ": "terminal_vel",
        }

        self.equations: List[Equation] = [
            Equation(
                name="Magnitude of static friction",
                formula="fₛ ≤ μₛN",
                variables={
                    "fₛ": "Static friction [N]",
                    "μₛ": "coefficient of static friction (dimensionless)",
                    "N": "Normal force (N)"
                }
            ),
            Equation(
                name="Magnitude of kinetic friction",
                formula="fₖ = μₖN",
                variables={
                    "fₖ": "Kinetic friction (N)",
                    "μₖ": "Coefficient of kinetic friction (dimensionless)",
                    "N": "Normal force (N)"
                }
            ),
            Equation(
                name="Centripetal force with tangential velocity",
                formula="F(c) = mv²/r",
                variables={
                    "F(c)": "Centripetal force (N)",
                    "m": "Mass of the object (kg)",
                    "v": "Tangential velocity (m/s)",
                    "r": "Radius (m)"
                },
                calculation=self.Calculate.centripetalForceTangVel
            ),
            Equation(
                name="Centripetal force with angular velocity",
                formula="F(c) = mrω²",
                variables={
                    "F(c)": "Centripetal force (N)",
                    "m": "Mass of the object (kg)",
                    "ω": "Tangential velocity (rads/s)",
                    "r": "Radius (m)"
                },
                calculation=self.Calculate.centripetalForceAngVel
            ),
            Equation(
                name="Ideal angle of a banked curve",
                formula="tan θ = v²/rg",
                variables={
                    "θ": "Ideal angle (degrees)",
                    "v": "Velocity (m/s)",
                    "r": "Radius of curvature (m)",
                },
                calculation=self.Calculate.idealAngBankedCurve
            ),
            Equation(
                name="Drag force",
                formula="F(D) = ½CρAv²",
                variables={
                    "F(D)": "Drag force (N)",
                    "C": "Drag coefficient (dimensionless)",
                    "ρ": "Fluid density (kg/m³)",
                    "A": "Area of the object (m²)",
                    "v": "Velocity of the object (m/s)"
                },
                calculation=self.Calculate.dragForce
            ),
            Equation(
                name="Stoke's law",
                formula="Fₛ = 6πrηv",
                variables={
                    "Fₛ": "Drag force (Stokes force) (N)",
                    "r": "Radius of the object (m)",
                    "η": "Dynamic viscosity of the fluid (N⋅s/m²)",
                    "v": "Velocity of the object (m/s)"
                },
                calculation=self.Calculate.stokesLaw
            ),
            Equation(
                name="Terminal velocity",
                formula="vₜ = √(2mg/ρCA)",
                variables={
                    "vₜ": "Terminal velocity (m/s)",
                    "m": "Mass of the object (kg)",
                    "C": "Drag coefficient (dimensionless)",
                    "A": "Area of the object (m²)",
                    "ρ": "Fluid density (kg/m³)",
                },
                calculation=self.Calculate.terminalVelocity
            )
        ]

        self.definitions: List[Definition] = [
            Definition(
                term="banked curve",
                meaning="curve in a road that is sloping in a manner that helps a vehicle negotiate the curve"
            ),
            Definition(
                term="centripetal force",
                meaning="any net force causing uniform circular motion"
            ),
            Definition(
                term="Coriolis force",
                meaning="inertial force causing the apparent deflection of moving objects when viewed in a rotating frame of reference"
            ),
            Definition(
                term="drag force",
                meaning="force that always opposes the motion of an object in a fluid; unlike simple friction, the drag force is proportional to some function of the velocity of the object in that fluid"
            ),
            Definition(
                term="friction",
                meaning="force that opposes relative motion or attempts at motion between systems in contact"
            ),
            Definition(
                term="ideal banking",
                meaning="sloping of a curve in a road, where the angle of the slope allows the vehicle to negotiate the curve at a certain speed without the aid of friction between the tires and the road; the net external force on the vehicle equals the horizontal centripetal force in the absence of friction"
            ),
            Definition(
                term="inertial force",
                meaning="force that has no physical origin"
            ),
            Definition(
                term="kinetic friction",
                meaning="force that opposes the motion of two systems that are in contact and moving relative to each other"
            ),
            Definition(
                term="noninertial frame of reference",
                meaning="accelerated frame of reference"
            ),
            Definition(
                term="static friction",
                meaning="force that opposes the motion of two systems that are in contact and are not moving relative to each other"
            ),
            Definition(
                term="terminal velocity",
                meaning="constant velocity achieved by a falling object, which occurs when the weight of the object is balanced by the upward drag force"
            )
        ]
    class Calculate:
        """
        Class holds methods to calculate equations in Chapter 6
        """

        @staticmethod
        def centripetalForceTangVel(
            centripetal_F: Optional[float]=None,
            mass: Optional[float]=None,
            velocity: Optional[float]=None,
            radius: Optional[float]=None
        ) -> float:
            """
            Function calculates the centripetal force as a function of
            tangential velocity, mass, and radius.
            Can also calculate for desired variable when arg == None and all 
            other args have values.

            Args:
                centripetal_F (Optional[float], optional): centripetal force [N]. Defaults to None.
                mass (Optional[float], optional): mass of the object [kg]. Defaults to None.
                velocity (Optional[float], optional): velocity [m/s]. Defaults to None.
                radius (Optional[float], optional): radius of curved trajectory [m]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """
            
            if mass is not None and mass <= 0:
                raise ValueError("We are operating with massive objects. \
                    Mass must be greater than zero.")

            if radius is not None and radius <= 0:
                    raise ValueError("Radius must be greater than zero.")

            if mass == None:
                
                if velocity == 0:
                    raise ValueError("Divison by zero is undefined.")

                # Calculates for the mass
                mass_result: float = (radius * centripetal_F) / (velocity * velocity)
                
                if mass_result <= 0:
                    raise ValueError("We are operating with massive objects. \
                    Mass must be greater than zero. Check your signs.")
                else:
                    return mass_result

            if velocity == None:

                # Calculates for the tangential velocity 
                radicand: float = (centripetal_F * radius) / mass
                
                if radicand < 0:
                    raise ValueError("Negative radicand produces an imaginary number. \
                        Check your signs.")

                return sqrt(radicand)

            if radius == None:

                if centripetal_F == 0:
                    raise ValueError("Divison by zero is undefined.")
                
                # Calculates for the radius
                radius_result: float = (mass * (velocity * velocity)) / centripetal_F

                if radius_result < 0:
                    raise ValueError("Radius cannot be negative. Check your signs.")
                else:
                    return radius_result
            
            if radius < 0: 
                raise ValueError("Radius cannot be a negative value.")
            if radius == 0:
                raise ValueError("Division by zero is undefined.")
            
            return (mass * (velocity * velocity)) / radius

        @staticmethod
        def centripetalForceAngVel(
            centripetal_F: Optional[float]=None,
            mass: Optional[float]=None,
            angular_vel: Optional[float]=None,
            radius: Optional[float]=None
        ) -> float:
            """
            Function calculates the centripetal force as a function of
            angular velocity, mass, and radius.
            Can also calculate for desired variable when arg == None and all 
            other args have values.

            Args:
                centripetal_F (Optional[float], optional): centripetal force [N]. Defaults to None.
                mass (Optional[float], optional): mass of the object [kg]. Defaults to None.
                angular_vel (Optional[float], optional): angular velocity [rads/s]. Defaults to None.
                radius (Optional[float], optional): radius of curved trajectory [m]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """
            
            if mass is not None and mass <= 0:
                raise ValueError("We are operating with massive objects. \
                    Mass must be greater than zero.")

            if radius is not None and radius <= 0:
                    raise ValueError("Radius must be greater than zero.")

            if mass == None:

                if angular_vel == 0:
                    raise ValueError("Division by zero is undefined.")
                
                if centripetal_F < 0 or angular_vel < 0:
                    raise ValueError("Mass cannot be negative. Check your signs.")

                # Calculates for the mass
                return centripetal_F / (radius * (angular_vel * angular_vel))

            if angular_vel == None:

                # Calculates for the angular velocity 
                radicand: float = centripetal_F / (mass * radius)

                if radicand < 0:
                    raise ValueError("Negative radicand produces an imaginary number.")
                return sqrt(radicand)

            if radius == None:

                if angular_vel == 0:
                    raise ValueError("Divison by zero is undefined.")
                
                if centripetal_F < 0 or angular_vel < 0:
                    raise ValueError("Radius cannot be negative. Check your signs.")

                # Calculates for the radius
                return  centripetal_F / (mass * (angular_vel * angular_vel)) 
            
            
            return mass * (angular_vel * angular_vel) * radius

        @staticmethod
        def idealAngBankedCurve(
            theta: Optional[float]=None,
            velocity: Optional[float]=None,
            radius: Optional[float]=None
        ) -> float:
            """
            Function calculates the ideal angle of a banked curve as a function
            of theta, velocity, and the radius of the curved trajectory.
            Can also calculate for desired variable when arg == None and all 
            other args have values.

            Args:
                theta (Optional[float], optional): angle of the banked curve [degrees]. Defaults to None.
                velocity (Optiona[float], optional): speed of the object [m/s] Defaults to None.
                radius (Optional[float], optional): radius of curved trajectory [m]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """
            
            if theta is not None:

                if theta < 0:
                    raise ValueError("Reconsider if theta can physically be a negative value.")

                # Converts degrees into radians
                theta_radians: float = theta * (pi/180)

            if radius is not None and radius <= 0:
                raise ValueError("Radius cannot be less than or equal to zero.")
           
            if velocity == None:

                if theta == 90.0 or theta == 270.0:
                    raise ValueError("Tangent function is undefined at 90.0 and 270.0 degrees.")

                # Calculates for velocity
                radicand: float = radius * g * tan(theta_radians)

                return sqrt(radicand)

            if radius == None:

                if velocity == 0:
                    raise ValueError("Division by zero is undefined.")

                # Calculates for radius
                return ((velocity * velocity) / g) * tan(theta_radians)

            # Calculates the ideal angle theta
            argument: float = (velocity * velocity) / (radius * g)

            return atan(argument) * (180/pi)
        
        @staticmethod
        def dragForce(
            drag_F: Optional[float]=None,
            drag_coeff: Optional[float]=None,
            fluid_dens: Optional[float]=None,
            area: Optional[float]=None,
            velocity: Optional[float]=None
        ) -> float:
            """
            Function calculates the drag force on an object as a function of 
            the drag coefficient, fluid density, area of the object, 
            and the velocity 
            Can also calculate for desired variable when arg == None and all 
            other args have values.

            Args:
                drag_F (Optional[float], optional): drag force [N]. Defaults to None.
                drag_coeff (Optional[float], optional): drag coefficient. Defaults to None.
                fluid_dens (Optional[float], optional): fluid density [kg/m³]. Defaults to None.
                area (Optional[float], optional): area of object [m²]. Defaults to None.
                velocity (Optiona[float], optional): velocity of the object [m/s]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if drag_coeff is not None and drag_coeff <= 0.0:
                raise ValueError("The drag coefficient cannot be less than or equalt to zero.")
            
            if area is not None and area <= 0:
                raise ValueError("Area cannot be less than zero or equal to zero.")
            
            if fluid_dens is not None and fluid_dens <= 0: 
                raise ValueError("Fluid density cannot be less than or equal to zero.")
            
            if drag_coeff == None:

                if velocity == 0.0: 
                    raise ValueError("Divison by zero is undefined.")
                if velocity < 0:
                    raise ValueError("Drag coefficient is a positive value. \
                        Check your signs.")

                # Calculates for drag coefficient
                return drag_F / (0.5 * fluid_dens * area * (velocity * velocity))

            if fluid_dens == None:

                if velocity == 0.0: 
                    raise ValueError("Divison by zero is undefined.")
                if velocity < 0:
                    raise ValueError("Fluid density is a positive value. \
                        Check your signs.")
                
                # Calculates fluid density
                return drag_F / (0.5 * drag_coeff * area * (velocity * velocity))

            if area == None:

                if velocity == 0.0: 
                    raise ValueError("Divison by zero is undefined.")
                if velocity < 0:
                    raise ValueError("Area cannot be negative. \
                        Check your signs.")
                
                # Calculates the area
                return drag_F / (0.5 * drag_coeff * fluid_dens * (velocity * velocity))
            
            if velocity == None:

                # Calculates the velocity
                radicand = drag_F / (0.5 * drag_coeff * fluid_dens * area)
                return sqrt(radicand)
            
            # Calculate drag force
            return -0.5 * drag_coeff * fluid_dens * area * (velocity * velocity)
                
        @staticmethod
        def stokesLaw(
            drag_Fs: Optional[float]=None,
            radius: Optional[float]=None,
            viscosity: Optional[float]=None,
            velocity: Optional[float]=None,
        ) -> float:
            """
            Function calculates the drag force on an object as a function of 
            the drag coefficient, fluid density, area of the object, 
            and the velocity 
            Can also calculate for desired variable when arg == None and all 
            other args have values.

            Args:
                drag_Fs (Optional[float], optional): drag force [N]. Defaults to None.
                radius (Optional[float], optional): radius of object [m]. Defaults to None.
                viscosity (Optional[float], optional): viscosity of the fluid [N⋅s/m²]. Defaults to None.
                velocity (Optional[float], optional): velocity of the object [m/s]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            const: float = 6*pi # Constant coefficient

            if radius is not None and radius <= 0:
                raise ValueError("Radius cannot be less than zero or equal to zero.")

            if viscosity is not None and viscosity < 0:
                raise ValueError("Viscocity cannot be a negative value.")
            
            if radius == None:

                if velocity == 0 or viscosity == 0:
                    raise ValueError("Divison by zero is undefined.")
                if velocity < 0:
                    raise ValueError("The radius cannot be negative. \
                        Check your signs.")
                # Calculates the radius
                return drag_Fs / (const * viscosity * velocity )
                
            if viscosity == None:

                if velocity <= 0:
                    raise ValueError("Velocity cannot be less than or euqal to 0. \
                        This makes viscosity a negative value.")
                
                # Calculates the viscosity
                return drag_Fs / (const * radius * velocity)
            
            if velocity == None:

                return drag_Fs / (const * radius * viscosity)
            
            return -const * radius * viscosity * velocity
        
        @staticmethod
        def terminalVelocity(
            terminal_vel: Optional[float]=None,
            mass: Optional[float]=None,
            drag_coeff: Optional[float]=None,
            area: Optional[float]=None,
            fluid_dens: Optional[float]=None
        ) -> float:
            """
            Function calculates terminal velocity on an object as a function of 
            the drag coefficient, fluid density, area of the object, 
            and its mass. 
            Can also calculate for desired variable when arg == None and all 
            other args have values.

            Args:
                terminal_vel (Optional[float], optional): terminal velocity [m/s]. Defaults to None.
                mass (Optional[float], optional): mass of the object [kg]. Defaults to None.
                drag_coeff (Optional[float], optional): drag coefficient. Defaults to None.
                area (Optional[float], optional): area of the object [m²]. Defaults to None.
                fluid_dens (Optional[float], optional): fluid density [kg/m³]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if drag_coeff is not None and drag_coeff < 0.0:
                raise ValueError("The drag coefficient cannot be a negative value.")

            if area is not None and area <= 0:
                raise ValueError("Area cannot be less than zero or equal to zero.")
            
            if fluid_dens is not None and fluid_dens <= 0: 
                raise ValueError("Fluid density cannot be less than or equal to zero.")

            if mass is not None and mass <= 0:
                raise ValueError("We are operating with massive objects. \
                    Mass must be greater than zero.")
            
            if mass == None:
                # Calculates the mass
                return sqrt(terminal_vel) * ((drag_coeff * area * fluid_dens) / (2 * g))

            if drag_coeff == None:
                # Calculates the drag coefficient
                return (2 * mass * g) / (sqrt(terminal_vel) * area * fluid_dens)
            
            if area == None: 
                
                if drag_coeff == 0:
                    raise ValueError("Division by zero is undefined.")
                
                # Calculates the area 
                return (2 * mass * g) / (sqrt(terminal_vel) * drag_coeff * fluid_dens)
                
            if fluid_dens == 0:

                if drag_coeff == 0:
                    raise ValueError("Division by zero is undefined.")
                
                # Calculates the area 
                return (2 * mass * g) / (sqrt(terminal_vel) * drag_coeff * area)
            
            radicand: float = (2 * mass * g) / (fluid_dens * drag_coeff * area)

            return sqrt(radicand)
            
                



            
