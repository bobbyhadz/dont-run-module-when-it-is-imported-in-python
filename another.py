# 👇️ Code that you always want to run

print('this line is always run (even on import)')


def main():
    site = 'bobbyhadz.com'

    print(site)

    def greet(name):
        return f'hello {name}'

    print(greet('bobby hadz'))


if __name__ == '__main__':
    # This doesn't run on import
    # It only runs when the module is run directly
    main()