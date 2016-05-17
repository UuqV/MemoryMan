class Memory:
    'Nick convinced me not to be lazy'
    slots = []
    numSlots = 256

    def __init__(self):
        for i in xrange(self.numSlots):
            self.slots.append('.')

    def __str__(self):
        outstring = str()
        outstring = outstring + '=' * 32 + '\n'
        for i in xrange(0, self.numSlots, 32):
            for j in xrange(0, 32):
                outstring = outstring + self.slots[i + j]
            outstring = outstring + '\n'
        outstring = outstring + '=' * 32
        return outstring
        
        
    def find_open_slot(self, pro_name, size_needed):
        i = 0
        while i < self.numSlots:
            if self.slots[i] == '.':
                j = i
                while self.slots[j] == '.':
                    j += 1
                    if (j - i) == size_needed:
                        self.slots[i:j] = pro_name
                        print j
                        return i
                        i = j
                i += 1
                print i
        return -1