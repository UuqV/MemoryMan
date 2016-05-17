from PageRefStr import page_ref_list

class VirtualMemSim:
    
    def __init__(self, path):
        self.page_ref_list = page_ref_list(path)
        self.frame_size = 3
        self.frame_list = self.empty_frame_list()
        self.page_fault_count = 0

    def simulate(self):
        print "\nSimulating OPT with fixed frame size of %d" % self.frame_size
        for i in range(0, len(self.page_ref_list)):
            self.reference_page(i, "OPT")
        print "End of OPT simulation (%d page faults)" % self.page_fault_count
        self.frame_list = self.empty_frame_list()
        self.page_fault_count = 0

        print "\nSimulating LRU with fixed frame size of %d" % self.frame_size
        for i in range(0, len(self.page_ref_list)):
            self.reference_page(i, "LRU")
        print "End of LRU simulation (%d page faults)" % self.page_fault_count
        self.frame_list = self.empty_frame_list()
        self.page_fault_count = 0

        print "\nSimulating LFU with fixed frame size of %d" % self.frame_size
        for i in range(0, len(self.page_ref_list)):
            self.reference_page(i, "LFU")
        print "End of LFU simulation (%d page faults)" % self.page_fault_count

    def reference_page(self, index, algo):
        'Check for and handle page faults'
        if algo not in ("OPT", "LRU", "LFU"):
            return -1

        page_num = self.page_ref_list[index]
        page_fault = False
        if page_num not in self.frame_list:
            page_fault = True
            self.page_fault_count += 1

        # Page replacement scheme
        victim_page = None
        if page_fault:
            if '.' in self.frame_list:
                i = self.frame_list.index('.')
                self.frame_list[i] = page_num
            else:
                if algo == "OPT":
                    # The optimal algorithm
                    next_uses = []
                    for candidate in self.frame_list:
                        next_use = len(self.page_ref_list)
                        remaining_refs = self.page_ref_list[index:]
                        if candidate in remaining_refs:
                            next_use = remaining_refs.index(candidate)
                        next_uses.append(next_use)
                    victim_index =  next_uses.index(max(next_uses)) # Pick the page used farthest away
                    victim_page = self.frame_list[victim_index]
                    self.frame_list[victim_index] = page_num
                elif algo in "LRU":
                    # The last recently used algorithm
                    prev_uses = []
                    prev_refs = self.page_ref_list[:index]
                    if len(prev_refs) > 0:
                        prev_refs.reverse()
                    for candidate in self.frame_list:
                        prev_use = len(self.page_ref_list)
                        if candidate in prev_refs:
                            prev_use = prev_refs.index(candidate)
                        prev_uses.append(prev_use)
                    victim_index =  prev_uses.index(max(prev_uses)) # Pick the page least recently used
                    victim_page = self.frame_list[victim_index]
                    self.frame_list[victim_index] = page_num
                elif algo == "LFU":
                    # The least frequently used algorithm
                    prev_uses = []
                    prev_refs = self.page_ref_list[:index]
                    if len(prev_refs) > 0:
                        prev_refs.reverse()
                    for candidate in self.frame_list:
                        times_used = 0
                        for ref in prev_refs:
                            if ref == candidate:
                                times_used += 1
                        prev_uses.append(times_used)
                    victim_index =  prev_uses.index(min(prev_uses)) # Pick the page least recently used
                    victim_page = self.frame_list[victim_index]
                    self.frame_list[victim_index] = page_num


        log_line = "referencing page %d" % self.page_ref_list[index]
        log_line += " [mem:"
        for frame in self.frame_list:
            log_line += " " + str(frame)
        log_line += "]"
        if page_fault:
            log_line += " PAGE FAULT"
            if victim_page == None:
                log_line += " (no victim page)"
            else:
                log_line += " (victim page %d)" % victim_page

        print log_line

    def empty_frame_list(self):
        l = []
        for i in range(0, self.frame_size):
            l.append('.')
        return l
