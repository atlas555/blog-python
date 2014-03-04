Title: 开始使用 Python 开发 Web 应用
Date: 2013-12-24 11:20
Category: Python
Tags: python, web
Slug: web_develop
Author: Atlas 晓

Python是一个通用编程语言，并很快成为每个自重程序员宝库中的一个必需品。
Python中有数不清的Web框架，从基本的微小架构到完整的架构，它们自有各自的优点。那么你准备使用它来做一些web开发，但在探讨细节之前，让我们从头开始。

##学习Python的基础
截至目前，Python有两个版本，2.7.5和3.3是目前Python的稳定版本。你选择哪个学习并不重要，因为区别非常小——尤其对于初学者而言。 但你应该知道，虽然Python 2有非常非常多的第三方支持，Python 3是设计语言的开发者关注的重点，很多第三方支持还没有移植到Python 3。这个选择需要你做出决定。然而，学习任何新的语言都会是一件令人却步的任务，找到合适的地方和人并从中学习是成功的一半。这是这篇指南的用处。让 Python简单、有趣并易于学习是你的蓝图。

> 对于初学者，Python 2和Python 3最大的不同很可能就是Python 2使用print不需要加括号，而Python 3需要，但就这么多。

- Codecademy python课程
	* Codecademy做了一项伟大的工作，将python的课程放在了一起，这对于初学者快速入门Python非常有用。

- ScreenCasts
	* 对于绝对的初学者，有一些非常棒的截屏视频。
	* 我学习python时参考的一些截屏视频是：
		* [ShowMeDo's Python Screencasts][1]

		* [TheNewBoston's Python Programming Tutorials][2]

两个教程非常优秀，你甚至可以在学习完这两个系列后开始编写脚本。非常建议观看下那些教程，它们是免费的，同时也是你将来参考时的非常好的资源。

- Python的官方网站
	* 当然，没有比官方python.org的文档更加好的资源了。但并不推荐给初学者，因为涉及的概念更加深入和高级，但它仍然是最好的资源。
	* 有了这个，你将拥有一些python知识，知道在python中怎么样处理东西。

###读一些书
有过剩的免费高质量的电子书可供选择。下面的快捷清单列出了一些最好的书。你可以免费下载它们的电子版，或者如果你想支持作者的话，你也可以选择购买纸质书籍（或者捐赠），我相信他们将非常感激这种方式。

[Think Python: How to Think Like a Computer Scientist][3]

> Think Python涉及理论方面的知识稍微多些。这可能会让初学者有些沮丧，但这本书在算法原理和高级概念上的相关知识非常值得一读。

[Invent With Python][4]

>如果“边学边做”是你的方式，那么构建自己的游戏将会是一个非常值得的经历！在这本书中，AI Sweigart假设没有Python的知识，并全程带领你构建自己的游戏。

###熟悉StackOverFlow
StackOverFlow不仅仅全是“新手”错误和问题；有一些非常聪明并乐于助人的人也在使用这个网站——从他们身上学习！

例如，看一下 [Python的隐藏特性][5]这个问题。你这里看到的很多提示和技巧可能很多正式的教程不会涉及，但它们对于中高级Python用户非常有用。

##进入Web开发
现在你完成了Python忍者训练，准备深入Ptyhon的Web开发，但现在的问题是有很多的框架，从中选择最好的框架非常困难，但从初学者的角度出发，[Flask][6]基本Web框架将非常适合Web开发入门，因为你仅仅需要知道Python就可以开始，而你已经学了很多知识了。

在你学习完Flask框架后，你将会知道创建静态页面非常简单，这是下一个问题出来了，使用它创建下一个web2.0的大应用合适么？答案是Yes，你可以用Flask创建任何你想的应用，但在通过很多步的努力之后，你会发现，你已经成功的重新建造了一个已经有的轮子，但它给予你巨大的灵活性和力量，一开始你可能会感觉势不可挡，而这也是很多初学者选择Django，然后在六个月左右换了其他的框架。

你可以读一下这个，知道哪些网站是由Flask驱动的

[The largest site built with Flask][7]

> 尽管Django和Pyramid也擅长Web开发，但他们是专为高级用户设计，而不是仅仅学习编写了几行python的初学者。但如果你想认真学习Web开发，学习Flask是个很好的入门框架，因为它不抽象任何事物，也没有任何魔法。

###常用的库和工具

[PyPy][8]

> 如果你要做的工作是计算密集型的，那么你会发现Python的性能是一个瓶颈，这时候你就需要PyPy。PyPy是Python解释器的一个替代品，可以有效加快处理速度。

[NumPy + SciPy][9]

> 这两个库通常是一起使用的（SciPy依赖于NumPy）。如果你需要做一些复杂的数值计算或科学研究工作，那么这两个库将是你的案头好友。NumPy和SciPy扩展了Python的数学函数功能，可以大大提高你的工作效率。

[BeautifulSoup][10]

> 正如其名，BeautifulSoup确实是非常优雅的。如果你需要解析一个HTML页面来获取一些信息，你应该知道这是非常烦人的事情。BeautifulSoup的作用就是为你做这些事情，并为你节省时间。强烈推荐使用。

[Python Image Library][11]

> The Python Image Library (PIL)是一个用来处理几乎所有图像操作的扩展库。如果你需要处理一个图像，PIL可以为你做很多。

了解了这些之后，你可以走上你自己的Python之路。

###一些Web开发库

[SQLAlchemy][12]

SQLAlchemy是Python的一个SQL和对象关系映射（ORM）工具集。它功能强大，并且很灵活，使得应用程序开发者可以方便地进行SQL操作。

[Alembic][13]

Alembic是一个轻量级的数据库集成工具，主要和[SQLAlchemy][14]协同使用。

###结论

今天就到此为止，欢迎随时分享你的想法。


本文中的所有译文仅用于学习和交流目的，转载请务必注明文章译者、出处、和本文链接<http://www.oschina.net/translate/get-started-python-web-development>;
我们的翻译工作遵照[CC][15]协议，如果我们的工作有侵犯到您的权益，请及时联系我们


（全文完）

[1]:http://showmedo.com/videotutorials/python
[2]:http://www.youtube.com/playlist?list=PLEA1FEF17E1E5C0DA&feature=plcp
[3]:http://www.greenteapress.com/thinkpython/thinkpython.html
[4]:http://inventwithpython.com/chapters/
[5]:http://stackoverflow.com/questions/101268/hidden-features-of-python
[6]:http://flask.pocoo.org/
[7]:http://www.quora.com/Flask/What-is-the-largest-site-created-using-Flask
[8]:http://pypy.org/
[9]:http://numpy.scipy.org/
[10]:http://www.crummy.com/software/BeautifulSoup/
[11]:http://www.pythonware.com/products/pil/
[12]:http://pypix.com/python/get-started-python-web-development/www.sqlalchemy.org
[13]:https://alembic.readthedocs.org/en/latest/
[14]:http://www.sqlalchemy.org/
[15]:http://zh.wikipedia.org/wiki/Wikipedia:CC


