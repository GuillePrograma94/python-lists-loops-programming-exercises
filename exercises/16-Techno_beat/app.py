def lyrics_generator(dj_input):
    lyrics = ""
    counter = 0
    for input in dj_input:
        if input == 0:
            lyrics += "Boom "
            counter = 0
        elif input == 1:
            lyrics += "Drop the Bass "
            counter += 1
            if counter == 3:
                lyrics += "!!!Break the bass!!! "
                counter = 0
    return lyrics


# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
