# Python3 program to implement First come First services
# First come First services (FCFS)
class Fcfs:
    def process_data(self):
        print("FIRST COME FIRST SERVE Scheduling")
        n = int(input("Enter number of processes : "))
        process_data = []
        
        for i in range(n):
            temporary = []
            key = f"P{i}"
            arrival_time = int(input(f"Enter arrival time of process {key}: "))
            burst_time = int(input(f"Enter the burst time of the process {key}: "))

            temporary.extend([key, arrival_time, burst_time])
            process_data.append(temporary)
        # print('ProcessData: ', process_data)
        Fcfs.scheduling_process(process_data)

    @staticmethod
    def scheduling_process(process_data):
        process_data.sort(key=lambda x: x[1])

        e_time = Fcfs.calculate_time_exit(process_data)
        avg_t_time = Fcfs.calculate_turnaround_time(process_data, e_time)
        avg_w_time = Fcfs.calculate_waiting_time(process_data)
        Fcfs.print_data(process_data, avg_t_time, avg_w_time)

    @staticmethod
    def calculate_time_exit(process_data):
        exit_time = []
        for i in range(len(process_data)):
            # first process
            if i == 0:
                exit_time.append(process_data[i][2])  # process_data[['p0',1,5],['p1',2,3]]
                process_data[i].append(process_data[i][2])
            # get prevET + newBT
            else:
                exit_time.append(exit_time[i - 1] + process_data[i][2])  # exit_time[5]+pr...data[['p0',1,5],['p1',2,3]]
                process_data[i].append(exit_time[i - 1] + process_data[i][2])
        # print("calculateTimeExit :", exit_time)
        return exit_time

    @staticmethod
    def calculate_turnaround_time(process_data, exit_time):
        turnaround_time = 0
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = exit_time[i] - process_data[i][1]  # turnaround_time = completion_time - arrival_time
            total_turnaround_time += turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)  # average_waiting_time=total_waiting_time/p
        # print('calculateTurnaroundTime: ', process_data)
        return average_turnaround_time

    @staticmethod
    def calculate_waiting_time(process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][4] - process_data[i][2]  # waiting_time = turnaround_time - burst_time
            total_waiting_time += waiting_time
            process_data[i].append(waiting_time)

        average_waiting_time = total_waiting_time / len(process_data)  # average=total_waiting_time/number_of_processes
        return average_waiting_time

    @staticmethod
    def print_data(process_data, avg_t_time, avg_w_time):
        print("\nProcess | Arrival|Burst| Exit|Turn Around|Wait ")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="\t    ")
            print()
        print("Average Waiting Time: ", avg_w_time)
        print("Average turn Around Time: ", avg_t_time)


algo = Fcfs()
algo.process_data()
