from ast2json import ast2json
import json
from ast import parse

ast = ast2json(parse(open('new.py').read()))

obj=json.loads(json.dumps(ast, indent=4))







def print_fun(a):
    arg=''
    for i in a['args']:
        arg+= str(print_rl(i))
        arg+=','
    arg = arg[:-1]
    return str(a['func']['id'])+'('+arg+')'
def print_dict(a):
    s=''
    if(a['_type']=='List'):
        s+='['
        for i in range(len(a['elts'])):
            if(a['elts'][i]['_type']=='Constant'):
                s+='\''
                s+=print_rl(a['elts'][i])
                s+='\''
                
            else:
                s+=print_rl(a['elts'][i])
            s+=','
        s=s[:-1]
        s+=']'
    if(a['_type']=='Dict'):
        s+='{'
        
        for i in range(len(a['keys'])):
           
            if(a['keys'][i]['_type']=='Dict' or a['keys'][i]['_type']=='List'):
                s+=print_dict(a['keys'][i])
            else:
                s+=print_rl(a['keys'][i])
            s+=':'        
            if(a['values'][i]['_type']=='Dict' or a['values'][i]['_type']=='List' ):
                s+=print_dict(a['values'][i])
            else:
                s+=print_rl(a['values'][i])
            s+=','
        s=s[:-1]
        s+='}'
    return s
        
        


def print_rl(a):
    if(a['_type']=='Constant'):
        return str(a['value'])
    elif(a['_type']=='Name'):
        return str(a['id'])
    elif(a['_type']=='Subscript'):
        s=''
        s+=str(a['value']['id'])
        s+='['
        s+=str(a['slice']['value']['value'])
        s+=']'
        return s
        
        
    x=''
    if(str(a['op']['_type'])=='Add'):
        x='+'
    if(str(a['op']['_type'])=='Sub'):
        x='-'
    if(str(a['op']['_type'])=='Div'):
        x='/'
    if(str(a['op']['_type'])=='Mult'):
        x='*'
    
    return (str(print_rl(a['left']))+x+str(print_rl(a['right'])))

def print_asgn(a,flag):
    if(flag==0):
        s= a['targets'][0]['id']
        s+='='
        if(a['value']['_type']=='Constant'):
            s+=str(a['value']['value'])
        elif(a['value']['_type']=='BinOp'):
            s+= print_rl(a['value'])
        elif(a['value']['_type']=='Call'):
            s+=print_fun(a['value'])
        elif(a['value']['_type']=='List'):
            s+=print_dict(a['value'])
        elif(a['value']['_type']=='Dict'):
            s+=print_dict(a['value'])
    return s
def checkKey(dict, key):
      
    if key in dict:
        return 1
    else:
        return 0

def fun(a):
    if(a['_type']=='If' or a['_type']=='For' or a['_type']=='While'):
        if(a['_type']=='If' and checkKey(a,'orelse')):
            for i in range(len(a['body'])):
                fun(a['body'][i])
            for i in range(len(a['orelse'])):
                fun(a['orelse'][i])
        else:
            for i in range(len(a['body'])):
                fun(a['body'][i])
                #print('hi')
    if(a['_type']=='Assign'):
        #print('got it')
        print(print_asgn(a,0))

def print_testValues(a):
    if(a['_type']=='Compare'):
        
        s= print_rl(a['left'])
        x=''
        
        
        if(a['ops'][0]['_type']=='Gt'):
            x='>'
        if(a['ops'][0]['_type']=='GtE'):
            x='>='
        if(a['ops'][0]['_type']=='Lt'):
            x='<'
        if(a['ops'][0]['_type']=='LtE'):
            x='<='
            
        if(a['ops'][0]['_type']=='NotEq'):
            x='!='
        if(a['ops'][0]['_type']=='Eq'):
            x='=='
        
        s+=x
        #print(s)
        #print(a['comparators'][0])
        s=s+(print_rl(a['comparators'][0]))
        #print(s)
        return s
        
def print_test(a):
    s=''
    x=''
   
    if(checkKey(a,'op') and a['op']['_type']=='And'):
        x='and'
    else:
        x='or'
    if(a['_type']=='BoolOp'):
        for i in range(len(a['values'])):
            s=s+ str(print_testValues(a['values'][i]))
            
            s=s+' '+x+' '
        sp = s.split()
        rm = sp[:-1]
        sp1 = ' '.join([str(ele) for ele in rm])
        print(sp1)
        
        
        
    else:
        print(print_testValues(a))
def print_test1(a,b):
    s=''
    s+=b['id']
    s+=' '
    s+='in '
    if(a['_type']=='Name'):
        s+=a['id']
    elif(a['_type']=='Call'):
        s+=print_fun(a)
    print(s)
        
        
    
def fun2(a):
    if( a['_type']=='For' or a['_type']=='While'):
        for i in range(len(a['body'])):
            fun2(a['body'][i])
    if(a['_type']=='If'):
        if(a['_type']=='If'):
            #print('if')
            print_test(a['test'])
            for i in range(len(a['body'])):
                fun2(a['body'][i])
            if(checkKey(a,'orelse')):
                for i in range(len(a['orelse'])):
                    fun2(a['orelse'][i])

def fun3(a):
    if(a['_type']=='If'):
            for i in range(len(a['body'])):
                fun3(a['body'][i])
            if(checkKey(a,'orelse')):
                for i in range(len(a['orelse'])):
                    fun3(a['orelse'][i])
    if( a['_type']=='For' or a['_type']=='While'):     
        if(a['_type']=='For'):
                #print('for')
            print_test1(a['iter'],a['target'])
            for i in range(len(a['body'])):
                fun3(a['body'][i])
        if(a['_type']=='While'):
                #print('while')
            print_test(a['test'])
            for i in range(len(a['body'])):
                fun3(a['body'][i])

print('Assignment Statements: ')                                  
    
for i in range(len(obj['body'])): 
    fun(obj['body'][i])

print('\n')
print('Branch Conditions: ')
for i in range(len(obj['body'])): 
    fun2(obj['body'][i])

print('\n')
print('Loop Conditions: ')   
for i in range(len(obj['body'])):
    fun3(obj['body'][i])