# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Experience(Item):
    '''
        Experience class save the all information about the experience of member , as in
        1. Title
        2. Organization
        3. Duration

        exp_title           -> str
        exp_organization    -> str
        exp_duration        -> str
    '''
    exp_title           = Field()
    exp_organization    = Field()
    exp_duration        = Field()

class Education(Item):
    '''
        Education class save the all information about the education of member , as in
        1. Name
        2. Degree
        3. Major
        4. Duration_Start
        5. Duration_End

        edu_name         -> str
        edu_degree       -> str
        edu_major        -> str
        edu_dstart       -> str
        edu_dend         -> str
    '''
    edu_name            = Field()
    edu_degree          = Field()
    edu_major           = Field()
    edu_dstart          = Field()
    edu_dend            = Field()


class Project(Item):
    '''
        Project class save the all information about the project of member , as in
        1. Name
        2. Description
        3. Team Member

        pro_name         -> str
        pro_desc         -> str
        pro_team         -> str
    '''
    pro_name           = Field()
    pro_desc           = Field()
    pro_team           = Field()


class ProfileData(Item):
    '''
        ProfileData class save the all information about the profile , as in
        1. Profile URL
        2. Experience of the LinkedIn Member

        profile_url         -> str
        profile_experience  -> list of Experience()
        profile_education   -> list of Education()
        profile_projects   -> list of Project()
    '''
    profile_url         = Field()
    profile_experience  = Field()
    profile_education   = Field()
    profile_projects    = Field()
