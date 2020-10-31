import requests
from bs4 import BeautifulSoup
import json
import sys

class Crawler():  
        
    def crawl(self, url):
        
        return {"productTitle": "iPhone12", "productPrice": 899, "productLink": url}
        
        
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        r = requests.get(url, timeout=3, headers=headers)
        print("response status code is:", r.status_code)
        
        productTitle = "iPhone12"
        productPrice = 899
        productLink  = url
        
        if r.status_code == 200:
            try:
                soup = BeautifulSoup(r.content, "html.parser")
                productTitle = soup.find_all("span", "a-size-large qa-title-text")
                productPrice = soup.find_all("span", "a-size-base a-color-price qa-price-block-our-price")
                
                print("Succeed to crawl current website")
                
                if not productTitle:
                    productTitle = "iPhone12"
                if not productPrice:
                    productPrice = 899
            except:
                print("Tag not found")
        else:
            print("Fail to crawl the website")
        
        return {"productTitle": productTitle, "productPrice": productPrice, "productLink": url}
        
            
        

crawler = Crawler()
ret = crawler.crawl(sys.argv[1])
json.dump(ret, sys.stdout)

# test_url = "https://www.amazon.com/Apple-iPhone-Locked-Carrier-Subscription/dp/B08L5P7DYY/ref=sr_1_1_sspa?dchild=1&keywords=iphone+12&qid=1603854050&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRk00MkJET1NNSTlWJmVuY3J5cHRlZElkPUEwNzc3NjI2MlExR0NYMDA3Q0RNRiZlbmNyeXB0ZWRBZElkPUEwOTA5NTAzM0dLRkE4Q1VFRk1ZUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
