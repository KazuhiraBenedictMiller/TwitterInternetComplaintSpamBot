import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

PromisedDown = YOUR_PROMISED_DOWN
PromisedUp = YOUR_PROMISED_UP

TwitterAcc = YOUR_TWITTER_EMAIL
TwitterID = YOUR_TWITTER_ID #The one that starts with the "@" but put in there without the "@" -- YOURS
TwitterPass = YOUR_TWITTER_PASSWORD
TweetTag = TWITTER_TARGET_ID #The one that starts with the "@" but put in there without the "@" -- ACCOUNT TO BE SPAMMED

chrome_driver_path = "./chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

LoadingTime = 70

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        self.driver.implicitly_wait(2)
        self.Down = 0
        self.Up = 0

    def GetInternetSpeed(self):
        self.driver.get("https://www.speedtest.net")

        # Accepting Cookies
        AcceptCookies = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        AcceptCookies.click()

        #Clicking Go
        Go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        Go.click()

        #Getting Speed
        time.sleep(LoadingTime)
        self.Down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.Up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def Tweet(self, Message):
        self.driver.get("https://twitter.com/")

        #Login
        Login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/a/div')
        Login.click()

        #Email
        Email = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        Email.send_keys(TwitterAcc)
        Email.send_keys(Keys.ENTER)

        #In case of double check
        try:
            ID = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            ID.send_keys(TwitterID)
            ID.send_keys(Keys.ENTER)

        except NoSuchElementException:
            pass

        #Password
        Password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        Password.send_keys(TwitterPass)
        Password.send_keys(Keys.ENTER)

        #Tweet
        time.sleep(10)
        ComposeTweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        ComposeTweet.click()

        Tweet = self.driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Tweet text')]")
        Tweet.send_keys(Message)
        Tweet.send_keys(Keys.CONTROL + Keys.ENTER)

Bot = Bot()
Bot.GetInternetSpeed()
Down = int(Bot.Down.split(".")[0])
Up = int(Bot.Up.split(".")[0])

if Down < PromisedDown or Up < PromisedUp:
    Message = f"Hey @{TweetTag}, How comes that my Minimum Promised Download/Upload Internet Speed is {PromisedDown}/{PromisedUp} Mbps and I only have available {Down}/{Up} Mbps right now?"
    Bot.Tweet(Message)

Bot.driver.quit()