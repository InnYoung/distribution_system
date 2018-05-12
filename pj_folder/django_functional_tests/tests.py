#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest
from django.test import LiveServerTestCase

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        sleep(3)
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_home_page(self):
        self.browser.get(self.live_server_url)

        # 验证首页title包含Tiger
        self.assertIn('tiger_distribution', self.browser.title)

        # 存在文本框
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # 输入“TigerTest1”，回车后页面更新，显示“1: TigerTest1”
        # 重定向到新url
        inputbox.send_keys('TigerTest1')
        sleep(2)
        inputbox.send_keys(Keys.ENTER)

        tiger1_list_url = self.browser.current_url
        self.assertRegex(tiger1_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: TigerTest1')

        # 页面又显示一个文本框
        # 输入“TigerTest2”，回车后页面更新，列表中添加“2: TigerTest1”
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('TigerTest2')
        sleep(2)
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: TigerTest1')
        self.check_for_row_in_list_table('2: TigerTest2')

        # 新用户tiger2访问页面
        self.browser.quit()
        self.browser = webdriver.Chrome()

        # 打开新页面,tiger1信息查看不到
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('TigerTest', page_text)
        
        # tiger2输入TigerTest3回车
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('TigerTest3')
        inputbox.send_keys(Keys.ENTER)
        sleep(2)

        # 列表更新，出现TigerTest3
        self.check_for_row_in_list_table('1: TigerTest3')

        # 获得tiger2唯一url
        tiger2_list_url = self.browser.current_url

        # 访问tiger1的url，显示已存item
        self.browser.quit()
        self.browser = webdriver.Chrome()
        self.browser.get(tiger1_list_url)
        self.check_for_row_in_list_table('1: TigerTest1')
        self.check_for_row_in_list_table('2: TigerTest2')

        # 访问tiger2的url
        self.browser.quit()
        self.browser = webdriver.Chrome()
        self.browser.get(tiger2_list_url)
        self.check_for_row_in_list_table('1: TigerTest3')


        self.fail('finish the test')
    

