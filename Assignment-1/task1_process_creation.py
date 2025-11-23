import os
import time

def main():
    N = int(input("Enter the number of child processes to create: "))
    children_pids = []

    for i in range(N):
        pid = os.fork()
        if pid == 0:
            # Child process
            print(f"Child {i+1}: PID={os.getpid()}, Parent PID={os.getppid()}")
            print(f"Child {i+1}: Hello from child process!")
            time.sleep(1)  # Simulate work
            os._exit(0)  # Exit child
        else:
            # Parent process
            children_pids.append(pid)

    # Parent waits for all children
    for _ in children_pids:
        finished_pid, status = os.wait()
        print(f"Parent: Child with PID {finished_pid} finished with status {status}")

if __name__ == "__main__":
    main()
