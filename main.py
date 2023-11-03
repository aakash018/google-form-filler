from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import random

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# import requests
import os

from selenium.webdriver.chrome.options import Options

first_names = [
    "John",
    "Mary",
    "James",
    "Jennifer",
    "Robert",
    "Linda",
    "Michael",
    "Patricia",
    "William",
    "Elizabeth",
    "David",
    "Susan",
    "Richard",
    "Karen",
    "Joseph",
    "Nancy",
    "Charles",
    "Lisa",
    "Thomas",
    "Betty",
    "Daniel",
    "Margaret",
    "Christopher",
    "Dorothy",
    "Matthew",
    "Sandra",
    "George",
    "Ashley",
    "Donald",
    "Kimberly",
    "Paul",
    "Emily",
    "Mark",
    "Jessica",
    "Kenneth",
    "Sarah",
    "Steven",
    "Donna",
    "Edward",
    "Laura",
    "Brian",
    "Carol",
    "Ronald",
    "Michelle",
    "Frank",
    "Deborah",
    "Gary",
    "Cynthia",
]

# List of 50 last names
last_names = [
    "Smith",
    "Johnson",
    "Brown",
    "Davis",
    "Wilson",
    "Anderson",
    "Miller",
    "Jones",
    "Taylor",
    "White",
    "Lee",
    "Martinez",
    "Clark",
    "Thomas",
    "Harris",
    "Walker",
    "Hall",
    "Young",
    "Garcia",
    "Rodriguez",
    "Jackson",
    "Perez",
    "Hernandez",
    "King",
    "Lewis",
    "Adams",
    "Scott",
    "Turner",
    "Moore",
    "Hill",
    "Allen",
    "Nelson",
    "Mitchell",
    "Baker",
    "Carter",
    "Green",
    "Evans",
    "Martin",
    "Roberts",
    "Wright",
    "James",
    "Gonzalez",
    "Kathleen",
    "Parker",
    "Morgan",
    "Ramirez",
    "Wilson",
    "Cooper",
    "Stewart",
    "Reed",
    "Bell",
]

managerial_roles = [
    "COO (Chief Operating Officer)",
    "CFO (Chief Financial Officer)",
    "CMO (Chief Marketing Officer)",
    "CIO (Chief Information Officer)",
    "HR Manager (Human Resources Manager)",
    "General Manager",
    "Project Manager",
    "Product Manager",
    "Operations Manager",
    "Sales Manager",
    "Marketing Manager",
    "Finance Manager",
    "IT Manager (Information Technology Manager)",
    "Supply Chain Manager",
    "Customer Service Manager",
    "Quality Assurance Manager",
    "Business Development Manager",
    "Research and Development (R&D) Manager",
    "Production Manager",
    "Purchasing Manager",
]

geo_regions = [
    "New England (US)",
    "Mid-Atlantic (US)",
    "Midwest (US)",
    "Southern Plains (US)",
    "Southwest (US)",
    "Pacific Northwest (US)",
    "Mountain West (US)",
    "Great Lakes (US)",
    "Florida (US)",
    "Texas Gulf Coast (US)",
    "Rocky Mountains (US)",
    "Northeast (US)",
    "Midwest (US)",
    "South (US)",
    "West Coast (US)",
    "Southeast (US)",
    "Southwest (US)",
    "Alaska (US)",
    "Hawaii (US)",
    "Caribbean",
    "Central America",
    "South America",
    "Western Europe",
    "Eastern Europe",
    "Scandinavia",
    "Southern Europe",
    "Eastern Asia",
    "Southeast Asia",
    "South Asia",
    "Central Asia",
    "Middle East",
    "Northern Africa",
    "Southern Africa",
    "Eastern Africa",
    "Central Africa",
    "Western Africa",
    "Northern Europe",
    "Baltic States",
    "Caucasus",
    "Central America and the Caribbean",
    "Andean Region",
    "Arabian Peninsula",
    "Indochina",
    "East Africa",
    "Horn of Africa",
    "Central Africa",
    "Caribbean Islands",
    "Melanesia",
    "Polynesia",
    "Micronesia",
]

options_list_first = [
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div'
]

options_list_second = [
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div'
]

options_list_third = [
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div'
]

options_list_fourth = [
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div'
]

options_list_fifth = [
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[2]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[3]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[4]/div[2]/div',
    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div'
]



# firstRound = False
class FormFiller :
    def __init__(self) -> None:
        # if firstRound:
        url = "https://docs.google.com/forms/d/e/1FAIpQLScxMaGmoWFaIrrwAhaaLB5_OH0onEn8HlIPE0fps6Jgjj1pzg/viewform?usp=sf_link"

        self.driver = webdriver.Chrome()
        self.driver.get(url)
    
        
        self.driver.maximize_window()
            # firstRound = False
    
    def firstPageFiller(self):
        driver = self.driver
        sleep(1)
        nameInput = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        position = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        years = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        region = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')

        submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

        nameInput.send_keys(f"{first_names[random.randint(0, 40)]} {last_names[random.randint(0, 40)]}")
        position.send_keys(managerial_roles[random.randint(0, 19)])
        years.send_keys(random.randint(2, 10))
        region.send_keys(geo_regions[random.randint(0, 49)])
        submit.click()

    def listClicker(self, index):
        first_ele = self.driver.find_element(By.XPATH, options_list_first[4])
        second_ele = self.driver.find_element(By.XPATH, options_list_second[4])
        third_ele = self.driver.find_element(By.XPATH, options_list_third[4])
        fourth_ele = self.driver.find_element(By.XPATH, options_list_fourth[4])
        fifth_ele = self.driver.find_element(By.XPATH, options_list_fifth[4])
        first_ele.click()
        second_ele.click()
        third_ele.click()
        fourth_ele.click()
        fifth_ele.click()

        submit = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
        submit_main = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]')
        if i < 5:
            submit.click()
        else:
            submit_main.click()

        

    def finalSubmit(self):
        submitter = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        submitter.click()
        sleep(1)

counter = 79
downloader = FormFiller()
print("Welcome")
for i in range(140):
    print("New Form Started")
    downloader.firstPageFiller()
    for i in range(6):
        downloader.listClicker(i)
    downloader.finalSubmit()
    counter = counter + 1
    print("Total Form Submitted: ", counter)

print(f"{counter} form submitted...")