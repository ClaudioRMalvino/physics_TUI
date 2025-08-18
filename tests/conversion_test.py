import unittest
from typing import List
from unittest.case import TestCase

from physics_TUI.unit_converter import Length


class TestLengthUnitConversion(unittest.TestCase):
    """
    Tests the conversion method within the Length class for unit conversion
    """


    def setUp(self) -> None:
        """
        Set up the Length instance for testing
        """
        self.length_converter = Length()

    def test_converting_from_meter_to_kilometer(self) -> None:
        """
        Function testrs converting from meters to kilometer 
        """

        # Test cases
        scalar: List[float] = [1.0, 30.0, 1000.0, 1500.0]
        meters: List[str] =["meter", "meter","meter", "meter"] 
        kilometers: List[str] = ["kilometer", "kilometer", "kilometer", "kilometer"]

        expected: List[float] = [0.001, 0.03, 1.0, 1.5]

        for i in range(len(expected)):
            result = self.length_converter.conversion(
                scalar=scalar[i],
                from_unit=meters[i],
                to_unit=kilometers[i]
            )
            self.assertEqual(result, expected[i],)

    def test_converting_from_kilometer_to_meter(self) -> None:
        """
        Function testrs converting from meters to kilometer 
        """

        # Test cases
        scalar: List[float] = [1.0, 30.0, 0.5, 0.1]
        meters: List[str] =["meter", "meter","meter", "meter"] 
        kilometers: List[str] = ["kilometer", "kilometer", "kilometer", "kilometer"]

        expected: List[float] = [1000, 30000, 500, 100]

        for i in range(len(expected)):
            result = self.length_converter.conversion(
                scalar=scalar[i],
                from_unit=kilometers[i],
                to_unit=meters[i]
                )
            self.assertEqual(result, expected[i],)

    def test_converting_from_nanometer_to_millimeter(self) -> None:
        """
        Function tests converting from nanometers to millimeter
        """

        # Test cases
        scalar: List[float] = [1.0, 30.0, 0.01, 250.0]
        nanometers: List[float] = ["nanometer", "nanometer", "nanometer", "nanometer",]
        millimeters: list[float] = ["millimeter", "millimeter", "millimeter", "millimeter",]

        expected: List[float] = [1.0E-6, 3.0E-5, 1.0E-8, 2.5E-4]

        for i in range(len(expected)):
            result = self.length_converter.conversion(
                scalar=scalar[i],
                from_unit=nanometers[i],
                to_unit=millimeters[i]
            )
            print(f"result = {result}")
            self.assertAlmostEqual(result, expected[i], places=6)

    def test_converting_from_inch_to_meter(self) -> None:
        """
        Function tests convering from inches to meters
        """
        
        
        