from evolve.evolve import obj
from random import randrange
from evolve.callbacks import define

ai = obj()
define(ai)
ai.set('')

""" The main loop """
for i in range(0,10000):
    #number = str(randrange(0,99))+'.'+str(randrange(0,99))
    number = '10.10'
    ai.set_memory('abdffsb')
    print 'generation :' + str(i)
    ai.execute()

    ai.test('helloworld')
    #print str(ai.champ_score) + ',' + str(ai.prev) +',' + str(ai.new) 
    #print ai.champ_instructions
    #print ai.champ_output 
    # once every 1000 iterations, revert the instructions to the champion
    if i %2000 == 0 and i>10:
        ai.instructions = ai.champ_instructions
    """
    for char in ai.memory:
        print hex(ord(char))
    """
print '---------------- Champion! ------------------'
print ai.champ_instructions
print ai.champ_score
print ai.champ_output   
