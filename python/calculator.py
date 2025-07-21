"""Simple calculator app"""


def main():
    while True:
        try:
            string = input("> ")
            print(eval(string))
        except (KeyboardInterrupt, EOFError):
            print()
            exit()
        except (BaseException, KeyboardInterrupt) as e:
            print(e)


if __name__ == "__main__":
    print("Welcome to calculator!")
    main()

try:
    x = 1
    print(x)
except:
    print("why except")