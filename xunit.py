class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.wasRun = None

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
