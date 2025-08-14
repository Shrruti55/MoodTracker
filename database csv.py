import pandas as pd
import os

# Folder for storing csv files
folder_name = "mood_data"
os.makedirs(folder_name, exist_ok=True)

# Mood data dictionary
mood_data = {
    "Happy": [
        {"Emoji": "🙂", "Mood": "Happy", "Quote": "Happiness is a journey, not a destination.", "Song": "love you zindagi - dear zindagi", "Background_Color": "#FFD700"},
        {"Emoji": "😄", "Mood": "Happy", "Quote": "Smile, it’s free therapy.", "Song": "phir se udd chala - Rockstar", "Background_Color": "#FFFACD"},
        {"Emoji": "😁", "Mood": "Happy", "Quote": "A day without laughter is a day wasted.", "Song": "Gallan goodiyan - dil dhadkane do", "Background_Color": "#FFFF99"}
    ],
    "Sad": [
        {"Emoji": "😢", "Mood": "Sad", "Quote": "Tears are words that the heart can’t express.", "Song": "Agar tum saath ho - Tamasha", "Background_Color": "#4682B4"},
        {"Emoji": "😭", "Mood": "Sad", "Quote": "Sometimes you just need a good cry.", "Song": "Ae dil hain mushki - Ae dil hai mushkil", "Background_Color": "#5F9EA0"},
        {"Emoji": "😞", "Mood": "Sad", "Quote": "Every storm runs out of rain.", "Song": "Raabta - agent vinod", "Background": "#87CEEB"}
    ],
    "Angry": [
        {"Emoji": "😡", "Mood": "Angry", "Quote": "Speak when you are angry and you'll make the best speech you'll ever regret.", "Song": "Bulleya - Ae dil hain mushkil", "Background_Color": "#FF4500"},
        {"Emoji": "😠", "Mood": "Angry", "Quote": "Anger is one letter short of danger.", "Song": "Bekhayali - kabir singh", "Background_Color": "#FF6347"},
        {"Emoji": "😤", "Mood": "Angry", "Quote": "Don't let anger control you, let it teach you.", "Song": "Jee karda - Badlapur", "Background_Color": "#FF7F50"}
    ],
    "Love": [
        {"Emoji": "😍", "Mood": "Love", "Quote": "You are my today and all of my tomorrows.", "Song": "tum mile - tum mile", "Background_Color": "#FF69B4"},
        {"Emoji": "🥰", "Mood": "Love", "Quote": "Every love story is beautiful, but ours is my favorite.", "Song": "teri meri kahani - gabbar is back", "Background_Color": "#FFC0CB"},
        {"Emoji": "❤️", "Mood": "Love", "Quote": "Love is composed of a single soul inhabiting two bodies.", "Song": "janam janam - dilwale", "Background_Color": "#FFB6C1"}
    ],
    "Tired_Neutral": [
        {"Emoji": "😴", "Mood": "Tired/Neutral", "Quote": "Sometimes the most productive thing you can do is rest.", "Song": "Let Her Go – Passenger", "Background_Color": "#A9A9A9"},
        {"Emoji": "😐", "Mood": "Tired/Neutral", "Quote": "Not every day has to be perfect.", "Song": "Sooraj dooba hain - Roy", "Background_Color": "#C0C0C0"},
        {"Emoji": "🤔", "Mood": "Tired/Neutral", "Quote": "The quieter you become, the more you can hear.", "Song": "ilahi - yeh jawani hai deewani", "Background_Color": "#D3D3D3"}
    ]
}

# Create CSV files in table form printing
for mood, entries in mood_data.items():
    df = pd.DataFrame(entries)
    file_path = os.path.join(folder_name, f"{mood}.csv")
    df.to_csv(file_path, index=False)
    print(f"\n {mood} Mood Data:")
    print(df)

print("\n All CSV files created successfully in the 'mood_data' folder.")

print("\n-------------------------------THNAK YOU-------------------------------------")