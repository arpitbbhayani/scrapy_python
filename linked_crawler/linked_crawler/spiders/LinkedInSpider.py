__author__ = 'devilo'

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from linked_crawler.items import Experience, ProfileData, Education, Project
from scrapy.selector import Selector

class LinkedInSpider(CrawlSpider):

    '''
        "http://www.linkedin.com/directory/people-a-87-15-70"
        "http://www.linkedin.com/pub/dir/Arpit/Bhayani"
    '''
    name = "LinkedinSpider"
    start_urls = [
        "http://www.linkedin.com/directory/people-a-87-15-70"
    ]
    allowed_domains = ["linkedin.com"]

    rules = (
        Rule(SgmlLinkExtractor(allow=("/*/",), restrict_xpaths=('//ul[@class="directory"]/li/*','//h2/strong/*',)),
        callback='parse_items',
        follow=True),
    )

    def parse_items(self , response):

        profile_data = ProfileData()
        list_exp = []
        list_edu = []
        list_pro = []

        if response.url.find('/pub/dir') == -1 and response.url.find('/directory/') == -1:
            selector = Selector(response)

            profile_data["profile_url"] = response.url

            profile_experience_xpath = selector.xpath('//div[@id="profile-experience"]')
            list_of_experience = profile_experience_xpath.xpath('.//div[contains(@class,"experience")]')

            for experience in list_of_experience:

                exp = Experience()

                exp["exp_title"]        = experience.xpath('.//*[@class="postitle"]//*[@class="title"]/text()').extract()
                exp["exp_organization"] = experience.xpath('.//*[@class="postitle"]//*[@class="org summary"]/text()').extract()
                exp["exp_duration"]     = experience.xpath('.//*[@class="duration"]/text()').extract()

                list_exp.append(exp)


            profile_education_xpath = selector.xpath('//div[@id="profile-education"]')
            list_of_education = profile_education_xpath.xpath('.//div[contains(@class,"education")]')
            for education in list_of_education:

                edu = Education()
                edu["edu_name"]        = education.xpath('h3/text() | h3/a/text()').extract()
                edu["edu_degree"]      = education.xpath('.//*[@class="degree"]/text()').extract()
                edu["edu_major"]       = education.xpath('.//*[@class="major"]/text()').extract()
                edu["edu_dstart"]      = education.xpath('.//*[@class="dtstart"]/text()').extract()
                edu["edu_dend"]        = education.xpath('.//*[@class="dtend"]/text()').extract()

                list_edu.append(edu)


            profile_projects_xpath = selector.xpath('//div[@id="profile-projects"]')
            list_of_projects = profile_projects_xpath.xpath('.//li[contains(@class,"project")]')
            for project in list_of_projects:

                pro = Project()
                pro["pro_name"]       = project.xpath('./*/*/text()').extract()
                pro["pro_desc"]       = project.xpath('.//*[@class=" \'\'"]/text()').extract()
                pro["pro_team"]       = project.xpath('.//*[@class="attribution"]/a/text()').extract()

                list_pro.append(pro)


        profile_data["profile_experience"] = list_exp
        profile_data["profile_education"]  = list_edu
        profile_data["profile_projects"]   = list_pro
        return profile_data