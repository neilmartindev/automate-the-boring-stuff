adj = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
verb = input("Enter a verb: ")

with open("madlib.txt", "w") as external_file:
    add_text = "The " + adj + " panda walked to the " + noun1 + " and then " + verb + ". A nearby " + noun2 + " was unaffected by these events"
    print(add_text, file=external_file)
    print(add_text)
    external_file.close()
    
    

