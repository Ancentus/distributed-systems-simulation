# Tightly Coupled VS Loosely Coupled Systems

1. Tightly coupled systems – have a single system wide primary memory shared by all the processors.

2. Loosely coupled system  – each processor has its own local memory.

In this program, we use Python's threading module to simulate two processors running in parallel. In the tightly coupled system, we use a global variable shared_memory that is shared by both threads. In the loosely coupled system, we use two local variables local_memory1 and local_memory2 which are local to each thread.

The tightly_coupled_system function increments the global variable shared_memory by 1 for each iteration, while the loosely_coupled_system function increments the local memory variable by 1 for each iteration.

After running the program, you will see that in the tightly coupled system, the shared memory value will be significantly higher compared to the loosely coupled system where each thread maintains its own local memory. This demonstrates the difference between tightly coupled and loosely coupled systems in terms of memory access. Tightly coupled systems may face issues with contention and consistency when multiple processors access shared memory, while loosely coupled systems provide more isolation and independence to individual processors.

## Run Simulation:

    python tight_vs_loose.py