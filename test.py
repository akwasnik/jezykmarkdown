import unittest
import main

class TestMain(unittest.TestCase):
  def test_add(self):
    result = main.add(10,5)
    self.assertEqual(result, 15)
  def test_divide(self):
    result = main.divide(10,5)
    self.assertEqual(result, 2)
  def test_divide(self):
    result = main.multiply(10,5)
    self.assertEqual(result, 50)

if __name__=='__main__':
  unittest.main()
