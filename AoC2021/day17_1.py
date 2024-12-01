testdata = [(-10,-5),(20,30)]
file = 'input/day17_1.txt'
with open(file, 'r') as reader:
    try:
        inputList = reader.readlines()
        inputList = [str(x.strip()) for x in inputList]
        # inputList = [str(x.strip()) for x in inputList]
        realdata = inputList
    finally:
        reader.close()

# target area: x=269..292, y=-68..-44
realdata = [(-68,-44),(269,292)]


target = realdata

def hasHitTarget(target, projectile):
    ytar = set(range(target[0][0],target[0][1]+1))
    xtar = set(range(target[1][0],target[1][1]+1))

    yproj = projectile[0]
    xproj = projectile[1]

    if xproj in xtar and yproj in ytar:
        return True
    else:
        return False
    # return [ytar, xtar]


def shoot(targetarea, yvel, xvel):
    trajectory = []
    failed = False
    xpos = 0
    ypos = 0
    step = 0
    count = 0 
    while not failed:
        step += 1
        xpos += xvel
        ypos += yvel
        if xvel > 0:
            xvel -= 1
        elif xvel < 0:
            xvel += 1
        else:
            xvel = 0
        yvel -= 1
        if hasHitTarget(target, (ypos,xpos)):
            print(f'Step: {step}: ({ypos}, {xpos})')
            print("hit: ", hasHitTarget(targetarea, (ypos,xpos)))
            count += 1

        if xpos > max(targetarea[1]) or ypos < min(targetarea[0]):
            failed = True
            print(f'cannot hit target anymore - beyond target')
            print(f'Step: {step}: ({ypos}, {xpos})')

        trajectory.append((ypos,xpos))

    if failed == False:
        print(f'no more hits Step: {step}: ({ypos}, {xpos})')
    
    if count >= 1:
        return trajectory
    else: 
        return [(0,0)]


high = []

for yvel in range(1,100+1):
    for xvel in range(1,25+1):
        traj = shoot(target, yvel, xvel)
        high.append(max([coord[0] for coord in traj]))

print(high)
print(max(high))