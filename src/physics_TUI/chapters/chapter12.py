from typing import List, Optional, Dict
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition

class Chapter12(PhysicsChapter):
    """
    Chapter Static Equilibrium and Elasticity
    """

    def __init__(self) -> None:
        super.__init__("Static Equilibrium and Elasticity")

        self.var_mapping: Dict[str, str] = {
            "Y": "young_mod",
            "F": "force",
            "A": "cross_section",
            "L₀": "init_length",
            "ΔL": "delta_length",
            "B": "bulk_mod",
            "Δp": "delta_pressure",
            "V₀": "init_volume",
            "ΔV": "delta_volume",
            "S": "shear_mod",
            "Δx": "delta_layers"
        }

        self.equations: List[Equation] = [
            Equation(
                name="First Equilibrium Condition",
                formula="∑Fₖ = 0",
                variables={}
            ),
            Equation(
                name="Second Equilibrium Condition",
                formula="∑τₖ = 0",
                variables={}
            ),
            Equation(
                name="Linear relation between stress and strain",
                formula="stress = (elastic modulus) × strain",
                variables={}
            ),
            Equation(
                name="Young's modulus",
                formula="Y = (tensile stress)/(tensile strain) = (F/A) × (L₀/ΔL)",
                variables={
                    "Y": "Elastic modulus for tensile stress (Pa)",
                    "F": "Force (N)",
                    "A": "Cross sectional area (m)",
                    "L₀": "Initial length of the object (m)",
                    "ΔL": "Change of length after deformation (m)"

                },
                calculation=self.Calculate.young_modulus
            ),
            Equation(
                name="Bulk modulus",
                formula="B = (bulk stress)/(bulk strain) = −Δp × (V₀/ΔV)",
                variables={
                    "B": "Elastic modulus for bulk stress (Pa)",
                    "Δp": "Change in pressure (Pa)",
                    "V₀": "Initial volume (m³)",
                    "ΔV": "Change in volume (m³)"
                },
                calculation=self.Calculate.bulk_modulus
            ),
            Equation(
                name="Shear modulus",
                formula="S = (tensile stress)/(tensile strain) = (F/A) × (L₀/Δx)",
                variables={
                    "S": "Elastic modulus for shear stress (Pa)",
                    "F": "Force (N)",
                    "A": "Cross sectional area (m)",
                    "L₀": "Initial length of the object (m)",
                    "Δx": "a gradual shift of layers in the direction tangent to the acting forces."
                },
                calculation=self.Calculate.shear_modulus
            )
        ]

        self.definitions: List[Definition] =[
            Definition(
                term="angular momentum",
                meaning="rotational analog of linear momentum, found by taking the product of moment of inertia and angular velocity"
            ),
            Definition(
                term="law of conservation of angular momentum",
                meaning="angular momentum is conserved, that is, the initial angular momentum is equal to the final angular \
                    momentum when no external torque is applied to the system precession"
            ),
            Definition(
                term="precession",
                meaning="circular motion of the pole of the axis of a spinning object around another axis due to a torque"
            ),
            Definition(
                term="rolling motion",
                meaning="combination of rotational and translational motion with or without slipping"
            )
        ]

        class Calculate:
            """
            Class holds methods to calculate equations in Chapter 12
            """

            @staticmethod
            def young_modulus(
                young_mod: Optional[float]=None,
                force: Optional[float]=None,
                cross_section: Optional[float]=None,
                init_length: Optional[float]=None,
                delta_length: Optional[float]=None,
            ) -> float:
                """
                Function calculates the Young modulus as a function of 
                the applied force, cross sectional area, initial length,
                and the change in length. 
                Can also calculate for desired variable when arg == None
                and all other args have values.

                Args:
                    young_mod (Optional[float], optional): Young modulus for tensile strength [Pa]. Defaults to None.
                    force (Optional[float], optional): the applies force [N]. Defaults to None.
                    cross_Section (Optional[float], optional): area of cross section [m²]. Defaults to None.
                    init_length (Optional[float], optional): initial length of the object [m]. Defaults to None.
                    delta_length (Optional[float], optional): change in length after deformation [m]. Defaults to None.

                Returns:
                    float: the result of whichever variable was left equal to None
                """

                if init_length is not None and init_length <= 0.0 \
                or cross_Section is not None and cross_Section < 0.0:
                    raise ValueError("The initial length \
                        and cross section cannot be less than or equal to zero.")

                if delta_length is not None and delta_length < 0.0:
                    raise ValueError("The change in length cannot be less than zero.")

                if force == None:
                    
                    # Calculates the applied force
                    numerator: float = delta_length * cross_section * young_mod
                    denominator: float = init_length

                    return numerator / denominator

                if cross_section == None:
                    
                    if young_mod == 0.0 or delta_length == 0.0:
                        raise ValueError("Division by zero is undefined.")
                    
                    # Calculates the cross sectional area of the object
                    numerator: float = init_length * force
                    denominator: float = young_mod * delta_length

                    return numerator / denominator

                if init_length == None:
                    
                    if force == 0.0:
                        raise ValueError("Division by zero is undefined.")
                    
                    # Calculates initial length of the object
                    numerator: float = young_mod * delta_length * cross_section
                    denominator: float = force 

                    return numerator / denominator
                
                if delta_length == None:

                    if young_mod == 0.0:
                        raise ValueError("Divison by zero is undefined.")
                    
                    # Calculates for the change in length
                    numerator: float = init_length * force
                    denominator: float = young_mod * cross_section

                    return numerator / denominator

                return (force / cross_section) * (init_length / delta_length)
            
            @staticmethod
            def bulk_modulus(
                bulk_mod: Optional[float]=None,
                delta_pressure: Optional[float]=None,
                init_volume: Optional[float]=None,
                delta_volume: Optiona[float]=None
            ) -> float:
                """
                Function calculates the Bulk modulus as a function of 
                the change in pressure, initial volume,
                and the change in volume. 
                Can also calculate for desired variable when arg == None
                and all other args have values.

                Args:
                    bulk_mod (Optional[float], optional): the bulk modulus [Pa]. Defaults to None.
                    delta_pressure (Optional[float], optional): change in pressure (Pa). Defaults to None.
                    init_volume (Optional[float], optional): initial volume [m³]. Defaults to None.
                    delta_volume (Optiona[float], optional): change in volume [m³]. Defaults to None.

                Returns:
                    float: the result of whichever variable was left equal to None
                """

                if init_volume is not None and init_volume <= 0.0:
                    raise ValueError("The volume of the object must be greater than zero.")

                if delta_pressure == None:
                    # Calculates the change in pressure
                    return -( bulk_mod * delta_volume) / init_volume

                if init_volume == None: 
                    
                    if delta_pressure == 0.0:
                        raise ValueError("Division by zero is undefined.")
                    
                    # Calculates the initial volume  
                    return -(bulk_mod * delta_pressure) / delta_pressure
                
                if delta_volume == None:
                    
                    if bulk_mod == 0.0: 
                        raise ValueError("Division by zero is undefined.")

                    return (-delta_pressure * init_volume) / bulk_mod
                
                if delta_volume == 0.0:
                    raise ValueError("Division by zero is undefined.")
                
                return (-delta_pressure * init_volume) / delta_volume
            
            @staticmethod
            def shear_modulus(
                shear_mod: Optional[float]=None,
                force: Optional[float]=None,
                cross_section: Optional[float]=None,
                init_length: Optional[float]=None,
                delta_layers: Optional[float]=None,
            ) -> float:
                """
                Function calculates the Shear modulus as a function of 
                the applied force, cross sectional area, initial length,
                and the change layer position. 
                Can also calculate for desired variable when arg == None
                and all other args have values.

                Args:
                    shear_mod (Optional[float], optional): Shear modulus for shear stress [Pa]. Defaults to None.
                    force (Optional[float], optional): the applies force [N]. Defaults to None.
                    cross_Section (Optional[float], optional): area of cross section [m²]. Defaults to None.
                    init_length (Optional[float], optional): initial length of the object [m]. Defaults to None.
                    delta_layers (Optional[float], optional): change in layer positions after deformation [m]. Defaults to None.

                Returns:
                    float: the result of whichever variable was left equal to None
                """

                if init_length is not None and init_length <= 0.0 \
                or cross_Section is not None and cross_Section < 0.0:
                    raise ValueError("The initial length \
                        and cross section cannot be less than or equal to zero.")

                if delta_layers is not None and delta_layers < 0.0:
                    raise ValueError("The change in length cannot be less than zero.")

                if force == None:
                    
                    # Calculates the applied force
                    numerator: float = delta_layers * cross_section * shear_mod
                    denominator: float = init_length

                    return numerator / denominator

                if cross_section == None:
                    
                    if shear_mod == 0.0 or delta_layers == 0.0:
                        raise ValueError("Division by zero is undefined.")
                    
                    # Calculates the cross sectional area of the object
                    numerator: float = init_length * force
                    denominator: float = shear_mod * delta_layers

                    return numerator / denominator

                if init_length == None:
                    
                    if force == 0.0:
                        raise ValueError("Division by zero is undefined.")
                    
                    # Calculates initial length of the object
                    numerator: float = shear_mod * delta_layers * cross_section
                    denominator: float = force 

                    return numerator / denominator
                
                if delta_layers == None:

                    if shear_mod == 0.0:
                        raise ValueError("Divison by zero is undefined.")
                    
                    # Calculates for the change in length
                    numerator: float = init_length * force
                    denominator: float = shear_mod * cross_section

                    return numerator / denominator

                return (force / cross_section) * (init_length / delta_layers)

                