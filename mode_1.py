# using __name__ and __main__

print("This is mode 1 " + __name__)

def main():
# pass - passes through without throwing any errors

    return "from mode 1 function"

# checks if code is run from the current file
if __name__ == '__main__':
    main()