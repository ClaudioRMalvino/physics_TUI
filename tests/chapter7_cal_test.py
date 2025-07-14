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

    def test_solving_for_distance(self) -> None:
        """
        Function tests solving for the distance (distance)
        """

        # Initial conditions
        work: List[float] = [0.0, 500.0, 500.0, 1000.] 
        const_F: List[float] = [500.0, 0.0, 500.0, 1000]
        theta: List[float] = [0.0, 0.0, 90.0, 0.0]

        expected: List[Any] = [
            0.0,
            ValueError("Division by zero is undefined."),
            ValueError("Division by zero is undefined."),
            1.0
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter7.Calculate.work_constant_force(
                        work=work[i], const_F=const_F[i], theta=theta[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter7.Calculate.work_constant_force(
                    work=work[i], const_F=const_F[i], theta=theta[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_theta(self) -> None:
        """
        Function tests solving for the angle (theta)
        """

        # Intiial conditions
        work: List[float] = [1000.0, 0.0, 0.0]
        const_F: List[float] = [100.0, 0.0, 10.0]
        distance: List[float] = [10.0, 10.0, 0.0]

        expected: List[Any] = [
            0.0,
            ValueError("Division by zero is undefined."),
            ValueError("Division by zero is undefined."),
            ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter7.Calculate.work_constant_force(
                        work=work[i], const_F=const_F[i], distance=distance[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter7.Calculate.work_constant_force(
                    work=work[i], const_F=const_F[i], distance=distance[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)

class TestWorkDoneByGravity(unittest.TestCase):
    """
    Tests the main use cases of calculations for the work done by gravity.
    """

    def test_solving_for_work(self) -> None:
        """
        Function tests solving for the work done by gravity (work)
        """

        # Initial conditions
        mass: List[float] = [0.0, 5.0, 45.0]
        initial_height: List[float] = [20.0 , 10.0, 100.0]
        final_height: List[float] = [10.0, 10.0, 0.0]

        expected: List[Any] = [
            ValueError(
                    "We are operating with massive objects. \
                Mass must be greater than zero."
                ),
                0.0,
                44190.0
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter7.Calculate.work_by_gravity(
                        mass=mass[i], 
                        initial_height=initial_height[i], 
                        final_height=final_height[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter7.Calculate.work_by_gravity(
                        mass=mass[i], 
                        initial_height=initial_height[i], 
                        final_height=final_height[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)
        
    def test_solving_for_mass(self) -> None:
        """
        Function tests solving for the mass of the object (mass)
        """

        # Initial conditions
        work: List[float] = [1000.0, 1000.0, 1000.0]
        initial_height: List[float] = [1000.0, 0.0, 100.0]
        final_height: List[float] = [0.0, 100.0, 100.0]

        expected: List[Any] = [
            0.1018,
            ValueError(
                        "Mass cannot be negative. Check your signs or initial and final heights."
                    ),

            ValueError("Division by zero is undefined.")
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter7.Calculate.work_by_gravity(
                        work=work[i], 
                        initial_height=initial_height[i], 
                        final_height=final_height[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter7.Calculate.work_by_gravity(
                        work=work[i], 
                        initial_height=initial_height[i], 
                        final_height=final_height[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_initial_height(self) -> None:
        """
        Function tests solving for the initial height (initial_height)
        """

        # Initial conditions
        work: List[float] = [1000.0, 2000.0, 1000.0]
        mass: List[float] = [25.0, 25.0, 50.0]
        final_height: List[float] = [0.0, 0.0, 0.0]

        expected: List[Any] = [
            4.07, 
            8.14,
            2.03
            ]

        for i in range(len(expected)):
            result = Chapter7.Calculate.work_by_gravity(
                        work=work[i], 
                        mass=mass[i], 
                        final_height=final_height[i]
            )
            self.assertAlmostEqual(result, expected[i], places=1)

    def test_solving_for_final_height(self) -> None:
        """
        Function tests solving for the final height (final_height)
        """

        # Initial conditions
        work: List[float] = [1000.0, 2000.0, 1000.0]
        mass: List[float] = [25.0, 25.0, 50.0]
        initial_height: List[float] = [ 4.07, 8.14, 2.03]

        expected: List[Any] = [0.0, 0.0, 0.0]


        for i in range(len(expected)):
            result = Chapter7.Calculate.work_by_gravity(
                        work=work[i], 
                        mass=mass[i], 
                        initial_height=initial_height[i]
            )
            self.assertAlmostEqual(result, expected[i], places=1)
    
class TestWorkBySpring(unittest.TestCase):
    """
    Tests the main use cases of calculations for the work done by a spring.
    """

    def test_solving_for_work(self) -> None:
        """
        Functions tests solving for the work done by the spring (work)
        """

        # Initial conditions
        spring_const: List[float] = [-1.0, 2.0, 10.0]
        initial_xpos: List[float] = [0.0, 3.0, 3.0]
        final_xpos: List[float] = [0.0, 0.0, 0.0]

        expected: List[Any] = [
            ValueError("Spring constant cannot be a negative value."),
            9.0,
            45.0
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter7.Calculate.work_by_spring(
                        spring_const=spring_const[i],
                        initial_xpos=initial_xpos[i],
                        final_xpos=final_xpos[i]
                    )      
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter7.Calculate.work_by_spring(
                        spring_const=spring_const[i],
                        initial_xpos=initial_xpos[i],
                        final_xpos=final_xpos[i]
                    )      
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_spring_const(self) -> None:
        """
        Function tests solving for the spring constant (spring_const)
        """

        # Initial conditions
        work: List[float] = [400.0, 400.0, 400.0]
        initial_xpos: List[float] = [0.25, 0.25, 2.0]
        final_xpos: List[float] = [0.0, 0.25, 0.0 ]

        expected: List[Any] = [
            12800,
            ValueError("Division by zero is undefined."),
            200.0
            ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter7.Calculate.work_by_spring(
                        work=work[i],
                        initial_xpos=initial_xpos[i],
                        final_xpos=final_xpos[i]
                    )      
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter7.Calculate.work_by_spring(
                        work=work[i],
                        initial_xpos=initial_xpos[i],
                        final_xpos=final_xpos[i]
                    )      
                self.assertAlmostEqual(result, expected[i], places=2)