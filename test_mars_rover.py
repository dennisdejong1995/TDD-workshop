import unittest
from mars_rover import MarsRover

class TestMarsRover(unittest.TestCase):
    def setUp(self):
        self.rover = MarsRover()

    def test_initial_position(self):
        self.assertEqual(self.rover.position, (0, 0))
        self.assertEqual(self.rover.direction, 'N')
