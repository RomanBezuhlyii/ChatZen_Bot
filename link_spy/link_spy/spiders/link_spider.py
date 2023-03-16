import scrapy
from scrapy.http import Request
import json
import user_data as user

class Link():
    link = ''
    date = ''
    def write(self,filename):
        with open(filename,'w') as fh:
            json.dump(self,fh,cls=SpiderEncoder, indent=4)

class SpiderEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,Link):
            return {'link': o.link,
                    'date': o.date}
        return super().default(o)

class DynamicLinkSpider(scrapy.Spider):
    name = 'link_spider'
    start_urls = [
        "https://moderation.vlstats.com/home/login"
    ]
    link = ''

    def start_requests(self):
        return [Request(url = "https://moderation.vlstats.com/", callback = self.login)]

    def login(self, response):
        return scrapy.FormRequest('https://moderation.vlstats.com/home/login',
                                  formdata={"username": user.parse_login, "password": user.parse_password},
                                  callback=self.parse_url)

    def parse_url(self,response):
        yield response.follow('https://moderation.vlstats.com/agency/invitations',callback=self.parse)

    def parse(self, response, **kwargs):
        links = response.xpath("//div[@class='input-group']//input[@id='invitationLink-0']//@value").extract()[0]
        date = response.xpath("//div[@class='col-md-8']//small//text()").get()
        print('----------------------------------------------------')
        print(links)
        print(date)
        print('----------------------------------------------------')
        l = Link()
        l.link=links
        clear_date = date[date.find('until') + 6:]
        l.date = clear_date
        l.write('parse_data.txt')
