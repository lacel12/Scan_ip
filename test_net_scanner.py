# test_net_scanner.py
import unittest
from net_scanner import scan_range

class TestScanner(unittest.TestCase):
    def test_scan_range(self):
        results = scan_range("127.0.0.1/32")
        self.assertEqual(len(results), 1)
        self.assertIn(results[0][1], ['Active', 'Inactive'])

if __name__ == '__main__':
    unittest.main()
