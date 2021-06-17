class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def add(self, value):
        new_node = Node(value)
        current = self.head

        while current.next is not None:
            current = current.next
        current.next = new_node

    def len(self):
        current = self.head
        count = 0
        while current.next is not None:
            count += 1
            current = current.next
        return count

    def delete(self, value):
        current = self.head

        while current.next is not None:
            prev = current
            current = current.next
            if current.value == value:
                prev.next = current.next
                return
        else:
            raise Exception(f"{ValueError}")

    def delete_by_index(self, index):
        if index > self.len() or index < 0:
            raise Exception(f"{IndexError} at {index}")
        current = self.head
        cur_idx = 0
        while True:
            prev = current
            current = current.next
            if cur_idx == index:
                prev.next = current.next
                return
            cur_idx += 1

    def display(self):
        ele = 'Head --> '
        current = self.head
        while current.next is not None:
            current = current.next
            ele += str(current.value) + ' --> '
        print(ele)

    def get(self, index):
        if index > self.len() or index < 0:
            raise Exception(f"{IndexError} at {index}")
        current = self.head
        cur_index = 0
        while current.next is not None:
            current = current.next
            if cur_index == index:
                return current.value
            cur_index += 1

    def __getitem__(self, index):
        return self.get(index)

    def insert(self, index, value):
        if index > self.len() or index < 0:
            return self.add(value)
        current = self.head
        prev = self.head
        cur_index = 0
        while True:
            current = current.next
            if cur_index == index:
                new_node = Node(value)
                prev.next = new_node
                new_node.next = current
                return
            prev = current
            cur_index += 1

    def set(self, index, value):
        if index > self.len() or index < 0:
            return self.add(value)
        current = self.head
        cur_index = 0
        while True:
            current = current.next
            if cur_index == index:
                current.value = value
                return
            cur_index += 1

    def insert_node(self, index, node):
        if index < 0:
            print("ERROR: 'Erase' Index cannot be negative!")
            return
        if index >= self.len():  # append the node
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = node
            return
        cur_node = self.head
        prior_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                prior_node.next = node
                return
            prior_node = cur_node
            cur_idx += 1

    def reverse(self):
        current = self.head
        prev = None

        while current is not None:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node
        self.head = prev

    def swapTwo(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self


# 6 -> 0 -> 8 -> 4 -> None
# None <- 6 <- 0 <- 8 <- 4


linked_list = LinkedList()

for i in range(1, 20):
    if i % 2 == 0:
        linked_list.add(i)

print("Length is", linked_list.len())

linked_list.display()

linked_list.delete(12)

linked_list.delete_by_index(5)

linked_list.get(3)

print("Element at 6th index is", linked_list[6])

linked_list.insert(5, 100)

linked_list.set(0, 999)

print("Length is", linked_list.len())

linked_list.display()

linked_list.reverse()

linked_list.display()

print(linked_list[5])

linked_list.display()
