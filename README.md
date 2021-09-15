# instagram-commenter

Instagram commenter bot. The bot gets accounts and comments from text files. Then, it connects each account and post a comment from the text file(by order). It has option of using proxy if needed.

Explanation in a few steps:
1. Connect.
2. Go to post and comment.
3. Logout
4. Delay for 30 secs to 2 mins.
5. Next account until done.

## Settings

Make sure you change paths in settings.py.

* ### Chrome Driver
Change path_of_driver to your chrome driver path.

* ### Accounts file
Change accounts_file to your accounts.txt file.
##### Make sure you write accounts in this form: Username:Password

* ### Comments file
Change comments_file to your comments.txt file.
Make sure you write each comment in a new line. # Do not include Emojis!

* ### Proxy

If you want to use proxy, change in line 9 to True. If not, change it to False.

In addition, in proxy.py file you need to insert your proxy hostname, port and authentication.


## Run

In main.py, you need to put target post URL. (line 12)

In the next line(line 13), you choose how many comments to post.
