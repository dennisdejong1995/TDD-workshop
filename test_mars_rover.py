import unittest
from mars_rover import MarsRover

class TestMarsRover(unittest.TestCase):
    def setUp(self):
        self.rover = MarsRover((0,0), 'N')

    def test_initial_position(self):
        self.assertEqual(self.rover.position, (0, 0))
        self.assertEqual(self.rover.direction, 'N')

    def test_receives_command(self):
        command = 'fblr'
        self.rover.execute(command)

    def test_goes_forward(self):
        command = 'f'
        self.rover.execute(command)
        self.assertEqual(self.rover.position, (1, 0))

    def test_goes_backward(self):
        command = 'b'
        self.rover.execute(command)
        self.assertEqual(self.rover.position, (-1, 0))

    def test_goes_forward_then_backward(self):
        command = 'fbb'
        self.rover.execute(command)
        self.assertEqual(self.rover.position, (-1, 0))

    def test_goes_left(self):
        command = 'l'
        self.rover.execute(command)
        self.assertEqual(self.rover.position, (0, -1))

    def test_goes_right(self):
        command = 'r'
        self.rover.execute(command)
        self.assertEqual(self.rover.position, (0, 1))