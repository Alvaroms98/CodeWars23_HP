if __name__ == "__main__":
    my_lives = 7
    # First input, the word to guess
    the_word = input()
    the_lenght = len(the_word)
    hidden_word = "_"*the_lenght

    # A list to save the matches
    match_letters = []

    # Second input, the try of the player
    attempt = input()

    # For loop to calculate the fails of the user in this attempt, and to save the matches in the list
    fails = 0
    for letter in attempt:
        if fails == 7:
            break
        if letter in the_word and letter not in match_letters:
            match_letters.append(letter)
        elif letter not in the_word:
            fails += 1
    # Update lives
    my_lives = my_lives - fails

    has_won = True
    # Loop to show the letters that match the word
    output = ""
    for i in range(the_lenght):
        curr = the_word[i]
        if curr in match_letters:
            output += curr
        else:
            output += "_"
            has_won = False
    
    # Outputs
    print(hidden_word)
    print(output)
    if has_won and my_lives > 0:
        print("Player wins!")
    elif my_lives <= 0:
        print("Player loses.")
        my_lives = 0
    else:
        print("Word not completed and player is still alive.")
    print(f"Lives: {my_lives}")
