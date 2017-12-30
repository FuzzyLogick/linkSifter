#!/usr/bin/env python3

'''
linkSifter.py is an HTML link discovery tool.  This is a non-aggressive searching tool, therefore it
does not spider.  Point it at a webpage and it downloads the HTML via the Requests module.  From there, it 
parses via BeautifulSoup to find "<a href" tags.  This tool can be modified to find other stuff too (just 
change the tags you are searching for).

This script depends on the module BeautifulSoup to work:
pip3 install beautifulsoup4

This Python script was written by James Russell.

Usage: ./linkSifter.py http://www.example.com

This is version 1.0
'''

    
from bs4 import BeautifulSoup
from pathlib import Path  
import requests
import sys


#messages
error = "Please provide a valid URL to the website you would like to extract links from."
usage = "Usage: ./{0} http://www.example.com"

user_agent = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0'} 
 

def process(url):
    response = requests.get(url, headers=user_agent)
    
    data = response.text
    
    
    soup = BeautifulSoup(data, 'lxml')
    
    
    
    #find all the "a" tags and assign them to tags.
    #to modify this script to search for other tags, change as needed.
    tags = soup.find_all('a')
    
    
    for tag in tags:
        #to sift through the "a" tags and print out anything after href.
        #to modify this script to search for other tags, change as needed.
        print(tag.get('href'))  
    
 

 
def main():
    if len(sys.argv) == 1:
        print("")             
        print("██╗     ██╗███╗   ██╗██╗  ██╗                       ")                   
        print("██║     ██║████╗  ██║██║ ██╔╝                       ")                   
        print("██║     ██║██╔██╗ ██║█████╔╝                        ")                    
        print("██║     ██║██║╚██╗██║██╔═██╗                        ")                   
        print("███████╗██║██║ ╚████║██║  ██╗                       ")                  
        print("╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝                       ")
        print("                                                    ")                                                
        print("    ███████╗██╗███████╗████████╗███████╗██████╗     ")
        print("    ██╔════╝██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗    ")
        print("    ███████╗██║█████╗     ██║   █████╗  ██████╔╝    ")
        print("    ╚════██║██║██╔══╝     ██║   ██╔══╝  ██╔══██╗    ")
        print("    ███████║██║██║        ██║   ███████╗██║  ██║    ")
        print("    ╚══════╝╚═╝╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝    ")
        print("")   
        print(usage.format(Path(sys.argv[0]).name))
        sys.exit(1)
        
    for url in sys.argv[1:]:
        try:
            process(url)
        except:
            print("")
            print(error)
            print("")
            print(usage.format(Path(sys.argv[0]).name))
            print("")
            sys.exit(1)
        
        
        
if __name__ == "__main__":
    main()        