
# Fluent Python | Notes-01-Data model

**转载请注明作者和出处：ZJ 微信公众号-「SelfImprovementLab」**

    本系列为 英文版「Fluent Python」和 中文版「流畅的 Python」学习笔记，仅添加个人理解，不足或有误还请指正。
    
    环境：Python 3.6
    
    [CSDN]()：
   
---

## 1.1 A Pythonic Card Deck

1.Python 最好的品质之一是一致性。

2.Python 解释器碰到特殊的句法时，会使用特殊方法去激活一些基本的对象操作，这些特殊方法的名字以两个下划线开头，以两个下划线结尾（例`__getitem__`）。比如 `obj[key]`的背后就是 `__getitem__` 方法，为了能求得 `my_collection[key]` 的值，解释器实际上会调用 `my_collection.__getitem__(key)`。

3.提到 `__getitem__ `这个特殊方法的时候,称为 双下`－getitem`”（dunder-getitem）这种说法。

**一摞Python风格的纸牌**

接下来我会用一个非常简单的例子来展示如何实现 `__getitme__` 和`__len__` 这两个特殊方法，通过这个例子我们也能见识到特殊方法的强大。



```python
"""
Chapter one :
Python Data Model

Author:
    ZJ

一摞有序的纸牌

"""
import collections

# 用 collections.namedtuple 构造简单的 纸牌 类
# collections.namedtuple 用以构建只有少数属性但是没有方法的对象，比如数据库条目。
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    # spades : 黑桃 ,diamonds: 方片 clubs:梅花  hearts: 红桃
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
    # 长度，大小
    def __len__(self):
        return len(self._cards)
    # position s索引位置
    def __getitem__(self, position):
        return self._cards[position]

```

用 collections.namedtuple 构建了一个简单的类来表示一张纸牌。

自 Python 2.6 开始，namedtuple 就加入到 Python 里，用以构建只有少数属性但是没有方法的对象，比如数据库条目。如下面这个控制台会话所示，利用 namedtuple，我们可以很轻松地得到一个纸牌对象：

注意： 若在 cmd 中执行语句，则先定位到当前路径下：

 D:\github\python\Fluent_Python_Note\fluent_python\01-data-model > python
 
 在 cmd 中运行 导入 frech_deck.py 中的 FrenchDeck 类
 
`>>> from frech_deck import FrenchDeck`
 
 当前路径下执行，可以写相对路径，否则 需要写绝对路径。


```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
beer_card = Card('7', 'diamonds')
print(beer_card)
```

    Card(rank='7', suit='diamonds')
    


```python
deck = FrenchDeck()
print(len(deck)) #  len() 函数 ，牌的张数，
print(deck[0]) # 索引 0 第一张
print(deck[-1]) # -1 代表取最后一张
```

    52
    Card(rank='2', suit='spades')
    Card(rank='A', suit='hearts')
    


```python
'''
随机抽取纸牌 random.choice 函数
'''
from random import choice

deck1 = choice(deck)
print(deck1)

deck2 = choice(deck)
print(deck2)
```

    Card(rank='4', suit='spades')
    Card(rank='2', suit='diamonds')
    

<font color=#0099ff>
**总结：Python 数据模型的两个好处**
    
- 作为你的类的用户，他们不必去记住标准操作的各式名称（“怎么得到元素的总数？是 .size() 还是 .length() 还是别的什么？”）。统一都是 len ( ) 函数
- 可以更加方便地利用 Python 的标准库，比如 random.choice 函数，从而不用重新发明轮子。</font>

因为` __getitem__` 方法把` []` 操作交给了 `self._cards `列表，所以我们的 deck 类自动支持切片（slicing）操作。下面列出了查看一摞牌最上面 3 张和只看牌面是 A 的牌的操作。其中第二种操作的具体方法是，先抽出索引是 12 的那张牌，然后每隔 13 张牌拿 1 张：


