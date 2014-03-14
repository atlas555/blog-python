Title: 自己设计Pelican静态博客主题
Date: 2013-12-24 18:20
Category: Pelican
Tags: pelican, theme, jinja
Slug: pelican_theme
Author: Atlas 晓


pelican的静态博客有很多[博客主题][1]的，比如我还是比较喜欢的[bootstrap2][2]，[elegant][3]、[niu-x2][4]、[gum][5]等等。这些主题虽然设计的不错了，但是对我来说感觉还是感觉有些欠缺，折腾的命啊！
 
## 知识准备

###Div + Css 设计

我设计的博客结构采用div+css，这个结构比较好驾驭，随便找本书看看这方面的知识，很容易掌握（注意不是精通），对于一个搞后台开发的人来说，前端美化不拿手，怎么办呢，这个好解决，你上google或者baidu一艘，静态博客模板，比如这个<http://www.mianfeimoban.com>，一搜一大堆，当然这些模板只有一个index.html和一个css的文件。这个已经足以！

比我我现在的网站主页就是我选择比较喜欢的一款，原来样例如下：

<img src="http://ww4.sinaimg.cn/mw690/b7ba225djw1eedvk5q83hj20sg0h7wif.jpg" alt="zhangxiaolong.org" title="灰色世界" width="500"  />

下载地址如下：[灰色世界设计](http://vdisk.weibo.com/s/dhRlxPvqHmWsl)

下载自己喜欢的模板之后，就是大刀阔斧的修改啦！

###How to create themes for Pelican
自己设计模板主题，当然得知道[pelican支持的框架][6]是怎么样的吧？
我们来看看，pelican让我们follow的结构：

	├── static
	│   ├── css
	│   └── images
	└── templates
	    ├── archives.html         // to display archives
	    ├── period_archives.html  // to display time-period archives
		├── article.html          // processed for each article
	    ├── author.html           // processed for each author
    	├── authors.html          // must list all the authors
    	├── categories.html       // must list all the categories
    	├── category.html         // processed for each category
    	├── index.html            // the index. List all the articles
    	├── page.html             // processed for each page
    	├── tag.html              // processed for each tag
    	└── tags.html             // must list all the tags. Can be a tag cloud.

简单易明白吧，结构包括两个部分，static目录下包括css和image文件，而templates下则是我们的各个html文件。

详细的介绍和各个变量的介绍请查看官网文档：<http://docs.getpelican.com/en/3.3.0/themes.html>

###jinja模板引擎

Jinja2(<http://jinja.pocoo.org/docs/>) is a modern and designer friendly **templating language for Python**, modelled after Django’s templates. It is fast, widely used and secure with the optional sandboxed template execution environment:

	<title>{% block title %}{% endblock %}</title>
	<ul>
	{% for user in users %}
 		 <li><a href="{{ user.url }}">{{ user.username }}</a></li>
	{% endfor %}
	</ul>

这个之前你打开某个现有模板的某个文件，比如index.html，会看到一些类似的内容，这就是jinja模板语言，需要我们去着重看懂修改的地方！


## 设计自己的博客主题
使用jinja的博客模板，如果冲头开始写代码的话需要花费比较长的时间，我这里直接是用的是本文中提到的那个主题gum框架为基础，进行自我设计。

gum框架比较满足我的需求，**主题分布为两列模式，包括head、left、right、footer这四个部分**。顾名思义，

head： 博客名字部分，副标题、导航等；

left： 是文章的主题部分，包含index主页，article部分，tag、cagelotory等的显示，文章评论和分享；

right：包括这么几个模块，文章分类、文章tags、最热文章、最新post等等可定制模块。这里的模块可以自由定制添加或者删除。

footer：博客协议、署名、版权、包括google分析的脚本等；

了解自己要做的博客整体结构之后，就是修改我们下载好的静态博客模板啦，这里就是需要div+css技术的知识了，将静态模板融入到这个框架之中，并修改使之契合。

（1）将博客模板的index.html和css文件替换gum框架中的，并且删除gum中多余不需要的文件，包括css，js，image等等。修改css代码和html代码，这块通过chrome或者foxfire等的调试工具调试html和css。

（2）咱们一步一步来做，首先修改简单的几个部分，包括head、footer，这部分很容易，略过；

（3）实际上最麻烦的地方是在left部分，这部分一开始要显示首页index，然后是article文章、标签或者分类目录，主要是修改templates下的一系列html文件。**jinja模板引擎的知识该排上用场了**

（4）right部分相对来说自由度很大，根据你自己的需求添加一些模块（box），我在博客中初步添加了日志分类、标签云、最热文章、最近发表、最新评论、文章归档。

OK，完成4大部分改造之后，我们的博客主题基本上已经搭建完成了，你会发现我们只是借用了gum的大框架，并没有使用他的一些细节东西，抛去不合适的就好！

几篇pelican静态博客的相关文章：

1. 《[Pelican + Github 搭建自己的静态博客][7]》
2. 《[Pelican静态博客添加多说评论、加this分享、优秀插件、绑定域名][8]》
3. 《[Pelican静态博客添加自定制的功能模块][9]》
4.  [我的pelican博客-todolist][10]

（全文完）

[1]:https://github.com/getpelican/pelican-themes
[2]:http://www.dongxf.com/
[3]:http://oncrashreboot.com/elegant-best-pelican-theme-features
[4]:http://blog.atime.me/
[5]:https://github.com/getpelican/pelican-themes/tree/master/gum
[6]:http://docs.getpelican.com/en/3.3.0/themes.html
[7]:http://zhangxiaolong.org/pages/2013/12/23/pelican_github/
[8]:http://zhangxiaolong.org/pages/2013/12/24/pelican_autochange/
[9]:http://zhangxiaolong.org/pages/2013/12/24/pelican_autofix/
[10]:http://zhangxiaolong.org/pages/2013/12/24/pelican_todo/
