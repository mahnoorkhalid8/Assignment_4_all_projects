def in_range(n, low, high):
     """Returns True if n is between low and high, inclusive.
     High is guaranteed to be greater than low."""

     if n >= low and n <= high:
          return True
     
     return False

print(in_range(2, 4, 9))