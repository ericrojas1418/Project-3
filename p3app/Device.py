

class Device:
    def __init__(self, device_name, x, y, channel, power_level, frequency, standard, supports_11k, supports_11v, supports_11r,
                 coverage_radius, device_limit):
        self.device_name = device_name
        self.x_coord = x
        self.y_coord = y
        self.channel = channel
        self.power_level = power_level
        self.frequency = frequency
        self.standard = standard
        self.supports_11k = supports_11k
        self.supports_11v = supports_11v
        self.supports_11r = supports_11r
        self.coverage_radius = coverage_radius
        self.device_limit = device_limit

__all__ = [
    Device.__name__
]