# coding: utf-8
from __future__ import (print_function, unicode_literals)

import sys
sys.path.append('..')
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag
from Pinyin2Hanzi import simplify_pinyin
from Pinyin2Hanzi import DefaultHmmParams
from Pinyin2Hanzi import viterbi

hmmparams = DefaultHmmParams()

dagparams = DefaultDagParams()

with open('./a.txt', 'r') as f:
    str=f.read()

result=[]
word=""
final=""
hhfinal=""
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
                y =  viterbi(hmm_params=hmmparams, observations=tuple(result), path_num = 2, log = True)
                if(len(y)==0):
                    print('error:', ' '.join(result))
                else:
                    hhfinal+=''.join(y[0].path)
                result=[]
            final+=char
            hhfinal+=char
if len(word)>0:
    result.append(simplify_pinyin(word))
if len(result)>0:
    x = dag(dagparams, result)
    if(len(x)==0):
        print('error:', ' '.join(result))
    else:
        final+=''.join(x[0].path)
    y =  viterbi(hmm_params=hmmparams, observations=tuple(result), path_num = 2, log = True)
    if(len(y)==0):
        print('error:', ' '.join(result))
    else:
        hhfinal+=''.join(y[0].path)
print(final)
print("--------------------------------------")
print(hhfinal)
