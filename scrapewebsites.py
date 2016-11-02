from urllib.request import urlopen
import re

my_address = "http://realpython.com/practice/dionysus.html"


html_page = urlopen(my_address)

html_text = html_page.read().decode('utf-8')

start_tag = '<title>'
end_tag   = '</title>'

start_index = html_text.find(start_tag)+len(start_tag)
end_index = html_text.find(end_tag)

print (html_text[start_index:end_index])

my_string ="Everything is <replaced> if its in <tags>"
my_string = re.sub("<.*>","Elephants",my_string)
print(my_string)

match_result = re.search("<title.*?>.</title.*?>",html_text, re.IGNORECASE)

titulo = match_result.group()
