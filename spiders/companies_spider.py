import scrapy
import json
import csv

class CompaniesSpiderSpider(scrapy.Spider):
    name = "companies_spider"
    #website access information
    start_urls = ["https://www.hlth.com/2023event/attending-companies"]
    headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en,es-ES;q=0.9,es;q=0.8',
            'Referer': 'https://www.hlth.com/2023event/attending-companies',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        } 
  
    def parse(self, response):
        #url list creation based on the dynamic webpage
        url_list = []
        letter = 'a-b'
        for pag in range(8):
            url_list.append(f'https://www.hlth.com/api/attending-companies/{letter}/2023/{pag}?limit=100')
        letter = 'c-e'
        for pag in range(9):
            url_list.append(f'https://www.hlth.com/api/attending-companies/{letter}/2023/{pag}?limit=100')
        letter = 'f-l'
        for pag in range(12):
            url_list.append(f'https://www.hlth.com/api/attending-companies/{letter}/2023/{pag}?limit=100')
        letter = 'm-q'
        for pag in range(11):
            url_list.append(f'https://www.hlth.com/api/attending-companies/{letter}/2023/{pag}?limit=100')
        letter = 'r-t'
        for pag in range(10):
            url_list.append(f'https://www.hlth.com/api/attending-companies/{letter}/2023/{pag}?limit=100')
        letter = 'u-z'
        for pag in range(5):
            url_list.append(f'https://www.hlth.com/api/attending-companies/{letter}/2023/{pag}?limit=100')        
        
        #code to crawl the list of URLs
        for url in url_list:
            yield scrapy.Request(url, callback=self.parse_api, headers=self.headers)
    
    #code to extract the company name from JSON format    
    def parse_api(self, response):
        raw_data = response.body
        data = json.loads(raw_data)
        names = [record['Name'] for record in data['records']]
        for name in names:
            yield {
                'CompanyName' : name
            }
    
    #save the companies names in a cvs file
    custom_settings = {
        'FEEDS' : {
            'companies_names.csv' : {'format': 'csv', 'overwrite': True}
        }
    }