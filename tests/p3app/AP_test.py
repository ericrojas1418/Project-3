import unittest
from p3app.AP import *
from p3app.Device import *

class MyTestCase(unittest.TestCase):
    test_counter = 0
    def setUp(self):
        self.test_AP = AP("AP1", "0", "0", "6","20", "2.4/5", "WiFi6", "true", "true", "true", "50", "10", "75")
        self.test_device1= Device("Client1", "10", "10", "WiFi6", "2.4/5", "true", "true", "true", "73")
        self.test_device2 = Device("Client2", "9", "8", "WiFi7", "2.4/4", "true", "true", "true", "73")
        MyTestCase.test_counter += 1
        print(f'beginning test number {MyTestCase.test_counter}')
    def test_device_adding_works(self):
        self.test_AP.add_device_to_network(self.test_device1)
        print(self.test_AP.network_devices)
        assert len(self.test_AP.network_devices) == 1

    def test_device_connect_log_works(self):
        self.test_AP.add_device_to_network(self.test_device1)
        print(self.test_AP.AP_log)
        assert len(self.test_AP.AP_log) == 1

    def test_device_connect_log_works2(self):
        self.test_AP.add_device_to_network(self.test_device1)
        self.test_AP.add_device_to_network(self.test_device2)
        print(self.test_AP.AP_log)
        assert len(self.test_AP.AP_log) == 2

    def test_device_denial_works(self):
        self.test_AP.device_limit = 1
        self.test_AP.add_device_to_network(self.test_device1)
        self.test_AP.add_device_to_network(self.test_device2)
        print(self.test_AP.AP_log)
        assert len(self.test_AP.AP_log) == 2

    def test_removal(self):
        self.test_AP.add_device_to_network(self.test_device1)
        self.test_AP.add_device_to_network(self.test_device2)
        self.test_AP.remove_device_from_network(self.test_device1)
        print(self.test_AP.AP_log)
        assert self.test_AP.current_device_count == 1
    def tearDown(self):
        print(f'Exiting test number {MyTestCase.test_counter}')
        print()
if __name__ == '__main__':
    unittest.main()
