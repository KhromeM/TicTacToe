


tiles= {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
# If the tiles are blank they have a value of 0, if X or O then 1,2 repectively
wins = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]

x1=('|-------|')
x2=('| *   * |')
x3=('|   *   |')
x4=('| *   * |')
x5=('|-------|')
e1=('|-------|')
e2=('|       |')
e3=('|       |')
e4=('|       |')
e5=('|-------|')
o1=('|-------|')
o2=('| * * * |')
o3=('| *   * |')
o4=('| * * * |')
o5=('|-------|')

def part1():
    l1= ''
    l2= ''
    l3= ''
    l4= ''
    l5= ''
    l=[7,8,9]
    for n in l:
        if tiles[n] == 0:
            l1 += e1
            l2 += e2
            l3 += e3
            l4 += e4
            l5 += e5
        elif tiles[n] == 1:
            l1+= x1
            l2+= x2
            l3+= x3
            l4+= x4
            l5+= x5
        else:
            l1+= o1
            l2+= o2
            l3+= o3
            l4+= o4
            l5+= o5
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)

def part2():
    l1= ''
    l2= ''
    l3= ''
    l4= ''
    l5= ''
    l=[4,5,6]
    for n in l:
        if tiles[n] == 0:
            l1 += e1
            l2 += e2
            l3 += e3
            l4 += e4
            l5 += e5
        elif tiles[n] == 1:
            l1+= x1
            l2+= x2
            l3+= x3
            l4+= x4
            l5+= x5
        else:
            l1+= o1
            l2+= o2
            l3+= o3
            l4+= o4
            l5+= o5
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)

def part3():
    l1= ''
    l2= ''
    l3= ''
    l4= ''
    l5= ''
    l=[1,2,3]
    for n in l:
        if tiles[n] == 0:
            l1 += e1
            l2 += e2
            l3 += e3
            l4 += e4
            l5 += e5
        elif tiles[n] == 1:
            l1+= x1
            l2+= x2
            l3+= x3
            l4+= x4
            l5+= x5
        else:
            l1+= o1
            l2+= o2
            l3+= o3
            l4+= o4
            l5+= o5
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)

def board():
    part1()
    part2()
    part3()

def inputx():
    i = input('Player X: Enter location of X : ')
    if tiles[int(i)] == 1 or tiles[int(i)] == 2:
        print('Space occupied, please enter another position.')
        return inputx()
    tiles[int(i)] = 1

def inputo():
    i = input('Player O: Enter location of O : ')
    if tiles[int(i)] == 1 or tiles[int(i)] == 2:
        print('Space occupied, please enter another position.')
        return inputo()
    tiles[int(i)] = 2


def wincheck():
    '''Checks if a player has won the game'''
    for a, b, c in wins:
        if tiles[a] == 1 and tiles[b] == 1 and tiles[c] == 1:
          print('X Wins!')
          return 'over'
        if tiles[a] == 2 and tiles[b] == 2 and tiles[c] == 2:
          print('O Wins!')
          return 'over'

def wincheck2():
    '''Checks if a player has won the game'''
    for a, b, c in wins:
        if tiles[a] == 1 and tiles[b] == 1 and tiles[c] == 1:
          return 'over'
        if tiles[a] == 2 and tiles[b] == 2 and tiles[c] == 2:
          return 'over'

def game():
    '''Calling this function starts the game'''
    board()
    while wincheck() != 'over':
        inputx()
        board()
        wincheck()
        if wincheck2() == 'over':
            return None
        inputo()
        board()
        wincheck()


game()

