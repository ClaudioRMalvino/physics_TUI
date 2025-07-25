import unittest
from typing import Any, List
from unittest.case import TestCase

from physics_TUI.chapters.chapter9 import Chapter9


class TestInelasticCollisionMomentum(unittest.TestCase):
    """
    Tests the main use cases of calculations for the inelastic collision of
    two bodies.
    """

    def test_solving_for_mass_1(self) -> None:
        """
        Function tests solving for the mass of the first object (mass_1)
        """

        # Initial conditions
        mass_2: List[float] = [
            -10.0,
            10.0,
            10.0,
        ]
        velocity_1: List[float] = [
            10.0,
            0.0,
            10.0,
        ]
        velocity_2: List[float] = [
            30.0,
            30.0,
            30.0,
        ]
        velocity_f: List[float] = [20.0, 20.0, 20.0]
        mass_f: List[float] = [10.0, 20.0, 20.0]

        expected: List[Any] = [
            ValueError(
                "We are operating with massive objects. Make sure all objects have a mass greater than zero."
            ),
            ValueError("Division by zero is undefined."),
            10.0,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter9.Calculate.inelastic_collision_momentum(
                        mass_2=mass_2[i],
                        velocity_1=velocity_1[i],
                        velocity_2=velocity_2[i],
                        velocity_f=velocity_f[i],
                        mass_f=mass_f[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter9.Calculate.inelastic_collision_momentum(
                    mass_2=mass_2[i],
                    velocity_1=velocity_1[i],
                    velocity_2=velocity_2[i],
                    velocity_f=velocity_f[i],
                    mass_f=mass_f[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_mass_2(self) -> None:
        """
        Function tests solving for the mass of the second object (mass_2)
        """

        # Initial conditions

        mass_1: List[float] = [
            -10.0,
            10.0,
            10.0,
        ]
        velocity_1: List[float] = [
            10.0,
            0.0,
            10.0,
        ]
        velocity_2: List[float] = [
            30.0,
            30.0,
            30.0,
        ]
        velocity_f: List[float] = [20.0, 20.0, 20.0]
        mass_f: List[float] = [10.0, 20.0, 20.0]

        expected: List[float] = []
