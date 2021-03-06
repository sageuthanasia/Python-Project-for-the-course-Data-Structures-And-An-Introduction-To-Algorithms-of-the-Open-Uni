"""
Stores the code for the LinkedList class.
"""


class LinkedList:
    """
    A class representing linked-lists.
    """

    def __init__(self, to_be_head):
        """Construct a LinkedList and set self.head to to_be_head."""
        self.head = to_be_head

    def get_head(self):
        """Return self.head."""
        return self.head

    def set_head(self, to_be_head):
        """Sets self.head to to_be_head."""
        self.head = to_be_head

    def print_list(self):
        """Print self."""
        temp = self.head
        while temp is not None:
            print(str(temp.get_val()) + " --> ", end="")
            temp = temp.get_next()
        print('None')
