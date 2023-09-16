import instaloader, re  
import pandas as pd
 
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
 
# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'kouki10354')
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
#before printing bio, decode it
bio_text = profile.biography
#profile can only include alphabets, numbers, japanese, katakana, hiragana, and kanji
#so, we need to filter out emojis and other symbols
symbol_lists = ["\U0001f4ad", "\u25b6", "\ufe0e", "\U0001f4e9"]
for symbol in symbol_lists:
    if symbol in bio_text:
        bio_text = bio_text.replace(symbol, "")
print("Sanitized Bio: ", bio_text)
print("External URL: ", profile.external_url)