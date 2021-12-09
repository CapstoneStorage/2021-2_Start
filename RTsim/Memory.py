class Memory:
    def __init__(self, capacity, worst_scale, voltage_active, voltage_idle):
        self.capacity = capacity
        self.worst_scale = worst_scale
        self.voltage_active = voltage_active
        self.voltage_idle = voltage_idle

        self.used_capacity = 0

        self.power_consumed_active = 0
        self.power_consumed_idle = 0

    def add_power_consumed_idle(self, power: float):
        self.power_consumed_idle += power

    def add_power_consumed_active(self, power:float):
        self.power_consumed_active += power

