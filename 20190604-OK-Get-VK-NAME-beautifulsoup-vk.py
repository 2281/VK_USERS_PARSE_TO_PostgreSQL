import os, time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import psycopg2

conn = psycopg2.connect(dbname='vk_base_test', user='postgres',
						password='12345', host='localhost')
cursor = conn.cursor()
conn.autocommit = True

global id
id = 15170994
 
def get_html(url):
	response = requests.get(url)
	return response.text
	
def get_name(html):
	global id
	soup = BeautifulSoup(html, 'lxml')
	username = soup.find('h2', class_='op_header').next
	print ([id, username])
	writetopostgres(id, username)
	
def writetopostgres(id, username):
    try:
        cursor.execute("INSERT INTO vk_users VALUES('{0}', '{1}');".format(id, username))
    except ValueError:
        print("Error in function")
 

def main():
	global id
	while id <= 15171000:
		url = 'https://vk.com/id{}'.format(id)
		try:
			all_links = get_name(get_html(url))
		except: pass
		id+=1
		time.sleep(1)
	a = input()
 
if __name__ == '__main__':
    main()