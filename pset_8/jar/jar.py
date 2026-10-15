class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Negative number")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return f"{self._size * '🍪'}"

    def deposit(self, n):
        if n + self._size > self._capacity:
            raise ValueError("Capacity Overload")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Sorry we haven't much cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar(6)
jar.deposit(6)
jar.withdraw(2)
print(jar)
