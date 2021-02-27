import requests
import bs4
import csv
#input txt file
f=open(r"C:\Users\Asus\OneDrive\Desktop\brownells.txt",'r')

#output csv file
csvfile = open(r'C:\Users\Asus\OneDrive\Desktop\scraping.csv', 'a')
csvwriter = csv.writer(csvfile)
#csv file header
csvwriter.writerow(["Product Name","Supplier Name","Stock Status","Hyperlink of Product Page"])

#list to store all urls
urls=[]
line = f.readline()   #reading all the lines of txt file
while line:
    line = line.rstrip()
    urls.append(line)
    line = f.readline()

ln=len(urls)   #no of urls are stored in ln
pre="https://www.brownells.com"

for i in range(ln):
    res = requests.get(urls[i])   #requesting the page
    soup = bs4.BeautifulSoup(res.text,'lxml')

    content = soup.find("h1", attrs={"class": "mbm"})
    li = content.find_all('span')
    Hyperlink = li[0].a['href']
    pname = li[1].text
    sname = li[0].text

    status1 = soup.find_all("span", attrs={"id": "spanStatus"})
    status2 = soup.find("p", attrs={"class": "alertMe"})
    if (status1 or status2):    stat = "Out of Stock"
    else:   stat = 'In Stock'

    csvwriter.writerow([pname.lstrip(),sname.lstrip(),stat.lstrip(),pre+Hyperlink]) #writing on csv file








