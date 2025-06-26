import unittest

from typing import List, Any
from physics_TUI.chapters.chapter6 import Chapter6

class TestCentripetalForceTangVel(unittest.TestCase):
    """
    Tests the main use cases of calculations for the centripetal acceleration
    equation utilziing the tangential velocity.
    """

    def test_solving_for_centripetal_F(self) -> None:
        """
        Function tests solving for the mass (mass)
        """

        # Initial conditions

        mass: List[float] = [-10.0, 10.0, 25.0, 25.0]
        radius: List[float] = [2.0, -2.0, 0.0, 2.0]
        velocity: List[float] = [15.0, 15.0, 15.0, 15.0]

        expected: List[Any] = [

            ValueError("We are operating with massive objects. \
                    Mass must be greater than zero."),
            ValueError("Radius cannot be a negative value."),
            ValueError("Division by zero is undefined."),
            2812.5
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter6.Calculate.centripetalForceTangVel(
                        mass=mass[i],
                        radius=radius[i],
                        velocity=velocity[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter6.Calculate.centripetalForceTangVel(
                        mass=mass[i],
                        radius=radius[i],
                        velocity=velocity[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)  
    
    def test_solving_for_mass(self) -> None:
        """
        Function tests solving for the centripetal force (centripetal_F)
        """

        # Initial conditions

        centripetal_F: List[float] = [-10.0, 10.0, 200.0, 200.0]
        radius: List[float] = [2.0, -2.0, 3.0, 3.0]
        velocity: List[float] = [15.0, 15.0, 0.0, 25.0]

        expected: List[Any] = [

            ValueError("We are operating with massive objects. \
                    Mass must be greater than zero. Check your signs."),
            ValueError("Radius must be greater than zero."),
            ValueError("Divison by zero is undefined."),
            0.96
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter6.Calculate.centripetalForceTangVel(
                        centripetal_F=centripetal_F[i],
                        radius=radius[i],
                        velocity=velocity[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter6.Calculate.centripetalForceTangVel(
                        centripetal_F=centripetal_F[i],
                        radius=radius[i],
                        velocity=velocity[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2) 
    
    def test_solving_for_velocity(self) -> None:
        """
        Function tests solving for the velocity (velocity)
        """

        # Initial conditions

        centripetal_F: List[float] = [-10.0, 10.0, 200.0]
        radius: List[float] = [2.0, 2.0, 3.0]
        mass: List[float] = [10.0, 10.0, 25.0]

        expected: List[Any] = [
            ValueError("Negative radicand produces an imaginary number. \
                        Check your signs."),
            1.41,
            4.89
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter6.Calculate.centripetalForceTangVel(
                        centripetal_F=centripetal_F[i],
                        radius=radius[i],
                        mass=mass[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter6.Calculate.centripetalForceTangVel(
                        centripetal_F=centripetal_F[i],
                        radius=radius[i],
                        mass=mass[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=1)
    
    def test_solving_for_radius(self) -> None:
        """
        Function tests solving for the radius (radius)
        """

        # Initial conditions

        centripetal_F: List[float] = [0.0, -10.0, 200.0]
        velocity: List[float] = [25.0, 25.0, 25.0]
        mass: List[float] = [10.0, 10.0, 10.0]

        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
            ValueError("Radius cannot be negative. Check your signs."),
            31.25         
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter6.Calculate.centripetalForceTangVel(
                        centripetal_F=centripetal_F[i],
                        velocity=velocity[i],
                        mass=mass[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter6.Calculate.centripetalForceTangVel(
                        centripetal_F=centripetal_F[i],
                        velocity=velocity[i],
                        mass=mass[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)

class TestCentripetalForceAngVel(unittest.TestCase):
    """
    Tests the main use cases of calculations for the centripetal acceleration
    equation utilziing the angular velocity.
    """

    def test_solving_for_centripetal_F(self) -> None:
        """
        Function tests solving for centripetal force with angular velocity (centripetal_F)
        """

        # Initial conditions

        mass: List[float] = [-10.0, 10.0, 5.0, 5.0]
        angular_vel: List[float] = [25.0, 0.0, 40.0, 40.0]
        radius: List[float] = [5.0, 5.0, 0.0, 5.0]

        expected: List[Any] = [
            ValueError("We are operating with massive objects. \
                    Mass must be greater than zero."),
            0.0,
            ValueError("Radius must be greater than zero."),
            40000.0, 
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter6.Calculate.centripetalForceAngVel(
                        radius=radius[i],
                        angular_vel=angular_vel[i],
                        mass=mass[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter6.Calculate.centripetalForceAngVel(
                        radius=radius[i],
                        angular_vel=angular_vel[i],
                        mass=mass[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)
    
    def test_solving_for_mass(self) -> None:
        """
        Function tests solving for mass with angular velocity (mass)
        """

        # Initial conditions

        centripetal_F: List[float] = [-10.0, 10.0, 5.0, 500.0]
        angular_vel: List[float] = [25.0, 0.0, 40.0, 15.0]
        radius: List[float] = [5.0, 5.0, 0.0, 5.0]

        expected: List[Any] = [
             ValueError("Mass cannot be negative. Check your signs."),
             ValueError("Division by zero is undefined."),
             ValueError("Radius must be greater than zero."),
            0.44
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter6.Calculate.centripetalForceAngVel(
                        radius=radius[i],
                        angular_vel=angular_vel[i],
                        centripetal_F=centripetal_F[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter6.Calculate.centripetalForceAngVel(
                        radius=radius[i],
                        angular_vel=angular_vel[i],
                        centripetal_F=centripetal_F[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_angular_vel(self) -> None:
        """
        Function tests solving for mass with angular velocity (mass)
        """

        # Initial conditions

        centripetal_F: List[float] = [-10.0, 200.0, 100.0]
        mass: List[float] = [25.0, 5.0, 200.0]
        radius: List[float] = [5.0, 1.0, 2.0]

        expected: List[Any] = [
            ValueError("Negative radicand produces an imaginary number."),
            6.32,
            0.5
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter6.Calculate.centripetalForceAngVel(
                        radius=radius[i],
                        mass=mass[i],
                        centripetal_F=centripetal_F[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter6.Calculate.centripetalForceAngVel(
                        radius=radius[i],
                        mass=mass[i],
                        centripetal_F=centripetal_F[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)
    
    def test_solving_for_radius(self) -> None:
        """
        Function tests solving for radius with angular velocity (radius)
        """

        # Initial conditions

        centripetal_F: List[float] = [10.0, -200.0, 3000.0]
        mass: List[float] = [25.0, 5.0, 20.0]
        angular_vel: List[float] = [0.0, 25.0, 8.0]

        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
            ValueError("Radius cannot be negative. Check your signs."),
            2.34
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter6.Calculate.centripetalForceAngVel(
                        angular_vel=angular_vel[i],
                        mass=mass[i],
                        centripetal_F=centripetal_F[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter6.Calculate.centripetalForceAngVel(
                        angular_vel=angular_vel[i],
                        mass=mass[i],
                        centripetal_F=centripetal_F[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)
    
class TestIdealAngBankedCurve(unittest.TestCase):
    """
    Tests the main use cases of calculations for  ideal angle of a banked curve.
    """
    
    def test_solving_for_theta(self) -> None:
        """
        Function tests solving for theta (theta)
        """

        # Initial conditions
        velocity: List[float] = [40.0, 11.0, 30.0]
        radius: List[float] = [-20.0, 20.0, 10.0]

        expected: List[Any] = [
            ValueError("Radius cannot be less than or equal to zero."),
            31.64,
            83.77
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter6.Calculate.idealAngBankedCurve(
                        velocity=velocity[i],
                        radius=radius[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter6.Calculate.idealAngBankedCurve(
                        velocity=velocity[i],
                        radius=radius[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)

    def test_solving_for_velocity(self) -> None:
        """
        Function tests solving for velocity (velocity)
        """

        # Initial conditions
        theta: List[float] = [31.64, -83.77, 31.64, 90.0]
        radius: List[float] = [-20.0, 20.0, 20.0, 10.0]

        expected: List[Any] = [
            ValueError("Radius cannot be less than or equal to zero."), 
            ValueError("Reconsider if theta can physically be a negative value."),
            11.0,
            ValueError("Tangent function is undefined at 90.0 and 270.0 degrees.")
            ]
        
        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter6.Calculate.idealAngBankedCurve(
                        theta=theta[i],
                        radius=radius[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter6.Calculate.idealAngBankedCurve(
                        theta=theta[i],
                        radius=radius[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)
    
    def test_solving_for_radius(self) -> None:
        """
        Function tests solving for radius (theta)
        """

        # Initial conditions
        theta: List[float] = [31.64, -83.77, 31.64, 15.0]
        velocity: List[float] = [0.0, 11.0, 11.0, 22.0]

        expected: List[Any] = [
            ValueError("Division by zero is undefined."),
            ValueError("Reconsider if theta can physically be a negative value."),
            7.59,
            13.206
            ]
        
        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter6.Calculate.idealAngBankedCurve(
                        theta=theta[i],
                        velocity=velocity[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter6.Calculate.idealAngBankedCurve(
                        theta=theta[i],
                        velocity=velocity[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)

class TestDragForce(unittest.TestCase):
    """
    Tests the main use cases of calculations for  ideal angle of a banked curve. 
    """

    def test_solving_for_drag_F(self) -> None:
        """
        Function tests solving for the drag force (drag_F)
        """

        # Initial conditions
        drag_coeff: List[float] = [-0.5, 0.5, 0.5, 0.5]
        fluid_dens: List[float] = [1.225, 1.225, -1.225, 1.225]
        area: List[float] = [0.5, -0.5, 0.5, 0.5]
        velocity: List[Float] = [16.0, 16.0, 16.0, 16.0]

        expected: List[Any] = [
            ValueError("The drag coefficient cannot be negative."),
            ValueError("Area cannot be less than zero or equal to zero."),
            ValueError("Fluid density cannot be less than or equal to zero."),
            39.2
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter6.Calculate.dragForce(
                        drag_coeff=drag_coeff[i],
                        fluid_dens=fluid_dens[i],
                        area=area[i],
                        velocity=velocity[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter6.Calculate.dragForce(
                        drag_coeff=drag_coeff[i],
                        fluid_dens=fluid_dens[i],
                        area=area[i],
                        velocity=velocity[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)            
    
    def test_solving_for_drag_coeff(self) -> None:
        """
        Function tests solving for the drag force (drag_F)
        """

        # Initial conditions
        drag_F: List[float] = [39.2, 39.2, 39.2]
        fluid_dens: List[float] = [1.225, 1.225, 1.225]
        area: List[float] = [0.5, 0.5, 0.5]
        velocity: List[Float] = [0.0, -16.0, 16.0]

        expected: List[Any] = [
            ValueError("Divison by zero is undefined."),
            ValueError("Drag coefficient is a positive value. \
                        Check your signs."),
            0.5
        ]

        for i in range(len(expected)):
            if isinstance(expected[i], ValueError):
                with self.assertRaises(ValueError) as context:
                    Chapter6.Calculate.dragForce(
                        drag_F=drag_F[i],
                        fluid_dens=fluid_dens[i],
                        area=area[i],
                        velocity=velocity[i]
                    )
                self.assertEqual(str(context.exception), str(expected[i]))
            else:
                result = Chapter6.Calculate.dragForce(
                        drag_F=drag_F[i],
                        fluid_dens=fluid_dens[i],
                        area=area[i],
                        velocity=velocity[i]
                    )
                self.assertAlmostEqual(result, expected[i], places=2)            
