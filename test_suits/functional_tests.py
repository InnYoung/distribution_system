#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_get_login_web(self):
        self.browser.get("http://localhost:8000")

        # 验证首页title包含Tiger
        self.assertIn('Tiger', self.browser.title)
        self.fail('finish the test')



# 登录失败

# 登录成功，跳转到用户中心界面

if __name__ == '__main__':
    unittest.main(warnings='ignore')
