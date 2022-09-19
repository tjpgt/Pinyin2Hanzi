# coding: utf-8
from __future__ import (print_function, unicode_literals)

import sys
sys.path.append('..')
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag
from Pinyin2Hanzi import simplify_pinyin

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
            result.append(simplify_pinyin(word))
        word=""
        if(char!=" "):
            if len(result)>0:
                x = dag(dagparams, result)
                if(len(x)==0):
                    print('error:', ' '.join(result))
                else:
                    final+=''.join(x[0].path)
                result=[]
            final+=char
if len(word)>0:
    result.append(simplify_pinyin(word))
if len(result)>0:
    x = dag(dagparams, result)
    if(len(x)==0):
        pass
    else:
        final+=''.join(x[0].path)
print(final)
