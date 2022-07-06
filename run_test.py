import unittest
from config import setting
from  package import HTMLTestRunner
from data import new_report,SendEmail
import time
from testcode.testapi import MyTestCase
#testcase=unittest.defaultTestLoader.discover(setting.TestCode_DIR,pattern="test*.py")
testcase=unittest.defaultTestLoader.loadTestsFromTestCase(MyTestCase)
testsuit=unittest.TestSuite()
testsuit.addTest(testcase)
filedir = setting.TestResult_DIR
filename = time.strftime("%Y%m%d_%H:%M:%S") + "_result.html"
filepath = filedir + "/" + filename
fp = open(filepath, "wb")
title = "少儿节目查询"
content="测试结果"
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="少儿节目查询",
                              description="环境：ubuntu  浏览器：chrome",
                                         tester="huangqiaojun")
runner.run(testsuit)
SendEmail.SendEmailUtil().sendemail(title,content)
fp.close()