import unittest
from freight import PriceBook, Ticket
class T(unittest.TestCase):
    def test_single(self):
        b = PriceBook([(0, 10, 2), (10, None, 5)])
        self.assertEqual(Ticket("a", 12, b).charge(), 10 * 2 + 2 * 5)
if __name__ == "__main__":
    unittest.main()
