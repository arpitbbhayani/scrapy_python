# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import io

class LinkedCrawlerPipeline(object):

    def __init__(self):
        self.file = io.open("/media/devilo/Disk Ahead/linkedin_dump.xml", "w" , encoding='utf8')
        self.file.write(u'<?xml version="1.0" encoding="utf8"?>\n')
        self.file.write(u'<pros>')

    def process_item(self, item, spider):

        if item.has_key("profile_url"):
            self.file.write(u'<pro>')

            # Write profile URL to the file
            self.file.write(u'<u>')
            self.file.write(item["profile_url"].replace(u'&' , '&amp;').replace(u'<' , '&lt;').replace(u'>' , '&gt;'))
            self.file.write(u'</u>')

            # Write experience to the file
            self.file.write(u'<ae>')
            if item.has_key("profile_experience"):

                for experience in item["profile_experience"]:
                    self.file.write(u'<e>')
                    self.file.write(u'<t>')
                    if len(experience["exp_title"]) != 0:
                        experience["exp_title"][0] = experience["exp_title"][0].strip()
                        self.file.write(experience["exp_title"][0].strip().replace(u'&' , '&amp;').replace(u'<' , '&lt;').replace(u'>' , '&gt;'))
                    self.file.write(u'</t>')
                    self.file.write(u'<o>')
                    if len(experience["exp_organization"]) != 0:
                        experience["exp_organization"][0] = experience["exp_organization"][0].strip()
                        self.file.write(experience["exp_organization"][0].replace(u'&' , '&amp;').replace(u'<' , '&lt;').replace(u'>' , '&gt;'))
                    self.file.write(u'</o>')
                    self.file.write(u'<d>')
                    if len(experience["exp_duration"]) != 0:
                        experience["exp_duration"][0] = experience["exp_duration"][0].strip()
                        self.file.write(experience["exp_duration"][0].replace(u'&' , '&amp;').replace(u'<' , '&lt;').replace(u'>' , '&gt;'))
                    self.file.write(u'</d>')
                    self.file.write(u'</e>')
            self.file.write(u'</ae>')

            # Write experience to the file
            self.file.write(u'<aed>')
            if item.has_key("profile_education"):

                for education in item["profile_education"]:
                    self.file.write(u'<ed>')
                    self.file.write(u'<n>')
                    if len(education["edu_name"]) != 0:
                        education["edu_name"][0] = education["edu_name"][0].strip()
                        self.file.write(education["edu_name"][0].replace(u'&' , '&amp;').replace(u'<' , '&lt;').replace(u'>' , '&gt;'))
                    self.file.write(u'</n>')
                    self.file.write(u'<dg>')
                    if len(education["edu_degree"]) != 0:
                        education["edu_degree"][0] = education["edu_degree"][0].strip()
                        self.file.write(education["edu_degree"][0].replace(u'&' , '&amp;').replace(u'<' , '&lt;').replace(u'>' , '&gt;'))
                    self.file.write(u'</dg>')
                    self.file.write(u'<m>')
                    if len(education["edu_major"]) != 0:
                        education["edu_major"][0] = education["edu_major"][0].strip()
                        self.file.write(education["edu_major"][0].replace(u'&' , '&amp;').replace(u'<' , '&lt;').replace(u'>' , '&gt;'))
                    self.file.write(u'</m>')
                    self.file.write(u'<ds>')
                    if len(education["edu_dstart"]) != 0:
                        education["edu_dstart"][0]= education["edu_dstart"][0].strip()
                        self.file.write(education["edu_dstart"][0].replace(u'&' , '&amp;').replace(u'<' , '&lt;').replace(u'>' , '&gt;'))
                    self.file.write(u'</ds>')
                    self.file.write(u'<de>')
                    if len(education["edu_dend"]) != 0:
                        education["edu_dend"][0] = education["edu_dend"][0].strip()
                        self.file.write(education["edu_dend"][0].replace(u'&' , '&amp;').replace(u'<' , '&lt;').replace(u'>' , '&gt;'))
                    self.file.write(u'</de>')
                    self.file.write(u'</ed>')
            self.file.write(u'</aed>')

            self.file.write(u'<ap>')
            if item.has_key("profile_projects"):

                for project in item["profile_projects"]:
                    self.file.write(u'<p>')
                    self.file.write(u'<n>')
                    if len(project["pro_name"]) != 0:
                        project["pro_name"][0] = project["pro_name"][0].strip()
                        self.file.write(project["pro_name"][0].replace(u'&' , '&amp;').replace(u'<' , '&lt;').replace(u'>' , '&gt;'))
                    self.file.write(u'</n>')
                    self.file.write(u'<d>')
                    if len(project["pro_desc"]) != 0:
                        project["pro_desc"][0] = project["pro_desc"][0].strip()
                        self.file.write(project["pro_desc"][0].replace(u'&' , '&amp;').replace(u'<' , '&lt;').replace(u'>' , '&gt;'))
                    self.file.write(u'</d>')
                    self.file.write(u'<at>')
                    if len(project["pro_team"]) != 0:
                        for team_member in project["pro_team"]:
                            self.file.write(u'<t>')
                            self.file.write(team_member.replace(u'&' , '&amp;').replace(u'<' , '&lt;').replace(u'>' , '&gt;'))
                            self.file.write(u'</t>')
                    self.file.write(u'</at>')
                    self.file.write(u'</p>')
            self.file.write(u'</ap>')

            self.file.write(u'</pro>')
        return item

    def close_spider(self, spider):
        self.file.write(u'</pros>')
        self.file.close()