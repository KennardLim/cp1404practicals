COLOUR_TO_CODE = {"White": "#ffffff","Black": "#000000","Red": "#ff0000","Orange": "#ffa500","Yellow": "#ffff00","Green": "#00ff00", "Blue": "#0000ff", "Indigo": "#4b0082", "Violet": "#ee82ee", "Cyan": "#00ffff", "Brown": "#a52a2a"}

colour = input("Colour: ").title()
while colour != "":
    try:
        print(f"{colour:{len(max(list(COLOUR_TO_CODE.keys()), key=len))}} is {COLOUR_TO_CODE[colour]}")
    except KeyError:
        print("Invalid Colour")
    colour = input("Colour: ").title()