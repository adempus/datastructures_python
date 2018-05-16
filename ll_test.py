from DataStructure.LinkedList import LinkedList


def create_singly_linked_list(data):
    singly_linked = LinkedList(data)
    return singly_linked


def test_push_front():
    print("Testing push front")
    linked_list = LinkedList()
    print("Size: ", len(linked_list))

    linked_list.push_front(13)
    print("Pushed value: 13\n Size: ", len(linked_list))
    print(linked_list.get_head_node().get_next().get_data())

    linked_list.push_front(42)
    print("Pushed value: 42\n Size: ", len(linked_list))
    print(linked_list.get_head_node().get_next().get_data())
    print(linked_list.get_head_node().get_next().get_next().get_data())

    linked_list.push_front(69)
    print("Pushed value: 69\n Size: ", len(linked_list))
    print(linked_list.get_head_node().get_next().get_data())
    print(linked_list.get_head_node().get_next().get_next().get_data())
    print(linked_list.get_head_node().get_next().get_next().get_next().get_data())


def test_push_back():
    print("\nTesting push back")
    linked_list = LinkedList()
    linked_list.push_back(27)
    print("Pushed value: 27\n Size: ",len(linked_list))

    linked_list.push_back(89)
    print("Pushed value: 89\n Size: ", len(linked_list))
    print(linked_list.get_head_node().get_next().get_data())
    print(linked_list.get_head_node().get_next().get_next().get_data())

    linked_list.push_back(93)
    print("Pushed value: 93\n Size: ", len(linked_list))
    print(linked_list.get_head_node().get_next().get_next().get_next().get_data())

    linked_list.push_back(900)
    print("Pushed value: 900\n Size: ", len(linked_list))
    print(linked_list.get_head_node().get_next().get_next().get_next().get_next().get_data())


def test_iterator():
    linked_list = LinkedList()
    linked_list.push_front(20)
    linked_list.push_back(42)
    linked_list.push_front(28)
    linked_list.push_back(89)
    linked_list.push_front(91)

    for node in linked_list:
        print(node)


def main():
    # test_push_front()
    # test_push_back()
    test_iterator()

main()
