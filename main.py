import json
import pyfiglet
import automation_tests

from unittest import main, TestLoader, TestSuite, TextTestRunner
from textwrap import dedent
from time import sleep
from automation_tests import *

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
    print('What do you want to test today...')
    sleep(0.5)

def outro():
    print('\n')
    print(pyfiglet.figlet_format("  Come Again!!", font = "slant"))
    sleep(0.5)
    print(pyfiglet.figlet_format("      Bye!!", font = "speed"))

def options():
    options = json.load(open('options.json'))    
    for key, value in options.items():
        print(f'    {key}: {value}')
    valid = False
    while not valid:
        try:
            module = str(input('\n  > '))
            module = module.lower()
            if module in options:
                valid = True
            elif module in options.values():
                valid = True
            else:
                print("Please enter a valid choice")
        except EOFError:
            pass        

    sleep(0.5)
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
                valid = True
            elif browser == '2' or browser == 'firefox':
                valid = True
            else:
                print("Please enter a valid choice")
        except EOFError:
            pass
        
    return module, browser

def test_module(choice, browser):
    options = json.load(open('options.json'))

    if choice in options:
        choice = options.get(choice)

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
            return False
    except EOFError:
        pass    

if __name__ == "__main__":
    try:
        intro()                
        flag = True
        while flag:
            module, browser = options()
            test_module(module, browser)
            flag = test_more()

    except KeyboardInterrupt:
        outro()
