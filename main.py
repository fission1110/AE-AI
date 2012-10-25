#!/usr/bin/env python
from evolve.evolve import obj
from random import randrange
from evolve.callbacks import define
import thread


def mainloop(input, expected_output, iterations = 10000, starting_code = '', stdout = False):
    """ The main loop """
    #spawn the ai object
    ai = obj()
    #set all the callbacks for the ai
    define(ai)
    #set the default code
    ai.set(starting_code)
    for i in range(0,iterations):
        #setup the code input
        starting_string = input(ai)
        #setup the code output
        target_string = expected_output(ai)
        #set the code input
        ai.set_memory(starting_string)
        #execute the code
        ai.execute()
        #write it to stdout ever 1000 times.
        if stdout and i%1000 == 0:
            print '---------------------------------------------------------------'
            print 'iteration number: ' + str(i)
            print 'champ instructions: ' + ai.champ_instructions
            print 'champ score: ' + str(ai.champ_score)
            print 'champ target: ' + target_string
            print 'champ input: ' + starting_string
            print 'champ current: ' + ai.champ_output

        #run the test routine..
        ai.test(target_string)
        # once every 1000 iterations, revert the instructions to the champion
        #this is to simulate multiple ai's running at once
        if i %2000 == 0 and i>10:
            ai.instructions = ai.champ_instructions
    if stdout:
        print 'champ code: ' + ai.champ_instructions
    return ai

def input(object):
    return "aaaaaaaaaaaaaaaaaaaaaa"
def expected_output(object):
    return "ZZZZZZZZZZZZZZZZZZZZZZ"

mainloop(input, expected_output, 10000000, '[.]', True) 







#Multi threading!
#try:
#       thread.start_new_thread( mainloop, (input, expected_output, 10000, '', True) )
#       thread.start_new_thread( mainloop, (input, expected_output, 10000, '', True ) )
#except:
#       print "Error: unable to start thread"
#while 1:
#    pass

