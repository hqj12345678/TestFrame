import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
#测试用例
TestCase_Path=os.path.join(BASE_DIR,"report","exportexcel","testcase.xlsx")
TestUiCase_Path=os.path.join(BASE_DIR,"report","exportexcel","testuicase.xlsx")
#测试程序
TestCode_DIR=os.path.join(BASE_DIR,"testcode")
#测试结果
TestResult_DIR=os.path.join(BASE_DIR,"report")
#配置
Config_Path=os.path.join(BASE_DIR,"data","config.ini")