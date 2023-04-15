from concurrent.futures import thread
import random
import time
import threading

# Define constant for number of workstations
NUM_WORKSTATIONS = 5

# Define a workstation class
class Workstation:
    def __init__(self, id):
        self.id = id
        self.is_idle = True
        self.processing_time = 0

    def process_job(self, job):
        self.is_idle = False
        self.processing_time = random.randint(1,5)
        print(f"Workstation {self.id} is processing job {job} for {self.processing_time} seconds.")
        time.sleep(self.processing_time)
        print(f"Workstation {self.id} finished processing job {job}.")
        self.is_idle = True

# Function to assign job to idle workstations
def assign_job(workstation, job_counter):
    while True:
        if workstation.is_idle:
            workstation.process_job(job_counter)
            break
        else:
            time.sleep(1)

# Create a list of workstations
workstations = []
for i in range(NUM_WORKSTATIONS):
    workstation = Workstation(i)
    workstations.append(workstation)

# Simulate job processing using threads
job_counter = 0
while True:
    # Slow down the simulation
    time.sleep(1)

    job_counter += 1
    print(f"Job {job_counter} arrived.")
    idle_workstations = [workstation for workstation in workstations if workstation.is_idle]
    if idle_workstations:
        workstation = random.choice(idle_workstations)
        thread = threading.Thread(target=assign_job, args=(workstation, job_counter))
        thread.start()
    else:
        print("All workstations are busy. Waiting for a workstation tobecome idle...")
        time.sleep(1)