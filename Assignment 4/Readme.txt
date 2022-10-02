Assignment 4: Coverage Guided Fuzzing

___Implementation___:
In this assignment we need to implement functions compareCoverage, updateTotalCoverage, 
mutate.
The comapreCoverage function it is basically to comapre the new coverage and the
previous coverage, in each iteration of the fuzzer loop it will check whether the coverage 
is improved or not after using the mutuated input and if it increases then it will add that
mutuated input to the corpus. To check the improvement, both lists are compared and True is
returned if the something new is there in the new_coverage matric than the previous and False
if not.

The updateTotalCoverage function is basically updating the total coverage metric that we have 
so far, if the coverage is improving it will get added to the total_metric that stores the all
covered lines so far in the IR , and it will return the updated matric.

The mutuate function is basically to get mutuate the input that we have used previously and it
will apply some tranformation on the input and return the new one. In my approach i have used 
the technique called Walking bit flips,in this method of mutuating inputs involves performing 
sequential, ordered bit flips. The number of bits flipped in a row varies from one to four.
Used the random function to get the number of bits to be flipped and then to get the postions 
to flip and finally iterate over all the inputs in this way and get the mutuated input and 
return it.


___Assumptions___:
I have assumed that the mutation method that i have used will work for every code it takes but
it is not very accurate assumption as there might be some input that it will not be able to 
generate considering the randomized behaviour of the function.


____Running the code____:
The source folder has the KachuaV_2.3 version that i have used for this assignment
the submission folder has the submission.py file that has all the implmented code
and to run it we can go to KachuaCore folder we can run the fuzzer using 
./kachua.py -t 20 --fuzz example/testcase1.tl -d '{":x": 5, ":y": 100}'
for testcase1 and so on..
The testcases folder contains all the testcases and the corresponding output files
and also all the tescases files are also present in the example folder of the Kachua
Core.
Here are the codes i used to run the testcases (in windows command prompt)
>python kachua.py -t 50 --fuzz example/testcase1.tl -d "{':x':100,':y':50}"
>python kachua.py -t 100 --fuzz example/testcase2.tl -d "{'move':20}"
>python kachua.py -t 50 --fuzz example/testcase3.tl -d "{'move':5}"
>python kachua.py -t 50 --fuzz example/testcase4.tl -d "{'x':5,'z':10,'w':15}"
>python kachua.py -t 50 --fuzz example/testcase5.tl -d "{':vara':20,':varb':30}"
 

