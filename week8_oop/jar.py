"""A cookie jar with a fixed capacity that can be deposited into and withdrawn from."""


class Jar:
    def __init__(self, size=0, capacity=12):
        if capacity < size or capacity < 0 or size < 0:
            raise ValueError("Invalid size/capacity")
        self.capacity = capacity  # calls capacity setter
        self.size = size          # calls size setter

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Not enough room in the jar")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies in the jar")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        self._capacity = new_capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        self._size = new_size

    def __str__(self):
        return "🍪" * self.size


def main():
    max_cookies = int(input("Capacity: "))
    current_cookies = int(input("Cookies: "))
    jar = Jar(current_cookies, max_cookies)  # calls __init__

    print(f"Current number of cookies is: {jar.size}")           # calls size getter

    jar.deposit(5)
    print(f"Current number of cookies after adding cookies is: {jar.size}")

    jar.withdraw(2)
    print(f"Current number of cookies after withdrawing cookies is: {jar.size}")

    print(jar)  # calls __str__


if __name__ == "__main__":
    main()
