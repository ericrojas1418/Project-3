

class Device:
    def __init__(self, device_name, x, y, standard, speed, supports_11k, supports_11v, supports_11r, minimal_rssi):
        self._device_name = device_name
        self._x_coord = x
        self._y_coord = y
        self._standard = standard
        self._speed = speed
        self._standard = standard
        self._supports_11k = supports_11k
        self._supports_11v = supports_11v
        self._supports_11r = supports_11r
        self._minimal_rssi = minimal_rssi

    def get_name(self):
        return self._device_name

    def get_x(self):
        return self._x_coord

    def get_y(self):
        return self._y_coord

    def get_standard(self):
        return self._standard

    def get_speed(self):
        return self._speed

    def get_supports_11k(self):
        return self._supports_11k

    def get_supports_11v(self):
        return self._supports_11v

    def get_supports_11r(self):
        return self._supports_11r

    def get_minimal_rssi(self):
        return self._minimal_rssi


__all__ = [
    Device.__name__
]