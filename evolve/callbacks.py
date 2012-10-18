
def define(object):
    """A simple declaration of the brainfuck primitives.. I chose the brainfuck primitives because it's a really simple instruction set, but is also turing complete"""
    def x(self):
        """ Incriment the point in memory at the data pointer by one"""
        output = ''
        #location to modify
        loc = self.data_ptr % len(self.memory)
        output = self.memory[:loc] + chr((ord(self.memory[loc])+1)%256) + self.memory[loc+1:]
        self.memory = output
    object.define('+', x)

    def x(self):
        """ Decriment the point in memory at the data pointer by one"""
        output = ''
        #location to modify
        loc = self.data_ptr % len(self.memory)
        output = self.memory[:loc] + chr(abs(ord(self.memory[loc])-1)) + self.memory[loc+1:]
        self.memory = output
    object.define('-', x)

    def x(self):
        """ Incriment the data pointer by one """
        self.data_ptr = (self.data_ptr + 1) % len(self.memory)
    object.define('>', x)

    def x(self):
        """ Decriment the data pointer by one """
        if self.data_ptr > 1:
            self.data_ptr = self.data_ptr-1
    object.define('<', x)

    def x(self):
        """ If the value at the data ptr is '0', jump to the next instance of ']' """
        if self.memory[self.data_ptr] == '0':
            if self.instructions.find(']', self.inst_ptr) != -1:
                self.inst_ptr = self.instructions.find(']', self.inst_ptr) + 1
    object.define('[', x)
    def x(self):
        """  If the value at the data ptr is not '0', jump to the previous instance of '['  """
        #print self.data_ptr
        if self.memory[self.data_ptr] != '0':
            if self.instructions.rfind('[', 0, self.inst_ptr) != -1:
                self.inst_ptr = self.instructions.rfind('[',0 , self.inst_ptr) + 1
    object.define(']', x)
    def x(self):
        """  """
        self.output += self.memory[self.data_ptr]
    object.define('.', x)
    #not sure if this is a good idea, currently it breaks things because there are 9 numbers, which out numbers the rest of the instructions.
    #for now, i'm just going to include a 0, that way evolution has some stable context to base it's jumps for example.
    #for n in range(0,10):
    #    """ Numbers 0-9 are used to set the char cell at the data pointer to their respective values """
    #    def x(self):
    #        self.memory = self.memory[:self.data_ptr] + str(n) + self.memory[self.data_ptr:]
    #    object.define(str(n), x)
    def x(self):
        self.memory = self.memory[:self.data_ptr] + str(0) + self.memory[self.data_ptr:]
    object.define(str(0), x)
