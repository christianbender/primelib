# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:44:23 2017

@author: Christian Bender

This python library contains some useful functions to deal with
prime numbers and whole numbers.

Overview:

isPrime(number)
sieveEr(N)
getPrimeNumbers(N)
primeFactorization(number)
greatestPrimeFactor(number)
smallestPrimeFactor(number)

----

isEven(number)
isOdd(number)
ggT(number1, number2)  // greatest common divisor
kgV(number1, number2)  // least common multiple

-----

goldbach(number)  // Goldbach's assumption

"""

def isPrime(number):
    """
        input: positive integer 'number'
        returns true if 'number' is prime otherwise false.
    """
    import math # for function sqrt
    
    # precondition
    assert(isinstance(number,int) and (number >= 0))
    
    status = True
    
    # 0 and 1 are none primes. 
    if number <= 1:
        status = False
    
    for divisor in range(2,int(round(math.sqrt(number)))+1):
        
        # if 'number' divisible by 'divisor' then sets 'status'
        # of false and break up the loop. 
        if number % divisor == 0:
            status = False
            break
    
    return status

# ------------------------------------------

def sieveEr(N):
    """
        input: positive integer 'N' > 2
        returns a list of prime numbers from 2 up to N.
        
        This function implements the algorithm called
        sieve of erathostenes.         
        
    """
    
    # precondition
    assert(isinstance(N,int) and (N > 2))
    
    # beginList: conatins all natural numbers from 2 upt to N
    beginList = [x for x in range(2,N+1)]

    ans = [] # this list will be returns.     
    
    # actual sieve of erathostenes
    for i in range(len(beginList)):
        
        for j in range(i+1,len(beginList)):
            
            if (beginList[i] != 0) and \
            (beginList[j] % beginList[i] == 0):
                beginList[j] = 0
    
    # filters actual prime numbers.           
    ans = [x for x in beginList if x != 0]
    
    return ans
    

# --------------------------------

def getPrimeNumbers(N):
    """
        input: positive integer 'N' > 2
        returns a list of prime numbers from 2 up to N (inclusive)
        This function is more efficient as function 'sieveEr(...)'
    """    
    
    # precondition
    assert(isinstance(N,int) and (N > 2))
    
    ans = []    
    
    for number in range(2,N+1):
        
        if isPrime(number):
            
            ans.append(number)
            
    return ans


# -----------------------------------------
    
def primeFactorization(number):
    """
        input: integer 'number' 
        returns a list of the prime number factors of 'number'
    """

    import math    # for function sqrt
    
    # precondition
    assert(isinstance(number,int))
    
    ans = [] # this list will be returns of the function.

    # potential prime number factors.

    factor = 2    

    # for negative numbers
    if number < 0:
        number *= -1
        
    quotient = number
    
    if not isPrime(number):
    
        while (quotient != 1):
            
            if isPrime(factor) and (quotient % factor == 0):
                    ans.append(factor)
                    quotient /= factor
            else:
                    factor += 1
    
    else:
        ans.append(number)
    
    return ans
    

# -----------------------------------------
    
def greatestPrimeFactor(number):
    """
        input: integer 'number' > 1
        returns the greatest prime number factor of 'number'
    """
    
    # precondition
    assert(isinstance(number,int) and (number > 1))
    
    # prime factorization of 'number'
    primeFactors = primeFactorization(number)
    
    return max(primeFactors)
    

# ----------------------------------------------
    
    
def smallestPrimeFactor(number):
    """
        input: integer 'number' > 1
        returns the smallest prime number factor of 'number'
    """
    
    # precondition
    assert(isinstance(number,int) and (number > 1))
    
    # prime factorization of 'number'
    primeFactors = primeFactorization(number)
    
    return min(primeFactors)
    
    
# ----------------------
    
def isEven(number):
    """
        input: integer 'number'
        returns true if 'number' is even, otherwise false.
    """   

    # precondition
    assert(isinstance(number, int))    
    
    return number % 2 == 0
    
# ------------------------
    
def isOdd(number):
    """
        input: integer 'number'
        returns true if 'number' is odd, otherwise false.
    """   

    # precondition
    assert(isinstance(number, int))    
    
    return number % 2 != 0
    
# ------------------------
    
    
def goldbach(number):
    """
        Goldbach's assumption
        input: a even positive integer 'number' > 2
        returns a list of two prime numbers whose sum is equal to 'number'
    """
    
    # precondition
    assert(isinstance(number,int) and (number > 2) and isEven(number))
    
    ans = [] # this list will returned
    
    primeNumbers = getPrimeNumbers(number)
    lenPN = len(primeNumbers)    

    # run variable for while-loops.
    i = 0
    j = 1
    
    # exit variable. for break up the loops
    loop = True
    
    while (i < lenPN and loop):
        
        j = i+1;
        
        
        while (j < lenPN and loop):
            
            if primeNumbers[i] + primeNumbers[j] == number:
                loop = False
                ans.append(primeNumbers[i])
                ans.append(primeNumbers[j])
                
            j += 1;
            
            
        i += 1
        
    return ans
    
# ----------------------------------------------

def ggT(number1,number2):
    """
        Greatest common divisor
        input: two positive integer 'number1' and 'number2'
        returns the greatest common divisor of 'number1' and 'number2'
    """
    
    # precondition
    assert(isinstance(number1,int) and isinstance(number2,int) \
    and (number1 >= 0) and (number2 >= 0))

    rest = 0    
    
    while number2 != 0:
        
        rest = number1 % number2
        number1 = number2
        number2 = rest
    
    return number1
    
# ----------------------------------------------------
    
def kgV(number1, number2):
    """
        Least common multiple
        input: two positive integer 'number1' and 'number2'
        returns the least common multiple of 'number1' and 'number2'
    """
    
    # precondition
    assert(isinstance(number1,int) and isinstance(number2,int) \
    and (number1 >= 1) and (number2 >= 1))
    
    ans = 1 # actual answer that will be return.
     
    # for kgV (x,1)
    if number1 > 1 and number2 > 1:
        
        # builds the prime factorization of 'number1' and 'number2'
        primeFac1 = primeFactorization(number1)
        primeFac2 = primeFactorization(number2)
        
    elif number1 == 1 or number2 == 1:
        
        primeFac1 = []
        primeFac2 = []
        ans = max(number1,number2)
    
    count1 = 0
    count2 = 0
     
    done = [] # captured numbers int both 'primeFac1' and 'primeFac2'
    
    # iterates through primeFac1
    for n in primeFac1:
        
        if n not in done:
        
            if n in primeFac2:
            
                count1 = primeFac1.count(n)
                count2 = primeFac2.count(n)
            
                for i in range(max(count1,count2)):
                    ans *= n
        
            else:
                
                count1 = primeFac1.count(n)
                
                for i in range(count1):
                    ans *= n
                    
            done.append(n)
    
    # iterates through primeFac2
    for n in primeFac2:
        
        if n not in done:
            
            count2 = primeFac2.count(n)
            
            for i in range(count2):
                ans *= n
                    
            done.append(n)
                    
    return ans
    