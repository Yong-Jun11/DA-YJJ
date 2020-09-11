import unittest
import project as prog

class TestMyProgram(unittest.TestCase):
    def test_Total(self):
        self.assertEqual(prog.total, 3192865)

    def test_Mean(self):
        self.assertEqual(prog.mean, 1064288.34)

if __name__ == '__main__':
    unittest.main()
