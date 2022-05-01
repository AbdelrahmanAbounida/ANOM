import csv
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Linked(webdriver.Chrome):

    def __init__(self, webdriver_path="C:\Program Files (x86)\chromedriver.exe", teardown=False):
        self.website_link = "https://www.linkedin.com/search/results/people/?keywords=abdelrahman%20yousef%20&origin=SWITCH_SEARCH_VERTICAL&sid=YId"
        self.webdriver_Path = webdriver_path
        self.teardown = teardown  # decides if u want to exit the browser
        # s = Service(driver_link)
        super(Linked, self).__init__(service=Service(webdriver_path))
        # os.environ['path'] += self.webdriver_Path
        self.maximize_window()
        self.implicitly_wait(20)

    def land_first_page(self):
        self.get(self.website_link)

    def agree(self, currency=None):
        try:
            agree_button = self.find_element(By.XPATH,'//button[@id="L2AGLb"]')
            agree_button.click()
        except:
            pass

    def getLinks(self):
        companies = self.get_companies_name()
        links =[]
        for company in companies[0:20]:
            search_bar = self.find_element(By.XPATH,'//input[@class="gLFyf gsfi"]')
            search_bar.clear()
            search_bar.send_keys(company)
            search_bar.send_keys(Keys.RETURN)

            link = self.find_element(By.XPATH,'//div[@class="yuRUbf"]/a[@href]').get_attribute("href")
            links.append(link)
        return companies,links



    def get_companies_name(self):
        wb = xlrd.open_workbook("companies.xlsx")
        sheet = wb.sheet_by_index(0)
        urls = []
        for i in range(sheet.nrows):
            urls.append(sheet.cell_value(i, 1))

        return urls[2:]


    def send_companies_to_Excel(self):
        companies , links= self.getLinks()
        headers = ["Company Name","Website URL"]
        res = zip(companies,links)
        with open('out.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for line in res:
                company = line[0]
                link = line[1]
                writer.writerow([company, link])


if __name__ == '__main__':
    x = Company()
    x.land_first_page()
    x.agree()
    x.send_companies_to_Excel()

