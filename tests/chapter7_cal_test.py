import unittest

from typing import List, Any
from unittest.case import TestCase
from physics_TUI.chapters.chapter7 import Chapter7


class TestWorkConstantForce(unittest.TestCase):
    """
    Tests the main use cases of calculations for the work given a cosntant
    force.
    """

    def test_solving_for_work(self) -> None:
        """
        Function tests solving for the work done by a system (work)
        """

        # Initial conditions
        const_F: List[float] = [0.0, 100.0, 500.0]
        distance: List[float] = [10.0, 10.0, 20.0]
        theta: List[float] = [0.0, 0.0, 90.0]

        expected: List[float] = [0.0, 1000.0, 0.0]

        for i in range(len(expected)):
            result = Chapter7.Calculate.work_constant_force(
                const_F=const_F[i], distance=distance[i], theta=theta[i]
            )
            self.assertAlmostEqual(result, expected[i], places=2)
    
    def test_solving_for_const_F(self) -> None:
        """
        Function tests solving for constant force applied to a sytem (const_F)
        """

        # Initial conditions
        work: List[float] = [0.0, 1000.0, 2000.0, 1000.0]
        theta: List[float] = [0.0, 0.0, 90.0, 45.0]
        distance: List[float] = [10.0, 10.0, 20.0, 0.0]

        expected: List[Any] = [
            0.0,
            100.0,
            ValueError("Division by zero is undefined."),
            ValueError("Division by zero is undefined.")
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter7.Calculate.work_constant_force(
                        work=work[i], distance=distance[i], theta=theta[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter7.Calculate.work_constant_force(
                    work=work[i], distance=distance[i], theta=theta[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)

