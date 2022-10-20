# ------------------------------- W E B - S C R A P I N G - U S I N G - S E L E N I U M ---------------------------------

# importing required drivers, modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
#to connect to sql server
import mysql.connector
#giving host, password, username
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ash#010902"
)
mycursor = mydb.cursor()
#data base to use
mycursor.execute("USE scraping")

# a function to login linkedin and navigate to jobs page
def linkedin_job():
    # browsing to site
    driver.get("https://www.linkedin.com/home")
    # wait 3 sec after going to site
    time.sleep(3)

    # clicking on sign in
    sign_in = driver.find_element(by=By.XPATH, value='/html/body/nav/div/a[2]')
    sign_in.click()
    time.sleep(3)

    # typing username after clicking on the username field
    username = driver.find_element(by=By.XPATH, value='//*[@id="username"]')
    username.send_keys("saiharshitha.192@gmail.com")
    time.sleep(3)

    # typing password
    password = driver.find_element(by=By.XPATH, value='//*[@id="password"]')
    password.send_keys("Ash#010902")
    time.sleep(3)

    # clicking on sign in
    log_in = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[2]/div[1]/form/div[3]/button')
    log_in.click()
    time.sleep(56)

    # navigating to jobs page
    jobs = driver.find_element(by=By.XPATH, value='/html/body/div[5]/header/div/nav/ul/li[3]/a/span')
    time.sleep(2)
    jobs.click()
    time.sleep(20)

# function to get link and employee list of that particular company
def company_link_and_employee_list():
    linkk = driver.find_elements(by=By.CLASS_NAME, value='overflow-hidden')
    time.sleep(10)
    # storing values in list and printing
    e = []
    for k in linkk:
        e.append(k.text)
    print(e)

# function to display the description of the company
def company_description():
    print("COMPANY DESCRIPTION")
    description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
    time.sleep(10)
    # storing the values in list and printing
    a1 = []
    for i in description:
        a1.append(i.text)
    print(a1)
    print('\n')

# main method
# uploading the webdriver installed in the laptop
s = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# going to careerguide to select few subcategories from categories
driver.get("https://www.careerguide.com/career-options")
time.sleep(3)

# asking user to input which category among the 2 he wants to choose
print("Enter category:")
print("1.Aerospace and aviation\n2.Engineering and Technology")
category = int(input())

