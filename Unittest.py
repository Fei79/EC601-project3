import unittest
import Project2

class Testing(unittest.TestCase):
    def test_nonmlb(self,keyword,teamarray):
        if keyword in teamarray:
            return "pass"
        else:
            return "fail"

if __name__ == '__main__':
    unittest.main()
