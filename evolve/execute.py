class execute(object):
    """
    This is an execution class. 
    All it does is execute code that has been given to it.
    It works prettymuch the same as the evolve class, exept
    rather than defining all the callbacks, you pass it the
    define function, and it will apply it to itself.
    """
    call_set = {}
    stack = []
    stack_len = 100
    output = ''
    data_ptr = 0
    inst_ptr = 0
    total_executions = 0
    def __init__(self, input, output, code, define):
        define(self)
        self.memory = input
    def execute(self):
        """docstring for execute"""
        # reset all the pointers before execution
        self.total_executions = 0
        self.inst_ptr = 0
        self.data_ptr = 0
        # while the inst_ptr is withing range, and it hasn't gone through more than 1000 iterations.
        while self.inst_ptr < len(self.instructions) and self.total_executions < 2000:            #execute the instruction at the inst_ptr
            if self.call_set.has_key(self.instructions[self.inst_ptr]):
                self.call_set[self.instructions[self.inst_ptr]](self)
            #incriment the inst_ptr and the total exectuions counter
            self.inst_ptr = self.inst_ptr + 1
            self.total_executions = self.total_executions + 1

    def define(self, letter, callback):
        """docstring for define"""
        self.call_set[letter]= callback
