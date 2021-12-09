from abc import *

class CPU(metaclass=ABCMeta):
    MAX_CPU_FREQUENCIES = 15

    def __init__(self):
        self.n_core = None

        self.frequencies = []
        self.n_frequencies = 0

        self.power_consumed_idle = 0
        self.power_consumed_active = 0

    def insert_cpu_frequency(self):
        return

    def assign_cpu_frequency(self, task):
        task.cpu_frequency = self.frequencies[0]

    @abstractmethod
    def reassign_cpu_frequency(self, task, system) -> bool:
        pass

    def exec_idle(self, time: int):
        self.power_consumed_idle += time * self.frequencies[-1].power_idle

    def add_power_consumed_idle(self, power):
        self.power_consumed_idle += power

    def add_power_consumed_active(self, power: float):
        self.power_consumed_active += power

class NoneDVFSCPU(CPU):
    def reassign_cpu_frequency(self, task, system) -> bool:
        return True

class DVFSCPU(CPU):
    def reassign_cpu_frequency(self, task, system):
        return