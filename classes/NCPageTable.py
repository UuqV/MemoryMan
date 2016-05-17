from ProcConfig import *

class PageTable:

    """
    A page table of configurable size that maps
    process memory blocks into physical memory
    """

    def __init__(self, size):
        'Create page table with size slots'
        self.size = size
        self.table = self.blank_table()

    def count_free(self):
        free = 0
        for i in range (0, self.size):
            if self.table[i] == '.':
                free += 1
        return free

    def add_proc(self, proc_config):
        'Put a proc into memory using first-fit'
        units_needed = proc_config.mem_size
        for i in range(0, self.size):
            if units_needed == 0:
                break
            if self.table[i] != '.':
                continue
            self.table[i] = proc_config.char_id
            units_needed -= 1

    def remove_proc(self, proc_config):
        'Remove all of a procs memory cells'
        for i in range(0, self.size):
            if self.table[i] == proc_config.char_id:
                self.table[i] = '.'

    def blank_table(self):
        'Create dict mapping 0 ... size-1 to chars'
        dic = {}
        for i in range(0, self.size):
            dic[i] = '.'
        return dic

    def __str__(self):
        'Human readable output with 32 columns'
        s = '='*32+"\n"
        for i in range(0, self.size):
            s += self.table[i]
            if i % 32 == 31:
                s += '\n'
        s += '='*32
        return s
