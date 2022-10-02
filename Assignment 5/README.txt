Assignment-5: Program Synthesis using Symbolic Execution

In this assignment we have been given two programs P1 and P2 and we have to find
the constant assignments to variables in P1 such that ir becomes semantically 
equivalent to P2.

Implementation:
To find out the values of constants we used the z3 solver to solve the equations 
and to generate the equations we apply the symbolic execution on the programs.
In my approach i first apply the symbolic execution on the first program that has
the constants in it which are need to solved, the symbolic execution will create the
json file names testData.json containing the output of the symbolic execution, 
the params, constraints, path coverage, symbolicEncodings, etc for all the paths
possible for the programs. Then did the same thing with the second program program 2
and stored the json data for both. Next applied 2 nested loops first for each path
of program i and the second for each path of program j, in each iteration i am
checking if the x and y value for that iteration is statisfying the constraints 
defined for that path in the other program or not if yes then i am adding the symbolic
encodings of both x and y from both program to a global z3 solver, a local solver is
also used to check the former(if the x and y values used in program i is statisfying 
the constaints used in program j for that iteration or not). This check is done for 
each path of program i with each path of program j and also in reverse order too.
In this way the global z3 solver collects all the equations possible to solve the 
unknown constants. And finally the z3 solver outputs the constants values.


How to run:

Version Used: v3.6
I Run the code in windows cmd.

First symbolic execution on program 1-
python kachua.py -t 100 -se example/eqtest1.tl -d "{':x': 5, ':y': 100}" -c "{':c1': 1, ':c2': 1}"

then to create the .kw file out of program 2 i used the below code-
python kachua.py -O example/eqtest2.tl 

then to call the main symbSubmission.py file used below-
python3 C:\Users\Hp\Desktop\pavt_assgn_sem_I\Kachua-v3.6\submission\symbSubmission.py -b optimized.kw -e "['x','y']"

Assumptions:

I write the above code considering only the first testcase values, to run with different
testcase, modified commands are to be used.
The second program will have no constant variables.

