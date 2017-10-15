import csv
import sys
import string
import copy
from collections import Counter
from operator import itemgetter
import numpy as np
from math import exp
import matplotlib.pyplot as plt

#from tabulate import tabulate
from collections import defaultdict
from math import log
from scipy import stats

def sigmoid(X):
    return sigmoid(X)


train = 1000
total=0
product_id = np.zeros((train,1))
customer_id = np.zeros((train,1))
price = np.zeros((train,1))
dataset=np.zeros((train*3,2))
dataset2=np.zeros((train*3,2))
test = 0
with open('test_values.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        i = 0
        for string in row:
            if i == 1 and total > 0 and total <=train:
                #print(total)
                product_id[total-1]= float(string)
            if i == 2 and total > 0 and total <=train:
                customer_id[total-1]=(float(string))
            if i == 5 and total > 0 and total <=train:
                price[total-1]=(float(string))
            #print(i,string)
            i=i+1
        if(total<=train and total>0):
            dataset[total-1] = [customer_id[total-1],price[total-1]]
            dataset2[total-1] = [customer_id[total-1],product_id[total-1]]
        total=total+1
        test=test+1
        if(total>train):
           spamreader = csv.reader(csvfile, delimiter=',')
           for row in spamreader:
                   i = 0
                   for string in row:
                           if i == 1:
                                   #print(total)
                                   product_id[total-test]= float(string)
                           if i == 2:
                                   customer_id[total-test]=(float(string))
                           if i == 5:
                                   price[total-test]=(float(string))
                                   #print(i,string)
                           i=i+1
                           dataset[total-1] = [customer_id[total-test],price[total-test]]
                           dataset2[total-1] = [customer_id[total-test],product_id[total-test]]



def lr_train(train_vectors, iterations=100, reg=0.01,
        lr=0.01, stop_diff=int(1e-6)):

    count_w = train
    w = np.zeros((count_w,1 ))

    for i in range(iterations):
        grad = np.zeros((count_w, 2))

        for vector in train_vectors:

            y = vector[1]
            x = vector[0]

            y_hat = lr_calc_prob(w, y)

            grad += (y - y_hat)*x

        #print(grad,"grad",reg,"reg",w,"w")
        w = [i*reg for i in w]
        grad -= w
        w += lr * grad

        if np.linalg.norm(grad) <= stop_diff:
            break

    return w

def lr_calc_prob(w, x):
    #print(np.sum(np.dot(w,x)))

    denominator = 1 + exp(-1 * np.sum(np.dot(w,x)))

    return denominator

def lr_classify(w, x):

    return lr_calc_prob(w, x)


def lr_train_test(train_vectors, test_vectors):

    w = lr_train(train_vectors)
    incorrect = 0.0

    for vector in test_vectors:
        y = vector[0]
        x = vector[1]

        y_hat = lr_classify(w, x)

        if y_hat is not y:
            incorrect += 1

    return incorrect/len(test_vectors)


zero_one_loss = lr_train(dataset)

i = test
op = [0];
for vector in dataset:
    y = vector[1]
    x = vector[0]
while i < total:
    pred_value = zero_one_loss*op
    if pred_value - x > 10:
        print("failed")




zero_one_loss = lr_train(dataset2)

i = test
op = [0];
for vector in dataset2:
    y = vector[1]
    x = vector[0]
while i < total:
    pred_value = zero_one_loss*op
    if pred_value - x > 10:
        print("failed second")
