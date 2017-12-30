# linkSifter


linkSifter.py is an HTML link discovery tool.  This is a non-aggressive searching tool, therefore it
does not spider.  Point it at a webpage and it downloads the HTML via the Requests module.  From there, it 
parses via BeautifulSoup to find "<a href" tags.  This tool can be modified to find other stuff too (just 
change the tags you are searching for).

This script depends on the module BeautifulSoup to work:
pip3 install beautifulsoup4

This Python script was written by James Russell.

Usage: ./linkSifter.py http://www.example.com

