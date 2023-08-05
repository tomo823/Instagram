#clarifai==2.6.2
#emoji==1.7.0


# imports
from instapy import InstaPy
from instapy import smart_run
 
# login credentials
insta_username = "ビズコ|25卒就活部"  # <- メールアドレスではなくusername
insta_password = "tomo0427"  # <- パスワード
 
# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    #片思いの相手リストを取得して表示する
    nonfollowers = session.pick_nonfollowers(username=insta_username, live_match=True, store_locally=True)
    print(nonfollowers)