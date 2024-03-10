import re


def parse_syscalls(log_file):
    syscall_data = {}
    current_process = None
    current_syscall = None
    syscall_start_time = None

    with open(log_file, 'r') as f:
        for line in f:
            match = re.match(r'(\d+)\s+(\d+\.\d+)\s+([\w_]+)\((.*)\)\s*=\s*([\w-]+)\s*(?:\{(.*)\})?\s*<([\d.]+)>', line)
            if match:
                process_id, timestamp, syscall_name, syscall_args, syscall_result, syscall_duration = match.groups()
                syscall_duration = float(syscall_duration)

                if current_process != process_id or current_syscall != syscall_name:
                    # New syscall or process
                    if current_process is not None and current_syscall is not None:
                        if current_process not in syscall_data:
                            syscall_data[current_process] = {}
                        if current_syscall not in syscall_data[current_process]:
                            syscall_data[current_process][current_syscall] = 0.0
                        syscall_data[current_process][current_syscall] += syscall_duration

                    current_process = process_id
                    current_syscall = syscall_name

                if syscall_result == 'unfinished':
                    syscall_start_time = float(timestamp)
                elif syscall_result == 'resumed':
                    if syscall_start_time is not None:
                        syscall_duration += float(timestamp) - syscall_start_time
                        syscall_start_time = None

        # Process the last syscall
        if current_process is not None and current_syscall is not None:
            if current_process not in syscall_data:
                syscall_data[current_process] = {}
            if current_syscall not in syscall_data[current_process]:
                syscall_data[current_process][current_syscall] = 0.0
            syscall_data[current_process][current_syscall] += syscall_duration

    # Print the result
    for process, syscalls in syscall_data.items():
        for syscall, duration in syscalls.items():
            print(f"{process} {syscall} {duration:.6f}")


if __name__ == "__main__":
    log_file = "D:\\Workdir\\idea\\Schedule\\data\\source\\alu-X86.txt"
    parse_syscalls(log_file)
