import os
from qlearn import *

DEFAULT_STATE = '       | ###  -| # #  +| # ####|       '
cmd = 0
env = Env(DEFAULT_STATE)
qt = QTable(env, ACTIONS)
qt.learn(100)

print(qt)