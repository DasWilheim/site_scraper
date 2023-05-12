import time
from selenium import webdriver
from pynput.keyboard import Controller, Key
import pandas as pd
import pyautogui as ag
from datetime import datetime, date
import pyperclip
import locale

# Set the locale to Dutch
locale.setlocale(locale.LC_TIME, 'nl_NL')

def close_tab():
    keyboard.press(Key.ctrl_l)
    keyboard.press("w")
    keyboard.release("w")
    keyboard.release(Key.ctrl_l)

keyboard = Controller()
browser = webdriver.Chrome()

click = False
run = True
enkelFoto = False
lastx = False
lastreviews = 80

url = '\
https://www.snappcar.nl/auto-huren/auto/opel-vivaro/1e9ebb5c-97ad-4342-0207-08db226efb70?searchId=057153b9-8c85-4454-9a48-3a84cf27f5aa&searchSessionId=0474c020-b8da-42f1-a992-77054fa09dd1\
    '

list_placeholder = []
list1 = []
list_index = []
kb = Controller()
browser.get(url)

time.sleep(0.2)  
browser.find_element_by_xpath('/html/body/app-root/ng-component/app-main-page/app-privacy-banner/section/div/button').click()
time.sleep(0.5)  
if enkelFoto:
    browser.execute_script("window.scrollTo(0,500)")
    time.sleep(1) 
    browser.execute_script("window.scrollTo(0,0)")
    time.sleep(0.5) 
    ag.moveTo(970,250)
    ag.click()
    
    time.sleep(0.5)
    ag.moveTo(1008, 555)
    time.sleep(0.1) 
    ag.mouseDown()
    time.sleep(0.1) 
    ag.moveTo(1084, 555)
    time.sleep(0.1) 
    ag.mouseUp()
else:   
    browser.execute_script("window.scrollTo(0,500)")
    time.sleep(1)  
    ag.moveTo(970,250)
    ag.click()
    time.sleep(1) 
    
    ag.moveTo(1010, 455)
    
    ag.mouseDown()
    
    ag.moveTo(1080, 455)
    time.sleep(0.1) 
ag.mouseUp()
time.sleep(0.1) 
ag.hotkey('ctrl', 'c')

time.sleep(0.1) 





# Read the contents of the clipboard
clipboard_contents = pyperclip.paste().replace(',','.')
price = float(clipboard_contents)
print(price*3)
try:

    previews = browser.find_element_by_xpath('//*[@id="car-detail-header"]/header/div/div/div[1]/p/span[1]').text.replace('\n',' $ ')[30:34].replace(' ','').replace('b','')
    
    hires = browser.find_element_by_xpath('//*[@id="car-detail-header"]/header/div/div/div[1]/p').text.replace('\n',' $ ')

    split_string = hires.split("$")
    number = split_string[-1].strip().split(" ")[-2].replace('x','')
    hireNumber = int(number)
    
    previews = int(previews)

            
    if lastx:
        hireNumber = hireNumber/previews* lastreviews
        previews = lastreviews
    a = previews
    print("done")
    
except:
    pass
    run = False
    print("could not find the correct values of reviews")
i = 0
run = True
while  run:

     i += 1
     try:
        time.sleep(0.3) 
        browser.find_element_by_xpath('//*[@id="car-detail-reviews"]/button').click()
        if i > lastreviews/3 and lastx:
                browser.find_element_by_xpath('//*[@il-reviws"]/button').click()

     except:
        print("done clicking")
        run = False
        dates = browser.find_element_by_xpath('//*[@id="car-detail-reviews"]/app-car-detail-review[{}]/div/div/p/span[2]'.format(a)).text
        try:
            date_object = datetime.strptime(dates, "%d %b. %Y").date()
        except:
            date_object = datetime.strptime(dates, "%d %B %Y").date()
            
        print(date_object)
        close_tab()
            
today = date.today()
print("Today's date:", today)

date1 = date_object
print("Date to calculate:", date1)

#calculate the difference
diff = today - date1
print("Difference:", diff)

#calculate the total months
total_months = diff.days / 30
print("Total months:", total_months)
#Main loop
print('')
print('Hires per maand',(hireNumber/total_months))
print('')
print("monthly income in euros", price* (hireNumber/total_months))

data = pd.DataFrame(list_placeholder, index=list_index, columns=['Company name','City'])
data.to_excel('webscraper_result_nummers.xlsx', sheet_name='Blad1', index=False) 
    


