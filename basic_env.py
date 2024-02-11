from env_objects import *
from arenas import *
from visualize import *

class GridWorld:
    def __init__(self):
        """Initialize the environment.
        
        Set up any necessary parameters like state and action spaces, initial state, etc.
        """
        self.renders = []
        self.arena = Arena()
        self.reset()

    def reset(self):
        """Reset the environment to start a new episode.
        
        Returns:
            The initial state of the episode.
        """
        self.state = None
        return self.state

    def step(self, action):
        """Take an action in the environment.
        
        Args:
            action: The action to be taken.
        
        Returns:
            next_state: The state of the environment after taking the action.
            reward: The reward received after taking the action.
            done: A boolean indicating if the episode has ended.
            info: A dictionary with additional information about the step.
        """
        
        invalid_movement = False
        reward = 0
        done = False
        info = {}

        agent = self.arena.agent
        a_x, a_y = agent.x, agent.y
        if (action == Action.UP):
            if self.arena.is_valid_position(a_x, a_y + 1):
                self.arena.agent.y += 1
            else: 
                invalid_movement = True
        if (action == Action.DOWN):
            if self.arena.is_valid_position(a_x, a_y - 1):
                self.arena.agent.y -= 1
            else: 
                invalid_movement = True
        if (action == Action.RIGHT):
            if self.arena.is_valid_position(a_x + 1, a_y):
                self.arena.agent.x += 1
            else:
                invalid_movement = True
        if (action == Action.LEFT):
            if self.arena.is_valid_position(a_x - 1, a_y):
                self.arena.agent.x -= 1
            else: 
                invalid_movement = True


        return self.state, reward, done, info
        

    def render(self, mode='txt'):
        """Render the environment.
        
        The rendering can be to the screen for human consumption, or it might generate data for analysis.
        
        Args:
            mode (str): The mode of rendering (e.g., 'txt' for output dump)
        """
        self.renders.append(self.arena.visualize())

    def close(self):
        """Perform any necessary cleanup.
        
        This method is called when the environment should be closed.
        """
        pass

    def visualize(self):
        gui = GameGUI(self.renders)

