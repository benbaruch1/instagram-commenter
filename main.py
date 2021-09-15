import random
import time
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import proxy
import settings

#  Target Details
photo_URL = "https://www.instagram.com/p/CTlLfpNHbEC/"
amount_of_comments = 1
print("Comments Requested: %d" % amount_of_comments)

if len(settings.accounts_list) < amount_of_comments and len(settings.accounts_list) != amount_of_comments:
    print("ERROR! Not enough accounts loaded for %d comments." % amount_of_comments)
    exit()


#  Start
comments_done = 0
account_number = 1
while comments_done < amount_of_comments:
    # driver = webdriver.Chrome(settings.path_of_driver)
    driver = proxy.get_chromedriver(use_proxy=settings.proxy)
    #  Account details + Comment
    username = settings.accounts_list[account_number - 1][0]
    password = settings.accounts_list[account_number - 1][1]
    comment = settings.comments_list[comments_done]

    driver.get("https://instagram.com")
    time.sleep(10)

    username_input_form = driver.find_element_by_name("username")
    password_input_form = driver.find_element_by_name("password")
    username_input_form.send_keys(username)
    password_input_form.send_keys(password)
    password_input_form.send_keys(Keys.RETURN)

    time.sleep(5)

    #  Save your login info window
    try:
        save_login_window = driver.find_element_by_class_name("cmbtv")
        if save_login_window.is_displayed():
            save_login_window.click()  # this will click "Not Now"
            time.sleep(5)
    except NoSuchElementException:  # if the window doesn't show up
        time.sleep(10)

    # Connection completed. Go to URL and comment.

    driver.get(photo_URL)
    comment_box = driver.find_element_by_class_name("Ypffh")
    comment_box.click()
    comment_box = driver.find_element_by_class_name("Ypffh")  # Need to click twice because IG algo
    comment_box.click()
    time.sleep(2)
    comment_box.send_keys(comment)
    time.sleep(2)
    comment_box.send_keys(Keys.RETURN)
    now = datetime.now()  # Get time now.
    time_log = now.strftime("%H:%M:%S")
    print("[%s] Comment posted from %s." % (time_log, username))
    time.sleep(5)
    driver.delete_all_cookies()
    driver.quit()

    comments_done += 1
    account_number += 1
    delay_time = random.randint(30, 120)
    now = datetime.now()  # Get time now.
    time_log = now.strftime("%H:%M:%S")
    print("[%s] Waiting %d seconds before next account..." % (time_log, delay_time))
    time.sleep(delay_time)  # Wait between 30 secs to 2 mins before next account.

