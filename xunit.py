class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def setUp(self):
        self.log = "setUp "

    def testMethod(self):
        self.wasRun = True
        self.log += "testMethod "

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod " == test.log)

if __name__ == '__main__':
    TestCaseTest("testTemplateMethod").run()
