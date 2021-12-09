import numpy as np
import pandas as pd
import os

# Set seed
np.random.seed(0)

path = "C:\\Users\\inslab\\Desktop\\Soomin\\졸프"
filename = "Task1"

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
num_light = 40
num_medium = 30
num_heavy = 30

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
    

# Light task voltage parameter
light_task_min_voltage = 0
light_task_max_voltage = 50
# Medium task parameter
medium_task_min_voltage = 50
medium_task_max_voltage = 100
# Heavy task parameter
heavy_task_min_voltage = 101
heavy_task_max_voltage = 150

# Light task process time parameter
light_task_min_ptime = 0
light_task_max_ptime = 10
# medium task process time parameter
medium_task_min_ptime = 20
medium_task_max_ptime = 80
# Heavy task process time parameter
heavy_task_min_ptime = 200
heavy_task_max_ptime = 400

# Light task transmission time parameter
light_task_min_ttime = 0
light_task_max_ttime = 10
# medium task transmission time parameter
medium_task_min_ttime = 20
medium_task_max_ttime = 40
# Heavy task transmission time parameter
heavy_task_min_ttime = 100
heavy_task_max_ttime = 200

# Light task memory parameter
light_task_min_memory = 0
light_task_max_memory = 10
# medium task  memory parameter
medium_task_min_memory = 20
medium_task_max_memory = 100
# Heavy task  memory parameter
heavy_task_min_memory = 1000
heavy_task_max_memory = 2000

task_voltage_type = []
task_ttime_type = []
task_ptime_type = []
task_memory_type =[]
   

if(num_task_type == 1):
    task_voltage_type.append([medium_task_min_voltage, medium_task_max_voltage])
    task_ttime_type.append([medium_task_min_ttime, medium_task_max_ttime])
    task_ptime_type.append([medium_task_min_ptime, medium_task_max_ptime])
    task_memory_type.append([medium_task_min_memory, medium_task_max_memory])
elif(num_task_type == 2):
    task_voltage_type.append([light_task_min_voltage, light_task_max_voltage])
    task_voltage_type.append([heavy_task_min_voltage, heavy_task_max_voltage])
    task_ttime_type.append([light_task_min_ttime, light_task_max_ttime])
    task_ttime_type.append([heavy_task_min_ttime, heavy_task_max_ttime])
    task_ptime_type.append([light_task_min_ptime, light_task_max_ptime])
    task_ptime_type.append([heavy_task_min_ptime, heavy_task_max_ptime])
    task_memory_type.append([light_task_min_memory, light_task_max_memory])
    task_memory_type.append([heavy_task_min_memory, heavy_task_max_memory])
else:
    task_voltage_type.append([light_task_min_voltage, light_task_max_voltage])
    task_voltage_type.append([medium_task_min_voltage, medium_task_max_voltage])
    task_voltage_type.append([heavy_task_min_voltage, heavy_task_max_voltage])
    task_ttime_type.append([light_task_min_ttime, light_task_max_ttime])
    task_ttime_type.append([medium_task_min_ttime, medium_task_max_ttime])
    task_ttime_type.append([heavy_task_min_ttime, heavy_task_max_ttime]) 
    task_ptime_type.append([light_task_min_ptime, light_task_max_ptime])
    task_ptime_type.append([medium_task_min_ptime, medium_task_max_ptime])
    task_ptime_type.append([heavy_task_min_ptime, heavy_task_max_ptime]) 
    task_memory_type.append([light_task_min_memory, light_task_max_memory])
    task_memory_type.append([medium_task_min_memory, medium_task_max_memory])
    task_memory_type.append([heavy_task_min_memory, heavy_task_max_memory]) 
    
os.chdir(path);

# Generate task_list
task_list = np.zeros((num_task, 4))
idx = 0
for i in range(num_task_type):
    for t in range(task_type[i]):
        task_list[idx][0] = (np.random.randint(low=task_voltage_type[i][0], high=task_voltage_type[i][1], size = 1))
        task_list[idx][1] = (np.random.randint(low=task_ptime_type[i][0], high=task_ptime_type[i][1], size = 1))
        task_list[idx][2] = (np.random.randint(low=task_memory_type[i][0], high=task_memory_type[i][1], size = 1))
        task_list[idx][3] = (np.random.randint(low=task_ttime_type[i][0], high=task_ttime_type[i][1], size = 1))
        idx += 1

# Randomly shuffle task_list
np.random.shuffle(task_list)
np.random.shuffle(task_list)
np.random.shuffle(task_list)


# Make task_list
task_list = pd.DataFrame(task_list)
task_list.to_csv(filename+".csv", index=False, header=False)
