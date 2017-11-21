"""
Chapter one :
Python Data Model

Author:
    ZJ
Blog:
    CSDN : http://blog.csdn.net/JUNJUN_ZHAO?ref=toolbar
    Github : https://laobadao.github.io/
Zhihu:
    https://www.zhihu.com/people/zhao-jun-jun-82-58/activities
Github:
    https://github.com/laobadao
"""
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

