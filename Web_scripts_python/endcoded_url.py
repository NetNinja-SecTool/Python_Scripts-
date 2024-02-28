def urlEncode():
    # Taking URL input from the user
    url = input("Enter the URL to encode: ")
    while not url:
        url = input("Please enter a valid URL: ")

    sozluk = {
        " ": "%20", "!": "%21", "#": "%23", "$": "%24", "%": "%25", "&": "%26", "'": "%27", "(": "%28",
        ")": "%29", "*": "%30", "+": "%2B", ",": "%2C",
        "-": "%2D", ".": "%2E", "/": "%2F", "0": "%30", "1": "%31", "2": "%32", "3": "%33", "4": "%34",
        "5": "%35", "6": "%36", "7": "%37", "8": "%38",
        "9": "%39", ":": "%3A", ";": "%3B", "<": "%3C", "=": "%3D", ">": "%3E", "?": "%3F", "@": "%40",
        "A": "%41", "B": "%42", "C": "%43", "D": "%44",
        "E": "%45", "F": "%46", "G": "%47", "H": "%48", "I": "%49", "J": "%4A", "K": "%4B", "L": "%4C",
        "M": "%4D", "N": "%4E", "O": "%4F", "P": "%50",
        "Q": "%51", "R": "%52", "S": "%53", "T": "%54", "U": "%55", "V": "%56", "W": "%57", "X": "%58",
        "Y": "%59", "Z": "%5A", "[": "%5B", "]": "%5D",
        "^": "%5E", "_": "%5F", "`": "%60", "a": "%61", "b": "%62", "c": "%63", "d": "%64", "e": "%65",
        "f": "%66", "g": "%67", "h": "%68", "i": "%69",
        "j": "%6A", "k": "%6B", "l": "%6C", "m": "%6D", "n": "%6E", "o": "%6F", "p": "%70", "q": "%71",
        "r": "%72", "s": "%73", "t": "%74", "u": "%75",
        "v": "%76", "w": "%77", "y": "%78", "z": "%7A", "{": "%7B", "|": "%7C", "}": "%7D", "~": "%7E"
    }

    # Encode URL
    encodeURL = ""
    for i in url:
        encodeURL += sozluk.get(i, i)

    # Print the encoded URL line by line
    print("[+]Encoded URL:")
    print(encodeURL)

# Call the function
urlEncode()
