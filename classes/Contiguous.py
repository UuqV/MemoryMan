from ProcConfig import *
from SimConfig import *
import SimConfig
from PageTable import PageTable

class Contiguous:

    """
    Loads config from a file and runs a full memory
    simulation using a page table
    """

    def __init__(self, path):
        self.unfinished_processes = SimConfig.load_proc_configs(path)
        self.time = 0
        self.page_table = PageTable(256)
        self.activeProcesses = []

    def simulate_first(self):
        self.log("Simulator started (Contiguous)");
    
        while len(self.unfinished_processes) != 0:
        
            for pro in self.unfinished_processes:
            
                for enter, exit in pro.arrival_exit_pairs:
                
                    if enter == self.time:
                        self.handle_first_arrival(pro)
                    
                    elif exit == self.time:
                        if pro.char_id in self.activeProcesses:
                            self.handle_removal(pro)
                            self.activeProcesses.remove(pro.char_id)
                        if exit == pro.arrival_exit_pairs[-1][1]:
                            self.unfinished_processes.remove(pro)
                
            self.time += 1
            
    def simulate_next(self):
        self.log("Simulator started (Contiguous)");
    
        while len(self.unfinished_processes) != 0:
        
            for pro in self.unfinished_processes:
            
                for enter, exit in pro.arrival_exit_pairs:
                
                    if enter == self.time:
                        self.handle_next_arrival(pro)
                    
                    elif exit == self.time:
                        if pro.char_id in self.activeProcesses:
                            self.handle_removal(pro)
                            self.activeProcesses.remove(pro.char_id)
                        if exit == pro.arrival_exit_pairs[-1][1]:
                            self.unfinished_processes.remove(pro)
                
            self.time += 1
            
    def simulate_best(self):
        self.log("Simulator started (Contiguous)");
    
        while len(self.unfinished_processes) != 0:
        
            for pro in self.unfinished_processes:
            
                for enter, exit in pro.arrival_exit_pairs:
                
                    if enter == self.time:
                        self.handle_best_arrival(pro)
                    
                    elif exit == self.time:
                        if pro.char_id in self.activeProcesses:
                            self.handle_removal(pro)
                            self.activeProcesses.remove(pro.char_id)
                        if exit == pro.arrival_exit_pairs[-1][1]:
                            self.unfinished_processes.remove(pro)
                
            self.time += 1

    def handle_first_arrival(self, proc_config):
        self.log("Process %s arrived (requires %d frames of physical memory)"
                % (proc_config.char_id, proc_config.mem_size))
        if self.page_table.free >= proc_config.mem_size:
            result = self.page_table.add_first_proc(proc_config)
            self.activeProcesses.append(proc_config.char_id)
            if result == -1:
                self.log("Placed process %s in memory:" % proc_config.char_id)
            else:
                self.log("Cannot place process %s -- starting defragmentation" % proc_config.char_id)
                print "time %dms: Defragmentation complete (moved %d frames: %s)" % (self.time + result, result, ', '.join(['%s' % i for i in self.activeProcesses]))
        else:
            self.log("Cannot place process %s -- skipping process %s" % (proc_config.char_id, proc_config.char_id))
        print self.page_table
        
        
    def handle_next_arrival(self, proc_config):
        self.log("Process %s arrived (requires %d frames of physical memory)"
                % (proc_config.char_id, proc_config.mem_size))
        if self.page_table.free >= proc_config.mem_size:
            result = self.page_table.add_next_proc(proc_config)
            self.activeProcesses.append(proc_config.char_id)
            if result == -1:
                self.log("Placed process %s in memory:" % proc_config.char_id)
            else:
                self.log("Cannot place process %s -- starting defragmentation" % proc_config.char_id)
                print "time %dms: Defragmentation complete (moved %d frames: %s)" % (self.time + result, result, ', '.join(['%s' % i for i in self.activeProcesses]))
        else:
            self.log("Cannot place process %s -- skipping process %s" % (proc_config.char_id, proc_config.char_id))
        print self.page_table
        
    def handle_best_arrival(self, proc_config):
        self.log("Process %s arrived (requires %d frames of physical memory)"
                % (proc_config.char_id, proc_config.mem_size))
        if self.page_table.free >= proc_config.mem_size:
            result = self.page_table.add_best_proc(proc_config)
            self.activeProcesses.append(proc_config.char_id)
            if result == -1:
                self.log("Placed process %s in memory:" % proc_config.char_id)
            else:
                self.log("Cannot place process %s -- starting defragmentation" % proc_config.char_id)
                print "time %dms: Defragmentation complete (moved %d frames: %s)" % (self.time + result, result, ', '.join(['%s' % i for i in self.activeProcesses]))
        else:
            self.log("Cannot place process %s -- skipping process %s" % (proc_config.char_id, proc_config.char_id))
        print self.page_table
        
    def handle_removal(self, proc_config):
        self.log("Process %s removed from physical memory"
                % proc_config.char_id)
        self.page_table.remove_proc(proc_config)
        print self.page_table

    def log(self, line):
        'Print one line with time info'
        print "time %dms: " % self.time + line


    