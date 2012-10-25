Ae-Ai - Adaptable Evolutionary Artificial Intelligence
==========================

Ae-Ai (Pronounced Aye Eye) is a turing complete artificial intelligence program.

Basically it's code, that randomly creates new code, and tests the output. Evolving to accomplish almost any task.

Here's how it works.
=========

It has a list of simple primitive instructions that are contained in a string. The evolutionary object loops through this string and executes the instructions.
There is a stack, an output buffer, and an execution stack. 
After the instructions are executed, the evolutionary object then checks itself for fitness, compares itself to its parent, and if it is more fit(which is determined by the levenshtein fuzzy string comparison) then it is then set as the new default instructions, which evolve. If it is beat by its parent, it then dies, and everything is reset to that parent.
It also has a 'Champion', which is the most fit algorithm so far. Every once in a while, it is reset to the champion, simulating multiple competing algorithms.


Here are the plans for the future!
=========

>Callback based inputs and expected outputs for dynamic challenges!:
Right now, it can't handle this. There are a few changes in the testing algorithm that need to be made. Making the champions settings get tested every-time.

>Multiple objects:
Many different competing algorithms.

>Mating:
Objects should be able to mate with each other. I need to find a sufficient string merging algorithm(or write one) that will prove to be advantageous.

>Speciation:
Once 2 instruction sets become too different, don't allow them to mate. Simulating speciation which will allow complete independent algorithms in the same gene pool.

>Multi-threading:
Multiple threads, each running an algorithm asynchronously

>Network support:
Multiple computers can be running independently via a hive model. The main server would then check for fitness of each bee in the hive, and decided champions.

>Easily adjustable environment variables:
Make it so that the world can be adjusted easily, maybe through a simple configuration file.




>REQUIREMENTS
=========
This requires the Levenshtein library for fuzzy string comparison. You can get it through your favorite packaging manager, or get the source at..
http://code.google.com/p/pylevenshtein/