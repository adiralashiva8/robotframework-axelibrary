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

    @keyword("Perform Accessibility Test")
    def perform_accessibility_test(self, result_file):
        # get webdriver instance
        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        webdriver = seleniumlib.driver
        # create axe instance
        axe_instance = Axe(webdriver)
        # inject axe-core javascript into current page
        axe_instance.inject()
        # run axe accessibility validations
        results = axe_instance.run()
        # write results to specified file
        axe_instance.write_results(results, result_file)
        # print results
        logger.info(axe_instance.report(results["violations"]))
