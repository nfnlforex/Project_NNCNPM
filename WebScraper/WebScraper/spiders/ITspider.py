import scrapy


class ItspiderSpider(scrapy.Spider):
    name = "ITspider"
    allowed_domains = ["www.lix.polytechnique.fr"]
    start_urls = ["https://www.lix.polytechnique.fr/~hermann/conf.php"]

    def parse(self, response):
        events = response.css('tr')

        for event in events:
            name = event.css('td.confname a::text').get()
            location=event.css('td.location ::text').get()
            if event.css('td.now-deadline ::text').get() !=None:
                 deadline = event.css('td.now-deadline ::text').get()  
            else:
                deadline = event.css('td.deadline ::text').get()  

            date = event.css('td.date ::text').get()  
            notification = event.css('td.notification ::text').get() 
            if name!=None and location!=None and deadline!=None and date!=None and notification!=None:
                  yield {
                      'name': name,
                      'location':location,
                      'deadline': deadline,
                      'date': date,
                      'notification': notification,
               }
