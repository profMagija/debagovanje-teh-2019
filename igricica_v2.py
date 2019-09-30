import random
import sys, os

print('''
    __  ___                    ______                      
   /  |/  /____ _ ____  ___   / ____/____ _ ____ ___   ___ 
  / /|_/ // __ `//_  / / _ \ / / __ / __ `// __ `__ \ / _ \
 / /  / // /_/ /  / /_/  __// /_/ // /_/ // / / / / //  __/
/_/  /_/ \__,_/  /___/\___/ \____/ \__,_//_/ /_/ /_/ \___/ 
      - by ProfMagija
''')

# adapted from https://stackoverflow.com/questions/510357/python-read-a-single-character-from-the-user
try:
    import msvcrt
    def getch():
        return msvcrt.getch()
except:
    import sys, tty, termios
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

N = 11
M = 2 * N + 1
mz = [['#']*M for _ in range(M)]

sx = (M-1)//2
sy = sx

dx, dy = (-1, 0, 1, 0), (0, 1, 0, 1)

def p():
    s=''
    for ml in mz:
        for mc in ml:
            s += mc*2
        s += '\n'
    print(s)

def gen(x, y):
    l = [0, 1, 2, 3]
    random.shuffle(l)

    for d in l:
        nx = x + 2*dx[d]
        ny = y + 2*dy[d]

        if 0 <= nx < M and 0 <= ny < M and mz[nx][ny] == '#':
            mz[x+dx[d]][y+dy[d]] = ' '
            mz[nx][ny] = ' '

            gen(nx, ny)

gen(sx, sy)

mz[sx][sy] = '@'

if random.randint(0, 1):
    mz[random.choice(range(N))*2 + 1][random.choice((0, M))] = ' '
else:
    mz[random.choice((0, M-1))][random.choice(range(N))*2+1] = ' '

p()

# H -> UP ARROW
# M -> RIGHT ARROW
# P -> DOWN ARROW
# K -> LEFT ARROW
# don't ask me why ...

cntrl = {b'H': (-1,0), b'M': (0,1), b'P': (0,-1), b'K': (1,0)}

while 0 < sx < M and 0 < sy < M:
    c = getch()
    if c == b'\x03':
        print('odustajes :(')
        sys.exit(1)
    if c not in cntrl:
        continue
    dx,dy = cntrl[c]

    if mz[sx + dx][sy+dy] == ' ':
        mz[sx][sy] = ' '

        sx += 2*dx
        sy += 2*dy
        
        mz[sx][sy] = '@'

    p()

print('pobedio si!')