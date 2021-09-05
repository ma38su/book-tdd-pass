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

    assert(test.wasRun)

    test.testMethod()

    assert(test.wasRun)

if __name__ == '__main__':
    main()
