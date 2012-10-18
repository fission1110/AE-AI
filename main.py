#!/usr/bin/env python
from evolve.evolve import obj
from random import randrange
from evolve.callbacks import define
import thread


def mainloop(input, expected_output, iterations = 10000, starting_code = '', stdout = False):
    """ The main loop """
    ai = obj()
    define(ai)
    ai.set(starting_code)
    for i in range(0,iterations):
        starting_string = input()
        target_string = expected_output()
        ai.set_memory(starting_string)
        ai.execute()
        if stdout and i%5000 == 0:
            print '---------------------------------------------------------------'
            print 'iteration number: ' + str(i)
            print 'champ instructions: ' + ai.champ_instructions
            print 'champ score: ' + str(ai.champ_score)
            print 'champ target: ' + target_string
            print 'champ input: ' + starting_string
            print 'champ current: ' + ai.champ_output

        ai.test(target_string)
        # once every 1000 iterations, revert the instructions to the champion
        if i %2000 == 0 and i>10:
            ai.instructions = ai.champ_instructions
    if stdout:
        print 'champ code: ' + ai.champ_instructions
    return ai

def input():
    return 'zyxwvutsrqponmlkjihgfedcba'
def expected_output():
    return 'abcdefghijklmnopqrstuvwxyz'
mainloop(input, expected_output, 10000000, '', True) 







#Multi threading!
#try:
#       thread.start_new_thread( mainloop, (input, expected_output, 10000, '', True) )
#       thread.start_new_thread( mainloop, (input, expected_output, 10000, '', True ) )
#except:
#       print "Error: unable to start thread"
#while 1:
#    pass

