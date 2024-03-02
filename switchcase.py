name = input("What's your name ? ")

#switch case
match name:
#with this '|' we can make more cases that they're gonna have the same result
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
        
    case "Draco":
        print("Slytherin")

    case "Cedrico":
        print("HufflePuff")
#it's what we call default case in C
    case _:
        print("Who?")
