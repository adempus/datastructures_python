import logging

from linear import LinkedList

logging.basicConfig(filename="/home/adempus/PycharmProjects/ByteExcersizes/DataStructure/tests/result_logs/linkedListDebug.log",
                    level=logging.DEBUG)
debugLogger = logging.getLogger()


def createLinkedList(data):
    singly_linked = LinkedList(data)
    return singly_linked


def testPushFront(linked_list):
    debugLogger.info(" \n----\nTesting LinkedList pushFront()\n"
                      "Pushing front values: 20, 18, 19, 16, 93, 40\n")
    testSize(linked_list)
    testVals = [20, 18, 19, 16, 93, 40]
    for v in testVals:
        linked_list.pushFront(v)

    debugLogger.info("Printing pushFront values from the list: \n")
    printList(linked_list)
    testSize(linked_list)


def testPushBack(linked_list):
    debugLogger.info(" \n----\nTesting LinkedList pushBack()\n"
                     "Pushing back values: 563, 112, 4, 10, 75, 420\n")
    testSize(linked_list)
    testVals = [563, 112, 4, 10, 75, 420]
    for v in testVals:
        linked_list.pushBack(v)

    debugLogger.info("Printing pushBack values from the list: \n")
    printList(linked_list)
    testSize(linked_list)


def testRemove(linked_list):
    testSize(linked_list)
    debugLogger.info("\n----\nTesting LinkedList remove\n"
                     "Removing previously added values: 20, 93, 112, 420\n")
    linked_list.remove(20)
    linked_list.remove(93)
    linked_list.remove(112)
    linked_list.remove(420)
    debugLogger.info("Printing list to confirm removal of previously added values.\n")
    printList(linked_list)
    testSize(linked_list)


def testIterator(linked_list):
    testSize(linked_list)
    debugLogger.info("\n----\nTesting LinkedList iterator\n"
                     "Pushing back values: 30, 45, 83, 77, 41, 19, 8, 11\n")
    testVals = [30, 45, 83, 77, 41, 19, 8, 11]
    for val in testVals:
        linked_list.pushBack(val)

    debugLogger.info("Printing values in loop from linked_list")
    printList(linked_list)
    testSize(linked_list)


def testInsert(linked_list):
    testSize(linked_list)
    debugLogger.info("\n----\nTesting LinkedList insert\n"
                     "Inserting value 50 after 30, 476 after 19, and 32 after 11\n")
    linked_list.insert(30, 50)
    linked_list.insert(19, 476)
    linked_list.insert(11, 32)
    debugLogger.info("Printing list to confirm insertion of values. ")
    printList(linked_list)
    testSize(linked_list)


def testSize(linked_list):
    debugLogger.info("\n----\nTesting LinkedList size()")
    debugLogger.info("Current size = "+str(len(linked_list)))


def printList(linked_list):
    for node in linked_list:
        debugLogger.info(" "+str(node))


def testReplace(linked_list):
    debugLogger.info("\n----\nTesting LinkedList replace()\n"
                     "Replacing values: 50 with \"fifty\", 476 \"four-hundred-seventy-six\" and 32 \"thirty-two\" \n")
    linked_list.replace(50, "fifty")
    linked_list.replace(476, "four-hundred-seventy-six")
    linked_list.replace(32, "thirty-two")
    debugLogger.info("Printing linked list to confirm replacements")
    printList(linked_list)


def testGetNode(linked_list):
    debugLogger.info("\n----\nTesting LinkedList getNode()\n"
                     "Getting node containing data: "+"four-hundred-seventy-six")
    retrievedNode = linked_list.getNode("four-hundred-seventy-six")
    debugLogger.info("\nPrinting data from retrieved node: "+str(retrievedNode))


def main():
    linked_list = LinkedList()
    testPushFront(linked_list)
    testPushBack(linked_list)
    testIterator(linked_list)
    testRemove(linked_list)
    testInsert(linked_list)
    testReplace(linked_list)
    testGetNode(linked_list)


main()
