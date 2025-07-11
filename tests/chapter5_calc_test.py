import unittest

from typing import List, Any
from physics_TUI.chapters.chapter5 import Chapter5

class Testnormal_force(unittest.TestCase):
    """
    Tests the main use cases of calculations for the normal force equation.
    """

    def test_solving_for_normal_force(self) -> None:
        """
        Functions tests solving for the normal force (normal_F)
        """
        # Initial conditions

        mass: List[float] = [-1.0, 10.0, 50.0, 50.0]
        theta: List[float] = [0.0, 0.0, 90.0, 75.0]

        expected: List[Any] = [
            ValueError("Mass cannot be negative."),
            98.2,
            0.0,
            127.08
        ] 

        for i in range(len(expected)):
                if isinstance(expected[i], ValueError):
                    with self.assertRaises(ValueError) as context:
                        Chapter5.Calculate.normal_force(
                            mass=mass[i],
                            theta=theta[i]
                        )
                    self.assertEqual(str(context.exception), str(expected[i]))
                else:
                    result = Chapter5.Calculate.normal_force(
                            mass=mass[i],
                            theta=theta[i]
                        )
                    self.assertAlmostEqual(result, expected[i], places=2)
    
    def test_solving_for_theta(self) -> None:
        """
        Functions tests solving for theta (theta).
        """

        # Initial conditions

        mass: List[float] = [-1.0, 10.0, 50.0, 50.0]
        normal_F: List[float] = [98.2, 98.2, 0.0, 127.08]

        expected: List[Any] = [
            ValueError("Mass cannot be negative."),
            0.0,
            90.0,
            75.0
        ]

        for i in range(len(expected)):
                if isinstance(expected[i], ValueError):
                    with self.assertRaises(ValueError) as context:
                        Chapter5.Calculate.normal_force(
                            mass=mass[i],
                            normal_F=normal_F[i]
                        )
                    self.assertEqual(str(context.exception), str(expected[i]))
                else:
                    result = Chapter5.Calculate.normal_force(
                            mass=mass[i],
                            normal_F=normal_F[i]
                        )
                    self.assertAlmostEqual(result, expected[i], places=2)
    
    def test_solving_for_mass(self) -> None:
        """
        Function tests solving for mass (mass)
        """

        # Initial conditions

        normal_F: List[float] = [98.2, 98.2, 0.0, 127.0]
        theta: List[float] = [180.0, 0.0, 90.0, 75.0]

        expected: List[Any] = [
            ValueError("Mass cannot be negative."),
            10.0,
            ValueError("Division by zero is undefined."),
            50.0
        ]

        for i in range(len(expected)):
                if isinstance(expected[i], ValueError):
                    with self.assertRaises(ValueError) as context:
                        Chapter5.Calculate.normal_force(
                            theta=theta[i],
                            normal_F=normal_F[i]
                        )
                    self.assertEqual(str(context.exception), str(expected[i]))
                else:
                    result = Chapter5.Calculate.normal_force(
                            theta=theta[i],
                            normal_F=normal_F[i]
                        )
                    self.assertAlmostEqual(result, expected[i], places=1)

class Testhookes_law(unittest.TestCase):
    """
    Tests the main use cases of calculations with F = -kx
    """

    def test_solving_for_force(self) -> None:
        """
        Function tests solving for the restorative force (force)
        """

        # Initial conditions

        spring_const: List[float] = [0.0, -2.0, 2.0, 10.0]
        displacement: List[float] = [0.10, 1.0, -1.0, 2.0]
        
        expected: List[Any] = [
            0.0,
            ValueError("Spring constant (k) cannot be a negative value."),
            2.0,
            -20.0
        ]

        for i in range(len(expected)):
                if isinstance(expected[i], ValueError):
                    with self.assertRaises(ValueError) as context:
                        Chapter5.Calculate.hookes_law(
                            spring_const=spring_const[i],
                            displacement=displacement[i]
                        )
                    self.assertEqual(str(context.exception), str(expected[i]))
                else:
                    result = Chapter5.Calculate.hookes_law(
                            spring_const=spring_const[i],
                            displacement=displacement[i]
                        )
                    self.assertAlmostEqual(result, expected[i], places=2)
    
    def test_solving_for_spring_const(self) -> None:
        """
        Function tests solving for the spring constant (spring_const)
        """

        # Initial conditions

        force: List[float] = [0.0, 20.0, -10.0, 2.0]
        displacement: List[float] = [10.0, 10.0, 0.0, -0.10]

        expected: List[Any] = [
            0.0,
            ValueError("Spring constant cannot be negative. \
                        Consider the relation between the direction \
                        of displacment and the restorative force."),
            ValueError("Divison by zero is undefined."),
            20.0
        ]

        for i in range(len(expected)):
                if isinstance(expected[i], ValueError):
                    with self.assertRaises(ValueError) as context:
                        Chapter5.Calculate.hookes_law(
                            force=force[i],
                            displacement=displacement[i]
                        )
                    self.assertEqual(str(context.exception), str(expected[i]))
                else:
                    result = Chapter5.Calculate.hookes_law(
                            force=force[i],
                            displacement=displacement[i]
                        )
                    self.assertAlmostEqual(result, expected[i], places=2)
    
    def test_solving_for_displacement(self) -> None:
        """
        Function tests solving for the spring constant (spring_const)
        """

        # Initial conditions

        force: List[float] = [0.0, 20.0, -10.0, 2.0]
        spring_const: List[float] = [10.0, 0.0, -10.0, 2.0]

        expected: List[Any] = [
            0.0,
            ValueError("Divison by zero is undefined."),
            ValueError("Spring constant (k) cannot be a negative value."),
            -1.0           
        ]

        for i in range(len(expected)):
                if isinstance(expected[i], ValueError):
                    with self.assertRaises(ValueError) as context:
                        Chapter5.Calculate.hookes_law(
                            force=force[i],
                            spring_const=spring_const[i]
                        )
                    self.assertEqual(str(context.exception), str(expected[i]))
                else:
                    result = Chapter5.Calculate.hookes_law(
                            force=force[i],
                            spring_const=spring_const[i]
                        )
                    self.assertAlmostEqual(result, expected[i], places=2)