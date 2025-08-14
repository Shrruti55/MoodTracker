from csvCRUDfile import *

# List available moods
print("Available moods:", list_moods())

# Add new entry
print(add_entry("Happy", "🤩", "Shine bright like the sun!", "wo kisna hai.mp3", "#FFFF00"))

# Get a random mood entry
print(get_mood("Happy"))

# Update entry at index 0
print(update_entry("Happy", 0, quote="Happiness doubles when shared."))

# Delete entry at index 1
print(delete_entry("Happy", 1))

# to restore the deleted entry
print(restore_last_deleted("Happy"))
