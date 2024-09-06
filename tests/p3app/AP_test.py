import unittest
from p3app.AP import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        test_AP = AP("AP1", "0", "0", "6","20", "2.4/5", "WiFi6", "true", "true", "true", "50", "10", "75")


if __name__ == '__main__':
    unittest.main()
