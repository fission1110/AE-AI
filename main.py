from evolve.evolve import obj
from random import randrange
from evolve.callbacks import define
import thread


def mainloop(input, expected_output, iterations = 10000, bf_starting_code = ''):
    """ The main loop """
    ai = obj()
    define(ai)
    ai.set(bf_starting_code)
    for i in range(0,iterations):
        ai.set_memory(input)
        ai.execute()

        ai.test(expected_output)
        # once every 1000 iterations, revert the instructions to the champion
        if i %2000 == 0 and i>10:
            ai.instructions = ai.champ_instructions
    print ai.champ_score
    return ai
try:
       thread.start_new_thread( mainloop, ("aaaaaa", 'bbbbb' ) )
       thread.start_new_thread( mainloop, ("aaaaaa", 'bbbbb' ) )
except:
       print "Error: unable to start thread"
while 1:
    pass

