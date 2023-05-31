import random # TODO: Optimize memory for what functions called in random.
import sys


DEFAULT_STATE = '       | ###  -| # #  +| # ####|       '


class Action:

    def __init__(self, name, dx, dy):
        self.name = name
        self.dx = dx
        self.dy = dy


ACTIONS = [
    Action('UP', 0, -1),
    Action('RIGHT', +1, 0),
    Action('DOWN', 0, +1),
    Action('LEFT', -1, 0)
]


class State:

    def __init__(self, env, x, y):
        self.env = env
        self.x = x
        self.y = y

    def clone(self):
        return State(self.env, self.x, self.y)

    def is_legal(self, action):
        cell = self.env.get(self.x + action.dx, self.y + action.dy)
        return cell is not None and cell in ' +-'
    
    def legal_actions(self, actions):
        legal = []
        for action in actions:
            if self.is_legal(action):
                legal.append(action)
        return legal
    
    def reward(self):
        cell = self.env.get(self.x, self.y)
        if cell is None:
            return None
        elif cell == '+':
            return +10
        elif cell == '-':
            return -10
        else:
            return 0

    def at_end(self):
        return self.reward() != 0

    def execute(self, action):
        self.x += action.dx
        self.y += action.dy
        return self

    def __str__(self):
        tmp = self.env.get(self.x, self.y)
        self.env.put(self.x, self.y, 'A')
        s = ' ' + ('-' * self.env.x_size) + '\n'
        for y in range(self.env.y_size):
            s += '|' + ''.join(self.env.row(y)) + '|\n'
        s += ' ' + ('-' * self.env.x_size)
        self.env.put(self.x, self.y, tmp)
        return s


class Env:

    def __init__(self, string):
        self.grid = [list(line) for line in string.split('|')]
        self.x_size = len(self.grid[0])
        self.y_size = len(self.grid)

    def get(self, x, y):
        if x >= 0 and x < self.x_size and y >= 0 and y < self.y_size:
            return self.grid[y][x]
        else:
            return None

    def put(self, x, y, val):
        if x >= 0 and x < self.x_size and y >= 0 and y < self.y_size:
            self.grid[y][x] = val

    def row(self, y):
        return self.grid[y]

    def random_state(self):
        x = random.randrange(0, self.x_size)
        y = random.randrange(0, self.y_size)
        while self.get(x, y) != ' ':
            x = random.randrange(0, self.x_size)
            y = random.randrange(0, self.y_size)
        return State(self, x, y)


class QTable:


    def __init__(self, env:Env, actions:list):
        '''Create 3 dimensional list of size env.x_size, env.y_size, ACTIONS(4)'''
        self.env = env
        self.actions = actions
        self.qtable = [[[0 for k in range(len(actions))] for j in range(env.x_size)] for i in range(env.y_size)]

    def get_q(self, state:State, action:Action):
        '''Obtain the specific value of the q-table'''
        if action.name == "UP":
            action_index = 0
        elif action.name == "RIGHT":
            action_index = 1
        elif action.name == "DOWN":
            action_index = 2
        elif action.name == "LEFT":
            action_index = 3

        return self.qtable[state.y][state.x][action_index]

    def get_q_row(self, state:State):
        ''' return the row of q table corresponding to the given state'''
        # TODO: Check if this is what this function is asking me to do.
        return self.qtable[state.y][state.x]

    def set_q(self, state:State, action:Action, val:float):
        '''set the value of the q table for the given state, action'''
        if action.name == "UP":
            action_index = 0
        elif action.name == "RIGHT":
            action_index = 1
        elif action.name == "DOWN":
            action_index = 2
        elif action.name == "LEFT":
            action_index = 3
        
        self.qtable[state.y][state.x][action_index] = val

    def learn_episode(self, alpha=.10, gamma=.90):
        '''with the given alpha and gamma values, learn q-values of a complete game'''
        # from a random initial state,

        # TODO: Figure out any bugs that might occur here with position initialization
        self.state = State(self.env, 
                           random.randint(self.env.x_size), 
                           random.randint(self.env.y_size))


        while True:
            if random.random > alpha:
                # TODO: Implement find optimal move
                pass
            else:
                # TODO: Choose move at random.
                break
            
            # TODO: Execute action
            # TODO: Print State
            # TODO: Compute reward of action
            # TODO: Compute1 Reward
            # TODO: Update Q-table.

            # TODO Check if game is in finished state.
            # TODO: If finished: break out of loop
            # TODO: If not finished continue to the next game loop.


        # consider a random legal action, execute that action,
        # compute the reward, and update the q table for (state, action).
        # repeat until an end state is reached (thus completing the episode)
        # also print the state after each action
    
    def learn(self, episodes:int, alpha=.10, gamma=.90):
        '''run <episodes> number of episodes for learning with the given alpha and gamma'''
        pass

    def string_helper(self, value):
        if value == 0:
            return '----'
        else:
            return round(value, 2)

    def __str__(self):
        '''return a string for the q table as described in the assignment'''
        # TODO: This is just a place holder

        output = ''
        labels = ["UP", "RIGHT", "DOWN", "LEFT"]

        for i in range(4):
            output += (labels[i] if i == 0 else ("\n" + labels[i]))
            for y in range(self.env.y_size):
                output += "\n"
                for x in range(self.env.x_size):
                    output += (self.string_helper(self.qtable[y][x][i]) + "\t") # TODO: Test to make sure x and y are being indexed properly

        return output

                


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        env = Env(sys.argv[2] if len(sys.argv) > 2 else DEFAULT_STATE)
        if cmd == 'learn':
            qt = QTable(env, ACTIONS)
            qt.learn(100)
            print(qt)
