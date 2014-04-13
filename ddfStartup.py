import pexpect
import sys
import unittest

from setupPlatformGlobalConfig import SetupPlatformGlobalConfig
from setupOpenSearch import SetupOpenSearch
from setupGeosciencesAustraliaGazetteer2010WebFeatureServerFederatedSource import SetupGeosciencesAustraliaGazetteer2010WebFeatureServerFederatedSource

class ddfTester():
    def startDDF(self):
        self.ddfProcess = pexpect.spawn("./bin/ddf", timeout=180)
        self.ddfProcess.logfile_read = sys.stdout
        # When we see the prompt, DDF is ready
        self.expectDdfPrompt()

    def expectDdfPrompt(self):
        self.ddfProcess.expect_exact("ddf@local\033[0m>")
        
    def runTests(self):
        self.ddfProcess.sendline("app:list")
        self.expectDdfPrompt()

        suite = unittest.TestLoader().loadTestsFromTestCase(SetupPlatformGlobalConfig)
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SetupOpenSearch))
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(SetupGeosciencesAustraliaGazetteer2010WebFeatureServerFederatedSource))
        unittest.TextTestRunner(verbosity=2).run(suite)

    def goInteractive(self):
        print('Return to interactive mode. Escape character is \'^]\'.')
        self.ddfProcess.sendline("")
        self.ddfProcess.interact()
        print

    def startAndTest(self):
        self.startDDF()
        self.runTests()
        self.goInteractive()

if __name__ == "__main__":
    ddfTester().startAndTest()

