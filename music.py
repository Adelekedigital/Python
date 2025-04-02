# Task 3: Music Playlist 🎵

# You are managing a music app and need to handle a user's playlist.

# Instructions:

# Create a list called playlist containing five song titles.

playlist = [
    "Rainbow",
    "Why me",
    "Balotelli",
    "Lonely",
    "Court"
    ]

# A user wants to add two new songs at once. Use an appropriate method to extend the list with these songs.

playlist.extend(["waterfall", "mundane"])

# The user decides to remove a song they no longer like. Remove the third song from the playlist.

# with item name
# playlist.remove("Balotelli")

# with index no
playlist.pop(2)

# Print the updated playlist
print(playlist)

# display the total number of songs in it.
print(len(playlist))

# Retrieve and print the first three songs in the playlist using slicing.
print(playlist[:3])
    







