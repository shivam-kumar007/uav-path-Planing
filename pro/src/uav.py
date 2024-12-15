class UAV:
    def __init__(self, start_position):
        self.position = start_position

    def move(self, new_position):
        """Move UAV to the new position."""
        self.position = new_position
