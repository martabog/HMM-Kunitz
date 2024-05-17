#!/usr/bin/env python3

"""Given in input the file with ID, e-value and class(1-Kunitz, not Kunitz-0) this script calculates the confusion matrix and all the parameters to evaluate the performance given a threshold provided in input."""

import sys
import numpy as np
import pickle

def get_data(predfile): 
    """Reads the input file and stores its information in a list called preds"""
    preds = [] #output = list of lists
    with open(predfile, "r") as f:
        for line in f:
            v = line.rstrip().split() #v = [seqID, e-value, label]
            v[1] = float(v[1]) #e-value
            v[2] = int(v[2]) #label 
            preds.append(v)
    return preds
    
    
#CONFUSION MATRIX (CM)
def compute_cm(preds,th=0.5): 
    '''Computes the confusion matrix based on the e-value threshold for each protein in preds obtained from get_data function.'''
    cm = np.zeros((2,2)) #matrix 2x2
    for pred in preds: 
        p=0  #prediction is 0 by default
        if pred[1]<=th: p=1 
        cm[p][pred[2]]+=1 #identify the cell [prediction][label=reality] and we add one case  
    return cm 
        
        
#OVERALL ACCURACY 
def get_accuracy(cm): 
    '''Calculates the overall accuracy based on the formula: (TN+TP)/(TN+TP+FN+FP) = (TN+TP)/tot'''
    q2 = float((cm[0][0]+cm[1][1])/np.sum(cm))
    return q2


#MATTHEW CORRELATION COEFFICIENT (MCC)   
def get_mcc(cm): 
    '''Calculates MCC which is a better estimation of performace when the set is unbalanced. 
    This is done according to the formula:(TP*TN-FP*FN)/sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))'''
    tp = cm[1][1]
    tn = cm[0][0]
    fn = cm[0][1]
    fp = cm[1][0]
    mcc = (tp*tn-fp*fn)/np.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))
    tpr = float(tp / (tp + fn))
    fpr = float(fp / (fp + tn))
    return mcc, tpr, fpr

l_tpr = []
l_fpr = []

if __name__=="__main__":
    for i in range(1,16):
        th = 10**(-i)
        predfile = sys.argv[1]
        preds = get_data(predfile)
        cm = compute_cm(preds,th)
      
        print('TP=', cm[1][1], 'TN=', cm[0][0], 'FN=', cm[0][1], 'FP=', cm[1][0])
        
        q2 = get_accuracy(cm)
        mcc, tpr, fpr = get_mcc(cm)
      
        l_tpr.append(tpr)
        l_fpr.append(fpr)

        print('TH=', th, 'Q2=', q2, 'MCC=', mcc)
        print("----------------------------------------------------")
    
        with open("performance_data.pickle", "wb") as f:
            pickle.dump([l_tpr, l_fpr], f)

    




