class TestResult:
    def __init__(self):
        self.runCount = 1
        self.failedCount = 0

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.failedCount)

class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return TestResult()

    def tearDown(self):
        pass


class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.wasRun = True
        self.log += "testMethod "

    def tearDown(self):
        self.log += "tearDown "


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 falied" == result.summary())

if __name__ == '__main__':
    TestCaseTest("testTemplateMethod").run()
