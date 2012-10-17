from random import randrange
from Levenshtein import ratio
import sys

class obj(object):
    """docstring for turing"""

    """ The container for all of the python function references """
    call_set = {}
    
    """ The pointer that points to the current place in self.memory """
    data_ptr = 0

    """ The instruction pointer points to any place in self.instructions """
    inst_ptr = 0

    """ This counter prevents infinite loops in execution while loop """
    total_executions = 0

    """ These variable store things for the champion """
    champ_score = 0
    champ_instructions = ''
    champ_memory = ''

    def execute(self):
        """ This loops through the instruction set, and executes the brainfuck primitives"""
        # reset all the pointers before execution
        self.total_executions = 0
        self.inst_ptr = 0
        self.data_ptr = 0
        # while the inst_ptr is withing range, and it hasn't gone through more than 1000 iterations.
        while self.inst_ptr < len(self.instructions) and self.total_executions < 1000:            #execute the instruction at the inst_ptr
            if self.call_set.has_key(self.instructions[self.inst_ptr]):
                self.call_set[self.instructions[self.inst_ptr]](self)
            #incriment the inst_ptr and the total exectuions counter
            self.inst_ptr = self.inst_ptr + 1
            self.total_executions = self.total_executions + 1

    def evolve(self, n):
        """ evolve n number of genes to something random """
        #TODO: make it so that it has the possibility to increase or decrease the length of the execution stack.
        self.prev_instructions = self.instructions
        for i in range(0,n):
            #pick a random letter to change
            letter_num = randrange(1,len(self.instructions)+1)
            #assign it to one of the letters in the call set
            self.instructions = self.instructions[0:letter_num-1] + self.call_set.keys()[randrange(0,len(self.call_set))] + self.instructions[letter_num:]

    def set(self, string):
        """ set the initial instructions, usually I set it to a string of 'a's """
        self.instructions = string

    def get(self):
        """ return the current instruction set """
        return self.instructions
    
    def define(self, letter, callback):
        """ define a char to a callback """
        self.call_set[letter] = callback

    def set_memory(self, string):
        """ set the initial memory. This is the input for the program. """
        self.memory = string
        self.prev_memory = string
        self.orig_memory = string
    
    def test(self, goal):
        """ Use fuzzy string comparison to test if it is better than it's parent """
        #if it reached its goal, kill the script.. I may want to take that part out, and give it something for efficiency
        if(self.memory == goal):
            print 'it worked!\r\n'
            print self.instructions
            sys.exit()
        # get the previous results, as well as these results
        #TODO: make it save the previoius results to the object, so that you 
        #can change the goal
        self.prev = ratio(self.prev_memory, goal)
        self.new = ratio(self.memory, goal)
        #if this beats the champions score, set it as the champ
        if self.new > self.champ_score:
            self.champ_score = self.new
            self.champ_instructions = self.instructions
            self.champ_memory = self.memory
        # if the previous won, set it to the previous instructions
        if self.prev > self.new:
            self.instructions = self.prev_instructions
        elif self.prev < self.new:
            #if the current one wins, give it privs
            self.instructions = self.instructions
        elif self.prev == self.new:
            """they both suck"""
            self.instructions = self.instructions
        #set some variables and evolve it
        self.prev_memory = self.memory
        self.memory = self.orig_memory
        self.evolve(1)
        return self.new
