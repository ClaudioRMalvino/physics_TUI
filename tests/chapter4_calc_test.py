import unittest

from typing import List, Any
from physics_TUI.chapters.chapter4 import Chapter4


class TestTimeoOfFlight(unittest.TestCase):
    """
    Calculates the time_of_flight calculation method
    """

    def test_solving_for_t(self) -> None:
        """
        Tests the main use case of calculating for t (time of flight)
        """

        # Initial conditions
        v_0: List[float] = [0.0, 25.0, 100.0]
        theta: List[float] = [10.0, 25.7, 75.8]

        expected: List[Any] = [0.0, 2.208, 19.744]

        results = []

        for i in range(len(expected)):
            result = Chapter4.Calculate.time_of_flight(
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
        t: List[float] = [0.0, 5.0, 20.0]
        theta: List[float] = [10.0, 25.8, 45.0]

        expected: List[Any] = [0.0, 56.41, 138.88]

        results = []

        for i in range(len(expected)):
            result = Chapter4.Calculate.time_of_flight(t=t[i], theta=theta[i])
            results.append(result)
        print(results)
        for i in range(len(expected)):
            self.assertAlmostEqual(results[i], expected[i], places=2)

    def test_solving_for_theta(self) -> None:
        """
        Tests the functions ability to solve for theta (launch angle)
        """

        # initial conditions
        v_0: List[float] = [0.0, 10.0, 56.41]
        t: List[float] = [0.0, -10.0, 20.0]

        #TO DO: DOUBLE CHECK WHY SOLUTIONS TO THE ANGLE ARE COMPLEX AND SOLVE FOR EXPECTED VALUES TO COMPLETE TESTING

        expected: List[ValueError] = [
            ValueError("Cannot solve for theta with this equation. Yields complex numbers. \n Please input a value for theta."),
            ValueError("Cannot solve for theta with this equation. Yields complex numbers. \n Please input a value for theta."),
            ValueError("Cannot solve for theta with this equation. Yields complex numbers. \n Please input a value for theta.")]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter4.Calculate.time_of_flight(
                        v_0=v_0[i],
                        t=t[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter4.Calculate.time_of_flight(
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

        v_0: List[float] = [0.0, 50.0, -10.0]
        x: List[float] = [0.0, 10, 50]
        y: List[float] = [0.0, 10, 25]

        expected: List[Any] = [
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
        theta: List[float] = [0.0, 45.0, 30.0]
        x: List[float] = [0.0, -10.0, 50]
        y: List[float] = [0.0, 20, 30]

        expected: List[Any] = [
            ValueError("Division by zero is undefined"),
            ValueError("Radicand cannot be negative. Outputs imaginary number."),
            4.626]

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
        theta: List[float] = [0.0, 45.0, 67.0]
        v_0: List[float] = [0.0, 25.0, 80.0]
        y: List[float] = [0.0, 0.0, 10.0]

        expected: List[ValueError] = [
            ValueError("Cannot solve for x with this equation. Consider calculating the range."),
            ValueError("Cannot solve for x with this equation. Consider calculating the range."),
            ValueError("Cannot solve for x with this equation. Consider calculating the range.")
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
        theta: List[float] = [0.0, 45.0, 67.0]
        v_0: List[float] = [0.0, 25.0, 80.0]
        x: List[float] = [0.0, 15.0, 30.0]

        expected: List[Any] = [
            ValueError("Division by zero is undefined"),
            11.46,
            66.15
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
        """
        Function tests solving for the projectile range (R)
        """

        # Initial conditions
        v_0: List[float] = [0.0, 10.0, 40.0]
        theta: List[float] = [10.0, 25.0, 45.0]

        expected: List[Any] = [0.0, 7.80, 162.93]

        for i in range(len(expected)):
            result = Chapter4.Calculate.projectile_range(
                v_0=v_0[i],
                theta=theta[i]
            )
            self.assertAlmostEqual(result, expected[i], places=2)
    
    def test_solving_for_v_0(self) -> None:
        """
        Function tests solving for initial velocity (v_0)
        """

        # Initial conditions
        R: List[float] = [0.0, 40.0, 80.0]
        theta: List[float] = [0.0, 45.0, 135.0 ]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            19.81,
            ValueError("Radicand cannot be negative. Outputs imaginary number.")
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter4.Calculate.projectile_range(
                        theta=theta[i],
                        r_total=R[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter4.Calculate.projectile_range(
                        theta=theta[i],
                        r_total=R[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=1)

    def test_solving_for_theta(self) -> None:
        """
        Function tests solving for initial velocity (v_0)
        """

        # Initial conditions
        R: List[float] = [0.0, 120, 30]
        v_0: List[float] = [0.0, 20, 20]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            ValueError("No real solution exists. Range too large for given velocity."),


        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter4.Calculate.projectile_range(
                        v_0=v_0[i],
                        r_total=R[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter4.Calculate.projectile_range(
                        v_0=v_0[i],
                        r_total=R[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=1)

class Testcentripetal_accel(unittest.TestCase):
    """
    Conducts test for the centripetal_accel function
    
    """
    
    def test_solving_for_accel(self) -> None:
        """
        Function tests solving for centripetal acceleration
        """
        
        # Initial conditions
        velocity: List[float] = [10.0, 0.0, 50, 10.0]
        radius: List[float] = [0.0, 10.0, 2, -1]
        
        expected: List[Any] = [
            ValueError("Radius cannot be less than or equal to zero."),
            0.0,
            1250,
            ValueError("Radius cannot be less than or equal to zero.")
        ]
        
        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter4.Calculate.centripetal_accel(
                        velocity=velocity[i],
                        radius=radius[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter4.Calculate.centripetal_accel(
                        velocity=velocity[i],
                        radius=radius[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=1)
    
    def test_solving_for_velocity(self) -> None:
        """
        Function tests solving for velocity
        """

        # Initial conditions
        accel: List[float] = [0.0, -10.0, 10.0, 10.0]
        radius: List[float] = [1.0, 1.0, -1.0, 20.0]
        
        expected: List[Any] = [
            0.0,
            ValueError("Radicand cannot be negative. Yields an imaginary number."),
            ValueError("Radius cannot be less than or equal to zero."),
            14.142
        ]
        
        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter4.Calculate.centripetal_accel(
                        accel=accel[i],
                        radius=radius[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter4.Calculate.centripetal_accel(
                        accel=accel[i],
                        radius=radius[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)
        
        