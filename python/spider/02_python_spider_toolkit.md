## **这个列表包含与网页抓取和数据处理的Python库**

> http://www.ttlsa.com/

### **1. 网络**

#### **通用**

- [urllib](https://docs.python.org/3.4/library/urllib.html?highlight=urllib#module-urllib) -网络库(stdlib)。
- [requests](https://github.com/requests/requests) -网络库。
- grab – 网络库（基于pycurl）。
- [pycurl](https://github.com/pycurl/pycurl) – 网络库（绑定[libcurl](https://curl.haxx.se/libcurl/)）。
- [urllib3](https://github.com/shazow/urllib3) – Python HTTP库，安全连接池、支持文件post、可用性高。
- [httplib2](https://github.com/jcgregorio/httplib2) – 网络库。
- [RoboBrowser](https://github.com/jmcarp/robobrowser) – 一个简单的、极具Python风格的Python库，无需独立的浏览器即可浏览网页。
- [MechanicalSoup](https://github.com/hickford/MechanicalSoup) -一个与网站自动交互Python库。
- [Mechanize](https://github.com/jjlee/mechanize) -有状态、可编程的Web浏览库。
- [socket](https://docs.python.org/3/library/socket.html) – 底层网络接口(stdlib)。
- [Unirest for Python](https://github.com/Mashape/unirest-python) – Unirest是一套可用于多种语言的轻量级的HTTP库。
- [hyper](https://github.com/Lukasa/hyper) – Python的HTTP/2客户端。
- [PySocks](https://github.com/Anorov/PySocks) – SocksiPy更新并积极维护的版本，包括错误修复和一些其他的特征。作为socket模块的直接替换。

#### **异步**

- [treq](https://github.com/dreid/treq) – 类似于requests的API（基于twisted）。
- [aiohttp](https://github.com/KeepSafe/aiohttp) – asyncio的HTTP客户端/服务器(PEP-3156)。

### **2. 网络爬虫框架**

#### **功能齐全的爬虫**

- [grab](http://docs.grablib.org/en/latest/#grab-spider-user-manual) – 网络爬虫框架（基于pycurl/multicur）。
- [scrapy](https://scrapy.org/) – 网络爬虫框架（基于twisted），不支持Python3。
- [pyspider](https://github.com/binux/pyspider) – 一个强大的爬虫系统。
- [cola](https://github.com/chineking/cola) – 一个分布式爬虫框架。

#### **其他**

- [portia](https://github.com/scrapinghub/portia) – 基于Scrapy的可视化爬虫。
- [restkit](https://github.com/benoitc/restkit) – Python的HTTP资源工具包。它可以让你轻松地访问HTTP资源，并围绕它建立的对象。
- [demiurge](https://github.com/matiasb/demiurge) – 基于PyQuery的爬虫微框架。

### **3. HTML/XML解析器**

#### **通用**

- [lxml ](http://lxml.de/)– C语言编写高效HTML/ XML处理库。支持XPath。
- [cssselect](https://pythonhosted.org/cssselect) – 解析DOM树和CSS选择器。
- [pyquery](http://pythonhosted.org/pyquery/) – 解析DOM树和jQuery选择器。
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) – 低效HTML/ XML处理库，纯Python实现。
- [html5lib](http://html5lib.readthedocs.org/en/latest/) – 根据WHATWG规范生成HTML/ XML文档的DOM。该规范被用在现在所有的浏览器上。
- [feedparser](http://pythonhosted.org/feedparser/) – 解析RSS/ATOM feeds。
- [MarkupSafe](https://github.com/mitsuhiko/markupsafe) – 为XML/HTML/XHTML提供了安全转义的字符串。
- [xmltodict](https://github.com/martinblech/xmltodict) – 一个可以让你在处理XML时感觉像在处理JSON一样的Python模块。
- [xhtml2pdf](https://github.com/chrisglass/xhtml2pdf) – 将HTML/CSS转换为PDF。
- [untangle](https://github.com/stchris/untangle) – 轻松实现将XML文件转换为Python对象。

#### **清理**

- [Bleach](http://bleach.readthedocs.org/en/latest/) – 清理HTML（需要html5lib）。
- [sanitize](https://github.com/Alir3z4/sanitize) – 为混乱的数据世界带来清明。

### **4. 文本处理**

#### **用于解析和操作简单文本的库**

- **通用**
- [difflib](https://docs.python.org/2/library/difflib.html) – （Python标准库）帮助进行差异化比较。
- [Levenshtein](https://github.com/ztane/python-Levenshtein/) – 快速计算Levenshtein距离和字符串相似度。
- [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) – 模糊字符串匹配。
- [esmre](https://code.google.com/p/esmre/) – 正则表达式加速器。
- [ftfy](https://github.com/LuminosoInsight/python-ftfy) – 自动整理Unicode文本，减少碎片化。
- **转换**
- [unidecode](https://pypi.python.org/pypi/Unidecode) – 将Unicode文本转为ASCII。
- **字符编码**
- [uniout](https://github.com/moskytw/uniout) – 打印可读字符，而不是被转义的字符串。
- [chardet](https://github.com/chardet/chardet) – 兼容 Python的2/3的字符编码器。
- [xpinyin](https://github.com/lxneng/xpinyin) – 一个将中国汉字转为拼音的库。
- [pangu.py](https://github.com/vinta/pangu.py) – 格式化文本中CJK和字母数字的间距。
- **Slug化**
- [awesome-slugify](https://github.com/dimka665/awesome-slugify) – 一个可以保留unicode的Python slugify库。
- [python-slugify](https://github.com/un33k/python-slugify) – 一个可以将Unicode转为ASCII的Python slugify库。
- [unicode-slugify](https://github.com/mozilla/unicode-slugify) – 一个可以将生成Unicode slugs的工具。
- [pytils](https://github.com/j2a/pytils) – 处理俄语字符串的简单工具（包括pytils.translit.slugify）。
- **通用解析器**
- [PLY](http://www.dabeaz.com/ply/) – lex和yacc解析工具的Python实现。
- [pyparsing](http://pyparsing.wikispaces.com/) – 一个通用框架的生成语法分析器。
- **人的名字**
- [python-nameparser](https://github.com/derek73/python-nameparser) -解析人的名字的组件。
- **电话号码**
- [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) -解析，格式化，存储和验证国际电话号码。
- **用户代理字符串**
- [python-user-agents](https://github.com/selwin/python-user-agents) – 浏览器用户代理的解析器。
- [HTTP Agent Parser](https://github.com/shon/httpagentparser) – Python的HTTP代理分析器。

### **5. 特定格式文件处理**

#### **解析和处理特定文本格式的库**

- **通用**
- [tablib ](https://github.com/kennethreitz/tablib)– 一个把数据导出为XLS、CSV、JSON、YAML等格式的模块。
- [textract](https://github.com/deanmalmgren/textract) – 从各种文件中提取文本，比如 Word、PowerPoint、PDF等。
- [messytables](https://github.com/okfn/messytables) – 解析混乱的表格数据的工具。
- [rows](https://github.com/turicas/rows) – 一个常用数据接口，支持的格式很多（目前支持CSV，HTML，XLS，TXT – 将来还会提供更多！）。
- **Office**
- [python-docx](https://github.com/python-openxml/python-docx) – 读取，查询和修改的Microsoft Word2007/2008的docx文件。
- [xlwt](https://github.com/python-excel/xlwt) / [xlrd](https://github.com/python-excel/xlrd) – 从Excel文件读取写入数据和格式信息。
- [XlsxWriter](https://xlsxwriter.readthedocs.org/) – 一个创建Excel.xlsx文件的Python模块。
- [xlwings](http://xlwings.org/) – 一个BSD许可的库，可以很容易地在Excel中调用Python，反之亦然。
- [openpyxl](https://openpyxl.readthedocs.org/en/latest/) – 一个用于读取和写入的Excel2010 XLSX/ XLSM/ xltx/ XLTM文件的库。
- [Marmir](https://github.com/brianray/mm) – 提取Python数据结构并将其转换为电子表格。
- **PDF**
- [PDFMiner](https://github.com/euske/pdfminer) – 一个从PDF文档中提取信息的工具。
- [PyPDF2](https://github.com/mstamy2/PyPDF2) – 一个能够分割、合并和转换PDF页面的库。
- [ReportLab](http://www.reportlab.com/opensource/) – 允许快速创建丰富的PDF文档。
- [pdftables](https://pypi.python.org/pypi/pdftables) – 直接从PDF文件中提取表格。
- **Markdown**
- [Python-Markdown](https://github.com/waylan/Python-Markdown) – 一个用Python实现的John Gruber的Markdown。
- [Mistune](https://github.com/lepture/mistune) – 速度最快，功能全面的Markdown纯Python解析器。
- [markdown2](https://pypi.python.org/pypi/markdown2) – 一个完全用Python实现的快速的Markdown。
- **YAML**
- [PyYAML](http://pyyaml.org/) – 一个Python的YAML解析器。
- **CSS**
- [cssutils](https://pypi.python.org/pypi/cssutils/) – 一个Python的CSS库。
- **ATOM/RSS**
- [feedparser](http://pythonhosted.org/feedparser/) – 通用的feed解析器。
- **SQL**
- [sqlparse](https://sqlparse.readthedocs.org/) – 一个非验证的SQL语句分析器。
- **HTTP**
- [http-parser](https://github.com/benoitc/http-parser) – C语言实现的HTTP请求/响应消息解析器。
- **微格式**
- [opengraph](https://github.com/erikriver/opengraph) – 一个用来解析Open Graph协议标签的Python模块。
- **可移植的执行体**
- [pefile](https://github.com/erocarrera/pefile) – 一个多平台的用于解析和处理可移植执行体（即PE）文件的模块。
- **PSD**
- [psd-tools](https://github.com/kmike/psd-tools) – 将Adobe Photoshop PSD（即PE）文件读取到Python数据结构。

### **6. 自然语言处理**

#### **处理人类语言问题的库**

- [NLTK](http://www.nltk.org/) -编写Python程序来处理人类语言数据的最好平台。
- [Pattern](http://www.clips.ua.ac.be/pattern) – Python的网络挖掘模块。他有自然语言处理工具，机器学习以及其它。
- [TextBlob](http://textblob.readthedocs.org/) – 为深入自然语言处理任务提供了一致的API。是基于NLTK以及Pattern的巨人之肩上发展的。
- [jieba ](https://github.com/fxsjy/jieba)– 中文分词工具。
- [SnowNLP](https://github.com/isnowfy/snownlp) – 中文文本处理库。
- [loso](https://github.com/fangpenlin/loso) – 另一个中文分词库。
- [genius](https://github.com/duanhongyi/genius) – 基于条件随机域的中文分词。
- [langid.py](https://github.com/saffsd/langid.py) – 独立的语言识别系统。
- [Korean](https://korean.readthedocs.org/) – 一个韩文形态库。
- [pymorphy2](https://github.com/kmike/pymorphy2) – 俄语形态分析器（词性标注+词形变化引擎）。
- [PyPLN](https://github.com/NAMD/pypln.backend) – 用Python编写的分布式自然语言处理通道。这个项目的目标是创建一种简单的方法使用NLTK通过网络接口处理大语言库。

### **7. 浏览器自动化与仿真**

- [selenium ](http://selenium.googlecode.com/git/docs/api/py/api.html)– 自动化真正的浏览器（Chrome浏览器，火狐浏览器，Opera浏览器，IE浏览器）。
- [Ghost.py](http://carrerasrodrigo.github.io/Ghost.py/) – 对PyQt的webkit的封装（需要PyQT）。
- [Spynner](https://github.com/makinacorpus/spynner) – 对PyQt的webkit的封装（需要PyQT）。
- [Splinter](https://github.com/cobrateam/splinter) – 通用API浏览器模拟器（selenium web驱动，Django客户端，Zope）。

### **8. 多重处理**

- [threading](https://docs.python.org/2.7/library/threading.html) – Python标准库的线程运行。对于I/O密集型任务很有效。对于CPU绑定的任务没用，因为python GIL。
- [multiprocessing](https://docs.python.org/2.7/library/multiprocessing.html) – 标准的Python库运行多进程。
- [celery](http://www.celeryproject.org/) – 基于分布式消息传递的异步任务队列/作业队列。
- [concurrent-futures](https://docs.python.org/3/library/concurrent.futures.html) – concurrent-futures 模块为调用异步执行提供了一个高层次的接口。

### **9. 异步**

#### **异步网络编程库**

- [asyncio](https://docs.python.org/3/library/asyncio.html) – （在Python 3.4 +版本以上的 Python标准库）异步I/O，时间循环，协同程序和任务。
- [Twisted](https://twistedmatrix.com/trac/) – 基于事件驱动的网络引擎框架。
- [Tornado](http://www.tornadoweb.org/) – 一个网络框架和异步网络库。
- [pulsar](https://github.com/quantmind/pulsar) – Python事件驱动的并发框架。
- [diesel ](https://github.com/jamwt/diesel)– Python的基于绿色事件的I/O框架。
- [gevent](http://www.gevent.org/) – 一个使用greenlet 的基于协程的Python网络库。
- [eventlet](http://eventlet.net/) – 有WSGI支持的异步框架。
- [Tomorrow](https://github.com/madisonmay/Tomorrow) – 异步代码的奇妙的修饰语法。

### **10. 队列**

- [celery](http://www.celeryproject.org/) – 基于分布式消息传递的异步任务队列/作业队列。
- [huey](https://github.com/coleifer/huey) – 小型多线程任务队列。
- [mrq](https://github.com/pricingassistant/mrq) – Mr. Queue – 使用[redis](http://www.ttlsa.com/redis/) & Gevent 的Python分布式工作任务队列。
- [RQ](http://python-rq.org/docs/) – 基于Redis的轻量级任务队列管理器。
- [simpleq](https://github.com/rdegges/simpleq) – 一个简单的，可无限扩展，基于Amazon SQS的队列。
- [python-gearman](https://github.com/Yelp/python-gearman) – Gearman的Python API。

### **11. 云计算**

- [picloud](http://docs.picloud.com/) – 云端执行Python代码。
- [dominoup.com](http://www.dominodatalab.com/) – 云端执行R，Python和matlab代码。

### **12. 电子邮件**

#### **电子邮件解析库**

- [flanker](https://github.com/mailgun/flanker) – 电子邮件地址和Mime解析库。
- [Talon](https://github.com/mailgun/talon) – Mailgun库用于提取消息的报价和签名。

### **13. 网址和网络地址操作**

#### **解析/修改网址和网络地址库**

- **URL**
- [furl](https://github.com/gruns/furl) – 一个小的Python库，使得操纵URL简单化。
- [purl](https://github.com/codeinthehole/purl) – 一个简单的不可改变的URL以及一个干净的用于调试和操作的API。
- [urllib.parse](https://docs.python.org/3/library/urllib.parse.html) – 用于打破统一资源定位器（URL）的字符串在组件（寻址方案，网络位置，路径等）之间的隔断，为了结合组件到一个URL字符串，并将“相对URL”转化为一个绝对URL，称之为“基本URL”。
- [tldextract](https://github.com/john-kurkowski/tldextract) – 从URL的注册域和子域中准确分离TLD，使用公共后缀列表。
- **网络地址**
- [netaddr](https://github.com/drkjam/netaddr) – 用于显示和操纵网络地址的Python库。

### **14. 网页内容提取**

#### **提取网页内容的库**

- **HTML页面的文本和元数据**
- [newspaper](https://github.com/codelucas/newspaper) – 用Python进行新闻提取、文章提取和内容策展。
- [html2text](https://github.com/Alir3z4/html2text) – 将HTML转为Markdown格式文本。
- [python-goose](https://github.com/grangier/python-goose) – HTML内容/文章提取器。
- [lassie](https://github.com/michaelhelmick/lassie) – 人性化的网页内容检索工具
- [micawber](https://github.com/coleifer/micawber) – 一个从网址中提取丰富内容的小库。
- [sumy](https://github.com/miso-belica/sumy) -一个自动汇总文本文件和HTML网页的模块
- [Haul](https://github.com/vinta/Haul) – 一个可扩展的图像爬虫。
- [python-readability](https://github.com/buriy/python-readability) – arc90 readability工具的快速Python接口。
- [scrapely](https://github.com/scrapy/scrapely) – 从HTML网页中提取结构化数据的库。给出了一些Web页面和数据提取的示例，- - - scrapely为所有类似的网页构建一个分析器。
- **视频**
- [youtube-dl](http://rg3.github.io/youtube-dl/) – 一个从YouTube下载视频的小命令行程序。
- [you-get](http://www.soimort.org/you-get/) – Python3的YouTube、优酷/ Niconico视频下载器。
- **维基**
- [WikiTeam](https://github.com/WikiTeam/wikiteam) – 下载和保存wikis的工具。

### **15. WebSocket的库**

#### **用于WebSocket的库**

- [Crossbar](https://github.com/crossbario/crossbar/) – 开源的应用消息传递路由器（Python实现的用于Autobahn的WebSocket和WAMP）。
- [AutobahnPython](https://github.com/tavendo/AutobahnPython) – 提供了WebSocket协议和WAMP协议的Python实现并且开源。
- [WebSocket-for-Python](https://github.com/Lawouach/WebSocket-for-Python) – Python 2和3以及PyPy的WebSocket客户端和服务器库。

### **16. DNS解析**

- [dnsyo](https://github.com/samarudge/dnsyo) – 在全球超过1500个的DNS服务器上检查你的DNS。
- [pycares](https://github.com/saghul/pycares) – c-ares的接口。c-ares是进行DNS请求和异步名称决议的C语言库。

### **17. 计算机视觉**

- [OpenCV](https://github.com/Itseez/opencv) – 开源计算机视觉库。
- [SimpleCV ](https://github.com/sightmachine/SimpleCV)– 用于照相机、图像处理、特征提取、格式转换的简介，可读性强的接口（基于OpenCV）。
- [mahotas](https://github.com/luispedro/mahotas) – 快速计算机图像处理算法（完全使用 C++ 实现），完全基于 numpy 的数组作为它的数据类型。

### **18. 代理服务器**

- [shadowsocks](https://github.com/shadowsocks/shadowsocks) – 一个快速隧道代理，可帮你穿透防火墙（支持TCP和UDP，TFO，多用户和平滑重启，目的IP黑名单）。
- [tproxy](https://github.com/benoitc/tproxy) – tproxy是一个简单的TCP路由代理（第7层），基于Gevent，用Python进行配置。

### **19. 其他Python工具列表**

- [awesome-python](https://github.com/vinta/awesome-python)
- [pycrumbs](https://github.com/kirang89/pycrumbs/blob/master/pycrumbs.md)
- [python-github-projects](https://github.com/checkcheckzz/python-github-projects)
- [python_reference](https://github.com/rasbt/python_reference)
- [pythonidae](https://github.com/svaksha/pythonidae)