Assignment 3: Kachua Movement Optimization
In this assignment i used that ir which the code was producing the analyzed and 
updated the movents of the Kachua as it was moving.
The folder contains 3 subfolders and the source folder has the Kachua-v2.0.5 folder
which has the Kachua version that is being used to do the assignment.
The movents were optimized using dataflow analysis techniques, the movents which can
be optimized are remove and added new code in the IR. Running the code using -O will 
give the optmized IR too
Limitations: The initial code that needs to be optmised cannot have right and left
movements, no nested loops, no backward movements backward can be done using forward
-x, and initially if there are movements inside the loop we can begin with the forward 0
statement.
The submission.py file has the optimize ir function it can be using:
./kachua.py -O example/testcase1.tl  -for optmized IR
All testcases and respective outputs are also there in the example folder 
of the Kachua and also inside the testcases folder.