Assignment 1: Abstract Syntax Tree Analysis

The Assignment is about creating a tool that can take any python file 
as input and then use a tool to convert the input python file 
into an IR Abstract Syntax Tree and then using this AST, print all the 
assignment statements, branch conditions and loop conditions.

To accomplish the task a tool ast2json is used that will convert the file
into ast, the AST represented is basically in the form of json data and we 
can traverse the whole tree by the traversing the json data.
To traverse the json file which has basically the whole tree in it.
Used the viasualization tool for the ast , understanding of json traversal 
and the official python ast doc https://docs.python.org/3/library/ast.html 
to accomplish the assignment. The traversal is somewhat similar to the dfs 
traversal of the graph or we can say a modification of that algorithm.
The tool is build such that it will use the new.py pyhton file as the input 
and will use the ast2json toll to dump the python file input into json format
(basically ast format ) and then separate functions will traverse the json file 
and print the corresponding requirements.

Steps to run:
1. To run this we need to be in ubuntu 20 environment because I have used the
   command 'python3 assign.py' in the run.sh file, the ast2json must be
    installed in your system to run this code.
2. Go to the folder that has the source folder that has two files one is the 
   tool and the other is the input python file.
3. run.sh file is also present in the source folder and also the base folder.
4. To simply run we can paste any test case file into the new.py file and the 
   use the terimnal to run the run.sh file as ./run.sh
5. The output will be displayed in the terminal itself. And the expected output file 
   is also present within the testcases folder. For instance, for the input file 
   testcase3.py the corresponding expected outfile is in file output3.txt and so on.
6. An important point to consider is that the run.sh file that is inside the source folder 
   that needs to get run with the new.py testcase file.
   
