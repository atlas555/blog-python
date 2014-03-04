Title: web搜索引擎工作原理和体系结构
Date: 2013-12-23 11:20
Category: 搜索引擎
Tags: 体系结构
Slug: search_article
Author: Atlas 晓



###学习摘要

搜索引擎：一个**网络应用软件系统**

工作原理：

**三段式**工作流程：

    <-->搜集<-->预处理<-->服务<-->

信息搜集：

    定期搜集
	增量搜集
	先宽搜索

信息预处理：

	* 关键词的提取  -- ”切词“
	* 重复或者转载网页的消除 
	* 连接分析 --TF\DF
	* 网页重要程度的计算 --Pagerank

信息查询服务：

    如何从集合生成一个列表，是服务子系统的主要工作。

	* 查询方式和匹配
	* 结果排序
	* 文档摘要  -- 静态方式 、 动态摘要（目前主要）

###体系结构
图示： 搜索引擎提携结构
![搜索引擎提携结构](http://d.pcs.baidu.com/thumbnail/8c6bcebdf6b7e3fd8fd7f79f9e2e7c38?fid=3741478698-250528-747803702&time=1387854022&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-GEjrc%2Bw2A3U6SciWcgP2xSwABAM%3D&expires=1h&prisign=unkown&r=404878228&size=c850_u580&quality=100)


