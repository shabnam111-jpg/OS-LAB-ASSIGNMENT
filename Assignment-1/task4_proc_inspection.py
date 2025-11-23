import os

def main():
    pid = input("Enter PID to inspect: ")
    status_file = f"/proc/{pid}/status"
    exe_file = f"/proc/{pid}/exe"
    fd_folder = f"/proc/{pid}/fd"

    try:
        # Read status
        with open(status_file) as f:
            for line in f:
                if line.startswith(("Name", "State", "VmRSS")):
                    print(line.strip())

        # Executable path
        exe_path = os.readlink(exe_file)
        print(f"Executable Path: {exe_path}")

        # Open file descriptors
        fds = os.listdir(fd_folder)
        print(f"Open File Descriptors: {fds}")

    except FileNotFoundError:
        print(f"No process with PID {pid} exists.")

if __name__ == "__main__":
    main()
