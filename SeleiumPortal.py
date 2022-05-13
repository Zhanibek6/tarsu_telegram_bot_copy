from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import tabulatedGraphs as graph
import HTMLTable


driver = webdriver.Chrome()


def login(mail, password):

	driver.get("http://portal.tarsu.kz/ind.php")
	# I have to do this second time because it goes to this
	# exact adress only in the second time
	driver.get("http://portal.tarsu.kz/ind.php")

	emailElem = driver.find_element_by_id("inpnm")
	passwordElem = driver.find_element_by_id("inppass")
	#buttonElem = driver.find_emement_by_class_name("btqr")

	emailElem.send_keys(mail)
	passwordElem.send_keys(password)
	passwordElem.send_keys(Keys.RETURN)


def weekResults(semester):
	getTable("week", semester)


def examResults(course):
	getTable("exam", course)


def getTable(where, sem):
	if where=="week":
		button = driver.find_element_by_link_text("НЕДЕЛЬНЫЕ РЕЗУЛЬТАТЫ")
		button.click() # Button click is here twice since it needs to be pressed before selecting the dropdown
		semDropdown = Select(driver.find_element_by_id("sem_id"))
	else:
		button = driver.find_element_by_link_text("ИТОГИ ВЕДОМОСТЕЙ")
		button.click()
		semDropdown = Select(driver.find_element_by_id("kurs_id"))

	# Thats different
	semDropdown.select_by_value(sem)

	# Finding a table
	table = driver.find_element_by_tag_name("table")
	rows = driver.find_elements_by_tag_name("tr")

	allData = []
	rowData = []

	stringData = ""

	# Iterate over tr's to do some stuff with td's
	for i in range(len(rows)-8): # We have to do the for loop like this to skip unnecessarry stuff
		row = rows[i] # Just for the convinience
		columns = row.find_elements_by_tag_name("td")
		countNewLine = 1 # This is used to count so I can switch to the new line
		for j in range(2,len(columns)): # Start from 2 to skip not needed stuff
			column = columns[j]
			rowData.append(column.text)

			stringData = stringData + column.text + ","
			if countNewLine == 6:
				allData.append(rowData)
				rowData = []
				countNewLine = 0

				stringData = stringData + "\n"
			countNewLine = countNewLine + 1

	HTMLTable.newTable(stringData)
	driver.get("file://C:/Projects/Python/TarsuTelegramBot/table.html")
	element = driver.find_element_by_xpath("//table")
	element.screenshot("img/test.png")

	driver.close()
	# return allData
	return graph.drawTable("week", allData)


def main(mail, psswrd, sems):
	mail = mail
	password = psswrd
	login(mail, password)
	table = getTable("week", sems)
	print(table)
	return table


if __name__ == "__main__":
	main("example@mail.com", "Password", "4")
