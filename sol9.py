    # TODO: What's your name?

def print_full_name(first, last):
    msg = "Hello "
    msg = msg + first + " " + last + "! "
    msg = msg + "You just delved into python."
    print(msg)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)