
import unittest

class TestLCS(unittest.TestCase):
    
    def test_LCS_input (self):
        a = 'ATGC'
        b = "AATG"
        self.assertEqual(type(a), str)
        self.assertEqual(str, type(b))
        
        
    def test_UpperCase(self):
        x = "ATCG"
        y = "GTCA"
        self.assertTrue(x.isupper())
        self.assertTrue(y.isupper())
        
        
    def test_non_empty_input(self):
        a = "AAA"
        b = "ATCG"
        self.assertNotEqual(len(a), len(""))
        self.assertNotEqual(len(""),len(b))
        
if __name__ == '__main__':
    unittest.main()
        
        
