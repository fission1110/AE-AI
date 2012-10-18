from random import randrange
from Levenshtein import ratio

class obj(object):
    """docstring for turing"""

    output = ''
    orig_output = ''
    prev = 0
    """ The container for all of the python function references """
    call_set = {}
    
    """ The pointer that points to the current place in self.output """
    data_ptr = 0

    """ The instruction pointer points to any place in self.instructions """
    inst_ptr = 0

    """ This counter prevents infinite loops in execution while loop """
    total_executions = 0

    """ These variable store things for the champion """
    champ_score = -10
    champ_instructions = ''
    champ_output = ''

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
        self.prev_instructions = self.instructions
        #Decide whether or not to add/delete n genes, or modify previous genes
        for i in range(0,n):
            coin = randrange(0,2)
            #pick a gene to manipulate
            gene = randrange(0,len(self.instructions)+1)
            if coin == 0:
                #assign it to one of the letters in the call set
                self.instructions = self.instructions[0:gene-1] + self.call_set.keys()[randrange(0,len(self.call_set))] + self.instructions[gene:]
            elif coin == 1:
                #flip another coin to decide if you should add or subtract a char
                coin2 = randrange(0,2)
                if coin2 == 0 and len(self.instructions) > 1:
                    #delete the char
                    self.instructions = self.instructions[0:gene-1] + self.instructions[gene:]
                elif coin2 == 1:
                    #add a new char
                    coin3 = randrange(0,len(self.instructions)+1) #begining, end, middle
                    newchar = self.call_set.keys()[randrange(0,len(self.call_set))]
                    if coin3 == 0:
                        self.instructions = newchar + self.instructions
                    if coin3 == 1:
                        self.instructions = self.instructions + newchar 
                    if coin3>1:
                        self.instructions = self.instructions[0:gene-1] + self.instructions[gene:]



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
        # get the previous results, as well as these results
        self.prev_instructions = self.instructions
        #handicap it .000001 for every letter in the code
        handicap = len(self.instructions) * .00000001 
        self.new = (ratio(self.output, goal)**2)- handicap #square the score to put a big emphasis on getting things right
        # score! it worked.
        if(self.output == goal):
            print 'it worked!\r\n'
            # give it a boost in terms of score
            # The reason for doing this, is you never want a success to be beaten by a
            # shorter algorithm that was unsuccessful. The handicap can mess things up.
            self.new = self.new + 10
            print self.instructions
            #import sys
            #sys.exit()
        #if this beats the champions score, set it as the champ
        if self.new > self.champ_score:
            self.champ_score = self.new
            self.champ_instructions = self.instructions
            self.champ_output = self.output
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
        self.prev_output = self.output
        self.memory = self.orig_memory
        self.output = ''
        self.prev = self.new
        #set the evolve rate randomly
        evolve_number = randrange(1,3)
        self.evolve(1)
        return self.new
