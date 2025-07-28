class MarsRover:
    def __init__(self, position, direction):
        self.position = (position[0], position[1])
        self.direction = direction

    def execute(self, command):
        for move in command:
            if move == 'f':
                self.position = (self.position[0]+1, self.position[1])
            elif move == 'b':
                self.position = (self.position[0]-1, self.position[1])
            elif move == 'l':
                self.position = (self.position[0], self.position[1]-1)
            elif move == 'r':
                self.position = (self.position[0], self.position[1]+1)