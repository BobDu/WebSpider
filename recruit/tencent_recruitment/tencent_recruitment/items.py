# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentRecruitmentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # ְλ��
    position_name = scrapy.Field()
    # ����
    country = scrapy.Field()
    # ����
    city = scrapy.Field()
    # ְλ���
    category = scrapy.Field()
    # ��ҵȺ
    business_group = scrapy.Field()
    # ��Ƹ����
    recruitment_type = scrapy.Field()
    # ��Ʒ����
    product_name = scrapy.Field()
    # ����ְ��
    responsibility = scrapy.Field()
    # ����Ҫ��
    requirement = scrapy.Field()
    # ����ʱ��
    release_time = scrapy.Field()
