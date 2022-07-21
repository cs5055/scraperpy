import requests
from bs4 import BeautifulSoup

def main():
	id = input('Enter your id: ')
	params = {
		'__VIEWSTATE':'__VIEWSTATE: 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',
		'__EVENTVALIDATION':'/wEWAwK//ZeTBQL02Yi2DgLWlvWyA4puCegkJF6IpiMn/Kmdpomyy4+t',
		'ctl00$CPHmaster$txtMemcd':id,'ctl00$CPHmaster$btnsearch':'Search Member'
		}
	req = requests.post('http://webopac.cit.ac.in/memberstatus.aspx', data=params)
	parse = BeautifulSoup(req.text, 'lxml')
	#print(parse)
	member_name = parse.find('span', id='ctl00_CPHmaster_lblmemname').text.strip()
	#print(member_name)
	member_code = parse.find('span', id='ctl00_CPHmaster_lblmemcd').text.strip()
	member_dept = parse.find('span', id='ctl00_CPHmaster_lbldept').text.strip()
	#print(member_name, member_code, member_dept)
	member_cat = parse.find('span', id='ctl00_CPHmaster_lblcat').text.strip()
	member_dues = parse.find('span',id="ctl00_CPHmaster_lbldue").text.strip()
	member_book_count = parse.find('span', id='ctl00_CPHmaster_lblissued').text.strip()
	#print(member_cat, member_due, member_book_count)
	items = parse.find('table', id='ctl00_CPHmaster_DgIssued')
	#print(items)
	rows = items.find_all('tr')[1:]
	#print(rows)
	for row in rows:
   		cols = row.find_all('td')
   		for col in cols:
      			print(col.text)
   		print('')


if __name__=='__main__':
	main()
