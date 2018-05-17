from DataStructure.LinkedList import LinkedList
import logging


logging.basicConfig(filename="/home/adempus/PycharmProjects/ByteExcersizes/DataStructure/debugLog.log",
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
    for node in linked_list:
        debugLogger.info(" "+str(node))
    testSize(linked_list)



def testPushBack(linked_list):
    debugLogger.info(" \n----\nTesting LinkedList pushBack()\n"
                     "Pushing back values: 563, 112, 4, 10, 75, 420\n")
    testSize(linked_list)
    testVals = [563, 112, 4, 10, 75, 420]
    for v in testVals:
        linked_list.pushBack(v)

    debugLogger.info("Printing pushBack values from the list: \n")
    for node in linked_list:
        debugLogger.info(" " + str(node))
    testSize(linked_list)


def testIterator():
    linked_list = LinkedList()
    linked_list.pushFront(20)
    linked_list.pushBack(42)
    linked_list.pushFront(28)
    linked_list.pushBack(89)
    linked_list.pushFront(91)

    for node in linked_list:
        print(node)


def testSize(linked_list):
    debugLogger.info("\nTesting LinkedList size()")
    debugLogger.info("current size = "+str(len(linked_list)))



def main():
    linked_list = LinkedList()
    testPushFront(linked_list)
    testPushBack(linked_list)
    #testIterator()

main()
