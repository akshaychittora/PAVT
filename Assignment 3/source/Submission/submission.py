
import sys
sys.path.insert(0, "KachuaCore/interfaces/")
from interfaces.fuzzerInterface import *
from kast import kachuaAST
from irgen import * 

# make sure dot or xdot works and grapviz is installed.

# Uncomment for Assignment-2
# sys.path.append("KachuaCore/kast")
# import kast.kachuaAST
# import graphviz

class CustomCoverageMetric(CoverageMetricBase):
    # Statements covered is used for 
    # coverage information.
    def __init__(self):
        super().__init__()

    # TODO : Implement this
    def compareCoverage(self, curr_metric, total_metric):
        # must compare curr_metric and total_metric
        # True if Improved Coverage else False
        return False

class CustomMutator(MutatorBase):
    def __init__(self):
        pass

    # TODO : Implement this
    def mutate(self, input_data):
        # Mutate the input data and return it
        # input_data.data -> type dict() with {key : variable(str), value : int}
        # must return input_data after mutation.
        return input_data

# Reuse code and imports from 
# earlier submissions (if any).
def genCFG(ir):
    # your code here
    cfg = None
    return cfg

def dumpCFG(cfg):
    # dump CFG to a dot file
    pass

def optimize(ir):
    # create optimized ir in ir2
    ir2 = ir # currently no oprimization is enabled
        # create optimized ir in ir2
    ir2 = ir # currently no optimization is enabled

    
    new_cfg=[]
    for id, item in enumerate(ir):
        temp_list=[]
        for i in range(len(ir)):
            if(id != i):
                item2=ir[i][1]
                if(ir[i][1]>1 and str(ir[i][0])=='False'):
                    if(item2+i== id ):
                        temp_list.append(i)
                
                elif(ir[i][1]>1):
                    if(item2+i== id or i+1== id):
                        temp_list.append(i)
                else:
                    if(i+ item2== id):
                        temp_list.append(i)
        new_cfg.append(temp_list)
        
    
    
    mark=[]
    for i in range(len(ir)):
        if(type(ir[i][0])==kachuaAST.MoveCommand):
            mark.append(1)
        else:
            mark.append(0)
    #last_node
    mark.append(0)
    
    
    in_out=[]
    for i in range(len(ir)+1):
        temp=[0,0]
        in_out.append(temp)
        
    #last_node
    def transfer(i):        
        if(ir[i][1]>1):
            x= ir[i][1]+i
            y= i+1
            value= in_out[x][0] * in_out[y][0]
        else:
            x= ir[i][1]+i
            value= in_out[x][0]
        kill=0
        in_my = mark[i] or (value)
        if(str(ir[i][0])=='pendown'):
            in_my= 0
            
        
        
        in_out[i][0]=in_my
        in_out[i][1]= value
    def copi(x):
        y=[]
        for i in x:
            temp_list=[]
            for j in range(len(i)):
                temp_list.append(i[j])
            y.append(temp_list)
        return y
    
    def copi_ir(x):
        y=[]
        for i in x:
            for j in range(len(i)):
                a= i[j][0]
                b=i[j][1]
                xt=(a,b)
            y.append(xt)
        return y
            
    
    
    pre= copi(in_out)
    for i in range(len(ir)-1,0,-1):
        transfer(i)
    while(sorted(pre) != sorted(in_out)):
        
        pre= copi(in_out)
        for i in range(len(ir)):
            transfer(i)
       
    
    ir2= ir
    
    flag=0
    i=0
    while(i<len(ir)):
        out= in_out[i][1]
        to_change= mark[i]    
        if(out ==1 and to_change==1 and flag==0):
            t=ir[i][0].expr

            removeInstruction(ir2,i)
            addInstruction(ir2,kachuaAST.AssignmentCommand(kachuaAST.Var(":t"), t),i)
            in_out.insert(i,[0,0])
            mark.insert(i,0)
            i+=2
            
            flag= 1 
            
            
        elif(out==1 and to_change==1 and flag==1):
            t1=ir[i][0].expr
            removeInstruction(ir2,i) 
            addInstruction(ir2,kachuaAST.AssignmentCommand(kachuaAST.Var(":t"), kachuaAST.BinArithOp(kachuaAST.Var("t"),t1,'+ ')),i)
            in_out.insert(i,[0,0])
            mark.insert(i,0)
            i+=2
            
            

        elif(out==0 and to_change==1 and flag==1):
            
            t1=ir[i][0].expr
            t2= ir[i][0].direction
            removeInstruction(ir2,i)
            expr1= kachuaAST.BinArithOp(kachuaAST.Var("t"), t1,'+')
            
            addInstruction(ir2, kachuaAST.MoveCommand(t2,expr1),i)
            in_out.insert(i,[0,0])
            mark.insert(i,0)
            i+=2
            
            flag=0
            
            
        i+=1
        
    for id, item in enumerate(ir2):
        print(str(id) + " "+ str(item[0]) + "  ["+ str(item[1])+"]")
            
          
    return ir2
