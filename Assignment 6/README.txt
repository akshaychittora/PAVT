Assignment-6B: Spectrum Based Fault Localization

In this assignment, we will explore Spectrum-based Fault Localization (SBFL) to 
identify buggy line/lines in a program in a regression testing scenario. Given
two programs, one was written by a team of developers which is correct and the 
another program is buggy, we need to find out the ranks for each component 
finding out its suspiciousness to be buggy.


Implementation:
To find the buggy component we use the SBFL freamework in Kachua, the SFBL
generates a test-suite using evolutionary search-based test-suite generation
framework. The test-suite is decided on a fitness function which is to be 
implemented. 

Fitness score function- I used the Ulysis: Multiverse Analysis, Ulysis computes 
the average worst-case wasted effort over all imaginary universe (multiverse), 
basically it assumes that a particular componenet is buggy and takes find out 
the worst case wasted effort for that component, and then find out the average 
for all components that gives a fitness score for that Test case (activity matrix).
The framework also gives out a error vector that will say whether the corresponding
test set fails or not,he SBFL framework will utilize your metric to compute the
suspiciousness score of each program component and rank them in order of their 
suspiciousness. Observe the rank of the buggy component in the ranked list. The
Closer it is to the top, the better is your fitness function and fault-localization
metric.

Suspiciousness function- Used the Ochiai score for the component to find out its
sucpiciousness score, the more the Ochiai score the more the suspiciousness, 
to find out the suspiciousness score we can take a component, then find the 
sqaureroot of the multiplication of the fraction that in what failing tests,
is that component executed and in what fraction of test where that coponent is
executed, the tests failed. Finding out this using the the parameters compnent 
index and the error vector of that test suite.

Getranklist function- this function will return the rank list of the coponents used
in the test suit, the fucntion will call the suspiciousness score of every component
and the rank them all according to the score.


 
How to run:

Version Used: v5.3
I Run the code in windows cmd.

to run the SBFL framework- 
python kachua.py --SBFL ./example/testcase5/sbfl1.tl --buggy ./example/testcase5/sbfl1_buggy.tl -vars "[':x']" --timeout 10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True
Arguments-
--buggy : Buggy turtle program.
-vars : Input variables to the program. if program does not have any input variable, pass -vars '[]'.
 --timeout :Time budget for to run each test cases.
--ntests : Intitial test-suite size.
genetic algorithm parameters:
--popsize : Population size.
--cxpb : Cross-over probability.
--mutpb : Mutation probability.
--ngen : Number of times GA to iterate.
--verbose : To show GA output to console


Assumptions:

I used the Ulysis score as the best possible fitness function for the codes another 
method can be used such as DDU but overall the percentage decrease in effort is more using
Ulysis than DDU.


