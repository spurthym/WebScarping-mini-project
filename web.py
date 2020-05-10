from bs4 import BeautifulSoup
import requests
import csv


source = requests.get("https://collegedunia.com/courses/courses-after-12th").text
soup = BeautifulSoup(source,'html.parser')

csv_file = open('data.csv','w',newline='\n')
csv_writer = csv.writer(csv_file)

for dta in soup.find_all('div',{'class':'container-fluid'}):
	for dt in dta.find_all('div',{'class':'stream-block col-lg-10'}):
		branch=dt.a.text
		csv_writer.writerow([branch])
		for data in dt.find_all('div',{'class':'stream-block-list'}):
			
			for datas in data.find_all('div',{'class':'course-header'}):
				field=datas.a.text
				link=datas.a['href']

				row=[field,link]
				csv_writer.writerow(row)


csv_file.close()