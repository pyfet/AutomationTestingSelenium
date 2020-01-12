import json
import pyfiglet
import automation_tests
import sys

from unittest import main, TestLoader, TestSuite, TextTestRunner
from selenium import webdriver
from textwrap import dedent
from time import sleep
from automation_tests import *
from count import *

website = 'https://www.way2automation.com/way2auto_jquery/index.php'

def intro():
    print(pyfiglet.figlet_format("              Hello!!", font = "graffiti"))
    sleep(0.5)
    print('-'*100)
    sleep(0.5)
    print(pyfiglet.figlet_format("      Automation", font = "slant"))
    print(pyfiglet.figlet_format("    Testing With", font = "slant"))
    sleep(0.5)
    print(pyfiglet.figlet_format("      Selenium", font = "slant"))
    sleep(0.5)
    print('-'*100)
    sleep(1)
    print(f'Performing test on {website}') 
    print('using python-selenium(https://selenium-python.readthedocs.io/)')
    print('What do you want to test today(Enter `exit` if you want to quit)...')
    sleep(0.5)

def outro():
    print('\n')
    print(pyfiglet.figlet_format("  Come Again!!", font = "slant"))
    sleep(0.5)
    print(pyfiglet.figlet_format("      Bye!!", font = "speed"))

def select_browser():
    print(
        dedent('''
            Select a web browser(beta):
                1. chrome
                2. firefox'''
            )
    )
    valid = False
    while not valid:
        try:
            browser = str(input('\n  > '))
            browser = browser.lower()
            if browser == '1' or browser == 'chrome':
                browser = "webdriver.Chrome()"
                valid = True
            elif browser == '2' or browser == 'firefox':
                browser = "webdriver.Firefox()"
                valid = True
            elif browser == 'exit':
                outro()
                sys.exit()
            else:
                print("Please enter a valid choice")
        except EOFError:
            pass
    sleep(1)
    return browser

def simulate_login(browser):
    print("\nYou can simulate Signup and Signin (press ENTER to pass)")
    print(dedent('''
        1. SignUp
        2. SignIn
    '''))
    
    valid = False
    while not valid:
        try:
            process = str(input(' > '))
            process = process.lower()
            if process == '1' or process == 'signup':
                driver = eval(browser)
                driver.set_window_size(1920, 1080)
                driver.get(website)
                authenticate = Authenticate(driver)
                authenticate.register()
                driver.close()
                valid = True
            elif process == '2' or process == 'signin':
                driver = eval(browser)
                driver.set_window_size(1920, 1080)
                driver.get(website)
                authenticate = Authenticate(driver)
                authenticate.login()
                driver.close()
                valid = True
            elif process == '':
                valid = False
            elif process == 'exit':
                outro()
                sys.exit()
            else:
                print("Please enter a valid choice")
        except EOFError:
            pass

def count_modules(browser):
    valid = False
    while not valid:
        try:
            count_modules = str(input('\nWould you like to count available modules? [y|N] (press ENTER to pass) > '))
            count_modules = count_modules.lower()
            if count_modules == 'y' or count_modules == 'yes':
                print('counting...    ---    ', end='')
                print(total_modules(browser))
                valid = True
            elif count_modules == 'n' or count_modules == 'no' or count_modules == '':
                valid = True
            elif count_modules == 'exit':
                outro()
                sys.exit()
            else:
                print("Please enter a valid choice")
        except EOFError:
            pass

    sleep(0.5)  
    print("The modules are subdivided into several sections:")
    options = json.load(open('section_options.json'))
    for key, value in options.items():
        print('    {:>3}: {}'.format(key, value.replace('_', ' ')))        

    valid = False
    while not valid:
        try:
            section = str(input('Enter a section name to get the number of modules present there (press ENTER to pass) > '))    
            section = section.replace(' ', '_')
            section = section.lower()
            if section in options:
                print('counting sections...    ---    ', end='')
                print(no_of_modules_in_section(browser, section))
                valid = True
            elif section in options.values():
                print('counting sections...    ---    ', end='')
                section = get_key(section)
                print(no_of_modules_in_section(browser, section))
                valid = True
            elif section == '':
                valid = True
            elif section == 'exit':
                outro()
                sys.exit()
            else:
                print("Please enter a valid choice")
        except EOFError:
            pass    
    sleep(1)

def select_module():    
    print("\nEnter a module to test")
    options = json.load(open('options.json'))
    for key, value in options.items():
        print(f'    {key}: {value}')
    valid = False
    while not valid:
        try:
            module = str(input('\n  > '))
            module = module.lower()
            if module in options:
                module = options.get(module)
                valid = True
            elif module in options.values():
                valid = True
            elif module == 'exit':
                outro()
                sys.exit()
            else:
                print("Please enter a valid choice")
        except EOFError:
            pass        
    sleep(1)        
    return module

def test_module(choice, browser):
    if choice == 'all':
        main(module=automation_tests)
    else:
        suite = unittest.TestSuite()
        suite.addTest(AutomationTest("test_"+choice))
        runner = unittest.TextTestRunner()
        runner.run(suite)

def test_more():
    try:
        choice = str(input("Do you wish to continue[yes|No]? > "))
        choice = choice.lower()
        if choice == 'y' or choice == "yes":
            return True
        elif choice == "n" or choice == "no":
            outro()
            sys.exit()
    except EOFError:
        pass    

if __name__ == "__main__":
    try:
        intro()                
        flag = True
        while flag:
            browser = select_browser()
            simulate_login(browser)
            count_modules(browser)
            module = select_module()
            test_module(module, browser)
            flag = test_more()
        outro()
    except KeyboardInterrupt:
        outro()
