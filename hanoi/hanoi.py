def ToH(DiskToMove, fromStack, toStack, otherStack):

    if ( DiskToMove != 0):
        ToH(DiskToMove-1, fromStack, otherStack, toStack)
        print( fromStack + " -> " + toStack)
        ToH(DiskToMove-1, otherStack, toStack, fromStack)


if __name__ == '__main__':
    print("Let's play a game")
    tower = int(input("Tower of Hanoi for n = "))
    ToH(tower, 'A', 'B', 'C')

