from lxml import etree

tree =  etree.parse("fundamentals/src/web_page.html")
html = tree.getroot()

title_element = html.cssselect("title")[0]
paragraph_element = html.cssselect("p")[0]
list_underline_items = html.cssselect("li")

print(title_element.text)
print(paragraph_element.text)

for li in list_underline_items:
    a = li.cssselect("a")
    if len(a) == 0:
        print(li.text)
    else:
        print(f"{li.text.strip()} {a[0].text}")



'''
Code source lecture by lecture
Lecture 7 source code
from lxml import etree
 
tree = etree.parse("/fundamentals/src/web_page.html")
print(etree.tostring(tree))
Lecture 8 source code
from lxml import etree
 
tree = etree.parse("/fundamentals/src/web_page.html")
title_element = tree.find("head/title")
print(title_element.text)
 
paragraph_element = tree.find("body/p")
print(paragraph_element.text)
 
list_items = tree.findall("body/ul/li")
for li in list_items:
    a = li.find("a")
    if a is not None:
        print(f"{li.text.strip()} {a.text}")
    else:
        print(li.text)
Lecture 9 source code
from lxml import etree
 
tree = etree.parse("src/web_page.html")
title_element = tree.xpath("//title/text()")[0]
print(title_element)
 
paragraph_element = tree.xpath("//p/text()")[0]
print(paragraph_element)
 
list_items = tree.xpath("//li")
for li in list_items:
    text = ''.join(map(str.strip, li.xpath(".//text()")))
    print(text)
Lecture 10 source code
from lxml import etree
 
html = etree.parse('test.html')
 
html_element = html.getroot()
 
title = html_element.cssselect('title')[0]
print(title.text)
 
p = html_element.cssselect('p')[0]
print(p.text)
 
 
list_items = html_element.cssselect('li')
for li in list_items:
        a = li.cssselect('a')
        if len(a) == 0:
                print(li.text)
        else:
                print(f"{li.text.strip()} {a[0].text}")
        
'''