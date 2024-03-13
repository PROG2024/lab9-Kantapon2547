"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter()
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class CounterTest(unittest.TestCase):

    def test_singleton_instance(self):
        """Check if both instances refer to the same object"""
        counter1 = Counter()
        counter2 = Counter()
        self.assertIs(counter1, counter2)

    def test_shared_count(self):
        """Check if the count is shared among all instances"""
        counter1 = Counter()
        counter1.increment()

        counter2 = Counter()
        counter2.increment()
        self.assertEqual(counter1.count, counter2.count)

    def test_count_not_reset(self):
        """# Check if the count is not reset to 0 when creating a new instance"""
        counter1 = Counter()
        counter1.increment()

        counter2 = Counter()
        self.assertEqual(counter2.count, 1)


if __name__ == '__main__':
    unittest.main()
