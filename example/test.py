# coding: utf-8
from __future__ import (print_function, unicode_literals)

import sys
sys.path.append('..')
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag

dagparams = DefaultDagParams()

with open('./a.txt', 'r') as f:
    str=f.read()

result=[]
word=""
final=""
for char in str:
    if char.isalpha():
        word+=char
    else:
        if len(word)>0:
            result.append(word)
        word=""
        if(char!=" "):
            if len(result)>0:
                x = dag(dagparams, result)
                final+=''.join(x[0].path)
                result=[]
            final+=char
if len(word)>0:
    result.append(word)
if len(result)>0:
    x = dag(dagparams, result)
    final+=''.join(x[0].path)
print(final)
