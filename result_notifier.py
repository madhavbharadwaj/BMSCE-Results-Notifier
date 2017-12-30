import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#numlist = list()
# 	NOTIFICATION DEC 2017 EXAMS
page = requests.get("http://202.129.209.25:8080/BMSResults/examDetails/getExamDetailsUploadPage.htm")
soup = BeautifulSoup(page.content, 'html.parser')

""""
# 	NOTIFICATION SUPPLEMENTARY JULY 2017 EXAMS
page1 = requests.get("http://202.129.209.25:8080/BMSResults/examDetails/getStudentAllocationDetails.htm")
soup1 = BeautifulSoup(page1.content, 'html.parser')"""


tags = soup.find_all('b')
c=0
for tag in tags:
      c = c + 1
cc = c-1

"""tags1 = soup1.find_all('b')
cx=0
for tag1 in tags1:
      cx = cx + 1
ccc = c-1"""

print("...................... Fetching Data from BMSCE Result Site ......................");
print("\t\t\t\tPython Script by Madhav\n");


for i in range(1,c):
    tx = soup.find_all('b')[i];
    print(tx.contents[0])
    if "MCA" in tx.contents[0]:
        x = i;
        print("\n\n \t Notification !!\n 'MCA' was Found  at (Line : " + str(x) + ")\n")
        Join = input('Would you like to Open the Link in Browser ? (y/n) : ')
        #Open 2 Possible Links for Result
        if Join.lower() == 'y':
            print("\n .... Opening 2 Possible Links of BMSResults .... \n ")
            browser = webdriver.Firefox(executable_path='G:\geckodriver')

            #link1
            browser.get('http://202.129.209.25:8080/BMSResults/examDetails/getExamDetailsUploadPage.htm')
            mainy = browser.current_window_handle
            #link2
            browser.execute_script(
                '''window.open("http://202.129.209.25:8080/BMSResults/examDetails/getStudentAllocationDetails.htm","_blank");''')
            # browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
    """if cc > 7:
        print("\t Notification !!\n 'There are Some Changes Made by Page Admin (Line : " + str(i) + ") \n")
        browser = webdriver.Firefox(executable_path='G:\geckodriver')
        browser.get('http://202.129.209.25:8080/BMSResults/examDetails/getExamDetailsUploadPage.htm')"""






