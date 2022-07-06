import pytest
from config import setting
if __name__=="__main__":
    html_path=setting.TestResult_DIR
    print(html_path)
    testcase_path=setting.TestCode_DIR+"/testapi_pytest.py"
    pytest.main(["-v","-s",f'--html=={html_path}/report.html',testcase_path])

