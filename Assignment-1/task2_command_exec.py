import os

def main():
    commands = ["ls", "date", "whoami"]  # Commands children will run

    N = len(commands)
    for i in range(N):
        pid = os.fork()
        if pid == 0:
            print(f"Child {i+1}: PID={os.getpid()}, executing '{commands[i]}'")
            os.execvp(commands[i], [commands[i]])  # Replace child process
        # Parent continues loop

    # Parent waits for all children
    for _ in range(N):
        os.wait()

if __name__ == "__main__":
    main()
