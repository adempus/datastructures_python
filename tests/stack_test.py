import logging
from datastructs.linear import Stack

logging.basicConfig(filename="./result_logs/stackDebug.log",
                    level=logging.DEBUG)
stackDebugLog = logging.getLogger()


def testStackPush(stack):
    stackDebugLog.info("\n----\nTesting push of values: \"twenty-four\", 40, 65, \"seventy-seven\"")
    stack.push("twenty-four")
    stack.push(40)
    stack.push(65)
    stack.push("seventy-seven")
    testStackSize(stack)


def testStackPop(stack):
    popValue1 = stack.pop()
    popValue2 = stack.pop()
    stackDebugLog.info("\n----\nTesting pop in stack. \n"
                       "Popping off two values from the stack: "
                       "\nValue 1: "+str(popValue1)+", Value 2: "+str(popValue2))
    testPrintStack(stack)
    testStackSize(stack)


def testStackSize(stack):
    stackDebugLog.info("\n----\nTesting stack size()")
    stackDebugLog.info("Current size = "+str(len(stack)))


def testIterateStack(stack):
    for node in stack:
        print(node)


def testPrintStack(stack):
    stackDebugLog.info("stack contents:  "+str(stack))


def main():
    stack = Stack()
    testStackSize(stack)
    testStackPush(stack)
    testPrintStack(stack)
    testStackPop(stack)


main()
