
import unittest
import code_python_sample_code_for_testing as cp

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = cp.add(5, 6)
        self.assertEqual(result, 11)
        self.assertEqual(cp.add(-6,9), 3)
        self.assertEqual(cp.add(-6,-2), -8)
        
    def test_multiply(self):
        result = cp.multiply(5, 6)
        self.assertEqual(result, 30)
        self.assertEqual(cp.multiply(-6,9), -54)
        self.assertEqual(cp.multiply(-6,-2), 12)
        
    def test_subtract(self):
        result = cp.subtract(5, 6)
        self.assertEqual(result, -1)
        self.assertEqual(cp.subtract(-6,9), -15)
        self.assertEqual(cp.subtract(-6,-2), -4)
        

if __name__=="__main__":
    unittest.main()