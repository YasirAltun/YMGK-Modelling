# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 21:14:27 2024

@author: CyberSurgeon
"""

from fuzzywuzzy import fuzz

import numpy as np
from sklearn.metrics import jaccard_score

def jackass(str1,str2):
    asc1 = [ord(i) for i in str1]
    asc2 = [ord(i) for i in str2]
    result = jaccard_score(asc1, asc2, average='macro')
    return 100- (result*100)

def fit_ani(str1,str2):
    asc1 = [ord(i) for i in str1]
    asc2 = [ord(i) for i in str2]
    s = 0
    for i in range(len(asc1)):
        t = asc1[i]-asc2[i]
        s += abs(t)    
    return s

def hamming_distance(chaine1, chaine2):
    return sum(c1 != c2 for c1, c2 in zip(chaine1, chaine2))


str1 = 'abcefg'
str2 = 'gfecba'
fitness = 100-fuzz.ratio(str1,str2)


print('Fuzz: ',fitness)

print('Jaccard', jackass(str1,str2))

print('Hamming: ',hamming_distance(str1,str2))

print('Fit_Ani: ',fit_ani(str1,str2))

'''
Genetik Algoritma

Verilen
1. Şifre ve düz metin arasındaki levenshtein uzaklığı olan uygunluk

Gereksinim
1. Mümkün olan en iyi a ve d. - genom, çoklu nesiller için (a,d) dizileri olacaktır.
 
a = 1.şey ila 4
d = 0 ila 4

Çaprazlamada, a1,d2 ve a2,d1 kullanarak rastgele yavrular üretiyoruz.
Mutasyonda, %10 zaman için, adımlara dayalı bir şey yapmamız gerekiyor.


x = [0.3,0.997,0.862,0.531,0.761]


x_sorted = [0.997,0.862,0.761,0.531,0.3]

[4,0,1,3,2]

[3,4,2,4,6]

[7,4,6,3,1]= anahtar
[65,66,...]

[şifre]


unni 
[90,81,81,67]

znny

abcd

[67,68,69,70]

90-67 +/-
81-68
.
.


'''