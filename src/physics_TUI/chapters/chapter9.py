from typing import List, Optional, Dict
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition
from math import log, exp

class Chapter9(PhysicsChapter):
    """
    Chapter on Linear Momentum and Collisions
    """

    def __init__(self) -> None:
        super().__init__("Linear Momentum and Collisions")

        self.var_mapping: Dict[str, str] = {
            "m₁": "mass_1",
            "m₂": "mass_2",
            "v₁": "velocity_1",
            "v₂": "velocity_2",
            "v":  "velocity_f",
            "M": "mass_f",
            "v(i)₁": "velocity_i1",
            "v(i)₂": "velocity_i2",
            "v(f)₁": "velocity_f1",
            "v(f)₂": "velocity_f2",
            "Δv": "delta_v",
            "u": "vel_exhaust",
            "m(i)": "initial_mass",
            "m": "final_mass"
        }

        self.equations: List[Equation] = [
            Equation(
                name="Definiiton of momentum",
                formula="p = mv",
                variables={
                    "p": "Momentum (N⋅s)",
                    "m": "Mass of the object (kg)",
                    "velocity": "m/s)"
                }
            ),
            Equation(
                name="Impulse",
                formula="J = ∫(t₁ to t₂) F(t)dt  or  J = F(ave) Δt",
                variables={
                    "J": "Impulse (N⋅s)",
                    "F(t)": "Force as a function of time (N)",
                    "F(ave)": "Average velocity",
                    "Δt": "Elapsed time"
                }
            ),
            Equation(
                name="Impulse-momentum theorem",
                formula="J = Δp",
                variables={
                    "J": "Impulse (N⋅s)",
                    "Δp": "Change in momentum (N⋅s)",
                }
            ),
            Equation(
                name="Average force from momentum",
                formula="F = Δp/Δt",
                variables={
                    "F": "Average force (N)",
                    "Δp": "Change in momentum (N⋅s)",
                    "Δt": "Elapsed time (s)"
                }
            ),
            Equation(
                name="Instantaneous force from momentum",
                formula="F(t) = dp/dt",
                variables={
                    "F(t)": "Instantaneous force (N)",
                    "dp/dt": "The rate of change of momentum with respect \
                        to time (N)"
                }
            ),
            Equation(
                name="Conservation of momentum",
                formula="dp₁/dt + dp₂/dt = 0  or  m₁v₁ + m₂v₂ = constant",
                variables={
                    "p₁": "Momentum from the first object (N⋅s)",
                    "p₂": "Momentum from the second object (N⋅s)",
                    "m₁": "Mass of the first object (kg)",
                    "v₁": "Velocity of the first object (m/s)",
                    "m₂": "Mass of the second object (m)",
                    "v₂": "Velocity of the second object (m/s)"
                }
            ),
            Equation(
                name="Generalized conservation of momentum",
                formula="∑(j=1 to N) pⱼ = constant",
                variables={
                    "∑(j=1 to N) pⱼ": "The sum of all momenta in the system"
                }
            ),
            Equation(
                name="Conservation of momentum in two dimensions",
                formula="p₁,ₓ = p₁,ᵢ,ₓ + p₂,ᵢ,ₓ, p₁,ᵧ = p₁,ᵢ,ᵧ + p₂,ᵢ,ᵧ",
            ),
            Equation(
                name="Inelastic collision of two objects (momentum)",
                formula="m₁v₁ + m₂v₂ = Mv",
                variables={
                    "m₁": "Mass of the first object",
                    "v₁": "Velocity of the first object (m/s)",
                    "m₂": "Mass of the second object (m)",
                    "v₂": "Velocity of the second object (m/s)",
                    "M": "Total mass of the object after collision (m₁ + m₂) (kg)",
                    "v": "Velocity after the collision (m/s)"
                },
                calculation=self.Calculate.inelastic_collision_momentum
            ),
            Equation(
                name="Elastic collision of two objects (momentum)",
                formula="m₁v(i)₁ + m₂v(i)₂ = m₁v(f)₁ + m₂v(f)₂",
                variables={
                    "m₁": "Mass of the first object (kg)",
                    "m₂": "Mass of the second object (kg)",
                    "v(i)₁": "Initial velocity of the first object (m/s)",
                    "v(i)₂": "Initial velocity of the second object (m/s)",
                    "v(f)₁": "Final velocity of the first object (m/s)",
                    "v(f)₂": "Final velocity of the second object (m/s)"
                },
                calculation=self.Calculate.elastic_collision_momentum
            ),
            Equation(
                name="External forces",
                formula="F(ext) = ∑(j=1 to N) dpⱼ/dt",
                variables={
                    "F(ext)": "External force (N)",
                    "∑(j=1 to N) dpⱼ/dt": "The sum of all the rate of \
                        change of momenta with respect to time in the system"
                }
            ),
            Equation(
                name="Newton's second law for an extended object",
                formula="F = dp(CM)/dt",
                variables={
                    "F": "Force (N)",
                    "dp(CM)/dt": "Rate of change of momentum from the center \
                        of mass with respect to time"
                }
            ),
            Equation(
                name="Acceleration of the center of mass",
                formula="a(CM) = d²/dt² (1/M ∑(j=1 to N) mⱼrⱼ) = 1/M ∑(j=1 to N) mⱼaⱼ",
                variables={
                    "a(CM)": "Acceleration of the center of mass (m/s²)",
                    "M": "Total mass of the system (kg)",
                    "∑(j=1 to N) mⱼaⱼ": "Sum of the product of mass and \
                        acceleration of each individual object in the system"
                }
            ),
            Equation(
                name="Position of the center of mass for a system of particles",
                formula="r(CM) = 1/M ∑(j=1 to N) mⱼrⱼ",
                variables={
                    "r(CM)": "Position of the center of mass of the system (m)",
                    "M": "Total mass of the system",
                    "∑(j=1 to N) mⱼrⱼ": "Sum of the product of mass and \
                        position of each object in the system"
                }
            ),
            Equation(
                name="Velocity of the center of mass",
                formula="v(CM) = d/dt (1/M ∑(j=1 to N) mⱼrⱼ) \
                    = 1/M ∑(j=1 to N) mⱼvⱼ",
                variables={
                    "v(CM)": "Velocity of the center of mass (m/s)",
                    "M": "Total mass of the system (m)",
                    "∑(j=1 to N) mⱼvⱼ": "The sum of the product of mass \
                        and velocity of each object in the system"
                }
            ),
            Equation(
                name="Position of the center of mass of a continuous object",
                formula="r(CM) = 1/M ∫ r dm",
            ),
            Equation(
                name="Rocket equation",
                formula="Δv = u ln(m(i)/m)",
                varables={
                    "Δv": "Change of velocity obtained from loss of mass",
                    "u": "Velocity of the gas being exhausted from the rocket",
                    "m(i)": "Initial mass of the rocket (with fuel)",
                    "m": "Mass of the rocket after the fuel has been exhausted"
                },
                calculation=self.Calculate.rocket_equation
            )
        ]

        self.definitions: List[Definition] = [
            Definition(
                term="center of mass",
                meaning="weighted average position of the mass"
                ),
            Definition(
                term="closed system",
                meaning="system for which the mass is constant and the net external force on the system is zero"
                ),
            Definition(
                term="elastic",
                meaning="collision that conserves kinetic energy"
                ),
            Definition(
                term="explosion",
                meaning="single object breaks up into multiple objects; kinetic energy is not conserved in explosions"
                ),
            Definition(
                term="external force",
                meaning="force applied to an extended object that changes the momentum of the extended object as a whole"
                ),
            Definition(
                term="impulse",
                meaning="effect of applying a force on a system for a time interval; this time interval is usually small, but does not have to be"
                ),
            Definition(
                term="impulse-momentum theorem",
                meaning="change of momentum of a system is equal to the impulse applied to the system"
                ),
            Definition(
                term="inelastic",
                meaning="collision that does not conserve kinetic energy"
                ),
            Definition(
                term="internal force",
                meaning="force that the simple particles that make up an extended object exert on each other. Internal forces can be attractive or repulsive"
                ),
            Definition(
                term="Law of Conservation of Momentum",
                meaning="total momentum of a closed system cannot change"
                ),
            Definition(
                term="linear mass density",
                meaning="λ, expressed as the number of kilograms of material per meter"
                ),
            Definition(
                term="momentum",
                meaning="measure of the quantity of motion that an object has; it takes into account both how fast the object is moving, and its mass; specifically, it is the product of mass and velocity; it is a vector quantity"
                ),
            Definition(
                term="perfectly inelastic",
                meaning="collision after which all objects are motionless, the final kinetic energy is zero, and the loss of kinetic energy is a maximum"
                ),
            Definition(
                term="rocket equation",
                meaning="derived by the Soviet physicist Konstantin Tsiolkovsky in 1897, it gives us the change of velocity that the rocket obtains from burning a mass of fuel that decreases the total rocket mass from m_i down to m"
                ),
            Definition(
                term="system",
                meaning="object or collection of objects whose motion is currently under investigation; however, your system is defined at the start of the problem, you must keep that definition for the entire problem"
                ),
        ]
        
        class Calculate:
            """
            Class holds methods to calculate equations in Chapter 9
            """

            @staticmethod
            def inelastic_collision_momentum(
                mass_1: Optional[float]=None,
                mass_2: Optional[float]=None,
                velocity_1: Optional[float]=None,
                velocity_2: Optional[float]=None,
                velocity_f: Optional[float]=None,
                mass_f: Optional[float]=None
            ) -> float:
                """
                Function calculates the final momentum of a system with 
                inelastic collision as a function of the masses and velocities
                pre and post collision.
                Can also calculate for desired variable when arg == None and all 
                other args have values.

                Args:
                    mass_1 (Optional[float], optional): initial mass of the first object [kg]. Defaults to None.
                    mass_2 (Optional[float], optional): initial mass of the second object [kg]. Defaults to None.
                    velocity_1 (Optional[float], optional): initial velocity of the first object [m/s]. Defaults to None.
                    velocity_2 (Optional[float], optional): initial velocity of the second object [m/s]. Defaults to None.
                    velocity_f (Optional[float], optional): final velocity of the collided object [m/s]. Defaults to None.
                    mass_f (Optional[float], optional): final mass of the collided object [kg]. Defaults to None.

                Returns:
                    float: the result of whichever variable was left equal to None
                """

                if mass_1 is not None and mass_1 <= 0.0 or mass_2 is not None \
                and mass_2 <= 0.0 or mass_f is not None and mass_f <= 0:
                    raise ValueError("We are operating with massive objects. \
                        Make sure all objects have a mass greater than zero.")
                
                if mass_1 == None:
                    
                    if velocity_1 == 0:
                        raise ValueError("Division by zero is undefined.")
                    
                    # Calculates mass of object 1
                    return ((mass_f * velocity_f) - (mass_2 * velocity_2)) / velocity_1
                
                if mass_2 == None:
                    
                    if velocity_2 == 0.0:
                        raise ValueError("Division by zero is undefined.")

                    # Calculates mass of object 2
                    return ((mass_f * velocity_f) - (mass_1 * velocity_1)) / velocity_2

                if velocity_1 == None:
                    # Calculates velocity of object 1
                    return ((mass_f * velocity_f) - (mass_2 * velocity_2)) / mass_1
                
                if velocity_2 == None:
                    # Calculates velocity of object 1
                    return ((mass_f * velocity_f) - (mass_1 * velocity_1)) / mass_2

                if mass_f == None:

                    if velocity_f == 0.0:
                        raise ValueError("Division by zero is undefined.")
                    
                    # Calculates the mass after collision
                    return ((mass_1 * velocity_1) + (mass_2 * velocity_2)) / velocity_f
                
                if velocity_f == None:
                    # Calculates the velocity after collision
                    return ((mass_1 * velocity_1) + (mass_2 * velocity_2)) / mass_f
                
                if mass_1 == None and velocity_1 == None:
                    # Calculates the initial momentum of the first object
                    return ( (mass_f * velocity_f) - (mass_2 * velocity_2))
                
                if mass_2 == None and velocity_2 == None:
                    # Calculates the initial momentum of the second object
                    return ( (mass_f * velocity_f) - (mass_1 * velocity_1))

                if mass_f == None and velocity_f == None:
                    #Calculates final momentum
                    return (mass_1 * velocity_1) + (mass_2 * velocity_2)

                return 0.0
            
            @staticmethod
            def elastic_collision_momentum(
                mass_1: Optional[float]=None,
                mass_2: Optional[float]=None,
                velocity_i1: Optional[float]=None,
                velocity_i2: Optional[float]=None,
                velocity_f1: Optional[float]=None,
                velocity_f2: Optional[float]=None
            ) -> float:
                """
                Function calculates the final momenta of a system with 
                eelastic collision as a function of the masses and velocities
                pre and post collision.
                Can also calculate for desired variable when arg == None and all 
                other args have values.

                Args:
                    mass_1 (Optional[float], optional): mass of object 1 [kg] Defaults to None.
                    mass_2 (Optional[float], optional): mass of object 2 [kg]. Defaults to None.
                    velocity_i1 (Optional[float], optional): initial velocity of object 1 [m/s]. Defaults to None.
                    velocity_i2 (Optional[float], optional): initial velocity of object 2 [m/s]. Defaults to None.
                    velocity_f1 (Optional[float], optional): final velocity of object 1 [m/s]. Defaults to None.
                    velocity_f2 (Optional[float], optional): final velocity of object 2 [m/s]. Defaults to None.

                Returns:
                    float: the result of whichever variable was left equal to None
                """

                if mass_1 is not None and mass_1 <= 0.0 or \
                    mass_2 is not None and mass_2 <= 0.0:
                    raise ValueError("We are operating with massive objects. \
                        Make sure all objects have a mass greater than zero.")
                
                if mass_1 == None:

                    if velocity_f1 == velocity_i1:
                        raise ValueError("Divison by zero is undefined.")
                    
                    # Calculates the mass of object 1
                    return ( (mass_2 * velocity_i2) - (mass_2 * velocity_f2) ) \
                        / (velocity_f1 - velocity_i1) 
                
                if mass_2 == None:

                    if velocity_i2 == velocity_f2:
                        raise ValueError("Divison by zero is undefined.")
                    
                    # Calculates the mass of object 2
                    return ( (mass_1 * velocity_i1) - (mass_1 * velocity_f1) ) \
                            / (velocity_i2 - velocity_f2)
                
                if velocity_i1 == None:
                    # Calculates the initial velocity of object 1
                    return  ( (mass_1 * velocity_f1) + (mass_2 * velocity_f2) \
                            - (mass_2 * velocity_i2) ) / mass_1
                
                if velocity_i2 == None:
                    # Calculates the initial velocity of object 2
                    return ( (mass_1 * velocity_f1) + (mass_2 * velocity_f2) \
                            - (mass_1 * velocity_i1) ) / mass_2

                if velocity_f1 == None:
                    # Calculates the final velocity of object 1
                    return ( (mass_1*velocity_i1) + (mass_2*velocity_i2) \
                        - (mass_2*velocity_f2) ) / mass_1
                
                if velocity_f2 == None:
                    # Calculates the final velocity of object 2
                    return ( (mass_1*velocity_i1) + (mass_2*velocity_i2) \
                        - (mass_1*velocity_f1) ) / mass_2

                if mass_1 == None and velocity_i1 == None:
                    
                    # Through the coefficient of restitution (COR) epsilon = 1 for
                    # perfectly elastic collisions we have v(i)₁ = v(f)₂ - v(f)₁ + v(i)₂
                    velocity_i1: float = velocity_f2 - velocity_f1 + velocity_i2

                    if velocity_i1 == velocity_f1:
                        raise ValueError("Division by zero is undefined.")

                    mass_1: float = ( (mass_2 * velocity_i2) - (mass_2 * velocity_f2) ) \
                        / (velocity_f1 - velocity_i1) 
                    
                    if mass_1 <= 0: 
                        raise ValueError("Mass cannot be less than or equal to zero.\
                            Check your signs.")

                    return mass_1*velocity_i1
                
                if mass_2 == None and velocity_i2 == None:
                    
                    # Through the coefficient of restitution (COR) epsilon = 1 for
                    # perfectly elastic collisions we have v(i)₁ - v(i)₂ = v(f)₂ - v(f)₁ 
                    velocity_i2: float = velocity_f2 - velocity_f1 - velocity_i1

                    if velocity_i2 == velocity_f2:
                        raise ValueError("Divison by zero is undefined.")
                    
                    # Calculates the mass of object 2
                    mass_2: float= ( (mass_1 * velocity_i1) - (mass_1 * velocity_f1) ) \
                            / (velocity_i2 - velocity_f2)
                    
                    if mass_2 <= 0: 
                        raise ValueError("Mass cannot be less than or equal to zero.\
                            Check your signs.")

                    return mass_2*velocity_i2
                
                if mass_1 == None and velocity_f1 == None:
                    
                    # Through the coefficient of restitution (COR) epsilon = 1 for
                    # perfectly elastic collisions we have v(i)₁ - v(i)₂ = v(f)₂ - v(f)₁ 
                    velocity_f1: float = velocity_f2 - velocity_i1 + velocity_i2

                    if velocity_i1 == velocity_f1:
                        raise ValueError("Division by zero is undefined.")

                    mass_1: float = ( (mass_2 * velocity_i2) - (mass_2 * velocity_f2) ) \
                        / (velocity_f1 - velocity_i1) 
                    
                    if mass_1 <= 0: 
                        raise ValueError("Mass cannot be less than or equal to zero.\
                            Check your signs.")

                    return mass_1*velocity_f1
                
                if mass_2 == None and velocity_f2 == None:
                    
                    # Through the coefficient of restitution (COR) epsilon = 1 for
                    # perfectly elastic collisions we have v(i)₁ - v(i)₂ = v(f)₂ - v(f)₁ 
                    velocity_f2: float = velocity_f1 + velocity_i1 - velocity_i2

                    if velocity_i2 == velocity_f2:
                        raise ValueError("Divison by zero is undefined.")
                    
                    # Calculates the mass of object 2
                    mass_2: float= ( (mass_1 * velocity_i1) - (mass_1 * velocity_f1) ) \
                            / (velocity_i2 - velocity_f2)
                    
                    if mass_2 <= 0: 
                        raise ValueError("Mass cannot be less than or equal to zero.\
                            Check your signs.")

                    return mass_2*velocity_f2

                return 0.0 

            @staticmethod
            def rocket_equation(
                delta_v: Optional[float]=None,
                vel_exhaust: Optional[float]=None,
                initial_mass: Optional[float]=None,
                final_mass: Optiona[float]=None
            ) -> float:
                """
                Function calculates the change in velocity of a rocket as a
                function of the exhaust velocity, velocity towards direction of
                motion, initial mass, and the mass after fuel has been exhausted.
                Can also calculate for desired variable when arg == None and all 
                other args have values.

                Args:
                    delta_v (Optional[float], optional): change in velocity (m/s). Defaults to None.
                    vel_exhaust (Optional[float], optional): velocity of exhaust (m/s). Defaults to None.
                    initial_mass (Optional[float], optional): initial mass of the rocket (kg). Defaults to None.
                    final_mass (Optiona[float], optional): final mass of the rocket (kg). Defaults to None.

                Returns:
                    float: the result of whichever variable was left equal to None
                """

                if initial_mass is not None and initial_mass <= 0 or final_mass <= 0:
                    raise ValueError("We are operating with massive objects. \
                        Mass must be greater than zero.")
                
                if vel_exhaust == None:
                    # Calculates velocity of the exhaust
                    return delta_v / log(initial_mass/final_mass)
                
                if initial_mass == None:
                    # Calculates the initial mass of the rocket
                    return exp(delta_v/vel_exhaust) * final_mass
                
                if final_mass == None:
                    # Calculates the final mass of the rocket
                    return initial_mass / exp(delta_v/vel_exhaust)
                
                # Calculates delta v of the rocket
                return vel_exhaust * log(initial_mass/final_mass)
