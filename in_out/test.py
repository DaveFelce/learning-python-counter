import unittest
from in_out.file import Read
from collections import Counter

class InOutTest(unittest.TestCase):
    def setUp(self):
        file = Read()
        self.nums = file.read_lines('/Users/davidfelce/test.file')[0]

    def test_equality(self):
        self.assertEqual(len(self.nums), 6)

    def test_obj_equality(self):
        self.assertIsInstance(self.nums, list, 'Yay is list')

    def test_assert_in(self):
        self.assertIn(2, self.nums, '2 should be in list')

    def test_counter(self):
        cnt = Counter(self.nums)
        self.assertIn((1, 2), cnt.most_common(2))
        self.assertIn((2, 2), cnt.most_common(2))
        self.assertNotIn((3, 3), cnt.most_common(2))

if __name__ == '__main__':
    unittest.main(verbosity=2)
