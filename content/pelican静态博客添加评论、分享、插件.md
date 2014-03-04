Title: Pelican静态博客添加多说评论、加this分享、优秀插件、绑定域名
Date: 2013-12-24 20:20
Category: Pelican
Tags: pelican
Slug: pelican_autochange
Author: Atlas 晓


通过上一篇搭建博客的文章，我们已经有了自己的博客站点，但是还是缺少一些完善的东西，比如说是评论系统、分享系统（这个绝对是互联网的趋势！）、sitemap等优秀的插件，当然有一个自己的域名可以更好的经营这个站点。

## 博客绑定域名
### 购买域名
我的域名是在[**godaddy**][1]上面买的，你可以在google上搜索godaddy的优惠码，域名比国内的便宜，info十几块钱吧，我的org域名是50+多，买了两年期限的，比较划算。godaddy上可以使用支付宝进行支付。购买流程呢，查看这篇文章吧，[**思齐博客**][2]比较详细，
### 域名解析
买完域名之后，使用godaddy的dns域名速度慢而且容易被墙，所以用国内的[**dnspod**][3]吧，百度google设置一下域名解析。

将申请的域名，比如我的域名zhangxiaolong.org这个域名解析到github的ip地址192.30.252.0/22--这个地址需要去github官网上查看。

### 博客绑定域名
域名买好了，dns解析好啦，只剩下最好一步了，在你博客output目录下新建CNAME文件，将你的域名写入到里面。ok,完事了。

## 添加多说评论
disqus评论系统我也用了一段时间，发现国内速度好慢，所以就替换成国内比较好的[**多说评论**][4]吧。
###文章的多说评论
因为是静态博客，所以我就用了通用代码就好，在多说官网上注册一个号码，然后点击工具一栏中，第一个选项显示的就是通用代码，比如我的,**short_name需要替换成你自己的！**

	<!-- Duoshuo Comment BEGIN -->
	<div class="ds-thread"></div>
	<script type="text/javascript">
	var duoshuoQuery = {short_name:"xxxxxx"};
	(function() {
		var ds = document.createElement('script');
		ds.type = 'text/javascript';ds.async = true;
		ds.src = 'http://static.duoshuo.com/embed.js';
		ds.charset = 'UTF-8';
		(document.getElementsByTagName('head')[0] 
		|| document.getElementsByTagName('body')[0]).appendChild(ds);
	})();
	</script>
	<!-- Duoshuo Comment END -->

将这段代码放到你要显示评论的地方就可以了，建议最好放到article.html模板中。

### 侧边栏添加最近评论模块
这部分内容请看下一篇文章《Pelican静态博客添加自定制的功能模块》中的介绍。

## 添加加this分享

个人认为互联网上分享是很重要的一个趋势，想在的公有云等等都是这么个理念在里头。这里添加[**JiaThis**][5],在官方网站上一步一步配置选择自己喜欢的样式，最后会生成代码，比如我的代码如下：

	<!-- JiaThis Button BEGIN -->
	<div class="jiathis_style">
	<a class="jiathis_button_qzone"></a>
	<a class="jiathis_button_tsina"></a>
	<a class="jiathis_button_tqq"></a>
	<a class="jiathis_button_weixin"></a>
	<a class="jiathis_button_renren"></a>
	<a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
	<a class="jiathis_counter_style"></a>
	</div>
	<script type="text/javascript" src="http://v3.jiathis.com/code/jia.js" charset="utf-8"></script>
	<!-- JiaThis Button END -->
最好，自己注册一下，查看分享流量。

## 添加优秀插件
pelican中有很多[**插件**][6],根据个人喜好及博客需求，我添加了四个个插件，分别是[**sitemap**][7]插件、[**random_article**][8]插件、[**neighbors**][9]、[**gzip_cache**][10].

###sitemap插件
> The sitemap plugin generates plain-text or XML sitemaps.

需要在pelicanconf.py配置文件中添加以下配置项：

	PLUGINS=['pelican.plugins.sitemap',]

	SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
	}
###random_article插件
> This plugin generates a html file which redirect to a random article using javascript's window.location. The generated html file is saved at SITEURL.
> Only published articles are listed to redirect.

To use it you have to add in your config file the name of the file to use:

	RANDOM = 'random.html'

Then in some template you add:

	<a href="{{ SITEURL }}/{{ RANDOM }}">random article</a>
###neighbors插件
>　This plugin adds next_article (newer) and prev_article (older) variables to the article's context

在需要显示的位置添加以下代码：

	<ul>
	{% if article.prev_article %}
    <li>
        <a href="{{ SITEURL }}/{{ article.prev_article.url}}">
            {{ article.prev_article.title }}
        </a>
    </li>
	{% endif %}
	{% if article.next_article %}
    <li>
        <a href="{{ SITEURL }}/{{ article.next_article.url}}">
            {{ article.next_article.title }}
        </a>
    </li>
	{% endif %}
	</ul>
###gzip_cache插件
> Certain web servers (e.g., Nginx) can use a static cache of gzip-compressed files to prevent the server from compressing files during an HTTP call. Since compression occurs at another time, these compressed files can be compressed at a higher compression level for increased optimization.

### 注意

在配置插件是都需要在pelicanconf.py配置文件中指明插件路径，否则pelican生成器不知道在那里找到！

（全文完）

我的几篇pelican静态博客的相关文章：

1. 《[Pelican + Github 搭建自己的静态博客][11]》
2. 《[自己设计Pelican静态博客主题][12]》
3. 《[Pelican静态博客添加自定制的功能模块][13]》
4.  [我的pelican博客-todolist][14]

（全文完）

[1]:http://www.godaddy.com/
[2]:http://www.siqiboke.com/post/19.html
[3]:https://www.dnspod.cn/
[4]:http://duoshuo.com/
[5]:http://www.jiathis.com/index2
[6]:https://github.com/getpelican/pelican-plugins
[7]:https://github.com/getpelican/pelican-plugins/tree/master/sitemap
[8]:https://github.com/getpelican/pelican-plugins/tree/master/random_article
[9]:https://github.com/getpelican/pelican-plugins/tree/master/neighbors
[10]:https://github.com/getpelican/pelican-plugins/tree/master/gzip_cache
[11]:http://zhangxiaolong.org/pages/2013/12/23/pelican_github/
[12]:http://zhangxiaolong.org/pages/2013/12/24/pelican_theme/
[13]:http://zhangxiaolong.org/pages/2013/12/24/pelican_autofix/
[14]:http://zhangxiaolong.org/pages/2013/12/24/pelican_todo/

