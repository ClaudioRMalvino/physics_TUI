from typing import Dict, Any
from math import fabs, pow


class Quantity:
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

    def conversion(self, scalar: float, from_unit: str, to_unit: str) -> float:
        """
        Method handles conversions from a unit to aother. This is implemented
        by relating every unit to the base unit.

        Args:
            scalar (float): The scalar value (distance)
            from_unit (str): The unit which the user want to convert from
            to_unit (str): The unit which the user wats to convert to

        Returns:
            float: the value of the conversion
        """

        base_unit: float = scalar * self.units[from_unit]
        conversion: float = base_unit / self.units[to_unit]

        return conversion


class Length(Quantity):
    """
    Represents the set of units of length.
    The base unit for the conversion method is meters.

    Args:
        Quantities (class): base class
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Length"
        self.units: Dict[str, float] = {
            "angstrom": 1.0E-10,
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


class Mass(Quantity):
    """
    Represents the set of units of mass.
    The base unit for the conversion method is grams.

    Args:
        Quantities (class): base class
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Mass"
        self.units: Dict[str, float] = {
            "atomic mass unit": 1.66E-24,
            "nanogram": 1.0E-9,
            "microgram": 1.0E-6,
            "milligram": 1.0E-3,
            "centigram": 1.0E-2,
            "decimgram": 1.0E-1,
            "gram": 1.0,
            "kilogram": 1.0E+3,
            "ounce": 28.349,
            "pound": 453.59,
            "ton": 907_184.74
        }


class Pressure(Quantity):
    """
    Represents the set of units of pressure
    The base unit for the conversion method is Pascals.

    Args:
        Quantities (class): base class
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Pressure"
        self.units: Dict[str, float] = {
            "nanopascal": 1.0E-9,
            "micropascal": 1.0E-6,
            "millipascal": 1.0E-3,
            "centipascal": 1.0E-2,
            "decipascal": 1.0E-1,
            "pascal": 1.0,
            "kilopascal": 1.0E+3,
            "bar": 1.0E+5,
            "psi": 6894.7572,
            "ksi": 6894757.2932,
            "atm": 101325
        }


class Energy(Quantity):
    """
    Represents the set of units of energy.
    The base unit for the conversion method is joules.

    Args:
        Quantities (class): base class
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Energy"
        self.units: Dict[str, float] = {
            "nanojoule": 1.0E-9,
            "microjoule": 1.0E-6,
            "millijoule": 1.0E-3,
            "centijoule": 1.0E-2,
            "decijoule": 1.0E-1,
            "joule": 1.0,
            "kilojoule": 1.0E+3,
            "megajoule": 1.0E+6,
            "watt-hour": 3.6E+3,
            "kilowatt-hour": 3.6E+6,
            "megawatt-hour": 3.6E+6,
            "calorie": 4186.8,
            "electron-volt": 1.60217E-19,
            "kiloelectron-volt": 1.60217E-16,
            "megaelectron-volt": 1.60217E-13,
            "erg": 1.0E-7,
        }


class Speed(Quantity):
    """
    Represents the set of units of speed.
    The base unit for the conversion method is m/s.

    Args:
        Quantities (class): base class
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Speed"
        self.units: Dict[str, float] = {
            "mm/s": 1.0E-3,
            "mm/min": 1.66666E-5,
            "mm/h": 2.77777E-7,
            "cm/s": 1.0E-2,
            "cm/min": 1.66666E-4,
            "cm/hr": 2.7778E-6,
            "m/s": 1.0,
            "m/min": 1.66666E-2,
            "m/h": 2.7777E-4,
            "km/s": 1.0E+3,
            "km/min": 16.66666,
            "km/h": 0.277777,
            "ft/s": 0.3048,
            "ft/min": 5.08E-3,
            "ft/h": 8.46667E-5,
            "yd/s": 0.9144,
            "yd/min": 1.524E-2,
            "yd/h": 2.54E-4,
            "mi/s": 1609.344,
            "mi/min": 26.8224,
            "mi/h": 0.44704,
        }


class Force(Quantity):
    """
    Represents the set of units of force.
    The base unit for the conversion method is newton [N].

    Args:
        Quantities (class): base class
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Force"
        self.units: Dict[str, float] = {
            "nanonewton": 1.0E-9,
            "micronewton": 1.0E-6,
            "millinewton": 1.0E-3,
            "centinewton": 1.0E-2,
            "decinewton": 1.0E-1,
            "newton": 1.0,
            "kilonewton": 1.0E+3,
            "meganewton": 1.0E+6,
            "pound-force": 4.44822,
            "ounce-fource": 0.27801
        }


class Time(Quantity):
    """
    Represents the set of units of time.
    The base unit for the conversion method is second [s].

    Args:
        Quantity (class): base Cass
    """

    def __init__(self) -> None:
        super().__init__()
        self.name: str = "Time"
        self.units: Dict[str, float] = {
            "nanosecond": 1.0E-9,
            "microsecond": 1.0E-6,
            "millisecond": 1.0E-3,
            "second": 1.0,
            "minute": 60,
            "hour": 3600,
            "day": 8.64E+5,
            "week": 6.048E+5,
            "month": 2.628E+6,
            "year": 3.15576E+7,
        }
