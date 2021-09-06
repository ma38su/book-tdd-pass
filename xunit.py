class TestSuite:
    def __init__(self):
        self.tests = []
    
    def add(self, test):
        self.tests.append(test)
    
    def run(self, result):
        for test in self.tests:
            test.run(result)

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failedCount = 0

    def testStarted(self):
        self.runCount += 1
    
    def testFailed(self):
        self.failedCount += 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.failedCount)

class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self, result):
        result.testStarted()

        try:
            self.setUp()
            try:
                method = getattr(self, self.name)
                method()
            except:
                result.testFailed()
        except:
            result.testFailed()
        self.tearDown()

    def tearDown(self):
        pass


class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.log += "testMethod "
        self.wasRun = True
    
    def testBrokenMethod(self):
        self.log += "testBrokenMethod "
        raise Exception

    def tearDown(self):
        self.log += "tearDown "


class TestCaseTest(TestCase):

    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown " == test.log)

    def testTemplateBrokenMethod(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        print(test.log)
        assert("setUp testBrokenMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())
    
    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedFormatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert("1 run, 1 failed" == self.result.summary())

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("testMethod"))
        suite.add(WasRun("testBrokenMethod"))
        suite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())

if __name__ == '__main__':
    suite = TestSuite()
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testTemplateBrokenMethod"))
    suite.add(TestCaseTest("testResult"))
    suite.add(TestCaseTest("testFailedFormatting"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testSuite"))

    result = TestResult()
    suite.run(result)
    print(result.summary())

