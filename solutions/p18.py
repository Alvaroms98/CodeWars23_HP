frames: list[str] = []
while True:
    inputt = input()
    if inputt == "#":
        break
    frames.append(inputt)

prev_width = 0
for sentence in frames:
    words = sentence.split(" ")
    # Get the max width of this sentence
    width = 0 
    for word in words:
        tam = len(word)
        if tam > width:
            width = tam
    
    first = "#"*(width+4) if width > prev_width else "#"*(prev_width+4)
    print(first)

    for word in words:
        out = "# "
        out += word
        curr_width = len(word)
        if curr_width < width:
            out += " "*(width - curr_width)
        out += " #"
        print(out)
    
    prev_width = width
    
print("#"*(width+4))


    

    