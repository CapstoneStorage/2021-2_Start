from System import Original, DVFS

system = int(input("[1] original [2] dvfs [3] cloud [4] dvfs+cloud"))
end_sim_time = int(input("시뮬레이션 시간: "))

if system = 1:
    Original(end_sim_time).run()
elif system = 2:
    DVFS(end_sim_time).run()