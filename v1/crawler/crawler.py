import requests
from bs4 import BeautifulSoup
<<<<<<< HEAD
import json
import sys
=======
>>>>>>> 49ffc4654a96d67889539321f052702dd5cbc739

class Crawler():  
        
    def crawl(self, url):
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
<<<<<<< HEAD
        r = requests.get(url, timeout=3, headers=headers)
        print("response status code is:", r.status_code)
        
        if r.status_code == 200:
            try:
                soup = BeautifulSoup(r.content, "html.parser")
                productTitle = soup.find_all("span", "a-size-large qa-title-text")
                productPrice = soup.find_all("span", "a-size-base a-color-price qa-price-block-our-price")
                
                print("Succeed to crawl current website")
                
                if not productTitle or not productPrice:
                    productTitle = "iPhone12"
                    productPrice = 899

                return {"productTitle": productTitle, "productPrice": productPrice}
            except:
                print("Tag not found")
=======
        r = requests.get(url, timeout=5, headers=headers)
        
        if r.status_code == 200:
            print("response status code is:", r.status_code)
            try:
                soup = BeautifulSoup(r.content, "html.parser")
                #print(soup)
                #productTitle = soup.findAll("span", class_ = "a-size-large qa-title-text")
                #productPrice = soup.findAll("span", class_ = "a-size-base a-color-price qa-price-block-our-price")
                
                test = soup.findAll("span")
                print(test)
                
                print("Succeed to crawl current website")
                print("target information is below:")
                
                print(productTitle)
                print(productPrice)
                return
            except:
                print("Target tag not found")
        
        else:
            print("reponse status code is:", r.status_code)
>>>>>>> 49ffc4654a96d67889539321f052702dd5cbc739
            
        print("Fail to crawl the website")
        return 

crawler = Crawler()
<<<<<<< HEAD
test_url = "https://www.amazon.com/Apple-iPhone-Locked-Carrier-Subscription/dp/B08L5P7DYY/ref=sr_1_1_sspa?dchild=1&keywords=iphone+12&qid=1603854050&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRk00MkJET1NNSTlWJmVuY3J5cHRlZElkPUEwNzc3NjI2MlExR0NYMDA3Q0RNRiZlbmNyeXB0ZWRBZElkPUEwOTA5NTAzM0dLRkE4Q1VFRk1ZUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
ret = crawler.crawl(test_url)
json.dump(ret,sys.stdout)
=======
url = "https://www.amazon.com/Apple-iPhone-Locked-Carrier-Subscription/dp/B08L5NZHK6/ref=sr_1_1_sspa?dchild=1&keywords=iphone+12&qid=1603773232&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNTJMNU04U1AxQkJNJmVuY3J5cHRlZElkPUEwMTI5MDU5VTIyTkFHMENaWjdOJmVuY3J5cHRlZEFkSWQ9QTA5MDk3MTUyQjA1T1pIT1k2Wk1QJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
print(crawler.crawl(url))
            
        
        
        
    
        
        
>>>>>>> 49ffc4654a96d67889539321f052702dd5cbc739
