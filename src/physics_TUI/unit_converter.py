from typing import Dict, Any
from math import fabs, pow


class Quantities:
    """
    Class describes the quantity object.
    """

    def __init__(self) -> None:
        self.name: str = ""

        # Holds a map of units of lengths and their relative conversion unit from
        # the base meters
        self.units: Dict[str, float] = {}

    def get_units(self) -> Dict[str, float]:
        """
        Returns the dictionary of the quantities corresponding
        units and their conversion factor.
        """
        return self.units


class Length(Quantities):
    """
    Represents the set of all units of length.

    Args:
        Quantities (class): base class
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Length"
        self.units: Dict[str, float] = {
            "nanometer": 1.0E-9,
            "micrometer": 1.0E-6,
            "millimeter": 1.0E-3,
            "centimeter": 1.0E-2,
            "decimeter": 1.0E-1,
            "meter": 1.0,
            "kilometer": 1.0E+3,
            "inch": 0.0254,
            "foot": 0.3048,
            "yard": 0.9144,
            "mile": 1609.34
        }

    def conversion(self, scalar: float, from_unit: str, to_unit: str) -> float:
        """
        Method handles conversions from a unit to aother. This is implemented
        by relating every unit to the base unit, meters. 

        Args:
            scalar (float): The scalar value (distance)
            from_unit (str): The unit which the user want to convert from
            to_unit (str): The unit which the user wats to convert to

        Returns:
            float: the value of the conversion
        """

        meters: float = scalar * self.units[from_unit]
        conversion: float = meters / self.units[to_unit]
        
        return conversion