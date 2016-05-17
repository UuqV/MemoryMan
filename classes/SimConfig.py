from ProcConfig import *

def load_proc_configs(path) :
    'Parse all proc configs from a file into a list'
    proc_configs = []
    with open(path) as f:
        for line in f:
            # Skip lines that are not procs
            if len(line.split(" ")) < 3:
                continue
            proc_configs.append(ProcConfig(line))
    return proc_configs
