Title: Pelican + Github 搭建自己的静态博客
Date: 2013-12-23 10:20
Category: Pelican
Tags: pelican, Github, 静态博客
Slug: pelican_github
Author: Atlas 晓

之前在Github上使用基本的[jekyll][1]模板搭建过一个博客，但是那时候前端技术的水平有限，搭出来的博客很不好看，一些基本的功能实现不出来，

之后又转向了[Octopress][2]模板，它是R系语言的编写的jekyll模板，又上手操作开发了一段时间，已经基本做出来了，但是奈何主题模板博主觉得都不好看，所以自己操作来做，发现Ruby语言不好下手啊，折腾了好久没有修改成博主喜欢的样式。

最后，同学推荐有一个使用Python语言写的[Pelican][3]静态网站生成器，眼前一亮，这个不错啊，python正在学习的过程中，下定决心就这个了。所以就有了下面的这番折腾！

##Pelican
Pelican是一个用**Python语言编写的静态网站生成器**，支持使用restructuredText和Markdown写文章，配置灵活，扩展性强。目前Pelican已发布3.2.2版本，有许多优秀的主题和插件可供使用。

Pelican 的Github地址是：<https://github.com/getpelican/pelican>

> Pelican Static Site Generator, Powered by Python
> 
> Pelican is a static site generator, written in Python, that requires no database or server-side logic.

>Some of the features include:

> - Write your content in reStructuredText, [Markdown][4], or AsciiDoc formats
- Completely static output is easy to host anywhere
- Themes that can be customized via [Jinja][5] templates
- Publish content in multiple languages
- Atom/RSS feeds
- Code syntax highlighting
- Import from WordPress, Dotclear, RSS feeds, and other services
- Modular plugin system and corresponding [plugin repository][6]

只需要懂一些python语言的基本知识就可以看懂pelican是怎么讲markdown或者restructuredText转化为Github可以接收的html文本。其中，关于博客模板的使用，这里pelican使用的jinja的模板。
	
jinja，是继python的web框架[Django][7]之后的一个简单模板引擎。关于python更多web框架的对比，请看这里<http://feilong.me/2011/01/talk-about-python-web-framework>

> Jinja2 is a full featured **template engine** for **Python**. It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed.

OK，这里我多说了一下jinja模板那引擎，是有原因的，在后面你将看到怎么自己定制自己的博客主题！看懂这个模板很重要！

##Github

Github绝对是个好去处，如果不熟悉，请自行百度或者google吧。

Git是版本管理的未来，他的优点我不再赘述，相关资料很多。推荐这本[Git中文教程][8]。

接下来，就是创建Github Pages了，
	
	什么是github page？ <http://pages.github.com/>
就是：The Automatic **Page Generator** can be used on GitHub to quickly create a **web page for a project, user or organization**.

**两种pages模式**

1. User/Organization Pages 个人或公司站点
	- 使用自己的用户名，每个用户名下面只能建立一个；
	- 资源命名必须符合这样的规则username/username.github.com；
	- 主干上内容被用来构建和发布页面

2. Project Pages 项目站点
	- gh-pages分支用于构建和发布；
	- 如果user/org pages使用了独立域名，那么托管在账户下的所有project pages将使用相同的域名进行重定向，除非project pages使用了自己的独立域名；
	- 如果没有使用独立域名，project pages将通过子路径的形式提供服务username.github.com/projectname；
	- 自定义404页面只能在独立域名下使用，否则会使用User Pages 404；
	
我是使用的第一种方式，直接利用master主干来构建和发布博客页面。如何构建请移步这里<http://pages.github.com/>。哈哈，偷懒下，就不翻译了，顺着做就好！这里比如已经建好了以下的工程项目：**example.github.com**

##利用Pelican快速构建自己的原始博客

首先是安装pelican，现在pelican是3.3.0版本的，**官方文档说明python版本得是2.7以上的，其中2.7支持的比较好！**博主刚开始用的是ubuntu默认的版本2.6.x，然后开始运行发现出错了，一看说明才明白的！

怎么安装呢，没有什么说明书是比官方材料更详细更好的！

安装步骤是：  利用pip安装来安装pelican，pip据说被另外一个取代了，但是还可以用的哦，或者利用 easy_install pelican 来安装，在或者下载pelican的github报道本地安装

	$ pip install pelican
或者，easy_install

	$ easy_install pelican
在或者，源码

	$ cd path-to-Pelican-source
	$ python setup.py install

**注意：这里使用virtualenv工具更加方便**，[virtualenv][9],virtualenv is a tool to create isolated Python environments.

	$ virtualenv ~/virtualenvs/pelican
	$ cd ~/virtualenvs/pelican
	$ . bin/activate

安装完pelican之后，别着急开始，先安装一个Markdown吧，我习惯使用markdown，	

	$ pip install Markdown

OK,到这里，pelican的环境部分我们已经配置完了，不过博主好奇刚才pelican的安装些什么了？也就是说pelican的依赖项：

