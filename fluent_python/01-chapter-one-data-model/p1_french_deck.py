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

一摞有序的纸牌

"""
import collections

# 用 collections.namedtuple 构造简单的 纸牌 类
# collections.namedtuple 用以构建只有少数属性但是没有方法的对象，比如数据库条目。
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

        # >> > import collections
        # >> > Card = collections.namedtuple('Card', ['rank', 'suit'])
        # >> > beer_card = Card('7', 'diamonds')
        # >> > beer_card
        # Card(rank='7', suit='diamonds')
        # >> > exit()

    # >> > from p1_french_deck import FrenchDeck
    # >> > deck = FrenchDeck()
    # >> > len(deck)
    # 52
    # >> > exit()
