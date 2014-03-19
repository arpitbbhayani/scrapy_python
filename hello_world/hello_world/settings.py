# Scrapy settings for hello_world project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'hello_world'

SPIDER_MODULES = ['hello_world.spiders']
NEWSPIDER_MODULE = 'hello_world.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hello_world (+http://www.yourdomain.com)'
