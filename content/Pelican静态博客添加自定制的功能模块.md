Title: Pelican静态博客添加自定制的功能模块
Date: 2013-12-24 14:20
Category: Pelican
Tags: pelican, sitemap
Slug: pelican_autofix
Author: Atlas 晓

博客大框架已经搭好了，基本的功能已经完善，剩下的工作就是我们自己的定制了！

日志2013-12-24 14:20写作,持续UPDATING...

### 最近发表文章列表

### 标签云模块修改

### 最近评论模块
在侧边栏最近评论模块中添加以下的代码：<http://dev.duoshuo.com/docs/4ff28d95552860f21f000010>
注意替换你的自己的二级域名:!
	
	<ul class="ds-recent-comments" data-num-items="10"></ul>
	<!--多说js加载开始，一个页面只需要加载一次 -->
	<script type="text/javascript">
	var duoshuoQuery = {short_name:"您的多说二级域名"};
	(function() {
    var ds = document.createElement('script');
    ds.type = 'text/javascript';ds.async = true;
    ds.src = 'http://static.duoshuo.com/embed.js';
    ds.charset = 'UTF-8';
    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ds);
	})();
	</script>
	<!--多说js加载结束，一个页面只需要加载一次 -->
### 最热文章列表
在侧边栏最热文章下添加以下的模块:<http://dev.duoshuo.com/docs/5020f288e759c1107f00000c>

多说代码如下：
	<ul  class="ds-top-threads" data-range="weekly" data-num-items="5"></ul>
	<!--多说js加载开始，一个页面只需要加载一次 -->
	<script type="text/javascript">
	var duoshuoQuery = {short_name:"您的多说二级域名"};
	(function() {
    var ds = document.createElement('script');
    ds.type = 'text/javascript';ds.async = true;
    ds.src = 'http://static.duoshuo.com/embed.js';
    ds.charset = 'UTF-8';
    (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ds);
	})();
	</script>
	<!--多说js加载结束，一个页面只需要加载一次 -->

其中，以下代码是必须的。而在每个页面中，如果使用多个多说控件，只需要添加一次多说js

	<ul  class="ds-top-threads" data-range="weekly" data-num-items="5"></ul>
参数说明

	//以下参数均为可选参数
 	data-range="weekly"      //热评统计时间范围：daily：日；weekly：周；monthly：月；默认值daily
	data-num-items="5"     //显示最新文章的条数，默认值5



###博客中几篇pelican静态博客的相关文章：

1. 《Pelican + Github 搭建自己的静态博客》
2. 《自己设计Pelican静态博客主题》
3. 《Pelican静态博客添加多说评论、加this分享、优秀插件、绑定域名》
4.  我的pelican博客-todolist

（全文完）


