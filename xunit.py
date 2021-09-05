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

class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)
    
    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetup)

if __name__ == '__main__':
    TestCaseTest("testRunning").run()
    TestCaseTest("testSetup").run()
