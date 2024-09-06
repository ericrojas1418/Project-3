import math

class AP:
    def __init__(self, AP_name, x_coord, y_coord, channel, power_level, frequency, standard, supports_11k, supports_11v,
                 supports_11r, coverage_radius, device_limit, minimal_rssi=None):
        self.AP_name = AP_name
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.channel = channel
        self.power_level = power_level
        self.frequency = frequency
        self.standard = standard
        self.supports_11k = supports_11k
        self.supports_11v = supports_11v
        self.supports_11r = supports_11r
        self.coverage_radius = coverage_radius
        self.device_limit = device_limit
        self.minimal_rssi = minimal_rssi

        # internal memory
        self.devices = {}
        self.AP_log = []
        self.currentStep = 0

        # internal memory for function specific modification
        self.network_knowledge = {

        }
        self.device_rssi = {}
        #method to call method to update dictionary of device_rssi
        self.calc_rssi()

    def calc_rssi(self):
        def calculate_device_distance_from_ap(device):
            distance = math.sqrt(((device.x_coord - self.x_coord)**2) + ((device.y_cord - self.x_coord)**2))
            return distance

        for device in self.devices:

            device_rssi = self.power_level - (  (20 * math.log10(calculate_device_distance_from_ap(device))  ) - 20 * math.log10(self.frequency) - 32.44)
            self.device_rssi[device.name] = device_rssi

    def protocol_radio_rm(self, data):
        # we're gonna need a network setup process in AC that has all the APs share themselves and their
        # details with each other
        if self.supports_11k:
            # import data about other APs
            # will receive list of strings about AP's names, their signal strength, valid channels, and surrounding APs
            # unpack list of strings of data, concatate that knowledge into network knowledge

            # export data about other APs
            # remember signal strength is RSSI
            string = f'AP_Name = {self.AP_name}, Signal_strength = '
        else:
            pass
    def roaming_occurs(self):
        pass
