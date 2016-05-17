from ProcConfig import *
import time

class PageTable:

    """
    A page table of configurable size that maps
    process memory blocks into physical memory
    """

    def __init__(self, size):
        'Create page table with size slots'
        self.size = size
        self.table = self.blank_table()
        self.free = size
        self.next = 0

    def add_first_proc(self, proc_config):
        'Put a proc into memory using first-fit'
        units = proc_config.mem_size
        units_needed = proc_config.mem_size
        self.free = self.free - units_needed
        i = 0
        for i in range(0, self.size):
            if units_needed == 0:
                break
            if self.table[i] == '.':
                units_needed -= 1
            else:
                units_needed = proc_config.mem_size
        if units_needed == 0:
            for j in range(i - units, i):
                self.table[j] = proc_config.char_id
            return -1
        else:
            left = self.defragment()
            self.add_first_proc(proc_config)
            return left
            
    def add_next_proc(self, proc_config):
        'Put a proc into memory using first-fit'
        units = proc_config.mem_size
        units_needed = proc_config.mem_size
        self.free = self.free - units_needed
        i = 0
        for i in range(self.next, self.size):
            if self.next == self.size:
                self.next = 0
                i = 0
            if units_needed == 0:
                break
            if self.table[i] == '.':
                units_needed -= 1
            else:
                units_needed = proc_config.mem_size
        if units_needed == 0:
            for j in range(i - units, i):
                self.table[j] = proc_config.char_id
            self.next = i
            return -1
        else:
            left = self.defragment()
            self.add_next_proc(proc_config)
            return left
            
    def add_best_proc(self, proc_config):
        'Put a proc into memory using first-fit'
        units = proc_config.mem_size
        units_needed = proc_config.mem_size
        self.free = self.free - units_needed
        i = -1
        best = 0
        bestSize = 0
        for i in range(0, self.size):
            if units_needed == 0:
                k = i
                size = 0
                while k < self.size and self.table[k] == '.':
                    k += 1
                    size += 1
                if size > bestSize:
                    bestSize = size
                    best = i
                units_needed = units
            if self.table[i] == '.':
                units_needed -= 1
            else:
                units_needed = units
        if i != -1:
            for j in range(best - units, best):
                self.table[j] = proc_config.char_id
            return -1
        else:
            left = self.defragment()
            self.add_best_proc(proc_config)
            return left
            
    def remove_proc(self, proc_config):
        'Remove all of a procs memory cells'
        for i in range(0, self.size):
            if self.table[i] == proc_config.char_id:
                self.table[i] = '.'
        self.free = self.free + proc_config.mem_size

    def blank_table(self):
        'Create dict mapping 0 ... size-1 to chars'
        dic = []
        for i in range(0, self.size):
            dic.append('.')
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
        
    def defragment(self):
        newTable = self.blank_table()
        newIndex = 0
        for i in range(0, self.size):
            if self.table[i] != '.':
                newTable[newIndex] = self.table[i]
                newIndex += 1
        self.table = newTable
        self.next = newIndex
        return newIndex
        
        
