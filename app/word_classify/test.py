
#!/usr/bin/env python3
# encoding: utf-8
# -*- coding: utf-8 -*-
# @Time : 2018-12-22 19:53
# @Author : Leon Chu <ieno_chu@apple.com>

from nltk.stem.lancaster import LancasterStemmer
lancaster_stemmer = LancasterStemmer()
res  = lancaster_stemmer.stem('don\'t')

print(round(3.5999999999999996,4))

abc = ''
if abc:
    print('yes')