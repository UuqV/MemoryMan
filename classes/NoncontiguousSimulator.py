import SimConfig
from NCPageTable import PageTable

class NoncontiguousSimulator:

    """
    Loads config from a file and runs a full memory
    simulation using a page table
    """

    def __init__(self, path):
        self.proc_configs = SimConfig.load_proc_configs(path)
        self.time = 0
        self.page_table = PageTable(256)

    def simulate(self):
        self.log("Simulator started (Non-contiguous)");

        while not self.is_finished():
            for proc_config in self.proc_configs:
                for pair in proc_config.arrival_exit_pairs:
                    arrival_time = pair[0]
                    exit_time = pair[1]
                    if self.time == arrival_time:
                        self.handle_arrival(proc_config)
                    if self.time == exit_time:
                        self.handle_exit(proc_config)
            self.time += 1
        self.time -= 1 # Nothing actually happens on the last step

        self.log("Simulator ended (Non-contiguous)");

    def is_finished(self):
        for proc_config in self.proc_configs:
            for pair in proc_config.arrival_exit_pairs:
                if self.time <= pair[1]:
                    return False
        return True

    def handle_arrival(self, proc_config):
        self.log("Process %s arrived (requires %d frames of physical memory)"
                % (proc_config.char_id, proc_config.mem_size))
        if proc_config.mem_size > self.page_table.count_free():
            self.log("Cannot place process %s -- skipping process %s" %
                    (proc_config.char_id, proc_config.char_id))
        else:
            self.log("Placed process %s in memory:" % proc_config.char_id)
            self.page_table.add_proc(proc_config)
            print self.page_table

    def handle_exit(self, proc_config):
        if self.page_table.is_in_mem(proc_config):
            self.log("Process %s removed from physical memory" % proc_config.char_id)
            self.page_table.remove_proc(proc_config)
            print self.page_table

    def log(self, line):
        'Print one line with time info'
        print "time %dms: " % self.time + line
