from selenium import webdriver
from bs4 import BeautifulSoup

html = 'https://www.oddschecker.com/us/motorsport/formula-one'
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get(html)

soup = BeautifulSoup(driver.page_source, 'html.parser')

events = soup.find_all(attrs={'data-testid': 'outright-events'})[0]
# Iterate through all listed bets
for betInfo in events.find_all(attrs={'data-testid': "outright-bet"}):
    team_name = betInfo.find(attrs={'data-testid': "outright-team-name"}).text
    print(team_name)
    odds = betInfo.find(attrs={'data-testid': "odds-primary"}).text
    print(odds)

driver.close()
