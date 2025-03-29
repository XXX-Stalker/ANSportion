import pyfiglet
def ascii_generator():
    text = input("WordArt:")
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)
if __name__ == "__main__":
    while True:
        ascii_generator()