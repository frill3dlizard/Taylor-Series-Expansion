# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 17:51:14 2024

@author: frillelizard
"""
import numpy as np
import math
#BELOW FUNCTIONS ARE USED TO EXPAND A TAYLOR SERIES OUT OF 
#THE SERIES NOTATION AND INTO POLYNOMIAL FORM

#----------------------------------

#Taylor series evaluated for a specific n
#For 1/x centered at c, starting at n=0
def taylor(n, c):
    x = np.zeros(n+1)
    for i in range(0,n+1):
        Binomial_expansion = math.comb(n,n-i)*(-c)**(n-i)
        x[i] = (-1)**n*Binomial_expansion / c**(n+1) 
    return x

#----------------------------------
def taylor_x2(n, c):
    x = np.zeros(n+1)
    for i in range(0,n+1):
        Binomial_expansion = math.comb(n,n-i)*(-c)**(n-i)
        x[i] = (-1)**(n)*(n+1)*Binomial_expansion / c**(n+2) 
    return x
#Taylor series for ln(x) around x=c (c>0)
#NOTE: This doesn't include the ln(c) constant that should be added
def taylor_lnx(n, centered_at):
    x = np.zeros(n+1)
    for i in range(0,n+1):
        Binomial_expansion = math.comb(n,n-i)*(-centered_at)**(n-i)
        x[i] = (-1)**(n+1)*Binomial_expansion / (n*centered_at**n)
    return x

#----------------------------------

#Taylor series for sin(x) and cos(x) centered at c
#Works for any real number c
def taylor_sin(n, c):
    f_dash = [np.sin(c), np.cos(c), -np.sin(c), -np.cos(c)]
    x = np.zeros(n+1)
    for i in range(0, n+1):
        Binomial_expansion = math.comb(n,n-i)*(-c)**(n-i)
        x[i] = f_dash[n%4] *Binomial_expansion  / math.factorial(n)
    return x

def taylor_cos(n,c):
    f_dash = [np.cos(c), -np.sin(c), -np.cos(c), np.sin(c)]
    x = np.zeros(n+1)
    for i in range(0, n+1):
        Binomial_expansion = math.comb(n,n-i)*(-c)**(n-i)
        x[i] = f_dash[n%4] *Binomial_expansion  / math.factorial(n)
    return x

#----------------------------------
#Taylor series for the exponential function centered at c
#works for all real values of c
def taylor_exponential(n, c):
    f = np.exp(c)
    x = np.zeros(n+1)
    for i in range(0, n+1):
        Binomial_expansion = math.comb(n,n-i)*(-c)**(n-i)
        x[i] = f *Binomial_expansion  / math.factorial(n)
    return x

#Sum part of series:
#Put coefficients into array of size n
#Will iterate Taylor series same amount, hence same 'n'
def array(n, centered_at, function):
    final_array = np.zeros(n+1)
    for k in range(0,n+1):
        #Get coefficients for nth taylor sum
        coefficients = function(k, centered_at)    
        #Add coefficients as you go
        final_array[:len(coefficients)] += coefficients 
    return final_array


#Gives an array with each element being the coefficient of x^(position in array)
#I.e. first element is x^0, second is x^1, etc.
array(n=17, centered_at=6, function=taylor)
asd= array(n=19, centered_at=3*np.pi/2, function=taylor_sin)
cos = array(n=19, centered_at=3*np.pi/2, function=taylor_cos)
ivnerse_x2 = array(n=20, centered_at=5, function = taylor_x2)
#----------------------------------
def array_lnx(n, centered_at):
    final_array = np.zeros(n+1)
    for k in range(1,n+1):
        coefficients = taylor_lnx(k, centered_at)    #Get coefficients for nth taylor sum
        #Add coefficients as you go
        final_array[:len(coefficients)] += coefficients 
    #Add the constant term    
    final_array[0]+=np.log(centered_at)
    return final_array

array_lnx(19, 6)

