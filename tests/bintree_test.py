from datastructs.nonlinear import BinaryTree

binTree0 = BinaryTree()
binTree1 = BinaryTree()

def testInsertion(values):
    for val in values:
        binTree0.insert(val)

    for val in values:
        binTree1.insert(val)


def testIsEqual():
    print(binTree0 == binTree1)


def main():
    insertVals = [
        60, 156, 98, 42, 91, 109, 44, 165, 161,
        55, 40, 99, 199, 104, 61, 85, 22, 39, 85,
        78, 75, 120, 182, 82, 175, 66, 71, 169,
        127, 115, 144
    ]
    testInsertion(insertVals)
    testIsEqual()


main()