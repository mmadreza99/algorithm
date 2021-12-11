# Python3 program to implement Shortest Remaining Time First
# Shortest Remaining Time First (SRTF)

# Function to find the waiting time
# for all processes
def find_waiting_time(processes, n, wt):
    rt = [0] * n

    # Copy the burst time into rt[]
    for i in range(n):
        rt[i] = processes[i][1]
    complete = 0
    t = 0
    minimum = 999999999
    short = 0
    check = False

    # Process until all processes gets
    # completed
    while complete != n:

        # Find process with minimum remaining
        # time among the processes that
        # arrives till the current time`
        for j in range(n):
            if ((processes[j][2] <= t) and
                    (rt[j] < minimum) and rt[j] > 0):
                minimum = rt[j]
                short = j
                check = True
        if check == False:
            t += 1
            continue

        # Reduce remaining time by one
        rt[short] -= 1

        # Update minimum
        minimum = rt[short]
        if minimum == 0:
            minimum = 999999999

        # If a process gets completely
        # executed
        if rt[short] == 0:

            # Increment complete
            complete += 1
            check = False

            # Find finish time of current
            # process
            fint = t + 1

            # Calculate waiting time
            wt[short] = (fint - processes[short][1] - processes[short][2])

            if wt[short] < 0:
                wt[short] = 0

        # Increment time
        t += 1


# Function to calculate turn around time
def find_turn_around_time(processes, n, wt, tat):
    # Calculating turnaround time
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]


# Function to calculate average waiting
# and turn-around times.
def find_avg_time(processes, n):
    wt = [0] * n
    tat = [0] * n

    # Function to find waiting time
    # of all processes
    find_waiting_time(processes, n, wt)

    # Function to find turn around time
    # for all processes
    find_turn_around_time(processes, n, wt, tat)

    # Display processes along with all details
    print("Processes Burst Time	 Waiting",
          "Time	 Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" ", processes[i][0], "\t\t",
              processes[i][1], "\t\t",
              wt[i], "\t\t", tat[i])

    print("\nAverage waiting time = %.5f " % (total_wt / n))
    print("Average turn around time = ", total_tat / n)


def process_data():
    print("FIRST COME FIRST SERVE Scheduling")
    n = int(input("Enter number of processes : "))
    proc = []

    for i in range(n):
        temporary = []
        key = f"P{i}"
        arrival_time = int(input(f"Enter arrival time of process {key}: "))
        burst_time = int(input(f"Enter the burst time of the process {key}: "))

        temporary.extend([key, burst_time, arrival_time])
        proc.append(temporary)

    print('ProcessData: ', proc)
    find_avg_time(proc, n)


# Driver code
if __name__ == "__main__":
    process_data()

