class WasRun:
    def __init__(self, name):
        self.name = name
        self.wasRun = None

    def run(self):
        self.testMethod()
        method = getattr(self, self.name)
        method()

    def testMethod(self):
        self.wasRun = True

def main():
    test = WasRun("testMethod")

    if test.wasRun:
        exit(1)

    test.testMethod()

    if not test.wasRun:
        exit(1)

if __name__ == '__main__':
    main()
