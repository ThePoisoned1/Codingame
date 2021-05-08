# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]
first = True

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if first:
        first = False
        aX = 0
        aY = 0
        bX = w
        bY = h
    else:
        if bomb_dir=="U":
            aX = x
            bX = x
            bY = y
        elif bomb_dir=="UR":
            aX=x
            bY=y
        elif bomb_dir=="R":
            aY = y
            bY = y
            aX = x
        elif bomb_dir=="DR":
            aX=x
            aY=y
        elif bomb_dir=="D":
            aX = x
            bX = x
            aY = y
        elif bomb_dir=="DL":
            aY=y
            bX=x
        elif bomb_dir=="L":
            aY=y
            bY=y
            bX=x
        elif bomb_dir=="UL":
            bX=x
            bY=y
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # the location of the next window Batman should jump to.
    x = (bX+aX)//2
    y = (bY+aY)//2
    print("{} {}".format(x,y))
