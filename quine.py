# This program creates a "Hello World!" program, then runs it.

def main():
    program = ["def sayHello():", "\n\tprint('Hello World!')"]
    f = open('hello.py', 'w+')
    for line in program:
        f.write(line)
    f.close()

    import hello
    hello.sayHello()

if __name__ == "main":
    main()
    
