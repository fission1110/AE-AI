from evolve import obj
evolve = obj()

evolve.set_memory('''<string>$10.25</string>''')
evolve.set('')
def define_vars():
    """A simple declaration of the brainfuck primitives.. I chose the brainfuck primitives because it's a really simple instruction set, but is also turing complete"""
    def x(self):
        """ Incriment the point in memory at the data pointer by one"""
        output = ''
        #location to modify
        loc = self.data_ptr % len(self.memory)
        output = self.memory[:loc] + chr((ord(self.memory[loc])+1)%256) + self.memory[loc+1:]
        self.memory = output
    evolve.define('+', x)

    def x(self):
        """ Decriment the point in memory at the data pointer by one"""
        output = ''
        #location to modify
        loc = self.data_ptr % len(self.memory)
        output = self.memory[:loc] + chr(abs(ord(self.memory[loc])-1)) + self.memory[loc+1:]
        self.memory = output
    evolve.define('-', x)

    def x(self):
        """ Incriment the data pointer by one """
        self.data_ptr = (self.data_ptr + 1) % len(self.memory)
    evolve.define('>', x)

    def x(self):
        """ Decriment the data pointer by one """
        if self.data_ptr > 1:
            self.data_ptr = self.data_ptr-1
    evolve.define('<', x)

    def x(self):
        """ If the value at the data ptr is 'a', jump to the next instance of ']' """
        if self.memory[self.data_ptr] == '0':
            if self.instructions.find(']', self.inst_ptr) != -1:
                self.inst_ptr = self.instructions.find(']', self.inst_ptr) + 1
    evolve.define('[', x)
    def x(self):
        """  If the value at the data ptr is not 'a', jump to the previous instance of '['  """
        #print self.data_ptr
        if self.memory[self.data_ptr] != '0':
            if self.instructions.rfind('[', 0, self.inst_ptr) != -1:
                self.inst_ptr = self.instructions.rfind('[',0 , self.inst_ptr) + 1
    evolve.define(']', x)
    def x(self):
        """  """
        self.output += self.memory[self.data_ptr]
    evolve.define('.', x)

define_vars()

""" The main loop """
for i in range(0,1000000):
    print 'generation :' + str(i)
    evolve.execute()

    evolve.test('$10.25')
    print str(evolve.champ_score) + ',' + str(evolve.prev) +',' + str(evolve.new) 
    print evolve.champ_instructions
    print evolve.champ_output 
    # once every 1000 iterations, revert the instructions to the champion
    if i %2000 == 0 and i>10:
        evolve.instructions = evolve.champ_instructions
    """
    for char in evolve.memory:
        print hex(ord(char))
    """
print '---------------- Champion! ------------------'
print evolve.champ_instructions
print evolve.champ_score
print evolve.champ_output   
