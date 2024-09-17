
class MySet:
    def __init__(self, elements=None):
        """Initialize the set with an optional list of elements."""
        if elements is None:
            self.elements = set()
        else:
            self.elements = set(elements)
    
    def add(self, element):
        """Add an element to the set."""
        self.elements.add(element)
    
    def delete(self, element):
        """Remove an element from the set if it exists."""
        self.elements.discard(element)  # discard() won't raise an error if the element doesn't exist
    
    def has(self, element):
        """Check if an element is in the set."""
        return element in self.elements
    
    def size(self):
        """Return the number of elements in the set."""
        return len(self.elements)
