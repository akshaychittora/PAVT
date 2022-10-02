Assignment 2: Constructing Control Flow Graphs

In this assignment we are constructing the CFG of the given 
code in the Turtle language. The cfg is build based on the IR 
created by the turtle language's code and we are using that IR 
to construct the cfg, basically the graph that will contains all 
the basic blocks and the links between them.

I used the usual algo to constrct the cfg, firstly marked all the
basic blocks' starting elements in the code. Then i have used 2 dict 
that will store the constructed cfg , the fist dict would contain the nodes
of the cfg at every index and the second dict would contain the link of the 
node of that index element in the first dict inside a dict, basically if the 
first node is connected to 2nd and 3rd the second dict would have the list 
conatining [2,3] and so on. And after the creation used the dot code to dump
that into a dot file.

The source code is inside the source folder the named submission.py and the 
respective test cases are inside the testcases folder. Graphviz tool is used 
to render the dot file and will show the output.