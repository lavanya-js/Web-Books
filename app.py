
import unittest

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(20, 20), 40)

    def test_subtract(self):
        self.assertEqual(subtract(30, 10), 20)

    def test_multiply(self):
        self.assertEqual(multiply(4, 10), 40)


if __name__ == "__main__":

    print("Student Calculator")
    print("Add:", add(20, 20))
    print("Subtract:", subtract(20, 10))
    print("Multiply:", multiply(5, 4))

    print("\nExecuting Automated Tests >>>\n")

    unittest.main(argv=['first-arg-is-ignored'], exit=False)
