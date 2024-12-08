# 5. Memory Management using Memory Variable Technique (MVT)
def mvt(memory, processes):
    for process in processes:
        if memory >= process:
            print(f"Allocating {process} to memory block")
            memory -= process
        else:
            print(f"Not enough memory for process {process}")
    print(f"Remaining memory: {memory}")

available_memory = 1000
process_sizes = [200, 300, 400, 500]
mvt(available_memory, process_sizes)