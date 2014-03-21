Scrapy
=======================

Installation
-----------------------
To install scrapy on Ubuntu
>       sudo apt-get install python-dev
>	sudo apt-get install python-pip
>       sudo pip install Scrapy

Source Code of Scrapy : https://github.com/scrapy/scrapy

Examples
-----------------------
- hello_world <br/>
	This is the hello world example for scrapy. In this example we simple create a spider and craw a website and print its contents onto the screen.
- basic_spider<br/>
	This is a simple one page parser that generates a csv file out of it.
- recursive-spider<br/>
	This is a recursiver scrapper which navigates through the link and scrapes each and every page and outputs the scrapped doc into csv document.
- linkedin-crawler<br/>
	This is a linkedin crawler that craws the linkedin public directory. Currently this is in development phase. This execution of the crawler generates the XML file with utf-8 encoding.

How to Execute
---------------------
> 1. Download the repository
>		<code>git clone https://github.com/arpitbbhayani/scrapy_python.git</code>
> 2. Install scrapy and setup your machine
>		<code>sudo apt-get install python-dev</code>
>		<code>sudo apt-get install python-pip</code>
>		<code>sudo pip install Scrapy</code>
> 3. Execute a spider
>	a. hello-world
>		scrapy runspider scrapy_python/hello_world/hello_world/spiders/hello_world_spider.py
>	b. basic-spider
>		scrapy runspider scrapy_python/basic_spider/basic_spider/spiders/BasicSpider.py
>	c. recursive-spider
>		scrapy runspider scrapy_python/recursive_spider/recursive_spider/spiders/BasicSpider.py
>	d. linkedin-crawler
>		scrapy runspider scrapy_python/linkedin_crawler/linkedin_crawler/spiders/LinkedInSpider.py

Tutorials
-----------------------
- http://doc.scrapy.org/en/latest/intro/tutorial.html
- http://mherman.org/blog/2012/11/05/scraping-web-pages-with-scrapy/
- http://mherman.org/blog/2012/11/08/recursively-scraping-web-pages-with-scrapy/#.Uyp-fnWSySQ

Good GitRepository
-----------------------
- https://github.com/yatish27/linkedin-scraper
