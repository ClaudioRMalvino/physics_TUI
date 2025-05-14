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
            result = Chapter4.Calculate.timeOfFlight(
                t=t[i],
                theta=theta[i]
            )
            results.append(result)
        print(results)
        for i in range(len(expected)):
            self.assertAlmostEqual(results[i], expected[i], places=2)
    
    # TO DO: Write test case for x variable
    
    #def test_solving_for_x(self) -> None:
        """
        Tests the functions ability to solve for x (position)
        """

        # initial conditions

        