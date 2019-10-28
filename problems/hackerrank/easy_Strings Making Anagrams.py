# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:41:43 2019

https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
"""

a = 'showman'
b = 'woman'

a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

a_len = len(set(a)); b_len = len(set(b))
#%%
from collections import Counter
a_count = Counter(a); b_count = Counter(b)

cnt = sum((b_count - a_count).values())+sum((a_count - b_count).values())
#Counter의 힘! 더하기 뺴기 연산이 가능하다!