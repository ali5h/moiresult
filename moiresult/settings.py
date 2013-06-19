# Scrapy settings for moiresult project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'moiresult'

SPIDER_MODULES = ['moiresult.spiders']
NEWSPIDER_MODULE = 'moiresult.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'moiresult (+http://www.yourdomain.com)'

# EXPORT_FORMAT = 'csv'
# EXPORT_FILE = 'scraped_items.csv'
# EXPORT_ENCODING = 'utf8'
# EXPORT_FIELDS = ('rec_id',
