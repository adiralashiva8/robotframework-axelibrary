import json
from .version import VERSION
from selenium import webdriver
from axe_selenium_python import Axe
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger

class AxeLibrary():

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self):
        self.axe_instance = None
        self.results = None

    @keyword("Run Accessibility Tests")
    def run_accessibility_tests(self, result_file):
        """
        Executes accessibility tests in current page by injecting axe-core javascript and write results into `result_file` (json). Return result statisitics

        |  = Attribute =  |  = Description =  |
        | result_file     |  File to store accessibility test results (.json). Ex: google.json  |
        """
        # get webdriver instance
        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        webdriver = seleniumlib.driver
        # create axe instance
        self.axe_instance = Axe(webdriver)
        # inject axe-core javascript into current page
        self.axe_instance.inject()
        # run axe accessibility validations
        self.results = self.axe_instance.run()
        # write results to specified file
        self.axe_instance.write_results(self.results, result_file)
        # generate json
        result_dict = {"inapplicable":len(self.results["inapplicable"]), "incomplete":len(self.results["incomplete"]),
         "passes":len(self.results["passes"]), "violations":len(self.results["violations"])} 
        logger.info(result_dict)
        # return result
        return result_dict
    
    @keyword("Get Json Accessibility Result")
    def get_json_accessibility_result(self):
        """
        Return accessibility test result in Json format. Need to be used after `Run Accessibility Tests` keyword    
        """
        axe_result = json.dumps(self.results, indent = 3)
        logger.info(axe_result)
        return axe_result
    
    @keyword("Log Readable Accessibility Result")
    def log_readable_accessibility_result(self, type):
        """
        Inserts readable accessibility result into `log.html` based on given `type`. Need to be used after `Run Accessibility Tests` keyword

        |  = Attribute =  |  = Description =  |
        | Type            |  `violations`, `incomplete` are two supported values  |
        """
        logger.info(self.axe_instance.report(self.results[type]))