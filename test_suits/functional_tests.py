#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get("http://localhost:8000")
assert "Django" in browser.title

sleep(20)
browser.close()