```python
# 取前三张牌 就是 黑桃 2 3 4 
print(deck[:3])
# 取索引为 12 的牌 黑桃 A ，然后每隔 13 张牌拿 1 张
print(deck[12::13])
```

    [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
    [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
    

因为实现了 `__getitem__` 方法，这一摞牌就变成可迭代。


```python
for card in deck:
    print(card)

```

    Card(rank='2', suit='spades')
    Card(rank='3', suit='spades')
    Card(rank='4', suit='spades')
    Card(rank='5', suit='spades')
    Card(rank='6', suit='spades')
    Card(rank='7', suit='spades')
    Card(rank='8', suit='spades')
    Card(rank='9', suit='spades')
    Card(rank='10', suit='spades')
    Card(rank='J', suit='spades')
    Card(rank='Q', suit='spades')
    Card(rank='K', suit='spades')
    Card(rank='A', suit='spades')
    Card(rank='2', suit='diamonds')
    Card(rank='3', suit='diamonds')
    Card(rank='4', suit='diamonds')
    Card(rank='5', suit='diamonds')
    Card(rank='6', suit='diamonds')
    Card(rank='7', suit='diamonds')
    Card(rank='8', suit='diamonds')
    Card(rank='9', suit='diamonds')
    Card(rank='10', suit='diamonds')
    Card(rank='J', suit='diamonds')
    Card(rank='Q', suit='diamonds')
    Card(rank='K', suit='diamonds')
    Card(rank='A', suit='diamonds')
    Card(rank='2', suit='clubs')
    Card(rank='3', suit='clubs')
    Card(rank='4', suit='clubs')
    Card(rank='5', suit='clubs')
    Card(rank='6', suit='clubs')
    Card(rank='7', suit='clubs')
    Card(rank='8', suit='clubs')
    Card(rank='9', suit='clubs')
    Card(rank='10', suit='clubs')
    Card(rank='J', suit='clubs')
    Card(rank='Q', suit='clubs')
    Card(rank='K', suit='clubs')
    Card(rank='A', suit='clubs')
    Card(rank='2', suit='hearts')
    Card(rank='3', suit='hearts')
    Card(rank='4', suit='hearts')
    Card(rank='5', suit='hearts')
    Card(rank='6', suit='hearts')
    Card(rank='7', suit='hearts')
    Card(rank='8', suit='hearts')
    Card(rank='9', suit='hearts')
    Card(rank='10', suit='hearts')
    Card(rank='J', suit='hearts')
    Card(rank='Q', suit='hearts')
    Card(rank='K', suit='hearts')
    Card(rank='A', suit='hearts')
    

 注意： 在 cmd  中执行 
 
 ```
 for card in deck: # doctest: + ELLIPSIS
 ...   print(card)# print(card) 前要手动输入 TAB 否则格式不正确
 ... # 然后再回车 就可以看到输出了
 
 ```
 
 反向迭代：


```python
for card in reversed(deck):
    print(card)
```

    Card(rank='A', suit='hearts')
    Card(rank='K', suit='hearts')
    Card(rank='Q', suit='hearts')
    Card(rank='J', suit='hearts')
    Card(rank='10', suit='hearts')
    Card(rank='9', suit='hearts')
    Card(rank='8', suit='hearts')
    Card(rank='7', suit='hearts')
    Card(rank='6', suit='hearts')
    Card(rank='5', suit='hearts')
    Card(rank='4', suit='hearts')
    Card(rank='3', suit='hearts')
    Card(rank='2', suit='hearts')
    Card(rank='A', suit='clubs')
    Card(rank='K', suit='clubs')
    Card(rank='Q', suit='clubs')
    Card(rank='J', suit='clubs')
    Card(rank='10', suit='clubs')
    Card(rank='9', suit='clubs')
    Card(rank='8', suit='clubs')
    Card(rank='7', suit='clubs')
    Card(rank='6', suit='clubs')
    Card(rank='5', suit='clubs')
    Card(rank='4', suit='clubs')
    Card(rank='3', suit='clubs')
    Card(rank='2', suit='clubs')
    Card(rank='A', suit='diamonds')
    Card(rank='K', suit='diamonds')
    Card(rank='Q', suit='diamonds')
    Card(rank='J', suit='diamonds')
    Card(rank='10', suit='diamonds')
    Card(rank='9', suit='diamonds')
    Card(rank='8', suit='diamonds')
    Card(rank='7', suit='diamonds')
    Card(rank='6', suit='diamonds')
    Card(rank='5', suit='diamonds')
    Card(rank='4', suit='diamonds')
    Card(rank='3', suit='diamonds')
    Card(rank='2', suit='diamonds')
    Card(rank='A', suit='spades')
    Card(rank='K', suit='spades')
    Card(rank='Q', suit='spades')
    Card(rank='J', suit='spades')
    Card(rank='10', suit='spades')
    Card(rank='9', suit='spades')
    Card(rank='8', suit='spades')
    Card(rank='7', suit='spades')
    Card(rank='6', suit='spades')
    Card(rank='5', suit='spades')
    Card(rank='4', suit='spades')
    Card(rank='3', suit='spades')
    Card(rank='2', suit='spades')
    

迭代通常是隐式的，譬如说一个集合类型没有实现 `__contains__` 方法，那么 `in` 运算符就会按顺序做一次迭代搜索。于是，`in` 运算符可以用在我们的 FrenchDeck 类上，因为它是可迭代的：



```python
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck) # beasts 没有这个类型 只有 spades : 黑桃 ,diamonds: 方片 clubs:梅花  hearts: 红桃 四种类型所以是 False
```

    True
    False
    

定义 `spades_high` 函数，对这摞牌进行升序排序。


```python
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
#  spades_high 黑桃最大的意思
def spades_high(card):
    # Card = collections.namedtuple('Card', ['rank', 'suit']) card 有 rank, suit'两个属性 ，访问 rank 属性   
    rank_value = FrenchDeck.ranks.index(card.rank)
    # 索引 * 4  len(suit_values) 再加上 card 对应花色 在字典中的值    
    return rank_value * len(suit_values) + suit_values[card.suit]
```


```python
for card in sorted(deck, key=spades_high):
    print(card)
# 这是从小到大排序，根据之前的规定，就是 梅花2 < 方片2 < 红桃2 < 黑桃2  < ....依次类推 
```

    Card(rank='2', suit='clubs')
    Card(rank='2', suit='diamonds')
    Card(rank='2', suit='hearts')
    Card(rank='2', suit='spades')
    Card(rank='3', suit='clubs')
    Card(rank='3', suit='diamonds')
    Card(rank='3', suit='hearts')
    Card(rank='3', suit='spades')
    Card(rank='4', suit='clubs')
    Card(rank='4', suit='diamonds')
    Card(rank='4', suit='hearts')
    Card(rank='4', suit='spades')
    Card(rank='5', suit='clubs')
    Card(rank='5', suit='diamonds')
    Card(rank='5', suit='hearts')
    Card(rank='5', suit='spades')
    Card(rank='6', suit='clubs')
    Card(rank='6', suit='diamonds')
    Card(rank='6', suit='hearts')
    Card(rank='6', suit='spades')
    Card(rank='7', suit='clubs')
    Card(rank='7', suit='diamonds')
    Card(rank='7', suit='hearts')
    Card(rank='7', suit='spades')
    Card(rank='8', suit='clubs')
    Card(rank='8', suit='diamonds')
    Card(rank='8', suit='hearts')
    Card(rank='8', suit='spades')
    Card(rank='9', suit='clubs')
    Card(rank='9', suit='diamonds')
    Card(rank='9', suit='hearts')
    Card(rank='9', suit='spades')
    Card(rank='10', suit='clubs')
    Card(rank='10', suit='diamonds')
    Card(rank='10', suit='hearts')
    Card(rank='10', suit='spades')
    Card(rank='J', suit='clubs')
    Card(rank='J', suit='diamonds')
    Card(rank='J', suit='hearts')
    Card(rank='J', suit='spades')
    Card(rank='Q', suit='clubs')
    Card(rank='Q', suit='diamonds')
    Card(rank='Q', suit='hearts')
    Card(rank='Q', suit='spades')
    Card(rank='K', suit='clubs')
    Card(rank='K', suit='diamonds')
    Card(rank='K', suit='hearts')
    Card(rank='K', suit='spades')
    Card(rank='A', suit='clubs')
    Card(rank='A', suit='diamonds')
    Card(rank='A', suit='hearts')
    Card(rank='A', suit='spades')
    

虽然` FrenchDeck` 隐式地继承了 `object` 类， 但功能却不是继承而来的。我们通过数据模型和一些合成来实现这些功能。通过实现 `__len__`和 `__getitem__` 这两个特殊方法，`FrenchDeck` 就跟一个 Python 自有的序列数据类型一样，可以体现出 Python 的核心语言特性（例如迭代和切片）。同时这个类还可以用于标准库中诸如 `random.choice、reversed` 和 `sorted` 这些函数。另外，对合成的运用使得 `__len__` 和 `__getitem__` 的具体实现可以代理给 `self._cards`这个 Python 列表（即 list 对象）。

**如何洗牌 How About Shuffling? **

按照目前的设计，FrenchDeck 是不能洗牌的，因为这摞牌是不可变的（immutable）：卡牌和它们的位置都是固定的，除非我们破坏这个类的封装性，直接对 `_cards `进行操作。第 11 章会讲到，其实只需要一行代码来实现 `__setitem__` 方法，洗牌功能就不是问题了。

## 1.2 如何使用特殊方法

1. 特殊方法的存在是为了被 Python 解释器调用的，你自己并不需要调用它们。如 应该使用 `len(my_object)` 若 `my_object` 为自定义类的对象，那么 Python 会自己去调用其中由你实现的 `__len__` 方法。
2. `__init__` 方法，你的代码里可能经常会用到它，目的是在你自己的子类的 `__init__` 方法中调用超类的构造器。

### 1.2.1 模拟数值类型

一个二维向量加法的例子，`Vector(2,4) + Vextor(2,1) =Vector(4,5)`



```python
'''
一个简单的二维向量类

'''

from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
```


```python
# 向量加法 :
v1 = Vector(2, 4)
v2 = Vector(2, 1)
v1 + v2
```




    Vector(4, 5)



`abs` 是一个内置函数，如果输入是整数或者浮点数，它返回的是输入值的绝对值；如果输入是复数（complex number），那么返回这个复数的模。为了保持一致性，我们的 API 在碰到 abs 函数的时候，也应该返回该向量的模：


```python
v = Vector(3, 4)
abs(v)
```




    5.0



标量乘法: 我们还可以利用 * 运算符来实现向量的标量乘法（即向量与数的乘法，得到的结果向量的方向与原向量一致 ，模变大）：
如果向量与负数相乘，得到的结果向量的方向与原向量相反。——编者注


```python
v * 3
```




    Vector(9, 12)




```python
abs(v * 3)
```




    15.0



上面提到的操作在代码里是用这些特殊方法实现的：`__repr__、__abs__、__add__ 和 __mul__`。虽然代码里有 6 个特殊方法，但这些方法（除了 `__init__`）并不会在这个类自身的代码中使用。即便其他程序要使用这个类的这些方法，也不会直接调用它们，就像我们在上面的控制台对话中看到的。上文也提到过，一般只有 Python 的解释器会频繁地直接调用这些方法。接下来看看每个特殊方法的实现。

### 1.2.2 字符串表示形式

Python 有一个内置的函数叫 repr，它能把一个对象用字符串的形式表达出来以便辨认，这就是“字符串表示形式”。在老的使用 % 符号的字符串格式中，这个函数返回的结果用来代替 %r 所代表的对象；同样，`str.format` 函数所用到的新式字符串格式化语法也是利用了 repr，才把 `!r` 字段变成字符串。在 `__repr__` 的实现中，我们用到了 %r 来获取对象各个属性的标准字符串表示形式——这是个好习惯，它暗示了一个关键：`Vector(1, 2)`和 `Vector('1', '2')` 是不一样的，后者在我们的定义中会报错，因为向量对象的构造函数只接受数值，不接受字符串 。

```
def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
```
1.`__repr__` = (represent) 所返回的字符串应该准确、无歧义，并且尽可能表达出如何用代码创建出这个被打印的对象。因此这里使用了类似调用对象构造器的表达形式（比如 Vector(3, 4) 就是个例子）。
2.`__repr__` 和` __str__` 的区别在于，后者是在 str() 函数被使用，或是在用 print 函数打印一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好。
3.如果你只想实现这两个特殊方法中的一个，`__repr__` 是更好的选择，因为如果一个对象没有 `__str__` 函数，而 Python 又需要调用它的时候，解释器会用 `__repr__` 作为替代。

### 1.2.3 算术运算符

通过 `__add__` 和` __mul__`，示例 1-2 为向量类带来了 + 和 * 这两个算术运算符。值得注意的是，这两个方法的返回值都是新创建的向量对象，被操作的两个向量（self 或 other）还是原封不动，代码里只是读取了它们的值而已。

### 1.2.4 自定义的布尔值

1.为了判定一个值 x 为真还是为假，Python 会调用 bool(x)，这个函数只能返回 True 或者 False。任何对象都可以用于需要布尔值的上下文中（比如 if 或 while 语句，或者 and、or 和 not 运算符）
2.我们对 `__bool__` 的实现很简单，如果一个向量的模是 0，那么就返回 False，其他情况则返回 True。因为 `__bool__` 函数的返回类型应该是布尔型，所以我们通过 bool(abs(self)) 把模值变成了布尔值。 没有 `__bool__`则调用 `x.__len__()` 0 返回 False else True。
3.让 `Vector.__bool__` 更高效

```
def __bool_(self):
    return bool(self.x or self.y)
```

## 1.3 特殊方法一览

[Python 语言参考手册中的“DataModel”](https://docs.python.org/3/reference/datamodel.html)（https://docs.python.org/3/reference/datamodel.html）

## 1.4 为什么len不是普通方法

“Python之禅”（https://www.python.org/doc/humor/#the-zen-of-python）
“实用胜于纯粹。
1.背后的原因是 CPython 会直接从一个 C 结构体里读取对象的长度，完全不会调用任何方法。获取一个集合中元素的数量是一个很常见的操作，在str、list、memoryview 等类型上，这个操作必须高效。
2.换句话说，len 之所以不是一个普通方法，是为了让 Python 自带的数据结构可以走后门，abs 也是同理。但是多亏了它是特殊方法，我们也可以把 len 用于自定义数据类型。

## 1.5 本章小结

通过实现特殊方法，自定义数据类型可以表现得跟内置类型一样，从而让我们写出更具表达力的代码——或者说，更具 Python 风格的代码。

## 1.6 延伸阅读

1.对本章内容和本书主题来说，Python 语言参考手册里的“Data Model”一章（https://docs.python.org/3/reference/datamodel.html）
是最符合规范的知识来源。
2.Martelli 是 StackOverflow 上的高产贡献者https://stackoverflow.com/users/95810/alex-martelli


---
 
**PS: 欢迎扫码关注公众号：「SelfImprovementLab」！专注「深度学习」，「机器学习」，「人工智能」,「Python」。以及 「早起」，「阅读」，「运动」，「英语 」「其他」不定期建群 打卡互助活动。**

<center><img src="http://upload-images.jianshu.io/upload_images/1157146-cab5ba89dfeeec4b.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240"></center>
