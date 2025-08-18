from typing import List, Optional, Dict
from physics_TUI.base_chapter import PhysicsChapter, Equation, Definition

# Global constant
g: float = 9.82  # Acceleration due to gravity on Earth [m/s^2]


class Chapter14(PhysicsChapter):
    """
    Chapter on Fluid Dynamics
    """

    def __init__(self) -> None:
        super().__init__("Ch.14 - Fluid Dynamics")

        self.var_mapping: Dict[str, str] = {
            "p": "pressure",
            "p₀": "pressure_atm",
            "ρ": "density",
            "h": "depth",
            "F(1)": "force_1",
            "A(1)": "area_1",
            "F(2)": "force_2",
            "A(2)": "area_2",
            "v(1)": "velocity_1",
            "v(2)": "Velocity_2",
            "ρ(1)": "density_1",
            "ρ(2)": "density_2",
            "p(1)": "pressure_1",
            "p(2)": "pressure_2",
            "y(1)": "height_1",
            "y(2)": "height_2",
            "η": "viscocity",
            "F": "force",
            "L": "distance",
            "A": "area",
            "v": "velocity",
            "R": "resistance",
            "l": "length",
            "r": "radius",
            "Q": "flow",      
        }

        self.equations: List[Equation] = [
            Equation(
                name="Density of a sample at constant density",
                formula="ρ = m/V",
                variables={
                    "ρ": "Density (kg/m³)",
                    "m": "mass (kg)",
                    "V": "Volume (m³)",
                },
            ),
            Equation(
                name="Pressure",
                formula="p = F/A",
                variables={"p": "Pressure (N/m²)", "F": "Force (N)", "A": "Area (m²)"},
            ),
            Equation(
                name="Hydrostatic pressure",
                formula="p = p₀ + ρgh",
                variables={
                    "p": "Pressure at depth (Pa)",
                    "p₀": "Pressure at atmosphere (Pa)",
                    "ρ": "Density of the fluid (kg/m³)",
                    "h": "Depth (m)",
                },
                calculation=self.Calculate.hydrostatic_pressure,
            ),
            Equation(
                name="Pressure gradiant in a fluid of constant density",
                formula="dp/dy = -ρg",
                variables={
                    "dp/dy": "Rate of change of pressure with respect to height",
                    "ρ": "Density of the fluid (kg/m³)",
                },
            ),
            Equation(
                name="Absolute pressure",
                formula="p(abs) = p(g) + p(atm)",
                variables={
                    "p(abs)": "Absolute pressure (Pa)",
                    "p(g)": "Gauge pressure (Pa)",
                    "p(atm)": "Atmospheric pressure (Pa)",
                },
            ),
            Equation(
                name="Pascal's principle",
                formula="F(1)/A(1) = F(2)/A(2)",
                variables={
                    "F(1)": "Force applied by piston 1 (N)",
                    "A(1)": "Area of piston 1 (m²)",
                    "F(2)": "Force applied by piston 2 (N)",
                    "A(2)": "Area of piston 2 (m²)",
                },
                calculation=self.Calculate.pascals_principle,
            ),
            Equation(
                name="Volume flow rate",
                formula="Q = dV/dt",
                variables={
                    "Q": "Flow rate",
                    "dV/dt": "Rate of change of the volume with respect to time",
                },
            ),
            Equation(
                name="Continuity equation (constant density)",
                formula="A(1)v(1) = A(2)v(2)",
                variables={
                    "A(1)": "Area of nozzle 1 (m²)",
                    "v(1)": "Velocity of fluid in nozzle 1 (m/s)",
                    "A(2)": "Area of nozzle 2 (m²)",
                    "v(2)": "Velocity of fluid in nozzle 2 (m/s)",
                },
                calculation=self.Calculate.continuity_const_density,
            ),
            Equation(
                name="Continuity equation (general form)",
                formula="ρ(1)A(1)v(1) = ρ(2)A(2)v(2)",
                variables={
                    "ρ(1)": "Density of the fluid in nozzle 1 (kg/m³)",
                    "A(1)": "Area of nozzle 1 (m²)",
                    "v(1)": "Velocity of fluid in nozzle 1 (m/s)",
                    "ρ(2)": "Density of the fluid in nozzle 2 (kg/m³)",
                    "A(2)": "Area of nozzle 2 (m²)",
                    "v(2)": "Velocity of fluid in nozzle 2 (m/s)",
                   
                },
                calculation=self.Calculate.continuity_const_general,
            ),
            Equation(
                name="Bernoulli's equation",
                formula="p(1) + ½ρv(1)² + ρgy(1) = p(2) + ½ρv(2)² + ρgy(2)",
                variables={
                    "ρ": "Density of the fluid (kg/m³)",
                    "p(1)": "Pressure of the fluid in moment 1 (Pa)",
                    "v(1)": "Velocity of the fluid in moment 1 (m/s)",
                    "y(1)": "Height of the fluid in moment 1 (m)",
                    "p(2)": "Pressure of the fluid in moment 1 (Pa)",
                    "v(2)": "Velocity of the fluid in moment 1 (m/s)",
                    "y(2)": "Height of the fluid in moment 1 (m)",
                },
                calculation=self.Calculate.bernoullis_equation,
            ),
            Equation(
                name="Viscocity",
                formula="η = FL/(vA)",
                variables={
                    "η": "Viscocity (Pa⋅s)",
                    "F": "Force (N)",
                    "L": "Distance between plates (m)",
                    "A": "Area of the plates (m²)",
                    "v": "Velocity of the fluid (m/s)",
                },
                calculation=self.Calculate.viscocity,
            ),
            Equation(
                name="Poiseuille’s law for resistance",
                formula="R = 8ηl/(πr⁴)",
                variables={
                    "R": "Resistance to laminar flow",
                    "η": "Viscocity (Pa⋅s)",
                    "l": "Length of the tube (m)",
                    "r": "Radius of the tube (m)",
                },
                calculation=self.Calculate.poiseuilles_law_resistance,
            ),
            Equation(
                name="Poiseuille’s law",
                formula="Q = (p(1) - p(2))πr⁴/(8ηl)",
                variables={
                    "Q": "Flow rate",
                    "η": "Viscocity (Pa⋅s)",
                    "l": "Length of the tube (m)",
                    "r": "Radius of the tube (m)",
                    "p(1)": "Pressure at point 1 (Pa)",
                    "p(2)": "Pressure at point 2 (Pa)",
                },
                calculation=self.Calculate.poiseuilles_law,
            ),
        ]

        self.definitions: List[Definition] = [
            Definition(
                term="absolute pressure",
                meaning="sum of gauge pressure and atmospheric pressure",
            ),
            Definition(
                term="Archimedes' principle",
                meaning="buoyant force on an object equals the weight of the fluid it displaces",
            ),
            Definition(
                term="Bernoulli's equation",
                meaning="equation resulting from applying conservation of energy to an incompressible frictionless fluid: p + ½ρv² + ρgh = constant, throughout the fluid",
            ),
            Definition(
                term="Bernoulli's principle",
                meaning="Bernoulli's equation applied at constant depth: p₁ + ½ρv₁² = p₂ + ½ρv₂²",
            ),
            Definition(
                term="buoyant force",
                meaning="net upward force on any object in any fluid due to the pressure difference at different depths",
            ),
            Definition(
                term="density", meaning="mass per unit volume of a substance or object"
            ),
            Definition(
                term="flow rate",
                meaning="abbreviated Q, it is the volume V that flows past a particular point during a time t, or Q = dV/dt",
            ),
            Definition(
                term="fluids",
                meaning="liquids and gases; a fluid is a state of matter that yields to shearing forces",
            ),
            Definition(
                term="gauge pressure",
                meaning="pressure relative to atmospheric pressure",
            ),
            Definition(
                term="hydraulic jack",
                meaning="simple machine that uses cylinders of different diameters to distribute force",
            ),
            Definition(
                term="hydrostatic equilibrium",
                meaning="state at which water is not flowing, or is static",
            ),
            Definition(term="ideal fluid", meaning="fluid with negligible viscosity"),
            Definition(
                term="laminar flow",
                meaning="type of fluid flow in which layers do not mix",
            ),
            Definition(
                term="Pascal's principle",
                meaning="change in pressure applied to an enclosed fluid is transmitted undiminished to all portions of the fluid walls of its container",
            ),
            Definition(
                term="Poiseuille's law",
                meaning="rate of laminar flow of an incompressible fluid in a tube: Q = (p₁-p₂)πr⁴/8ηl",
            ),
            Definition(
                term="Poiseuille's law for resistance",
                meaning="resistance to laminar flow of an incompressible fluid in a tube: R = 8ηl/πr⁴",
            ),
            Definition(
                term="pressure",
                meaning="force per unit area exerted perpendicular to the area over which the force acts",
            ),
            Definition(
                term="Reynolds number",
                meaning="dimensionless parameter that can reveal whether a particular flow is laminar or turbulent",
            ),
            Definition(
                term="specific gravity",
                meaning="ratio of the density of an object to a fluid (usually water)",
            ),
            Definition(
                term="turbulence",
                meaning="fluid flow in which layers mix together via eddies and swirls",
            ),
            Definition(
                term="turbulent flow",
                meaning="type of fluid flow in which layers mix together via eddies and swirls",
            ),
            Definition(
                term="viscosity", meaning="measure of the internal friction in a fluid"
            ),
        ]

    class Calculate:
        """
        Class holds methods to calculate equations in Chapter 14
        """

        @staticmethod
        def hydrostatic_pressure(
            pressure: Optional[float]=None,
            pressure_atm: Optional[float]=None,
            density: Optional[float]=None,
            depth: Optional[float]=None,
        ) -> float:
            """
            Function calculates the hydrostatic pressure as a function of
            the depth, atmospheric pressure, and fluid density.
            Can also calculate for desired variable when arg == None
            and all other args have values.

            Args:
                pressure (Optional[float], optional): hydrostatic pressure (Pa). Defaults to None.
                pressure_atm (Optional[float], optional): atmospheric pressure (Pa). Defaults to None.
                density (Optional[float], optional): density of the fluid [kg/m³]. Defaults to None.
                depth (Optional[float], optional): depth [m]. Defaults to None.

            Raises:
                ValueError: "Division by zero is undefined."
                ValueError: "Hydrostatic or atmospheric pressure cannot be a negative value."


            Returns:
                float: the result of whichever variable was left equal to None
            """

            if pressure is not None and pressure < 0.0 or pressure_atm is not None and pressure_atm < 0.0:
                raise ValueError("Hydrostatic or atmospheric pressure cannot be a negative value.")

            if pressure_atm == None:
                # Calculates the atmospheric pressure
                return pressure - (density * g * depth)

            if density == None:

                if depth == 0.0:
                    raise ValueError("Division by zero is undefined.")
                # Calculates the fluid density
                return (pressure - pressure_atm) / (g * depth)
            
            if depth == None:
                
                if density == 0.0:
                    raise ValueError("Division by zero is undefined.")
                # Calculates the depth
                return (pressure - pressure_atm) / (g * density)

            return pressure_atm + ( density * g * depth)
        
        @staticmethod
        def pascals_principle(
            force_1: Optional[float]=None,
            area_1: Optional[float]=None,
            force_2: Optional[float]=None,
            area_2: Optional[float]=None
        ) -> float:
            """
            Function utilizes Pascal's principle to calculate the force and area of
            two connected hydraulic systems.
           
            Args:
                force_1 (Optional[float], optional): Force applied in hydraulic 1 [N]. Defaults to None.
                area_1 (Optional[float], optional): Area of hydraulic 1 [m²]. Defaults to None.
                force_2 (Optional[float], optional): Force applied in hydraulic 2 [N]. Defaults to None.
                area_2 (Optional[float], optional): Area of hydraulic 2 [m²]. Defaults to None.

            Raises:
                ValueError: "Division by zero is undefined."

            Returns:
                float: the result of whichever variable was left equal to None
            """
            
            if force_1 == None:

                if area_2 == 0.0:
                    raise ValueError("Division by zero is undefined.")

                return (force_2 / area_2) * area_1
            
            if area_1 == None:

                if force_2 == 0.0:
                    raise ValueError("Division by zero is undefined.")

                return (force_1 * area_2) / force_2
            
            if force_2 == None:

                if area_1 == 0.0:
                    raise ValueError("Division by zero is undefined.")

                return (force_1 / area_1) * area_2
            
            if area_2 == None:

                if force_1 == 0.0:
                    raise ValueError("Division by zero is undefined.")

                return (force_2 * area_1) / force_1
            
            return 0.0

        
        @staticmethod
        def continuity_const_density(
            area_1: Optional[float]=None,
            velocity_1: Optional[float]=None,
            area_2: Optional[float]=None,
            velocity_2: Optional[float]=None
        ) -> float: 
            """
            Function utilizes the continuity equation to calculate the area and velocity
            of a fluid traversing two distinct nozzles. 

            Args:
                area_1 (Optional[float], optional): cross sectional area of the first tube [m²]. Defaults to None.
                velocity_1 (Optional[float], optional): velocity of the fluid in the first tube [m/s]. Defaults to None.
                area_2 (Optional[float], optional): cross sectional area of the second tube [m²]. Defaults to None.
                velocity_2 (Optional[float], optional): velocity of the fluid in the second tube [m/s]. Defaults to None.

            Raises:
                ValueError: "Divison by zero is undefined."
               
            Returns:
                float: the result of whichever variable was left equal to None
            """

            if area_1 is not None and area_1 <= 0.0 or area_2 is not None and area_2 <= 0.0:
                raise ValueError("Area cannot be less than or equal to zero.")
            
            if area_1 == None:

                if velocity_1 == 0.0:
                    raise ValueError("Divison by zero is undefined.")
                
                return (area_2 * velocity_2) / velocity_1
            
            if velocity_1 == None:
                return (area_2 * velocity_2) / area_1
            
            if area_2 == None:

                if velocity_2 == 0.0:
                    raise ValueError("Divison by zero is undefined.")
                
                return (area_1 * velocity_1) / velocity_2

            if velocity_2 == None:
                return (area_1 * velocity_1) / area_2
            
            return 0.0
        
        @staticmethod 
        def continuity_const_general(
            density_1: Optional[float]=None,
            area_1: Optional[float]=None,
            velocity_1: Optional[float]=None,
            density_2: Optional[float]=None,
            area_2: Optional[float]=None,
            velocity_2: Optional[float]=None
        ) -> float:
            """
            Function utilizes the  general continuity equation to calculate the area, velocity
            and density of a fluid traversing two distinct nozzles. 

            Args:
                density_1 (Optional[float], optional): density of fluid in first nozzle [kg/m³]. Defaults to None.
                area_1 (Optional[float], optional): cross setional area of the first nozzle [m²]. Defaults to None.
                velocity_1 (Optional[float], optional): velocity of the fluid in the first nozzle [m/s]. Defaults to None.
                density_2 (Optional[float], optional): density of fluid in second nozzle [kg/m³]. Defaults to None.
                area_2 (Optional[float], optional): cross setional area of the second nozzle [m²]. Defaults to None.
                velocity_2 (Optional[float], optional): velocity of the fluid in the second nozzle [m/s]. Defaults to None.

            Raises:
                ValueError: "Area cannot be less than or equal to zero."
                ValueError: "Density of a fluid cannot be less than or equal to zero."
                ValueError: "Division by zero is undefined."

            Returns:
                float: the result of whichever variable was left equal to None
            """

            if area_1 is not None and area_1 <= 0.0 or area_2 is not None and area_2 <= 0.0:
                raise ValueError("Area cannot be less than or equal to zero.")

            if density_1 is not None and density_1 <= 0.0 or density_2 is not None and density_2 <= 0.0:
                raise ValueError("Density of a fluid cannot be less than or equal to zero.")
            
            if density_1 == None:

                if velocity_1 == 0.0:
                    raise ValueError("Division by zero is undefined.")
                
                numerator:float = (density_2 * area_2 * velocity_2)
                denominator: float = area_1 * velocity_1
                
                return numerator/denominator
            
            if area_1 == None:

                if velocity_1 == 0.0:
                    raise ValueError("Division by zero is undefined.")
                
                numerator:float = (density_2 * area_2 * velocity_2)
                denominator: float = density_1 * velocity_1
                
                return numerator/denominator
            
            if velocity_1 == None:
                  
                numerator:float = (density_2 * area_2 * velocity_2)
                denominator: float = density_1 * area_1
                
                return numerator/denominator

            if density_2 == None:

                if velocity_2 == 0.0:
                    raise ValueError("Division by zero is undefined.")
                
                numerator:float = (density_1 * area_1 * velocity_1)
                denominator: float = area_2 * velocity_2
                
                return numerator/denominator
            
            if area_2 == None:

                if velocity_1 == 0.0:
                    raise ValueError("Division by zero is undefined.")
                
                numerator:float = (density_1 * area_1 * velocity_1)
                denominator: float = density_2 * velocity_2
                
                return numerator/denominator
            
            if velocity_2 == None:

                numerator:float = (density_1 * area_1 * velocity_1)
                denominator: float = density_2 * area_2
                
                return numerator/denominator
            
            return 0.0
            
        @staticmethod
        def bernoullis_equation(
            density: Optional[float]=None,
            pressure_1: Optional[float]=None,
            velocity_1: Optional[float]=None,
            height_1: Optional[float]=None,
            pressure_2: Optional[float]=None,
            velocity_2: Optional[float]=None,
            height_2: Optional[float]=None,
        ) -> float:
            """
            Function utilizes Bernoullis equation to solve for the density of the fluid,
            pressure, velocity, and height at two points.

            Args:
                density (Optional[float], optional): density of the fluid [kg/m³]. Defaults to None.
                pressure_1 (Optional[float], optional): pressure of the fluid at position 1 [Pa]. Defaults to None.
                velocity_1 (Optional[float], optional): velocity of the fluid at position 1 [m/s]. Defaults to None.
                height_1 (Optional[float], optional): height of the fluid at position 1 [m]. Defaults to None.
                pressure_2 (Optional[float], optional): pressure of the fluid at position 2 [Pa]. Defaults to None.
                velocity_2 (Optional[float], optional): velocity of the fluid at position 2 [m/s]. Defaults to None.
                height_2 (Optional[float], optional): height of the fluid at position 2 [m]. Defaults to None.

            Raises:
                ValueError: "Density of a fluid cannot be less than or equal to zero."
                ValueError: "Division by zero is undefined."
                ValueError: "Negative radicand yields an imaginary number"

            Returns:
                float: the result of whichever variable was left equal to None
            """
            
            if density is not None and density <= 0.0:
                raise ValueError("Density of a fluid cannot be less than or equal to zero.")

            if density == None:

                term1: float = 0.5 * (velocity_1 * velocity_1)
                term2: float = g * height_1
                term3: 0.5 * (velocity_2 * velocity_2)
                term4: float = g * height_2
                numerator: float = pressure_2 - pressure_1
                denominator: float = term1 + term2 - term3 - term4

                if denominator == 0.0:
                    raise ValueError("Divison by zero is undefined.")

                return numerator / denominator
            
            if pressure_1 == None:

                term1: float = 0.5 * (velocity_1 * velocity_1)
                term2: float = g * height_1
                term3: 0.5 * (velocity_2 * velocity_2)
                term4: float = g * height_2

                return pressure_2 + term3 + term4 - term1 - term2
            
            if velocity_1 == None:
                
                term1: float = 0.5 * (velocity_1 * velocity_1)
                term2: float = g * height_1
                term3: 0.5 * (velocity_2 * velocity_2)
                term4: float = g * height_2
                coeff: float = (0.5) * density
                radicand:float = pressure_2 - pressure_1 + term3 + term4 - term2
                
                if radicand < 0.0:
                    raise ValueError("Negative radicand yields an imaginary number")
                
                return sqrt(coeff*radicand)
            
            if height_1 == None:
                
                term1: float = 0.5 * (velocity_1 * velocity_1)
                term2: float = g * height_1
                term3: 0.5 * (velocity_2 * velocity_2)
                term4: float = g * height_2

                return (pressure_2 - pressure_1 + term3 + term4 - term1) / g
            
            if pressure_2 == None:

                term1: float = 0.5 * (velocity_1 * velocity_1)
                term2: float = g * height_1
                term3: 0.5 * (velocity_2 * velocity_2)
                term4: float = g * height_2

                return pressure_1 - term3 - term4 + term1 +term2
            
            if velocity_2 == None:
                
                term1: float = 0.5 * (velocity_1 * velocity_1)
                term2: float = g * height_1
                term3: 0.5 * (velocity_2 * velocity_2)
                term4: float = g * height_2
                coeff: float = (0.5) * density
                radicand:float = -pressure_2 + pressure_1 - term4 + term2 + term1
                
                if radicand < 0.0:
                    raise ValueError("Negative radicand yields an imaginary number")
                
                return sqrt(coeff*radicand)
            
            if height_2 == None:
                
                term1: float = 0.5 * (velocity_1 * velocity_1)
                term2: float = g * height_1
                term3: 0.5 * (velocity_2 * velocity_2)
                term4: float = g * height_2

                return (-pressure_2 + pressure_1 - term3 + term2 + term1) / g
            
            return 0.0

        @staticmethod
        def viscocity(
            viscocity: Optional[float]=None,
            force: Optional[float]=None,
            distance: Optional[float]=None,
            area: Optional[float]=None,
            velocity: Optional[float]=None,
        ) -> float:
            
            if length is not None and length <= 0.0 or area is not None and area <= 0.0:
                raise ValueError("Dimensions of length and area cannot be less than or equal to zero.")
            
            if force == None:
                return viscocity * ((velocity * area) / distance)
            
            if distance == None:
                return viscocity * ((velocity * area) / force)
            
            if area == None:

                if velocity == 0.0 or viscocity == 0.0:
                    raise ValueError("Division by zero is undefined.")

                return ((force * distance) / (viscocity * velocity))
            
            if velocity == None:
                
                if viscocity == 0.0:
                    raise ValueError("Division by zero is undefined.")

                return ((force * distance) / (viscocity * area))
            
            if viscocity == 0.0:
                    raise ValueError("Division by zero is undefined.")
            
            return (force * distance) /  (velocity * area)
        
        @staticmethod
        def poiseuilles_law_resistance(
            resistance: Optional[float]=None,
            viscocity: Optional[float]=None,
            length: Optional[float]=None,
            radius: Optional[float]=None,
        ) -> float:
            
            if length is not None and length <= 0.0 or radius is not None and radius <= 0.0:
                raise ValueError("Dimensions of length and radius cannot be less than or equal to zero.")
            
            if viscocity == None:
                return (resistance * pi * radius**4) / (8.0 * length)
            
            if length == None:
                return (resistance * pi * radius**4) / (8.0 * viscocity)
            
            if radius == None:
                
                if resistance == 0.0:
                    raise ValueError("Division by zero is undefined.")
                radicand: float = (8.0 * viscocity * length) / (pi * resistance)

                return radicand**1/4
            
            return (8.0 * viscocity * length) / (pi * radius**4)            

        @staticmethod
        def poiseuilles_law(
            flow: Optional[float]=None,
            viscocity: Optional[float]=None,
            length: Optional[float]=None,
            radius: Optional[float]=None,
            pressure_1: Optional[float]=None,
            pressure_2: Optional[float]=None,
        ) -> float:
            
            if length is not None and length <= 0.0 or radius is not None and radius <= 0.0:
                raise ValueError("Dimensions of length and radius cannot be less than or equal to zero.")
            
            if viscocity == None:
                
                if flow == 0.0:
                    raise ValueError("Division by zero is undefined.")

                numerator: float = (pressure_2 - pressure_1) * (pi * (radius**4))
                denominator: float = 8.0 * length * flow

                return numerator / denominator
            
            if length == None:
                
                if viscocity == 0.0 or flow == 0.0:
                    raise ValueError("Division by zero is undefined.")

                numerator: float = (pressure_2 - pressure_1) * (pi * (radius**4))
                denominator: float = 8.0 * viscocity * flow

                return numerator / denominator
                
            if radius == None:

                numerator: float = flow * 8.0 * viscocity * length
                denominator: float = (pressure_2 - pressure_1) * pi
                radicand: float = numerator / denominator

                return (radicand)**1/4

            if pressure_1 == None:

                numerator: float = -flow * 8.0 * viscocity * length
                denominator: float = pi * radius**4
                return (numerator/denominator) + pressure_2

            if pressure_2 == None:

                numerator: float = flow * 8.0 * viscocity * length
                denominator: float = pi * radius**4
                return (numerator/denominator) + pressure_1
            
            numerator: float = (pressure_2 - pressure_1) * pi * radius**4
            denominator: float = 8.0 * viscocity * length

            return numerator / denominator


