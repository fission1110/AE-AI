A turing complete evolutionary AI
==========================

This is an evolutionary AI that writes code.
I have a brianfuck program contained in a string, it manipulates a memory buffer that is used as output. If it get's it right, it will spit out the brainfuck code, and all will be well with the world.
This works through the process of random mutaion, with non-random selection.

Currently it kind of sucks, and here's how I plan on making it better..

Make it so that there is multiple children for each object. Right now, the competion is only from parent->child. And to simulate multiple children, it remembers the champion, and switches back to that champion every 1000 iterations. With a pool of multiple children, you could just kill off the weekest, and give them a set ammount of resources. This requires that I have a methodology for comparing different objects, rather than just comparing children to parents.

Turn this into a library that you can feed in a dictionary of 'input':'expected output', and train it to do basically any task.

Make it so that the length of the program is not set, and that the longer they make the program, the lower the score they get.. Make it pull toward efficiency.

Create a way to save the program state to a file, so that you can save your results or execute this on a cluster of computers all with different environment variables.

Add more commands. Brain fuck may be turing complete but it isn't exactly effecient. 

>>>REQUIREMENTS
This requires the Levenshtein library for fuzzy string comparison. You can get it through your favorite packaging manager, or get the source at..
http://code.google.com/p/pylevenshtein/
