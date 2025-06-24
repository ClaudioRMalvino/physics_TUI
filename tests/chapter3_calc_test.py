import unittest

from typing import List, Any
from physics_TUI.chapters.chapter3 import Chapter3


class TestPositionFromVelAndAcc(unittest.TestCase):
    """
    Tests the positionFromVelandAcc calculation method
    """

    def test_solving_for_x_f(self) -> None:
        """
        Tests the main use case for calculating x(t)
        """
        x_0: List[float] = [0.0, 5.0, 10.0]
        v_0: List[float] = [0.0, 25.0, 50.0]
        t: List[float] = [0.0, 15.0, 20.0]
        accel: List[float] = [0.0, 5.0, 10.0]

        expected: List[Any] = [0, 942.5, 3010]

        results = []

        for i in range(len(expected)):
            result = Chapter3.Calculate.positionFromVelAndAcc(
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
                    Chapter3.Calculate.positionFromVelAndAcc(
                        x_0=x_0[i], v_0=v_0[i], accel=accel[i], x_f=x_f[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                # Check for numerical result
                result = Chapter3.Calculate.positionFromVelAndAcc(
                    x_0=x_0[i], v_0=v_0[i], accel=accel[i], x_f=x_f[i]
                )
                self.assertAlmostEqual(result, expected[i], places=7)


class TestVelocityFromDistance(unittest.TestCase):
    """
    Tests the velocityFromDistance calculation method
    """

    def test_solving_for_v_f(self) -> None:
        """ositionFromVelAndAcc
        Tests the main use case for calculating final velocity
        """
        x_0: List[float] = [0.0, 5.0, 10.0]
        v_0: List[float] = [0.0, 25.0, 5.0]
        x_f: List[float] = [0.0, 15.0, 20.0]
        accel: List[float] = [0.0, 5.0, -10.0]

        expected: List[Any] = [0, 26.93, ValueError("The discriminant cannot be negative")]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter3.Calculate.velocityFromDistance(
                        x_0=x_0[i], v_0=v_0[i], x_f=x_f[i], accel=accel[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter3.Calculate.velocityFromDistance(
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
                    Chapter3.Calculate.velocityFromDistance(
                        x_f=x_f[i], v_0=v_0[i], accel=accel[i], v_f=v_f[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                # Check for numerical result
                result = Chapter3.Calculate.velocityFromDistance(
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
                    Chapter3.Calculate.velocityFromDistance(
                        x_0=x_0[i], x_f=x_f[i], accel=accel[i], v_f=v_f[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter3.Calculate.velocityFromDistance(
                    x_0=x_0[i], x_f=x_f[i], accel=accel[i], v_f=v_f[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)


class TestHeightofFreeFall(unittest.TestCase):

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
            result = Chapter3.Calculate.heightOfFreeFall(y_0=y_0[i], v_0=v_0[i], t=t[i])
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
            result = Chapter3.Calculate.heightOfFreeFall(
                y_0=y_0[i], v_0=v_0[i], y_f=y_f[i]
            )
            results.append(result)

        for i in range(len(expected)):
            self.assertAlmostEqual(results[i], expected[i], places=7)


class TestVelFreeFallFromHeight(unittest.TestCase):
    """
    Tests the velFreeFallFromHeight calculation method
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
                    Chapter3.Calculate.velFreeFallFromHeight(
                        y_0=y_0[i],
                        v_0=v_0[i],
                        y_f=y_f[i],
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter3.Calculate.velFreeFallFromHeight(
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
            result = Chapter3.Calculate.velFreeFallFromHeight(
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
                    Chapter3.Calculate.velFreeFallFromHeight(
                        y_0=y_0[i], y_f=y_f[i], v_f=v_f[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter3.Calculate.velFreeFallFromHeight(
                    y_0=y_0[i], y_f=y_f[i], v_f=v_f[i]
                )
                self.assertAlmostEqual(result, expected[i], places=2)
