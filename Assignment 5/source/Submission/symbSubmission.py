from z3 import *
import argparse
import json
import sys
sys.path.insert(0, '../KachuaCore/')
from sExecutionInterface import *
from sExecution import *
import z3solver as zs
from irgen import *
from interpreter import *
import ast

def example(s):
    # To add symbolic variable x to solver
    s.addSymbVar('x')
    s.addSymbVar('y')
    # To add constraint in form of string
    s.addConstraint('x==5+y')
    s.addConstraint('And(x==y,x>5)')
    # s.addConstraint('Implies(x==4,y==x+8')
    # To access solvers directly use s.s.<function of z3>()
    print("constraints added till now",s.s.assertions())
    # To assign z=x+y
    s.addAssignment('z','x+y')
    # To get any variable assigned
    print("variable assignment of z =",s.getVar('z'))

def checkEq(args,ir):

    file1 = open("../Submission/testData.json","r+")
    testData1=json.loads(file1.read())
    file1.close()
    s = zs.z3Solver()
    testData1 = convertTestData(testData1)
    #print(testData)
    output = args.output
    # example(s)
    # TODO: write code to check equivalence
    print(output)
    ou={}
    for i in testData1["1"]["params"]:
        if(i in output):
            new= ":"+i
            ou[new]=testData1["1"]["params"][i]
        
    symbolicExecutionMain(ir,ou,{},100)
    file2 = open("../Submission/testData.json","r+")
    testdata2=json.loads(file2.read())
    file2.close()
    s = zs.z3Solver()
    testdata2 = convertTestData(testdata2)
    for i in testData1["1"]["params"]:
        s.addSymbVar(i)
    s1= zs.z3Solver()
    for i in testdata2:
        #print("hi")
        f= testdata2[i]
        k= f["params"]
        for l in k:
            s1.addAssignment(l,k[l])
        for j in testData1:    
            p=testData1[j]["constraints"][0]
            p=p.split(',')
            for e in p:
                s1.addConstraint(e)
            if(str(s1.s.check())=='sat'):
                for u in output:
                    eq= ""
                    eq+=f["symbEnc"][u]+"=="+testData1[j]["symbEnc"][u]
                    s.addConstraint(eq)
                    #print(eq)
            s1.s.reset()
        
    s2=zs.z3Solver()
    for i in testData1:
        #print("hi2")
        f= testData1[i]
        k= f["params"]
        for l in output:
            s2.addAssignment(l,k[l])
        for j in testdata2:
            p=testdata2[j]["constraints"][0]
            p=p.split(',')
            for e in p:
                s2.addConstraint(e)
            if(str(s2.s.check())=='sat'):
                for u in output:
                    eq= ""
                    eq+=f["symbEnc"][u]+"=="+testdata2[j]["symbEnc"][u]
                    s.addConstraint(eq)
                    #print(eq)
            s2.s.reset()

    
    if(str(s.s.check())=='sat'):
        print(s.s.model())
    else:
        print("The programs cannot equated sementically")
        

    
if __name__ == '__main__':
    cmdparser = argparse.ArgumentParser(
        description='symbSubmission for assignment Program Synthesis using Symbolic Execution')
    cmdparser.add_argument('progfl')
    cmdparser.add_argument(
        '-b', '--bin', action='store_true', help='load binary IR')
    cmdparser.add_argument(
        '-e', '--output', default=list(), type=ast.literal_eval,
                               help="pass variables to kachua program in python dictionary format")
    args = cmdparser.parse_args()
    ir = loadIR(args.progfl)
    checkEq(args,ir)
    exit()
