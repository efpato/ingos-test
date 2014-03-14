#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from json import JSONDecoder
from selenium.webdriver import Firefox

from controller import Controller


class KaskoCalcTestCase(unittest.TestCase):
    config = JSONDecoder().decode(open("config.json").read())
    url = config.get("url")
    controller = Controller(Firefox())

    @classmethod
    def setUpClass(cls):
        cls.controller.driver.maximize_window()
        cls.controller.driver.get(cls.url)

    @classmethod
    def tearDownClass(cls):
        cls.controller.driver.close()

    def test(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