# condition if he chooses aerospace and aviation
if category == 1:
    # asking the user to select subcategory
    print("Enter an option:")
    print("1.Aircraft maintenance\n2.Ground operation staff/manager")
    n = int(input())

    # for aircraft maintenance
    if n == 1:
        # clicking on aircraft maintenance and waiting for 10 sec
        sub_category = driver.find_element(by=By.XPATH, value='/html/body/form/div[6]/div[3]/div/div[2]/div/div[1]/div[1]/ul/li[5]/a')
        sub_category.click()
        time.sleep(10)

        # redirect to linkedin
        linkedin_job()

        # searching aircraft maintenance job in Hyderabad location
        js = driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3279877460&geoId=105556991&keywords=aircraft%20mainenance&location=Hyderabad%2C%20Telangana%2C%20India&refresh=true")
        time.sleep(30)

        # basic job and company details are extracted
        print('\n JOBS DETAILS: ')
        print("order in which it's displaying: Name of the job position---company---place")

        # finding and storing all jobs by class name
        job_list = driver.find_elements(by=By.CLASS_NAME, value='job-card-list__entity-lockup')
        time.sleep(20)
        c = []
        for i in job_list:
            c.append(i.text)
        print(c)
        #gives position
        print("\n POSITION: ")
        job_position = driver.find_elements(by=By.CLASS_NAME, value='job-card-list__title')
        jobs = []
        for n in job_position:
            jobs.append(n.text)
        print(jobs)
        #gives location
        print('\n LOCATION:')
        job_location = driver.find_elements(by=By.CLASS_NAME, value='job-card-container__metadata-item')
        job_location_list = []
        for i in job_location:
            job_location_list.append(i.text)
        print(job_location_list)
        # finding and storing all company names by class name
        print("\nCOMPANY NAMES:")
        company_list = driver.find_elements(by=By.CLASS_NAME, value='artdeco-entity-lockup__subtitle')
        time.sleep(5)
        d = []
        for j in company_list:
            d.append(j.text)
        print(d)
        #storing in database
        for i in range(0, len(d)):
            add_db = ("INSERT INTO jobs_details_aircraft_maintenance" "(company, position, location)" "VALUES(%s,%s,%s)")
            add_db_values = (d[i], jobs[i], job_location_list[i])
            mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        # top few companies number of people, description and links are extracted after redirecting to aircraft_maintenance_companies
        print("CYIENT")
        driver.get("https://www.linkedin.com/company/cyient/about/")
        time.sleep(20)
        company_link_and_employee_list()
        #company description
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in database
        comp_name = ["CYIENT"]
        statee = ["Telangana"]
        sub_category_ = ["Aircraft maintenance"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        print("HONEY WELL")
        driver.get("https://www.linkedin.com/company/honeywell/about/")
        time.sleep(20)
        company_link_and_employee_list()
        #company description
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in database
        comp_name = ["HONEY WELL"]
        statee = ["Telangana"]
        sub_category_ = ["Aircraft maintenance"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        print("EVOPLAY")
        driver.get("https://www.linkedin.com/company/evoplay/about/")
        time.sleep(20)
        company_link_and_employee_list()
        #company description
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in database
        comp_name = ["EVOPLAY"]
        statee = ["Telangana"]
        sub_category_ = ["Aircraft maintenance"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        print("CANONICAL")
        driver.get("https://www.linkedin.com/company/canonical/about/")
        time.sleep(20)
        company_link_and_employee_list()
        #company description
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in database
        comp_name = ["CANONICAL"]
        statee = ["Telangana"]
        sub_category_ = ["Aircraft maintenance"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

    # for ground operation manager/staff
    if n == 2:
        # clicking on ground operation manager/staff and waiting for 10 sec
        sub_category = driver.find_element(by=By.XPATH, value='/html/body/form/div[6]/div[3]/div/div[2]/div/div[1]/div[1]/ul/li[10]/a')
        sub_category.click()
        time.sleep(10)

        # redirect to linkedin
        linkedin_job()

        # searching ground operation manager job in Hyderabad location
        js = driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3177952395&geoId=105556991&keywords=ground%20operations%20manager&location=Hyderabad%2C%20Telangana%2C%20India&refresh=true")
        time.sleep(30)

        # basic job and company details are extracted
        print('\n JOBS DETAILS: ')
        print("order in which it's displaying: Name of the job position---company---place")

        # finding and storing all jobs by class name
        job_list = driver.find_elements(by=By.CLASS_NAME, value='job-card-list__entity-lockup')
        time.sleep(20)
        c = []
        for i in job_list:
            c.append(i.text)
        print(c)
        #position
        print("\n POSITION: ")
        job_position = driver.find_elements(by=By.CLASS_NAME, value='job-card-list__title')
        jobs = []
        for n in job_position:
            jobs.append(n.text)
        print(jobs)
        #location
        print('\n LOCATION:')
        job_location = driver.find_elements(by=By.CLASS_NAME, value='job-card-container__metadata-item')
        job_location_list = []
        for i in job_location:
            job_location_list.append(i.text)
        print(job_location_list)

        # finding and storing all company names by class name
        print("\nCOMPANY NAMES:")
        company_list = driver.find_elements(by=By.CLASS_NAME, value='artdeco-entity-lockup__subtitle')
        time.sleep(5)
        d = []
        for j in company_list:
            d.append(j.text)
        print(d)
        #storing in db
        for i in range(0,len(d)):
            add_db = ("INSERT INTO jobs_details_ground_operation_manager" "(company, position, location)" "VALUES(%s,%s,%s)")
            add_db_values = (d[i],jobs[i], job_location_list[i])
            mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        # top few companies number of people, description and links are extracted after redirecting to aircraft_maintenance_companies
        print("FRANKLIN TEMPLETON INDIA")
        driver.get("https://www.linkedin.com/company/franklintempletonindia/about/")
        time.sleep(20)
        company_link_and_employee_list()
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in db
        comp_name = ["FRANKLIN TEMPLETON INDIA"]
        statee = ["Telangana"]
        sub_category_ = ["Ground operation manager"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0],statee[0],sub_category_[0])
        mycursor.executemany(add_db,(add_db_values,))
        mydb.commit()

        print("FIS")
        driver.get("https://www.linkedin.com/company/fis/about/")
        time.sleep(20)
        company_link_and_employee_list()
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in db
        comp_name = ["FIS"]
        statee = ["Telangana"]
        sub_category_ = ["Ground operation manager"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

# condition if he chooses aerospace and aviation
if category == 2:
    # asking the user to select subcategory
    print("Enter an option:")
    print("1.Computer engineer\n2.Electronics engineer")
    n = int(input())

    # if he chooses computer engineer
    if n == 1:
        # clicking on computer engineer and waiting for 10 sec
        sub_category = driver.find_element(by=By.XPATH,value='/html/body/form/div[6]/div[3]/div/div[2]/div/div[5]/div[3]/ul/li[11]/a')
        sub_category.click()
        time.sleep(10)

        # redirect to linkedin
        linkedin_job()

        # searching computer engineer job in Hyderabad location
        js = driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3298905143&geoId=105556991&keywords=computer%20engineer&location=Hyderabad%2C%20Telangana%2C%20India&refresh=true")
        time.sleep(30)

        # basic job and company details are extracted
        print('\n JOBS DETAILS: ')
        print("order in which it's displaying: Name of the job position---company---place")

        # finding and storing all jobs by class name
        job_list = driver.find_elements(by=By.CLASS_NAME, value='job-card-list__entity-lockup')
        time.sleep(20)
        c = []
        for i in job_list:
            c.append(i.text)
        print(c)
        #position
        print("\n POSITION: ")
        job_position = driver.find_elements(by=By.CLASS_NAME, value='job-card-list__title')
        jobs = []
        for n in job_position:
            jobs.append(n.text)
        print(jobs)
        #location
        print('\n LOCATION:')
        job_location = driver.find_elements(by=By.CLASS_NAME, value='job-card-container__metadata-item')
        job_location_list = []
        for i in job_location:
            job_location_list.append(i.text)
        print(job_location_list)

        # finding and storing all company names by class name
        print("\nCOMPANY NAMES:")
        company_list = driver.find_elements(by=By.CLASS_NAME, value='artdeco-entity-lockup__subtitle')
        time.sleep(5)
        d = []
        for j in company_list:
            d.append(j.text)
        print(d)
        for i in range(0, len(d)):
            add_db = ("INSERT INTO jobs_details_computer_engineer" "(company, position, location)" "VALUES(%s,%s,%s)")
            add_db_values = (d[i], jobs[i], job_location_list[i])
            mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        # top few companies number of people, description and links are extracted after redirecting to aircraft_maintenance_companies
        print("TOP FEW JOBS: ")
        print('\n')

        print("CODVO")
        driver.get("https://www.linkedin.com/company/codvo/about/")
        time.sleep(20)
        company_link_and_employee_list()
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in db
        comp_name = ["CODVO"]
        statee = ["Telangana"]
        sub_category_ = ["Computer engineer"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        print("GE RENEWABLE ENERGY")
        driver.get("https://www.linkedin.com/company/gerenewableenergy/about/")
        time.sleep(20)
        company_link_and_employee_list()
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in db
        comp_name = ["GE RENEWABLE ENERGY"]
        statee = ["Telangana"]
        sub_category_ = ["Computer engineer"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        print("THERMO FISHER SCIENTIFIC")
        driver.get("https://www.linkedin.com/company/thermo-fisher-scientific/about/")
        time.sleep(20)
        company_link_and_employee_list()
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in db
        comp_name = ["THERMO FISHER SCIENTIFIC"]
        statee = ["Telangana"]
        sub_category_ = ["Computer engineer"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        print("SHADOWING AI")
        driver.get("https://www.linkedin.com/company/shadowing-ai/about/")
        time.sleep(20)
        company_link_and_employee_list()
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in db
        comp_name = ["SHADOWING AI"]
        statee = ["Telangana"]
        sub_category_ = ["Computer engineer"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        print("LOGICPLANET IT SERVICES (INDIA) PRIVATE LIMITED")
        driver.get("https://www.linkedin.com/company/logicplanet-it-services-india-private-limited/about/")
        time.sleep(20)
        company_link_and_employee_list()
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in db
        comp_name = ["LOGICPLANET IT SERVICES (INDIA) PRIVATE LIMITED"]
        statee = ["Telangana"]
        sub_category_ = ["Computer engineer"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

    # if he chooses electrical engineer
    if n == 2:
        # clicking on electrical engineer and waiting for 10 sec
        sub_category = driver.find_element(by=By.XPATH,value='/html/body/form/div[6]/div[3]/div/div[2]/div/div[5]/div[3]/ul/li[13]/a')
        sub_category.click()
        time.sleep(10)

        # redirect to linkedin
        linkedin_job()

        # searching electrical engineer job in Hyderabad location
        js = driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3262352809&geoId=105556991&keywords=electrical%20engineer&location=Hyderabad%2C%20Telangana%2C%20India&refresh=true")
        time.sleep(30)

        # basic job and company details are extracted
        print('\n JOBS DETAILS: ')
        print("order in which it's displaying: Name of the job position---company---place")

        # finding and storing all jobs by class name
        job_list = driver.find_elements(by=By.CLASS_NAME, value='job-card-list__entity-lockup')
        time.sleep(20)
        c = []
        for i in job_list:
            c.append(i.text)
        print(c)
        #position
        print("\n POSITION: ")
        job_position = driver.find_elements(by=By.CLASS_NAME, value='job-card-list__title')
        jobs = []
        for n in job_position:
            jobs.append(n.text)
        print(jobs)
        #location
        print('\n LOCATION:')
        job_location = driver.find_elements(by=By.CLASS_NAME, value='job-card-container__metadata-item')
        job_location_list = []
        for i in job_location:
            job_location_list.append(i.text)
        print(job_location_list)

        # finding and storing all company names by class name
        print("\nCOMPANY NAMES:")
        company_list = driver.find_elements(by=By.CLASS_NAME, value='artdeco-entity-lockup__subtitle')
        time.sleep(5)
        d = []
        for j in company_list:
            d.append(j.text)
        print(d)
        print('\n')
        #storing in db
        for i in range(0, len(d)):
            add_db = ("INSERT INTO jobs_details_electrical_engineer" "(company, position, location)" "VALUES(%s,%s,%s)")
            add_db_values = (d[i], jobs[i], job_location_list[i])
            mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()


        # top few companies number of people, description and links are extracted after redirecting to aircraft_maintenance_companies
        print("TOP FEW JOBS: ")
        print('\n')

        print("QUALCOMM")
        driver.get("https://www.linkedin.com/company/qualcomm/about/")
        time.sleep(20)
        company_link_and_employee_list()
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in db
        comp_name = ["QUALCOMM"]
        statee = ["Telangana"]
        sub_category_ = ["Electrical engineer"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        print("NVIDIA")
        driver.get("https://www.linkedin.com/company/nvidia/about/")
        time.sleep(20)
        company_link_and_employee_list()
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in db
        comp_name = ["NVIDIA"]
        statee = ["Telangana"]
        sub_category_ = ["Electrical engineer"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        print("MICRON TECHNOLOGY")
        driver.get("https://www.linkedin.com/company/micron-technology/about/")
        time.sleep(20)
        company_link_and_employee_list()
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in db
        comp_name = ["MICRON TECHNOLOGY"]
        statee = ["Telangana"]
        sub_category_ = ["Electrical engineer"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        print("SYNOPSYS")
        driver.get("https://www.linkedin.com/company/synopsys/about/")
        time.sleep(20)
        company_link_and_employee_list()
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in db
        comp_name = ["SYNOPSYS"]
        statee = ["Telangana"]
        sub_category_ = ["Electrical engineer"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()

        print("THERMO FISHER SCIENTIFIC")
        driver.get("https://www.linkedin.com/company/thermo-fisher-scientific/about/")
        time.sleep(20)
        company_link_and_employee_list()
        print("COMPANY DESCRIPTION")
        description = driver.find_elements(by=By.CLASS_NAME, value='white-space-pre-wrap')
        time.sleep(10)
        # storing the values in list and printing
        a1 = []
        for i in description:
            a1.append(i.text)
        print(a1)
        print('\n')
        #storing in db
        comp_name = ["THERMO FISHER SCIENTIFIC"]
        statee = ["Telangana"]
        sub_category_ = ["Electrical engineer"]
        add_db = ("INSERT INTO company_details" "(name, description,state,sub_category )" "VALUES(%s,%s,%s,%s)")
        add_db_values = (comp_name[0], a1[0], statee[0], sub_category_[0])
        mycursor.executemany(add_db, (add_db_values,))
        mydb.commit()


# mycursor.execute("CREATE DATABASE scraping")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
print()
'''
creating tables: 

mycursor.execute("CREATE TABLE job_category (category VARCHAR(255))")
mycursor.execute("CREATE TABLE job_sub_category (sub_category VARCHAR(255), PRIMARY KEY(sub_category))")
mycursor.execute("CREATE TABLE State (state VARCHAR(255), PRIMARY KEY(state))")
mycursor.execute("CREATE TABLE jobs_details (company VARCHAR(255), position VARCHAR(200), location VARCHAR(200) )")
mycursor.execute("CREATE TABLE company_details (name VARCHAR(200), description VARCHAR(255), state VARCHAR(255), "
                 "sub_category VARCHAR(255), FOREIGN KEY (state) REFERENCES State(state),FOREIGN KEY (sub_category) "
                 "REFERENCES job_sub_category(sub_category))")'''

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
'''
mycursor.execute("ALTER TABLE jobs_details RENAME TO jobs_details_aircraft_maintenance")
mycursor.execute("CREATE TABLE jobs_details_ground_operation_manager (company VARCHAR(255), position VARCHAR(200), location VARCHAR(200) )")
mycursor.execute("CREATE TABLE jobs_details_computer_engineer (company VARCHAR(255), position VARCHAR(200), location VARCHAR(200) )")
mycursor.execute("CREATE TABLE jobs_details_electrical_engineer (company VARCHAR(255), position VARCHAR(200), location VARCHAR(200) )")'''

'''
category = "INSERT INTO job_category (category) VALUES (%s)"
category_val1 = [("Aerospace and Aviation")]
category_val2 = [("Engineering and Technology")]
mycursor.execute(category, category_val1)
mycursor.execute(category, category_val2)
mydb.commit()
print(mycursor.rowcount, "record inserted in job_category table")

sub_category = "INSERT INTO job_sub_category (sub_category) VALUES (%s)"
s_category_val = [("Aircraft maintenance")]
mycursor.execute(sub_category, s_category_val)
s_category_val = [("Ground operation manager")]
mycursor.execute(sub_category, s_category_val)
s_category_val = [("Computer engineer")]
mycursor.execute(sub_category, s_category_val)
s_category_val = [("Electrical engineer")]
mycursor.execute(sub_category, s_category_val)
mydb.commit()
print(mycursor.rowcount, "record inserted in job_sub_category table")


State = "INSERT INTO State (state) VALUES ('Telangana')"
mycursor.execute(State)
mydb.commit()
print(mycursor.rowcount, "record inserted in state table")'''

# ---------------------------------------------------E  N  D-------------------------------------------------------------