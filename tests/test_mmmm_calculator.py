from mmmm_calculator import add, div
import unittest


class AddFunctionTests(unittest.TestCase):
    def test_add_adds_two_integers_correctly(self):
        assert add(1, 1) == 2
        assert add(1, 2) == 3
        assert add(100, 321) == 421

    def test_add_adds_two_floats_correctly(self):
        assert add(0.1, 0.1) == 0.2
        assert add(0.1, 0.2) == 0.3
        assert add(0.00213, 0.00342) == 0.00555

    def test_add_adds_two_strings_correctly(self):
        assert add("1", 1) == 2
        assert add(1, "1") == 2
        assert add("1", "2") == 3
        self.assertRaisesRegex(TypeError, ".*not a number.*", add, "x", 1)
        self.assertRaisesRegex(TypeError, ".*not a number.*", add, "y", "2")
        self.assertRaisesRegex(TypeError, ".*not a number.*", add, 0, "c")
        self.assertRaisesRegex(TypeError, ".*not a number.*", add, 89, "")

        assert add("1.2", 2.3) == 3.5
        assert add("3.995", "1.005") == 5

    def test_add_on_other_data_types(self):
        self.assertRaisesRegex(TypeError, ".*not a number.*", add, 89, None)
        self.assertRaisesRegex(TypeError, ".*not a number.*", add, None, 101)
        self.assertRaisesRegex(TypeError, ".*not a number.*", add, None, None)
        self.assertRaisesRegex(TypeError, ".*not a number.*", add, 1, {"a": 11})
        self.assertRaisesRegex(TypeError, ".*not a number.*", add, {"b": 2}, 2)


class DivFunctionTests(unittest.TestCase):
    def test_division_by_zero_throws_error(self):
        self.assertRaises(Exception, div, 2, 0)
