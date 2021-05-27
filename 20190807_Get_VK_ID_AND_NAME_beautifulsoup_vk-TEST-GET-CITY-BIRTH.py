import os, time
from datetime import datetime
from bs4 import BeautifulSoup
import requests, psycopg2

conn = psycopg2.connect(dbname='vk_base_test', user='postgres',
						password='12345', host='localhost')
cursor = conn.cursor()
conn.autocommit = True

global id
#id = 556441600
id = 356440500
 
def get_html(url):
	response = requests.get(url)
	return response.text
	
def get_name(html):
	global id
	soup = BeautifulSoup(html, 'lxml')
	#allsoup = BeautifulSoup(html).prettify()
	#with open("soup.html", "a") as f:
		#f.writelines(allsoup)
	username = soup.find('h2', class_='op_header').next
	city = (soup.find('div', class_='pp_info').next).split(", ")
	if len(city) > 1:
		birthdate = city[0]
	else:
		birthdate = 'unknown'
	try:
		status = soup.find('div', class_='pp_status').next
	except:
		status = 'empty'
	try:	
		alive = soup.find('span', class_='pp_last_activity_offline_text').next
	except:
		alive = 'no activ user'
	#interests = 
	#foto =
	writetopostgres(id, username, city, birthdate, status, alive)
	
def writetopostgres(id, username, city, birthdate, status, alive):
	try:
		print ([id, username, city[-1], birthdate, status, alive])
		cursor.execute("INSERT INTO vk_users VALUES('{0}', '{1}', '{2}', '{3}', '{4}', '{5}');".format(id, username, city[-1], birthdate, status, alive))
	except ValueError:
		print("Error in function")
 

def main():
	global id
	while id <= 356440510:
	#while id <= 556441700:
		url = 'https://vk.com/id{}'.format(id)
		try:
			all_links = get_name(get_html(url))
		except: pass
		id+=1
		time.sleep(1)
	a = input()
 
if __name__ == '__main__':
    main()