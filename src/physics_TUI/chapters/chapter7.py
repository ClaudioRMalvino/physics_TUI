from typing import List, Optional, Dict
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition
from math import pi, cos, acos, sqrt
# Global constants
g: float = 9.82 # Acceleration due to gravity on Earth

class Chapter7(PhysicsChapter):
    """
    Chapter on Work and Kinetic Energy 
    """

    def __init__(self) -> None:
        super().__init__("Work and Kinetic Energy")

        self.var_mapping: Dict[str, str] = {
            "W": "work",
            "F": "const_F",
            "d": "distance",
            "θ": "theta",
            "m": "mass",
            "y₁": "initial_height",
            "y₂": "final_height",
            "k": "spring_const",
            "x₁": "initial_xpos",
            "x₂": "final_xpos",
            "K": "kinetic_E",
            "v": "velocity",
            "v₁": "initial_vel",
            "v₂": "final_vel",
            "p": "momentum",
            "W(net)": "net_work",
        }

        self.equations: List[Equation] = [
            Equation(
                name="Work done by constant force",
                formula="W = Fdcos(θ)",
                variables={
                    "W": "Work (J)",
                    "F": "Constant force (N)",
                    "d": "Distance travelled (m)",
                    "θ": "Angle between the direction of \
                        motion and force vector (degrees)"
                },
                calculation=self.Calculate.workConstantForce
            ),
            Equation(
                name="Work done by gravity",
                formula="W = -mg(y - y₀)",
                variables={
                    "W": "Work (J)",
                    "m": "Mass (kg)",
                    "y₁": "Initial height (m)",
                    "y₂": "Final height (m)"
                },
                calculation=self.Calculate.workByGravity
            ),
            Equation(
                name="Work done by a spring",
                formula="W = -½k(x² - x₀²)",
                variables={
                    "W": "Work (J)",
                    "k": "Spring constant (kg/s²)",
                    "x₁": "Initial position (m)",
                    "x₂": "Final position"
                },
                calculation=self.Calculate.workBySpring
            ),
            Equation(
                name="Kinetic energy",
                formula="K = ½mv²",
                variables={
                    "K": "Kinetic energy (J)",
                    "m": "Mass (kg)",
                    "v": "Velocity (m/s)"
                },
                calculation=self.Calculate.kineticEnergy
            ),
            Equation(
                name="Kinetic energy (momentum representation)",
                formula="K = ½(p²/m)",
                variables={
                    "K": "Kinetic energy (J)",
                    "m": "Mass (kg)",
                    "p": "Momentum"
                },
                calculation=self.Calculate.kineticEnergyMomentum
            ),
            Equation(
                name="Work-Energy theorem",
                formula="W(net) = ½mv² - ½mv₀²",
                variables={
                    "W(net)": "Net work (J)",
                    "m": "Mass (kg)",
                    "v₂": "Final velocity (m/s)",
                    "v₁": "Initial velocity (m/s)"
                },
                calculation=self.Calculate.workEnergyTheorem
            ),
            Equation(
                name="Average power",
                formula="P(ave) = ΔW/Δt",
                variables={
                    "P(ave)": "Average power (J/s)",
                    "ΔW": "Elapsed work done (W)",
                    "Δt": "Elapsed time (s)"
                }
            ),    
        ]

        self.definitions: List[Definition] = [
            Definition(
                term="average power",
                meaning="work done in a time interval divided by the time interval"
            ),
            Definition(
                term="kinetic energy",
                meaning="energy of motion, one-half an object's mass times the square of its speed"
            ),
            Definition(
                term="net work",
                meaning="work done by all the forces acting on an object"
            ),
            Definition(
                term="power",
                meaning="(or instantaneous power) rate of doing work"
            ),
            Definition(
                term="work",
                meaning="done when a force acts on something that undergoes a displacement from one position to another"
            ),
            Definition(
                term="work-energy theorem",
                meaning="net work done on a particle is equal to the change in its kinetic energy"
            ),
        ]

    class Calculate:
        """
        Class holds methods to calculate equations in Chapter 7
        """

        @staticmethod
        def workConstantForce(
            work: Optional[float]=None,
            const_F: Optional[float]=None,
            distance: Optional[float]=None,
            theta: Optional[float]=None
        ) -> float:
            """
            Function calculates the work done as a function of
            constant applied force and the distance travelled.
            Can also calculate for desired variable when arg == None and all 
            other args have values.

            Args:
                work (Optional[float], optional): total work done [J]. Defaults to None.
                const_F (Optional[float], optional): constant applied force [N]. Defaults to None.
                distance (Optional[float], optional): distance travelled [m]. Defaults to None.
                theta (Optional[float], optional): angle between direction of motion 
                                                        and the force vectors [degrees]. Defaults to None.
            Returns:
                float: the result of whichever variable was left equal to None
            """
            
            # Converts user input of degrees into SI units of radians
            if theta is not None:
                theta_radians: float = theta * (pi/180.0)

            if cont_F == None:
                # Calculates for constant force
                return work/(cos(theta_radians) * distance)
            
            if distance == None:
                # Calculates for distance
                return work / (const_F * cos(theta_radians))
            
            if theta == None:
                # Calculates for theta and then converts into degrees
                argument: float = work/(const_F * distance)
                return acos(argument) * (180/pi)

            return const_F * distance * cos(theta_radians)

        @staticmethod
        def workByGravity(
            work: Optional[float]=None,
            mass: Optional[float]=None,
            initial_height: Optional[float]=None,
            final_height: Optional[float]=None,
        ) -> float: 
            """
            Function calculates the work done as a function of
            gravity, mass and the distance travelled.
            Can also calculate for desired variable when arg == None and all 
            other args have values.

            Args:
                work (Optional[float], optional): work done in the system [J]. Defaults to None.
                mass (Optional[float], optional): mass of the object [kg]. Defaults to None.
                initial_height (Optional[float], optional): initial height of the object [m]. Defaults to None.
                final_height (Optional[float], optional): final height of the object [m]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if mass is not None and mass < 0:
                raise ValueError("We are operating with massive objects. \
                Mass must be greater than zero.")
            
            if mass == None:

                result: float = -work / (g * (final_height - initial_height))

                if result < 0:
                    raise ValueError("Mass cannot be negative. \
                        Check your signs or initial and final heights.")
                else:
                    return result
            
            if initial_height == None:
                return (work/(mass * g)) + final_height
            
            if final_height == None:
                return (-work/(mass * g)) + initial_height
            
            return -mass * g * (final_height - initial_height)
        
        @staticmethod
        def workBySpring(
            work: Optional[float]=None,
            spring_const: Optional[float]=None,
            initial_xpos: Optional[float]=None,
            final_xpos: Optional[float]=None,
        ) -> float:
            """
            Function calculates the work done as a function of
            spring constant, and the displacement along the x-axis.
            Can also calculate for desired variable when arg == None and all 
            other args have values.

            Args:
                work (Optional[float], optional): work done by the system [J]. Defaults to None.
                spring_const (Optional[float], optional): spring constant[kg/s²]. Defaults to None.
                initial_xpos (Optional[float], optional): initial position on the x-axis [m]. Defaults to None.
                final_xpos (Optional[float], optional): final position on the x-axis [m]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if spring_const is not None and spring_const < 0:
                raise ValueError("Spring constant cannot be a negative value.")

            if spring_const == None:
                return (-2.0 * work) / ( (final_xpos * final_xpos) - (initial_xpos * initial_xpos) )
            
            if initial_xpos == None:
                return ( (2.0 * work) / spring_const) + (final_xpos * final_xpos)

            if final_xpos == None:
                return ( (-2.0 * work) / spring_const) + (final_xpos * final_xpos)
            
            return -0.5 * spring_const * ( (final_xpos * final_xpos) - (initial_xpos * initial_xpos))


        @staticmethod
        def kineticEnergy(
            kinetic_E: Optional[float]=None,
            mass: Optional[float]=None,
            velocity: Optional[float]=None
        ) -> float:
            """
            Function calculates the kinetic energy of a system as a function of
            mass, and velocity.
            Can also calculate for desired variable when arg == None and all 
            other args have values.

            Args:
                kinetic_E (Optional[float], optional): kinetic energy of the system [J]. Defaults to None.
                mass (Optional[float], optional): mass of the object [m]. Defaults to None.
                velocity (Optional[float], optional): velocity of the object [m/s]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if mass is not None and mass < 0:
                raise ValueError("We are operating with massive objects. \
                Mass must be greater than zero.")
            
            if velocity is not None and velocity < 0:
                raise ValueError("This is a scalar product. Velocity cannot be negative")
            
            if mass == None:
                return kinetic_E * (2.0/(velocity*velocity))

            if velocity == None:

                radicand: float = kinetic_E * (2.0 / mass)
                return sqrt(radicand)
            
            return 0.5 * mass * (velocity * velocity)

        @staticmethod
        def kineticEnergyMomentum(
            kinetic_E: Optional[float]=None,
            mass: Optional[float]=None,
            momentum: Optional[float]=None,
        ) -> float:
            """
            Function calculates the kinetic energy of a system as a function of
            mass, and momentum.
            Can also calculate for desired variable when arg == None and all 
            other args have values.

            Args:
                kinetic_E (Optional[float], optional): kinetic energy of the system [J]. Defaults to None.
                mass (Optional[float], optional): mass of the object [m]. Defaults to None.
                momentum (Optional[float], optional): momentum of the object. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if mass is not None and mass < 0:
                raise ValueError("We are operating with massive objects. \
                Mass must be greater than zero.")
            
            if velocity is not None and velocity < 0:
                raise ValueError("This is a scalar product. Velocity cannot be negative")
            
            if mass == None:

                return (momentum*momentum) / (kinetic_E * 2.0)
            
            if momentum == None:
                return kinetic_E * 2.0 * mass
            
            return (momentum * momentum) / (2.0 * mass)
        
        @staticmethod
        def workEnergyTheorem(
            net_work: Optional[float]=None,
            mass: Optional[float]=None,
            final_vel: Optional[float]=None,
            initial_vel: Optional[float]=None
        ) -> float:
            """
            Function calculates the net work done in a system as a function of
            initial kinetic energy and final kinetic energy.
            Can also calculate for desired variable when arg == None and all 
            other args have values.


            Args:
                net_work (Optional[float], optional): net work done by the system [J]. Defaults to None.
                mass (Optional[float], optional): mass of the object [m]. Defaults to None.
                final_vel (Optional[float], optional): final velocity [m/s] . Defaults to None.
                initial_vel (Optional[float], optional): initial velocity [m/s]. Defaults to None.

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if mass is not None and mass < 0:
                raise ValueError("We are operating with massive objects. \
                Mass must be greater than zero.")

            if mass == None:

                return (2.0 * net_work) / ( (final_vel * final_vel) - (initial_vel * initial_vel) )
            
            if final_vel == None:

                radicand: float = ((2.0 * net_work) / mass) + (initial_vel * initial_vel)
                if radicand < 0:
                    raise ValueError("Negative radicand produces a complex number. \
                        Check your signs.")
                else:
                    return sqrt(radicand)

            if initial_vel == None:

                radicand: float = ((-2.0 * net_work) / mass) + (final_vel * final_vel)
                if radicand < 0:
                    raise ValueError("Negative radicand produces a complex number. \
                        Check your signs.")
                else:
                    return sqrt(radicand)
            
            return (0.5 * mass) * ( (final_vel*final_vel) - (initial_vel*initial_vel))



                


