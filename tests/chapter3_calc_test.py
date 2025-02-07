import unittest

from physics_TUI.chapters.chapter3 import Chapter3

class TestPositionFromVelAndAcc(unittest.TestCase):

    def test_solving_for_x_f(self) -> None:
        """
        Tests the main use case for calculating x(t)
        """
        x_0 = [0.0, 5.0, 10]
        v_0 = [0.0, 25, 50]
        t = [0.0, 15.0, 20]
        accel = [0.0, 5.0, 10]

        expected = [0,942.5, 3010]

        results = []

        for i in range(len(expected)):
            result = Chapter3.Calculate.positionFromVelAndAcc(
                x_0=x_0[i],
                v_0=v_0[i],
                t=t[i],
                accel=accel[i]
            )
            results.append(result)
        print(results)
        for i in range(len(expected)):
            self.assertAlmostEqual(results[i], expected[i], places=7)
    
    def test_solving_for_t(self) -> None:

        """
        Tests for the more complicated task of solving for t.
        """
        x_0 = [0.0, 5.0, 10]
        v_0 = [0.0, 25, 50]
        accel = [0.0, 5.0, 10]
        x_f = [0.0, 942.5, 3010]


        expected = [ValueError("v₀ and a cannot both be equal to zero"), 15.0, 20.0]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                # Check for exception
                with self.assertRaises(ValueError) as context:
                    Chapter3.Calculate.positionFromVelAndAcc(
                        x_0=x_0[i],
                        v_0=v_0[i],
                        accel=accel[i],
                        x_f=x_f[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                # Check for numerical result
                result = Chapter3.Calculate.positionFromVelAndAcc(
                    x_0=x_0[i],
                    v_0=v_0[i],
                    accel=accel[i],
                    x_f=x_f[i]
                )
                self.assertAlmostEqual(result, expected[i], places=7)