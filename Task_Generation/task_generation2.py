import numpy as np
import pandas as pd
import os

# Set seed
np.random.seed(1)

'''
Dataset1: Medium Tasks (100)
Dataset2: Light(80) + Heavy(20) Tasks
Dataset3: Light(70) + Medium(20) + Heavy(10) Tasks
'''

path = "C:\\Users\\inslab\\Desktop\\Soomin\\졸프"
filename = "Dataset3"

# Number of tasks
num_task = 100
num_task_type = 3 # light, medium, heavy

'''
# Randomly set the number of light, medium, heavy tasks
num_light = np.random.randint(low = 0, high = num_task, size = 1)
num_medium = np.random.randint(low = 0, high = num_task - num_light, size = 1)
num_heavy = num_task - num_light - num_medium
# print(num_light, num_medium, num_heavy)
'''

# Manually set the number of Light, Medium, Heavy tasks
# if two types of task num_light, num_task-num_light
num_light = 70
num_medium = 20
num_heavy = 10


task_type = []

# Set the number of tasks for each task type
if(num_task_type == 1):
    task_type.append(num_task)
elif(num_task_type == 2):
    task_type.append(num_light)
    task_type.append(num_task-num_light)
else:
    task_type.append(num_light)
    task_type.append(num_medium)
    task_type.append(num_heavy)
    

# Light task worst case execution time parameter
light_task_min_wetime = 1
light_task_max_wetime = 10
# Medium task worst case execution time parameter
medium_task_min_wetime = 20
medium_task_max_wetime = 40
# Heavy task worst case execution time parameter
heavy_task_min_wetime = 100
heavy_task_max_wetime = 150

# Light task period of task parameter
light_task_min_period = 10
light_task_max_period = 30
# medium task period of task parameter
medium_task_min_period =50
medium_task_max_period = 90
# Heavy task period of task parameter
heavy_task_min_period = 200
heavy_task_max_period = 400

# Light task memory footprint parameter
light_task_min_memory = 1
light_task_max_memory = 10
# medium task  memory footprint parameter
medium_task_min_memory = 20
medium_task_max_memory = 50
# Heavy task  memory footprint parameter
heavy_task_min_memory = 100
heavy_task_max_memory = 200

# Light task cloud transmission time parameter
light_task_min_cttime = 1
light_task_max_cttime = 20
# medium task transmission time parameter
medium_task_min_cttime = 30
medium_task_max_cttime = 50
# Heavy task transmission time parameter
heavy_task_min_cttime = 60
heavy_task_max_cttime = 100

task_wetime_type = []
task_period_type = []
task_memory_type = []
task_cttime_type =[]
   

if(num_task_type == 1):
    task_wetime_type.append([light_task_min_wetime, light_task_max_wetime])
    task_period_type.append([light_task_min_period, light_task_max_period])
    task_memory_type.append([light_task_min_memory, light_task_max_memory])
    task_cttime_type.append([light_task_min_cttime, light_task_max_cttime])
elif(num_task_type == 2):
    task_wetime_type.append([light_task_min_wetime, light_task_max_wetime])
    task_wetime_type.append([medium_task_min_wetime, medium_task_max_wetime])
    task_period_type.append([light_task_min_period, light_task_max_period])
    task_period_type.append([medium_task_min_period, medium_task_max_period])
    task_memory_type.append([light_task_min_memory, light_task_max_memory])
    task_memory_type.append([medium_task_min_memory, medium_task_max_memory])
    task_cttime_type.append([light_task_min_cttime, light_task_max_cttime])
    task_cttime_type.append([medium_task_min_cttime, medium_task_max_cttime])
else:
    task_wetime_type.append([light_task_min_wetime, light_task_max_wetime])
    task_wetime_type.append([medium_task_min_wetime, medium_task_max_wetime])
    task_wetime_type.append([heavy_task_min_wetime, heavy_task_max_wetime])
    task_period_type.append([light_task_min_period, light_task_max_period])
    task_period_type.append([medium_task_min_period, medium_task_max_period])
    task_period_type.append([heavy_task_min_period, heavy_task_max_period]) 
    task_memory_type.append([light_task_min_memory, light_task_max_memory])
    task_memory_type.append([medium_task_min_memory, medium_task_max_memory])
    task_memory_type.append([heavy_task_min_memory, heavy_task_max_memory]) 
    task_cttime_type.append([light_task_min_cttime, light_task_max_cttime])
    task_cttime_type.append([medium_task_min_cttime, medium_task_max_cttime])
    task_cttime_type.append([heavy_task_min_cttime, heavy_task_max_cttime]) 
    
os.chdir(path);

# Generate task_list
task_list = np.zeros((num_task, 4))
idx = 0
for i in range(num_task_type):
    for t in range(task_type[i]):
        task_list[idx][0] = (np.random.randint(low=task_wetime_type[i][0], high=task_wetime_type[i][1], size = 1))
        task_list[idx][1] = (np.random.randint(low=task_period_type[i][0], high=task_period_type[i][1], size = 1))
        task_list[idx][2] = (np.random.randint(low=task_memory_type[i][0], high=task_memory_type[i][1], size = 1))
        task_list[idx][3] = (np.random.randint(low=task_cttime_type[i][0], high=task_cttime_type[i][1], size = 1))
        idx += 1

# Randomly shuffle task_list
np.random.shuffle(task_list)

# Make task_list
task_list = pd.DataFrame(task_list)
task_list.to_csv(filename+".csv", index=False, header=False)
