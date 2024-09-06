import math
from p3app.Device import Device
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
        self.network_devices = {}
        self.AP_log = []
        self.currentStep = 0

        # internal memory for function specific modification
        self.network_knowledge = {

        }
        self.device_rssi = {}
        #method to call method to update dictionary of device_rssi

    #this will come in helpful after movements
    def add_device_to_network(self,new_device): #To calculate signal strength, we inbed the two necessary functions, bc otherwise would be redundant
        def calc_rssi(device):

            def calculate_device_distance_from_ap(device):
                distance = math.sqrt(((int(device.get_x()) - int(self.x_coord)) ** 2) + ((int(device.get_y()) - int(self.y_coord)) ** 2))
                return distance

            device_rssi = int(self.power_level) - ((20 * math.log10(calculate_device_distance_from_ap(device))) -
                                                   (20 * math.log10(eval(self.frequency))) - 32.44)
            return device_rssi

        if isinstance(new_device, Device): #If we try to add a device, we make a dictionary of the device's information, and update our existing dictionary to include it
            signal_strength = calc_rssi(new_device)
            self.network_devices.update({new_device.get_name() : [new_device.get_x(),new_device.get_y(),new_device.get_standard(), new_device.get_standard(), new_device.get_speed(), new_device.get_supports_11k(), new_device.get_supports_11v(), new_device.get_supports_11r(), new_device.get_minimal_rssi(), signal_strength]}) #Information will be stored in this order. x_coord, y_coord, standard,speed, supports_11k, supports_11v, supports_11r, minimal_rssi required, SIGNAL STRENGTH
        else:
            raise ValueError("Can only Device type objects to our Device Network")

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


__all__ = [
    AP.__name__
]