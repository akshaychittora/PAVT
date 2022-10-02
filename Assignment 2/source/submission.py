
import sys
sys.path.insert(0, './ast')

import kachuaAST
import graphviz


def genCFG(ir):
    #for idx, item in enumerate(ir):
        #print( item[0] , ' ', item[1] )
    points=[]
    points.append(0)
    print(ir)
    for id, item in enumerate(ir):
        if(item[1]>1):
            
            points.append(id+1)
            points.append(id+item[1])
            
        elif(item[1]<1):
            points.append(id+1)
            points.append(id+item[1])
        
    points = sorted(set(points))
    #print(points)
    
    
    cfg1={}
    cfg2={}
    cfg1[0]="Start"
    cfg2[0]=[1]
    for i in range(len(points)-1):
        c=[]
        str1=""
        for j in range(points[i],points[i+1]):
            if(str(ir[j][0])!='False'):
                c.append(str(ir[j][0]))
        str1 = "\n".join(c)
        d=[]
        d.append(i+1+1)
        for k in range(points[i],points[i+1]):
            if(int(ir[k][1])!=1):
                d.append(1+points.index(k+int(ir[k][1])))
        cfg1[i+1]=str1
        cfg2[i+1]=d
    cfg1[len(points)]='End'
    cfg= [cfg1,cfg2] 
    #print(cfg2)
    
    return cfg

def dumpCFG(cfg):
    # dump CFG to a dot file
    dot = graphviz.Digraph(comment='CFG')
    dot  #doctest: +ELLIPSIS  
    cfg1={}
    cfg2={}
    
    cfg1=cfg[0]
    cfg2=cfg[1]
    for i in cfg1:
        dot.node(str(i),cfg1[i])
        
    for i in cfg2:
        for j in cfg2[i]:
            dot.edge(str(i),str(j))
    print(dot.source) 
    
    dot.render('test-output/cfg.gv',view=True) 
    
    pass
