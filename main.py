import time
import  datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

print("running program")
chrome_options = Options()
chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options)

def cleanup(string):
    newString= ''
    for thing in string:
        if thing == ".":
            break
        try:
            temp = int(thing)
            newString = newString + str(temp)
        except :
            pass

    return newString
def getPrice():
    #   t = driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/main/div/div/div/div/section/header/div[1]/h2/span/div/div[1]")
    t = driver.find_elements(by= By.XPATH ,value= "/html/body/div[1]/div[1]/div[2]/main/div/div/div/div/section/header/div[1]/h2/span/div/div[1]")
    text =  t[0].text
    return cleanup(text)




driver.get("https://robinhood.com/crypto/BTC/")


while True:
    f = open("output1.csv", "a")
    for thing in range(10):
        time.sleep(10)

        price = getPrice()

        # sting = "\n" + str(datetime.datetime.now().strftime("%H:%M:%S")) + "," + price
        sting = "\n" + str(datetime.datetime.now().now()) + "," + price
        if len(price) > 3:
            f.write(sting)
        else:
            print("empty")
        print(sting)

    f.close()


driver.close()





