from DataStructure.LinkedList import LinkedList


def create_singly_linked_list(data):
    singly_linked = LinkedList(data)
    return singly_linked


def test_push_front():
    linked_list = LinkedList()
    linked_list.push_front(5)
    print(linked_list._head_node.get_next().get_data())
    print("size: ", len(linked_list))
    linked_list.push_front(4)
    print(linked_list._head_node.get_next().get_data())
    print(linked_list._head_node.get_next().get_next().get_data())
    print(linked_list._head_node.get_next().get_next().get_next().get_next().get_data())
    print("size: ", len(linked_list))


def test_push_back():
    linked_list = LinkedList()
    linked_list.push_front(15)
    linked_list.push_back(12)

def main():
    test_push_front()


main()
