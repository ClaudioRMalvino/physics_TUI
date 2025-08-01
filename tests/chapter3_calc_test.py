import unittest

from typing import List, Any
from physics_TUI.chapters.chapter3 import Chapter3


class Testposition_from_vel_and_accel(unittest.TestCase):
    """
    Tests the position_from_vel_and_accel calculation method
    """

    def test_solving_for_x_f(self) -> None:
        """
        Tests the main use case for calculating x(t)
        """
        x_0: List[float] = [0.0, 5.0, 10.0]
        v_0: List[float] = [0.0, 25.0, 50.0]
        t: List[float] = [0.0, 15.0, 20.0]
        accel: List[float] = [0.0, 5.0, 10.0]

        expected: List[float] = [0, 942.5, 3010]

        results = []

        for i in range(len(expected)):
            result = Chapter3.Calculate.position_from_vel_and_accel(
                x_0=x_0[i], v_0=v_0[i], t=t[i], accel=accel[i]
            )
            results.append(result)

        for i in range(len(expected)):
            self.assertAlmostEqual(results[i], expected[i], places=4)

    def test_solving_for_t(self) -> None:
        """
        Tests for the more complicated task of solving for time.
        """
        x_0: List[float] = [0.0, 5.0, 10.0]
        v_0: List[float] = [0.0, 25.0, 50.0]
        accel: List[float] = [0.0, 5.0, 10.0]
        x_f: List[float] = [0.0, 942.5, 3010.0]

        expected: List[Any] = [ValueError("v₀ and a cannot both be equal to zero"), 15.0, 20.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                # Check for exception
                with self.assertRaises(ValueError) as context:
                    Chapter3.Calculate.position_from_vel_and_accel(
                        x_0=x_0[i], v_0=v_0[i], accel=accel[i], x_f=x_f[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                # Check for numerical result
                result = Chapter3.Calculate.position_from_vel_and_accel(
                    x_0=x_0[i], v_0=v_0[i], accel=accel[i], x_f=x_f[i]
                )
                self.assertAlmostEqual(result, expected[i], places=7)

    def test_solving_for_accel(self) -> None:
        """
        Tests solving for acceleration (accel)
        """

        # Initial conditions

        x_0: List[float] = [0.0, 5.0, 10.0]
        v_0: List[float] = [0.0, 25.0, 50.0]
        t: List[float] = [0.0, 15.0, 20.0]
        x_f: List[float] = [0, 942.5, 3010]

        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
            5.0, 
            10.0]

        for i in range(len(expected)):
                if isinstance(expected[i], ValueError):
                    with self.assertRaises(ValueError) as context:
                        Chapter3.Calculate.position_from_vel_and_accel(
                            x_0=x_0[i],
                            v_0=v_0[i],
                            t=t[i],
                            x_f=x_f[i]
                        )
                    self.assertEqual(str(context.exception), str(expected[i]))
                else:
                    result = Chapter3.Calculate.position_from_vel_and_accel(
                            x_0=x_0[i],
                            v_0=v_0[i],
                            t=t[i],
                            x_f=x_f[i]
                        )
                    self.assertAlmostEqual(result, expected[i], places=2)
    
    def test_solving_for_x_0(self) -> None:
        """
        Function tests solving for initial position (x_0)
        """

        # Initial conditions

        v_0: List[float] = [0.0, 25.0, 50.0]
        t: List[float] = [0.0, 15.0, 20.0]
        accel: List[float] = [0.0, 5.0, 10.0]
        x_f: List[float] = [0, 942.5, 3010]

        expected: List[float] = [0.0, 5.0, 10.0]

        for i in range(len(expected)):
                if isinstance(expected[i], ValueError):
                    with self.assertRaises(ValueError) as context:
                        Chapter3.Calculate.position_from_vel_and_accel(
                            accel=accel[i],
                            v_0=v_0[i],
                            t=t[i],
                            x_f=x_f[i]
                        )
                    self.assertEqual(str(context.exception), str(expected[i]))
                else:
                    result = Chapter3.Calculate.position_from_vel_and_accel(
                            accel=accel[i],
                            v_0=v_0[i],
                            t=t[i],
                            x_f=x_f[i]
                        )
                    self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_v_0(self) -> None:
        """
        Function tests solving for intiial velocity (v_0)
        """

        # Initial conditions

        x_0: List[float] = [0.0, 5.0, 10.0]
        t: List[float] = [0.0, 15.0, 20.0]
        accel: List[float] = [0.0, 5.0, 10.0]
        x_f: List[float] = [0, 942.5, 3010]

        expected: List[Any] = [
            ValueError("Division by zero is undefined"), 
            25.0, 
            50.0]

        for i in range(len(expected)):
                if isinstance(expected[i], ValueError):
                    with self.assertRaises(ValueError) as context:
                        Chapter3.Calculate.position_from_vel_and_accel(
                            accel=accel[i],
                            x_0=x_0[i],
                            t=t[i],
                            x_f=x_f[i]
                        )
                    self.assertEqual(str(context.exception), str(expected[i]))
                else:
                    result = Chapter3.Calculate.position_from_vel_and_accel(
                            accel=accel[i],
                            x_0=x_0[i],
                            t=t[i],
                            x_f=x_f[i]
                        )
                    self.assertAlmostEqual(result, expected[i], places=2)



class Testvelocity_from_distance(unittest.TestCase):
    """
    Tests the velocity_from_distance calculation method
    """

    def test_solving_for_v_f(self) -> None:
        """
        Function tests solving for final velocity (V_f)
        """

        x_0: List[float] = [0.0, 5.0, 10.0]
        v_0: List[float] = [0.0, 25.0, 5.0]
        x_f: List[float] = [0.0, 15.0, 20.0]
        accel: List[float] = [0.0, 5.0, -10.0]

        expected: List[Any] = [0, 26.93, ValueError("The discriminant cannot be negative")]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter3.Calculate.velocity_from_distance(
                        x_0=x_0[i], v_0=v_0[i], x_f=x_f[i], accel=accel[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter3.Calculate.velocity_from_distance(
                    x_0=x_0[i], v_0=v_0[i], x_f=x_f[i], accel=accel[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_x_0(self) -> None:
        """
        Tests for the more complicated task of solving for intial position.
        """
        x_f: List[float] = [0.0, 5.0, 10.0]
        v_0: List[float] = [0.0, 25.0, 50.0]
        accel: List[float] = [0.0, 5.0, 10.0]
        v_f: List[float] = [0.0, 60.0, 120.0]

        expected: List[Any] = [
            ValueError("acceleration cannot be equal to zero"),
            -292.5,
            -585,
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                # Check for exception
                with self.assertRaises(ValueError) as context:
                    Chapter3.Calculate.velocity_from_distance(
                        x_f=x_f[i], v_0=v_0[i], accel=accel[i], v_f=v_f[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                # Check for numerical result
                result = Chapter3.Calculate.velocity_from_distance(
                    x_f=x_f[i], v_0=v_0[i], accel=accel[i], v_f=v_f[i]
                )
                self.assertAlmostEqual(result, expected[i], places=7)

    def test_solving_for_v_0(self) -> None:
        """
        Tests for the more complicated task of solving for initial velocity.
        """
        x_0: List[float] = [0.0, 5.0, 10.0]
        x_f: List[float] = [0.0, 25.0, 50.0]
        accel: List[float] = [0.0, 5.0, 20.0]
        v_f: List[float] = [0.0, 60, 10.0]

        expected: List[Any] = [0, 58.31, ValueError("The discriminant cannot be negative")]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter3.Calculate.velocity_from_distance(
                        x_0=x_0[i], x_f=x_f[i], accel=accel[i], v_f=v_f[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter3.Calculate.velocity_from_distance(
                    x_0=x_0[i], x_f=x_f[i], accel=accel[i], v_f=v_f[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)


class Testheight_of_free_fall(unittest.TestCase):

    def test_solving_for_y_f(self) -> None:
        """
        Tests the main use case for calculating y_f (final height)
        """
        y_0: List[float] = [0.0, 5.0, 10.0]
        v_0: List[float] = [0.0, 25.0, 50.0]
        t: List[float] = [0.0, 15.0, 20.0]

        expected: List[Any] = [0, -724.75, -954]

        results = []

        for i in range(len(expected)):
            result = Chapter3.Calculate.height_of_free_fall(y_0=y_0[i], v_0=v_0[i], t=t[i])
            results.append(result)

        for i in range(len(expected)):
            self.assertAlmostEqual(results[i], expected[i], places=4)

    def test_solving_for_t(self) -> None:
        """
        Tests for the more complicated task of solving for time.
        """
        y_0: List[float] = [0.0, 5.0, 10.0]
        v_0: List[float] = [0.0, 25.0, 50.0]
        y_f: List[float] = [0.0, 30.0, 0.0]

        expected: List[Any] = [0, 1.367, 10.3795]

        results = []

        for i in range(len(expected)):
            result = Chapter3.Calculate.height_of_free_fall(
                y_0=y_0[i], v_0=v_0[i], y_f=y_f[i]
            )
            results.append(result)

        for i in range(len(expected)):
            self.assertAlmostEqual(results[i], expected[i], places=7)


class Testvel_free_fall_from_height(unittest.TestCase):
    """
    Tests the vel_free_fall_from_height calculation method
    """

    def test_solving_for_v_f(self) -> None:
        """
        Tests the main use case for calculating final velocity
        """
        y_0: List[float] = [0.0, 5.0, 10.0]
        v_0: List[float] = [0.0, 25.0, 5.0]
        y_f: List[float] = [0.0, 15.0, 20.0]

        expected: List[Any] = [0, 20.70266, ValueError("The discriminant cannot be negative")]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter3.Calculate.vel_free_fall_from_height(
                        y_0=y_0[i],
                        v_0=v_0[i],
                        y_f=y_f[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter3.Calculate.vel_free_fall_from_height(
                    y_0=y_0[i],
                    v_0=v_0[i],
                    y_f=y_f[i],
                )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_y_0(self) -> None:
        """
        Tests for the more complicated task of solving for intial position.
        """
        y_f: List[float] = [0.0, 5.0, 10.0]
        v_0: List[float] = [0.0, 25.0, 50.0]
        v_f: List[float] = [0.0, 60.0, 120.0]

        expected: List[Any] = [0.0, 156.476, 615.906]

        results = []

        for i in range(len(expected)):
            result = Chapter3.Calculate.vel_free_fall_from_height(
                y_f=y_f[i], v_0=v_0[i], v_f=v_f[i]
            )
            results.append(result)

        for i in range(len(expected)):
            self.assertAlmostEqual(results[i], expected[i], places=2)

    def test_solving_for_v_0(self) -> None:
        """
        Tests for the more complicated task of solving for initial velocity.
        """
        y_0: List[float] = [0.0, 5.0, 60.0]
        y_f: List[float] = [0.0, 25.0, 50.0]
        v_f: List[float] = [0.0, 60.0, 5.0]

        expected: List[Any] = [0, 63.188, ValueError("The discriminant cannot be negative")]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter3.Calculate.vel_free_fall_from_height(
                        y_0=y_0[i], y_f=y_f[i], v_f=v_f[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter3.Calculate.vel_free_fall_from_height(
                    y_0=y_0[i], y_f=y_f[i], v_f=v_f[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)
