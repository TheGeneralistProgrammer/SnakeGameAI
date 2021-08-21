from snakeai.game.constants import Actions, Coords
import random

class Snake():
    """A class which stores the info about the game
    
    Attributes
    ------------
    dim : int
        the side of the board
    MAX_SCORE : int
        The maximum score achievable
    MAX_GROWING : int
        The maximum length of the snake
    score : int
        The current score
    direction : Actions
        The current direction
    isGameOver : Bool
        whether the snake has reached game over
    """
    def __init__(self, dim):
        """
        Parameters
        -------------
        dim : int
            The side of the board
        """
        self.dim = dim
        self.MAX_SCORE = dim*dim
        self.MAX_GROWING = int(0.9*dim*dim)
        self.reset()
    
    def reset(self):
        """Prepare to start the game"""
        self._snake = [Coords(0,0)]
        self.setApple()
        self.direction = Actions.DOWN
        self.score = 0
        self.isGameOver = False
    
    def setApple(self):
        """Choose new valid position for the apple"""
        positions = list()
        for x in range(self.dim):
            for y in range(self.dim):
                c = Coords(x, y)
                if not c in self._snake:
                    positions.append(c)
        self.apple = random.choice(positions)
    
    def changeDirection(self, direction):
        """Change the direction of the snake
        
        Parameters
        -------------
        direction : Actions
            the new direction of the snake
        """
        self.direction = direction

    @property
    def snake(self):
        """snake : list(Coords) The body of the nake (head is last)"""
        return self._snake.copy()
    
    def step(self):
        """Update model by moving snake of one step"""
        nextHead = self._snake[-1] + self.direction.value
        if nextHead in self._snake: # Check collision with itself
            self.isGameOver = True
            return
        if not (0 <= nextHead.x < self.dim and 0 <= nextHead.y < self.dim): # Check collision with border
            self.isGameOver = True
            return
        self._snake.append(nextHead)
        if nextHead == self.apple:
            self.score += 1
            self.setApple()
            self.isGameOver = self.score > self.MAX_SCORE
            if self.score <= self.MAX_GROWING:
                return
        self._snake.pop(0)


    