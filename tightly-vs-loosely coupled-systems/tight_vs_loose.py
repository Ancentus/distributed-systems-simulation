import threading

# Global variable for tightly coupled system
shared_memory = 0

# Function for tightly coupled system
def tightly_coupled_system():
    global shared_memory
    for _ in range(1000000):
        shared_memory += 1

# Function for loosely coupled system
def loosely_coupled_system(local_memory):
    for _ in range(1000000):
        local_memory[0] += 1

if __name__ == "__main__":
    # Tightly coupled system
    shared_memory = 0
    t1 = threading.Thread(target=tightly_coupled_system)
    t2 = threading.Thread(target=tightly_coupled_system)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Tigtly Coupled System: Shared Memory = ", shared_memory)

    # Loosely Coupled System
    local_memory1 = [0]
    local_memory2 = [0]
    t3 = threading.Thread(target=loosely_coupled_system, args=(local_memory1,))
    t4 = threading.Thread(target=loosely_coupled_system, args=(local_memory2,))
    t3.start()
    t4.start()
    t3.join()
    t4.join()
    print("Loosely Coupled System: Local Memory 1 = ", local_memory1[0])
    print("Loosely Coupled System: Local Memory 2 = ", local_memory2[0])