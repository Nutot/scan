import os
import random
import string
import time
filtered_files=os.listdir('img')
g = len(filtered_files)
def rand():
    for filename in os.listdir('img'):
        os.rename(f'{"img"}/{filename}',f'{"img"}/{''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))}.{'jpg'}')
def so():
    for f in range(g-1):
         for filename in os.listdir('img'):
             try:
                f = f + 1
                os.rename(f'{"img"}/{filename}', f'{"img"}/{f}.{'jpg'}')
             except FileExistsError:
                 break





rand()
