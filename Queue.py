class Task:
    task_count = 0
    task_list = []

    def __init__(self, voltage_req, process_time, trans_time, dest_time, memory_req, left_time):
        Task.task_count += 1
        self.no = Task.task_count

        self.voltage_req = voltage_req
        self.process_time = process_time
        self.trans_time = trans_time
        self.dest_time =0

        self.memory_req = memory_req

        self.left_time = process_time

        Task.task_list.append(self)

    def calc_dest(task):
        dest_time = task.process_time

