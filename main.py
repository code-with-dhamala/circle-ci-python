def to_upper(name):
    return name.upper()


def say_hello(name):
    print(f"Hello, {to_upper(name)}!")

    if __name__ == "__main__":
        name = "Mahendra"
        say_hello(name)
        up = to_upper(name)
        print(f"Uppercase Name: {up}")
