from abc from *
from CPU import NoneDVFSCPU, DVFSCPU
from Memory import Memory
from Input from InputUtils

class System(metaclass=ABCMeta):
    def __init__(self, end_sim_time : int):
        self.name = None

        self.CPU = None
        self.memories = None

        self.time = 0
        self.end_sim_time = end_sim_time

        self.tasks = []
        self.wait_period_queue =[]
        self.queue = []

    def run(self):
        # input file setup
        InputUtils.set_processor(self)
        InputUtils.set_memory(self)
        InputUtils.set_tasks(self)
        self.setup_tasks()

        #end_time까지 시뮬레이터 돌리기
        while self.time < self.end_sim_time:
            # current time에서 실행될 테스크를 코어 갯수만큼 선택
            exec_task_list = []
            # 코어 갯수보다 큐에 있는 테스크의 갯수가 적으면 모두 실행
            if len(self.queue) < self.CPU.n_core:
                for item in self.queue:
                    exec_task_list.append(item[1])
                self.queue = []
                #남은 코어 갯수만큼 active가 아닌 idle로 돌린다.
                for item in range(self.CPU.n_core - len(self.queue)):
                    self.CPU.exec_idle()
            else:
                for i in range(self.CPU.n_core):
                    exec_task_list.append(self.pop_queue())

            # exec_task_list의 테스크를 실행
            for task in exec_task_list:
                task.active(system = self, time = 1)

            # idle 테스크 실행 (전력소모 계산)


class Original(System):
    def __init__(self, end_sim_time):
        super().__init__(end_sim_time)
        self.name = "Original"
        self.desc = "Nod DVFS with dram"
        self.CPU = NoneDVFSCPU()

    def assign_task(self, task):
        return

    def reassign_task(self, task):
        return


class DVFS(System):
    def __init__(self, end_sim_time):
        super().__init__(end_sim_time)
        self.name = "DVFS"
        self.desc = "DVFS with dram"
        self.CPU = DVFSCPU()

    def assign_task(self, task):
        return

    def reassign_task(self, task):
        return