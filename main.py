import random
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from anticaptchaofficial.recaptchav2proxyless import *
catchall = input("Catchall: ")
password = "EnterPasswordHere" #enter password that will be used for the account
while True:

    print("Starting Browser")
    first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria', 'Alfonso','Mannix','Peter','Dante','Deborah','Xanthus','Lester','Jolie','Forrest','Orli','Adele','Shad','Mufutau','Hamish','Kirk','Wesley','Shad','Candace','Zachery','Maxine','Candace','Fitzgerald','Blythe','Margaret','Drew','Sawyer','Nomlanga','Ulla','Daniel','Ethan','Clayton','Veda','Yasir','Ashely','Mufutau','Leo','Flavia','Dante','Brielle','Nell','Ariana','Ashely','Jason','Patrick','Brennan','Mallory','Hyatt','Reuben','Uta','Althea','Mara','Megan','Lara','Jena','Carissa','September','Courtney','Pearl','Joelle','Chloe','Charles','Sigourney','Lyle','Ashton','Nell','Giacomo','Jemima','Brandon','Elmo','Lois','Brody','Malcolm','Blair','Gisela','Orson','Lila','Madeson','Dustin','Plato','Pearl','Althea','Slade','Iris','Burton','Dahlia',]
    last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']
    numbers = ['20', '21', '22', '23', '24', '25', '98', '99', '60', '100'] 
    first = random.choice(first_names)
    last = random.choice(last_names)
    choosenumber = random.choice(numbers)
    email = (first+last+choosenumber+"@"+catchall)
    options = Options()
    options.add_argument('ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--enable-javascript")
    #options.add_argument("--headless")
    #options.add_argument("start-maximized")
    #options.add_argument("--enable-logging --v=1")
    driver = webdriver.Chrome("C:/Users/User/Desktop/test/chromedriver", options=options)
    time.sleep(10)
    driver.get("https://www.shiekh.com/customer/account/createpost/")
    time.sleep(10)
    print ("solve captcha to continue...")
    time.sleep(2)
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key("") #enter your 2cap key
    solver.set_website_url("https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcj-R8TAAAAABs3FrRPuQhLMbp5QrHsHufzLf7b&co=aHR0cHM6Ly93d3cuc2hpZWtoLmNvbTo0NDM.&hl=en&v=NjbyeWjjFy97MXGZ40KrXu3v&theme=dark&size=normal&cb=rvbapbbu412e")
    solver.set_website_key("6Lcj-R8TAAAAABs3FrRPuQhLMbp5QrHsHufzLf7b")
    g_response = solver.solve_and_return_solution()
    if g_response != 0:
     print("task finished with no errors " + g_response)
    else:
     print("task finished with error " + solver.error_code)
    time.sleep(5)
    print("captcha solved...")
    time.sleep(50)
    print ("continuing with account creation...")
    
    s1 = driver.find_element_by_xpath('//*[@id="firstname"]')
    s1.send_keys(first)
    print ("using first name: " + first)
    
    s2 = driver.find_element_by_xpath('//*[@id="lastname"]')
    s2.send_keys(last)
    print("using last name: " +last)
    
   # s3 = driver.find_element_by_xpath('//*[@id="is_subscribed"]')
    #s3.click()
    
    fn = driver.find_element_by_xpath('//*[@id="email_address"]')
    fn.send_keys(email)
    print("using email: " +email)
    em = driver.find_element_by_xpath('//*[@id="password"]')
    em.send_keys(password)
    print("using password: " +password)
    time.sleep(1)
    
    si = driver.find_element_by_xpath('//*[@id="password-confirmation"]')
    si.send_keys(password)
    
    s4 = driver.find_element_by_xpath('//*[@id="form-validate"]/div/div[1]/button/span')
    s4.click()
    time.sleep(5)

    print("Successfully created Sheikh account with email: " + email) 

    time.sleep(1)
    driver.close()