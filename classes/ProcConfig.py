class ProcConfig:
    """
    Holds immutable configuration info for one process

    char_id - A single char A-Z that uniquely ids this proc
    mem_size - The size in memory units
    arrival_exit_pairs - List of tuples: (arrival, exit)
    """

    def __init__(self, config_line):
        tokens = config_line.split(" ")
        self.char_id = tokens[0]
        self.mem_size = int(tokens[1])
        self.arrival_exit_pairs = []
        for pair in tokens[2:]:
            arrival_time = int(pair.split("-")[0])
            exit_time = int(pair.split("-")[1])
            self.arrival_exit_pairs.append((arrival_time, exit_time))