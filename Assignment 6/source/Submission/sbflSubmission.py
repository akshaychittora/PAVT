#!/usr/bin/env python3

import argparse
import sys
import numpy as np
sys.path.insert(0,'../KachuaCore/')
from irgen import *
from kast.builder import astGenPass
import csv

def fitnessScore(IndividualObject):
    """
    Parameters
    ----------
    IndividualObject : Individual (definition of this class is in KachuaCore/sbfl.py)
        This is a object of class Individual. The Object has 3 elements
        1. IndividualObject.individual : activity matrix.
                                    type : list, row implies a test
                                    and element of rows are components.
        2. IndividualObject.fitness : fitness of activity matix.
                                    type : float
        3. Indivisual.fitness_valid : a flag used by Genetic Algorithm.
                                    type : boolean
    Returns
    -------
    fitness_score : flaot
        returns the fitness-score of the activity matrix.
        Note : No need to set/change fitness and fitness_valid attributes.
    """
    #Design the fitness function
    fitness_score = 0
    activity_mat = np.array(IndividualObject.individual,dtype='int');
    activity_mat = activity_mat[:,:activity_mat.shape[1]-1]
    #Use 'activity_mat' to compute fitness of it.
    #ToDo : Write your code here to compute fitness of test-suite
    #using ulysis
    x,y= activity_mat.shape
    #y= activity_mat[0].len()
    tr=[]
    for j in range(y):
        tr1=[]
        for i in range(x):
            tr1.append(activity_mat[i][j])
        tr.append(tr1)
        
    an=[0]*len(tr)
    for i in range(len(tr)-1):
        if(tr[i]==[0]*len(tr[i])):
            an[i]=1
        else:
            for j in range(i+1,len(tr)):
                if(tr[i]==tr[j]):
                   an[i]+=1
                   an[j]+=1
                
    le= len(an)-1    
    ans=0
    for i in an:
        if(i!=1):
            ans+= float(i/le)
        else:
            ans+= 1
    fitness_score = ans/(le+1)
    #print(activity_mat)
    return fitness_score

#This class takes a spectrum and generates ranks of each components.
#finish implementation of this class.
class SpectrumBugs():
    def __init__(self,spectrum):
        self.spectrum = np.array(spectrum,dtype='int')        
        self.comps = self.spectrum.shape[1] - 1
        self.tests = self.spectrum.shape[0]
        self.activity_mat = self.spectrum[:,:self.comps]
        self.errorVec = self.spectrum[:,-1]

    def getActivity(self,comp_index):
        '''
        get activity of component 'comp_index'
        Parameters
        ----------
        comp_index : int
        '''
        return self.activity_mat[:,comp_index]

    def suspiciousness(self,comp_index):
        '''
        Parameters
        ----------
        comp_index : int
            component number/index of which you want to compute how suspicious
            the component is. assumption: if a program has 3 components then
            they are denoted as c0,c1,c2 i.e 0,1,2
        Returns
        -------
        sus_score : float
            suspiciousness value/score of component 'comp_index'
        '''
        sus_score = 0
        #ToDo : implement the suspiciousness score function.
        x = self.getActivity(comp_index)
        y = self.errorVec
        match=0
        count1=0
        count2=0
        for i in range(len(y)):
            if(x[i]==1):
                count2+=1
            if(y[i]==1):
                if(x[i]==1):
                    match+=1
                count1+=1
        if(match==0):
            sus_score=0
        else:
            p= float(match/count1)
            q= float(match/count2)
            sus_score= np.sqrt(p*q)
        return sus_score
    def getRankList(self):
        '''
        find ranks of each components according to their suspeciousness score.
        
        Returns
        -------
        rankList : list
            ranList will contain data in this format:
                suppose c1,c2,c3,c4 are components and their ranks are
                1,2,3,4 then rankList will be :
                    [[c1,1],
                     [c2,2],
                     [c3,3],
                     [c4,4]]
        '''
        rankList = []
        #ToDo : implement rankList
        n= self.comps
        x=[]
        for i in range(n):
            x.append(self.suspiciousness(i))
        y=sorted(range(len(x)), key=lambda k: x[k])
        for i in range(len(y)):
            y[i]+=1
        for i in range(len(y)):
            rankList.append([str('c'+str(i+1)),y[i]])
        rankList= sorted(rankList,key=lambda x:x[1])
        return rankList

#do not modify this function.
def computeRanks(spectrum,outfilename):
    '''
    Parameters
    ----------
    spectrum : list
        spectrum
    outfilename : str
        components and their ranks.
    '''
    S = SpectrumBugs(spectrum)
    rankList = S.getRankList();
    with open(outfilename,"w") as file:
        writer = csv.writer(file)
        writer.writerows(rankList) 
