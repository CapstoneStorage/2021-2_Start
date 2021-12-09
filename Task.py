class Task:
    count = 0
    task_list = []

    def __init__(self, wcet, period, memory_req, memory_active_ratio, cpu):
        self.wcet = wcet
        self.period = self.deadline = period
        self.memory_req = memory_req
        self.memory_active_ratio = memory_active_ratio

        self.cpu = cpu
        self.cpu_frequency = None
        self.memory = None

        self.det = 0
        self.det_remain = 0
        self.gap = 0

        Task.n_task += 1
        self.no = Task.n_task
        Task.task_list.append(self)

    def calc_priority(self):
        return float(self.deadline)/self.det_remain

    def calc_det(self):
        return

    def exec_idle(self, time, update_deadline):
        self.memory.power_consumed_idle += time * self.memory_req + self.memory.power_idle
        if update_deadline:
            self.deadline -= 1

    def exec_active(self, time, system):
        self.deadline -= time
        self.det_remain -= time

        wcet_scaled_cpu = 1/self.cpu_frequency.wcet_scale
        wcet_scaled_mem = 1/self.memory.wcet_scale
        wcet_scaled = wcet_scaled_cpu + wcet_scaled_mem

        self.cpu.add_power_consumed_active()
        self.cpu.add_power_comsumed_idle()
        self.memory.add_power_consumed_active()
        self.memory.add_power_consumed_idle()

