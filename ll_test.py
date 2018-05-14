from DataStructure.LinkedList import LinkedList


def create_singly_linked_list(data):
    singly_linked = LinkedList(data)
    return singly_linked


def main():
    string_var = "first element"
    s_linked_list = create_singly_linked_list(string_var)
    print(len(s_linked_list))


main()