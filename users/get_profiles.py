import instaloader, re, csv , os, inspect
import pandas as pd
 
# Creating an instance of the Instaloader class


def get_filtered_profile(username):
    # Loading a profile from an Instagram handle
    #print(instaloader.instaloader)
    bot = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(bot.context, username)
    print(type(bot))
    print("Username: ", profile.username)
    #print("User ID: ", profile.userid)
    #print("Followers Count: ", profile.followers)
    #print("Following Count: ", profile.followees)
    #before printing bio, decode it
    bio_text = profile.biography
    #profile can only include alphabets, numbers, japanese, katakana, hiragana, and kanji
    #so, we need to filter out emojis and other symbols
    symbol_lists = ["\U0001f4ad", "\u25b6", "\ufe0e", "\U0001f4e9"]
    for symbol in symbol_lists:
        if symbol in bio_text:
            bio_text = bio_text.replace(symbol, "")
    print("Sanitized Bio: ", bio_text)
    return bio_text
    #print("External URL: ", profile.external_url)


def filter(text):
    evaluation = False
    filter_list = ["Kumamoto", "kumamoto", "くま", "Km", "KU", "熊", "🧸", "🐻"]
    for kuma in filter_list:
        if kuma in text:
            text = text.replace(kuma, "")
            evaluation = True
            break

    return evaluation

#extract followers list from csv file into list as followers
def read_csv():
    with open("followers.csv", 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            followers.append(row)


def filter_list(followers):
    filtered_followers = []
    for follower in followers:
        profile_text = get_filtered_profile(follower)
        if filter(profile_text):
            filtered_followers.append(follower)
    return filtered_followers



def write_csv(filtered_followers):
    with open("kumamoto_followers.csv", 'a') as f:
        writer = csv.writer(f)
        for follower in filtered_followers:
            writer.writerow([follower])

if __name__ == "__main__":
    followers = []
    read_csv()
    filtered_followers = filter_list(followers[0])
    print(filtered_followers)
    write_csv(filtered_followers)