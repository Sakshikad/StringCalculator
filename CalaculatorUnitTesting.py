import unittest
import StringCalaculator

class TestCalci(unittest.TestCase):
    def test_Empty_String(self):
        self.assertEqual(StringCalaculator.find_sum(""),0)
    def test_Single_Numeric_String(self):
        self.assertEqual(StringCalaculator.find_sum("1"),1)
    def test_Negative_Numbers(self):
        self.assertEqual(StringCalaculator.find_sum("-5"),"negative not allowed")
    def test_More_than_one_Numeric_Numbers(self):
        self.assertEqual(StringCalaculator.find_sum("1,2,3"), 6)
    def test_delimiter(self):
        self.assertEqual(StringCalaculator.find_sum("//;\n1;2"),3)
    def test_greater_than_1000(self):
        self.assertEqual(StringCalaculator.find_sum("3,1005"),3)

if __name__ == '__main__':
    unittest.main()
