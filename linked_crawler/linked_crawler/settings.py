# Scrapy settings for linked_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'linked_crawler'

SPIDER_MODULES = ['linked_crawler.spiders']
NEWSPIDER_MODULE = 'linked_crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'linked_crawler (+http://www.yourdomain.com)'
