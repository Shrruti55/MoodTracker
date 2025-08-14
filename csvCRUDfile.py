import pandas as pd
import os
import random

# Folder name from the CSV generator
FOLDER_NAME = "mood_data"

# READ: Get a random entry from a database CSV
def get_mood(mood_name):
    file_path = os.path.join(FOLDER_NAME, f"{mood_name}.csv")
    if not os.path.exists(file_path):
        return f"No CSV file found for mood: {mood_name}"
    df = pd.read_csv(file_path)
    return df.sample(1).to_dict(orient="records")[0]  # Returns a random row as a dict

#  CREATE: Add a new entry to a database CSV
def add_entry(mood_name, emoji, quote, song, bg_color):
    file_path = os.path.join(FOLDER_NAME, f"{mood_name}.csv")
    new_entry = {
        "Emoji": emoji,
        "Mood": mood_name,
        "Quote": quote,
        "Song": song,
        "Background_Color": bg_color
    }
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    else:
        df = pd.DataFrame([new_entry])
    df.to_csv(file_path, index=False)
    return f"Entry added to {mood_name} mood."

#  UPDATE: Update entry by index in a database CSV
def update_entry(mood_name, index, emoji=None, quote=None, song=None, bg_color=None):
    file_path = os.path.join(FOLDER_NAME, f"{mood_name}.csv")
    if not os.path.exists(file_path):
        return f"No CSV file found for mood: {mood_name}"
    df = pd.read_csv(file_path)
    if index < 0 or index >= len(df):
        return "Invalid index."
    if emoji: df.at[index, "Emoji"] = emoji
    if quote: df.at[index, "Quote"] = quote
    if song: df.at[index, "Song"] = song
    if bg_color: df.at[index, "Background_Color"] = bg_color
    df.to_csv(file_path, index=False)
    return f"Entry {index} updated in {mood_name} mood."

#  DELETE: Delete entry by index in a database CSV but with backup already saved
def delete_entry(mood_name, index):
    file_path = os.path.join(FOLDER_NAME, f"{mood_name}.csv")
    backup_path = os.path.join(FOLDER_NAME, f"{mood_name}_backup.csv")

    if not os.path.exists(file_path):
        return f"No CSV file found for mood: {mood_name}"
    
    df = pd.read_csv(file_path)
    if index < 0 or index >= len(df):
        return "Invalid index."

    # Row to be deleted
    deleted_row = df.iloc[[index]]

    # Save to backup file (append mode)
    if os.path.exists(backup_path):
        backup_df = pd.read_csv(backup_path)
        backup_df = pd.concat([backup_df, deleted_row], ignore_index=True)
    else:
        backup_df = deleted_row
    backup_df.to_csv(backup_path, index=False)

    # Delete from main CSV
    df = df.drop(index).reset_index(drop=True)
    df.to_csv(file_path, index=False)

    return f"Entry {index} deleted from {mood_name} mood (backup saved)."

def restore_last_deleted(mood_name):
    file_path = os.path.join(FOLDER_NAME, f"{mood_name}.csv")
    backup_path = os.path.join(FOLDER_NAME, f"{mood_name}_backup.csv")

    if not os.path.exists(backup_path):
        return "No backup found."

    backup_df = pd.read_csv(backup_path)
    if backup_df.empty:
        return "Backup is empty."

    # Get last deleted row
    last_row = backup_df.tail(1)

    # Remove it from backup
    backup_df = backup_df.iloc[:-1]
    backup_df.to_csv(backup_path, index=False)

    # Add it back to main CSV
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, last_row], ignore_index=True)
    else:
        df = last_row
    df.to_csv(file_path, index=False)

    return f"Last deleted entry restored to {mood_name} mood."


#  EXTRA: List all moods available in folder
def list_moods():
    return [f.split(".")[0] for f in os.listdir(FOLDER_NAME) if f.endswith(".csv")]

# SEARCH: Search for entries in a mood CSV by keyword or specific field
def search_entries(mood_name, keyword=None, emoji=None, quote=None, song=None, bg_color=None):
    file_path = os.path.join(FOLDER_NAME, f"{mood_name}.csv")
    if not os.path.exists(file_path):
        return f"No CSV file found for mood: {mood_name}"
    
    df = pd.read_csv(file_path)

    # Apply filters one by one
    if keyword:
        # Search in all columns for keyword
        df = df[df.apply(lambda row: row.astype(str).str.contains(keyword, case=False, na=False).any(), axis=1)]
    if emoji:
        df = df[df["Emoji"].str.contains(emoji, case=False, na=False)]
    if quote:
        df = df[df["Quote"].str.contains(quote, case=False, na=False)]
    if song:
        df = df[df["Song"].str.contains(song, case=False, na=False)]
    if bg_color:
        df = df[df["Background_Color"].str.contains(bg_color, case=False, na=False)]

    if df.empty:
        return "No matching entries found."
    else:
        return df.to_dict(orient="records")
