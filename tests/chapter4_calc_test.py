import unittest

from physics_TUI.chapters.chapter4 import Chapter4


class TestTimeoOfFlight(unittest.TestCase):
    """
    Calculates the timeofFlight calculation method
    """

    def test_solving_for_t(self) -> None:
        """
        Tests the main use case  of calculating for t (time of flight)
        """

        # Initial conditions
        v_0 = [0.0, 25.0, 100.0]
        theta = [10.0, 25.7, 75.8]

        expected = [0.0, 2.208, 19.744]

        results = []

        for i in range(len(expected)):
            result = Chapter4.Calculate.timeOfFlight(
                v_0=v_0[i],
                theta=theta[i],
            )
            results.append(result)

        for i in range(len(expected)):
            self.assertAlmostEqual(results[i], expected[i], places=2)

    def test_solving_for_v_0(self) -> None:
        """
        Tests the functions ability to solve for v_0 (initial velocity)
        """

        # initial conditions
        t = [0.0, 5.0, 20.0]
        theta = [10.0, 25.8, 45.0]

        expected = [0.0, 56.41, 138.88]

        results = []

        for i in range(len(expected)):
            result = Chapter4.Calculate.timeOfFlight(t=t[i], theta=theta[i])
            results.append(result)
        print(results)
        for i in range(len(expected)):
            self.assertAlmostEqual(results[i], expected[i], places=2)

    def test_solving_for_theta(self) -> None:
        """
        Tests the functions ability to solve for theta (launch angle)
        """

        # initial conditions
        v_0 = [0.0, 10.0, 45.0]
        t = [0.0, -10.0, 10.0]

        #TO DO: DOUBLE CHECK WHY SOLUTIONS TO THE ANGLE ARE COMPLEX AND SOLVE FOR EXPECTED VALUES TO COMPLETE TESTING

        expected = [
            ValueError("Cannot solve for theta with this equation. Yields complex numbers. \n Please input a value for theta."),
            ValueError("Cannot solve for theta with this equation. Yields complex numbers. \n Please input a value for theta."),
            ValueError("Cannot solve for theta with this equation. Yields complex numbers. \n Please input a value for theta.")]


        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter4.Calculate.timeOfFlight(
                        v_0=v_0[i],
                        t=t[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter4.Calculate.timeOfFlight(
                        v_0=v_0[i],
                        t=t[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)

class TestTrajectory(unittest.TestCase):
    """
    Tests the trajectory calculation method
    """

    def test_solving_for_theta(self) -> None:
        """
        Tests solving for theta
        """

        v_0 = [0.0, 50.0, -10.0]
        x = [0.0, 10, 50]
        y = [0.0, 10, 25]

        expected = [
            ValueError(
                "Cannot solve for theta with this equation. Please input a value for theta."
            ),
            ValueError(
                "Cannot solve for theta with this equation. Please input a value for theta."
            ),
            ValueError(
                "Cannot solve for theta with this equation. Please input a value for theta."
            ),
        ]

        for i in range(len(expected)):
            with self.assertRaises(ValueError) as context:
                Chapter4.Calculate.trajectory(
                    v_0=v_0[i],
                    x=x[i],
                    y=y[i]
                )
            self.assertEqual(str(context.exception), str(expected[i]))

    def test_solving_for_v_0(self) -> None:
        """
        Test solves for v_0 (initial velocity)
        """

        # Initial conditions
        theta = [0.0, 45.0, 67.0]
        x = [0.0, -10.0, 100]
        y = [0.0, 20, 50]

        expected = [
            ValueError("Division by zero is undefined"),
            ValueError("Discriminant cannot be negative. Outputs imaginary number."),
            88.30
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter4.Calculate.trajectory(
                        theta=theta[i],
                        x=x[i],
                        y=y[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter4.Calculate.trajectory(
                        theta=theta[i],
                        x=x[i],
                        y=y[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_x(self) -> None:
        """
        Function tests solving for horizontal position (x)
        """

        # Initial conditions
        theta = [0.0, 45.0, 67.0]
        v_0 = [0.0, 25.0, 80.0]
        y = [0.0, 0.0, 10.0]

        expected = [
            ValueError("Division by zero is undefined"),
            63.64,
            ValueError("Can only solve for x when y is zero.")
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter4.Calculate.trajectory(
                        theta=theta[i],
                        v_0=v_0[i],
                        y=y[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter4.Calculate.trajectory(
                        theta=theta[i],
                        v_0=v_0[i],
                        y=y[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=1)

        def test_solving_for_y(self) -> None:
            """
            Function tests solving for vertical position (y)
            """
            # Initial conditions
            theta = [0.0, 45.0, 67.0]
            v_0 = [0.0, 25.0, 80.0]
            x = [0.0, 15.0, 30.0]

            expected = [
                ValueError("Division by zero is undefined"),
                18.53,
                75.20
            ]

            for i in range(len(expected)):
                if isinstance(expected[i], ValueError):
                    with self.assertRaises(ValueError) as context:
                        Chapter4.Calculate.trajectory(
                            theta=theta[i],
                            v_0=v_0[i],
                            x=x[i]
                        )
                    self.assertEqual(str(context.exception), str(expected[i]))
                else:
                    result = Chapter4.Calculate.trajectory(
                            theta=theta[i],
                            v_0=v_0[i],
                            x=x[i]
                        )
                    self.assertAlmostEqual(result, expected[i], places=1)

class TestRange(unittest.TestCase):
    """
    Tests for the range function
    """
    
    def test_solving_for_R(self) -> None:

        # Initial conditions
        v_0 = [0.0, 10.0, 40.0]
        theta = [10.0, 25.0, 45.0]

        expected = [0.0, 7.80, 162.93]

        for i in range(len(expected)):
            result = Chapter4.Calculate.projectileRange(
                v_0=v_0[i],
                theta=theta[i]
            )
            self.assertAlmostEqual(result, expected[i], places=2)