from get_codes import get_code as gt
import unittest

class TestCode(unittest.TestCase):
	def test_code(self):
		code = gt('Russian Federation')
		self.assertEqual(code,'ru')

unittest.main()