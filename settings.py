#  Chrome Settings
path_of_driver = r"C:\python\chromedriver.exe"

#  Comments and usernames files
accounts_file = r"C:\python\instagram-commenter\accounts.txt"
comments_file = r"C:\python\instagram-commenter\comments.txt"

#  Proxy
proxy = True  # Set True or False.

#  Load comments to list
with open(comments_file, "r", encoding='utf-8') as fptr:
    comments_list = fptr.read()
    comments_list = comments_list.split("\n")

#  Load Accounts to list
accounts_list = []

with open(accounts_file, "r") as fptr:
    temp = fptr.read()
    temp_list = temp.split("\n")

for element in temp_list:
    accounts_list.append(element.split(":"))

accounts_list = [(element[0], element[1]) for element in accounts_list]  #  make accounts as tuple. unchangeable

print("""Proxy: %s
Comments Loaded: %d
Accounts Loaded: %d
""" % (proxy, len(comments_list), len(accounts_list)))