> - feedgenerator, to generate the Atom feeds
- jinja2, for templating support
- pygments, for syntax highlighting
- docutils, for supporting reStructuredText as an input format
- pytz, for timezone definitions
- blinker, an object-to-object and broadcast signaling system
- unidecode, for ASCII transliterations of Unicode text
- six, for Python 2 and 3 compatibility utilities
- MarkupSafe, for a markup safe string implementation
- markdown, for supporting Markdown as an input format

好家伙，这么多啊，都看看 发现都不错！之后用到了在展开慢慢来说。

现在，让我们看看pelican是多么神奇吧，

	$ pelican-quickstart

运行命令之后，在当前目录下有以下的文件

	yourproject/
	├── content
	│   └── (pages)
	├── output
	├── develop_server.sh
	├── fabfile.py
	├── Makefile
	├── pelicanconf.py       # Main settings file
	└── publishconf.py       # Settings to use when ready to publish

我来说说都是些什么吧，

content这里是放置你的博文的，例如我的hello_python.md文章；pages是让永和可以自己定制些页面，比如aboutme.md等等页面；

output这个目录下放置的就是一会利用pelican生成的静态博客内容，当然是html的；

pelicanconf.py，是博客的配置文件，后面慢慢讲；

Makefile，make命令的配置文件，如果你懂linux这个就so easy！不过不懂也没事。

develop_server.sh 本地服务的脚本，用到在讲

大致看完这个之后，我们可以先写一篇自己的文章瞅瞅啊，文章模板如下：

	Title: My super title
	Date: 2010-12-03 10:20
	Category: Python
	Tags: pelican, publishing
	Slug: my-super-post
	Author: Alexis Metaireau
	Summary: Short version for index and feeds
	
	This is the content of my super blog post.

这里有个不好的地方，就是每次新建文章得自己来写tItle了什么的，待之后自己写个脚本来解决这个问题（留待解决的问题1）

写完保存后，要有以下的几个命令来生成博客内容啦

利用下面的命令来生成你的博客site：

	$ make html

我比较喜欢下面的这个命令，它是实时生成你的站点，就是说你修改你的博客什么的它会实时的生成！很棒吧。

	$ make regenerate

ok，生成之后，我们要看下显示的效果，用下面的命令吧

	$ make serve

下面这个我比较喜欢，理由同上面的那个regerate，哈哈

	$ make devserver

至此，我们可以在本地浏览刚才建好的博客了，地址就是<http://localhost:8000>

停止服务器则是下面的命令：

	$ ./develop_server.sh stop

生成站点的内容，我们刚才说过你可以在output目录下查看，我们看看刚才的范例文章的html文件吧：

	<html>
    <head>
        <title>My super title</title>
        <meta name="tags" content="thats, awesome" />
        <meta name="date" content="2012-07-09 22:28" />
        <meta name="category" content="yeah" />
        <meta name="author" content="Alexis Métaireau" />
        <meta name="summary" content="Short version for index and feeds" />
    </head>
    <body>
        This is the content of my super blog post.
    </body>
	</html>

是不是很方便，省去了自己写html的很多麻烦，**专注于写作**！

##在Github上显示自己的博客

接下来就是上传博客的时候了，我们要将生成的站点内容上传到刚才建好的**example.github.com**的工程master主干中，

进入到output目录下，
	
	git init
	git remote origin https://github.com/username/username.github.com.git 
生成 .git的目录，此时我们上传到github上面，

	git pull
	git add .
	git commit -m "update"
	git push origin master

此时可能需要输入账户和密码，稍后说明如何不需要每次push都输入账户和密码。

上传之后，我们打开github的这个项目，点击右侧的setting项，在下面可以看到github正在生成你的站点，稍等10多分钟，在浏览器中输入example.github.com，哈哈见证奇迹的时刻到了！

此篇文章主要介绍搭建原始的博客网站，其中没有设计到博客主题的定制，配置文件的优化修改，评论，等等需要美化的东西。

好东西需要慢慢来，下几篇文章预告：
	
1. 《[自己设计Pelican静态博客主题][10]》
2. 《[Pelican静态博客添加多说评论、加this分享、优秀插件、绑定域名][11]》
3. 《[Pelican静态博客添加自定制的功能模块][12]》
4.  [我的pelican博客-todolist][13]

**在完善完博客之后，我将把我的pelican静态博客主题进行开源共享！**

（全文完）

[1]:http://jekyllrb.com/
[2]:http://octopress.org/
[3]:http://blog.getpelican.com/
[4]:http://daringfireball.net/projects/markdown/
[5]:http://jinja.pocoo.org/
[6]:https://github.com/getpelican/pelican-plugins
[7]:https://www.djangoproject.com/
[8]:http://gitbook.liuhui998.com/
[9]:http://www.virtualenv.org/en/latest/virtualenv.html
[10]:http://zhangxiaolong.org/pages/2013/12/24/pelican_theme/
[11]:http://zhangxiaolong.org/pages/2013/12/24/pelican_autochange/
[12]:http://zhangxiaolong.org/pages/2013/12/24/pelican_autofix/
[13]:http://zhangxiaolong.org/pages/2013/12/24/pelican_todo/
