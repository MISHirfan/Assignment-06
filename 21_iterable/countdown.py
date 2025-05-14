# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0. 


class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start  # Track current number for iteration
    
    def __iter__(self):
        return self  # Return the iterator object (self)
    
    def __next__(self):
        if self.current < 0:  # Stop when current goes below 0
            raise StopIteration
        value = self.current  # Return current value
        self.current -= 1     # Decrement for next iteration
        return value

# Example usage
countdown = Countdown(5)
for num in countdown:
    print(num)  # Output: 5, 4, 3, 2, 1, 0