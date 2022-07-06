#index,title,playsource,category,result,TestResult,tester
import unittest,ddt
from data import FileUtil
from database import mongodata
mFileUtil=FileUtil.FileUtil()
datas=mFileUtil.ReadData("少儿模式")
@ddt.ddt
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("start")
        self.mongodata=mongodata.SearchMongo()
    @ddt.data(*datas)
    def test_data(self,data):
        writes={}
        search_dicts={}
        categorys={}
        index=int(data["index"].split("_")[1])
        print("第"+str(index)+"条用例")
        row=index+1
        title=data["title"]
        search_dicts["title"]=title
        playsource=data["playsource"]
        category=data["category"]
        if category=="少儿":
            #categorys[playsource]=category
            #search_dicts["categorys"]=categorys
            search_dicts["title"]=title
            res=self.mongodata.search(search_dicts)
            if res==False:
                result="FAIL"
                testdata="库中不存在该节目"
                tester="huangqiaojun"
                writes["result"] = result
                writes["testdata"] =testdata
                writes["tester"] =tester
                mFileUtil.WriteData(row,writes)
                self.assertEqual(1,0,"库中不存在该节目")
            else:
                result = "PASS"
                testdata = "库中存在该节目"
                tester = "huangqiaojun"
                writes["result"] = result
                writes["testdata"] = testdata
                writes["tester"] = tester
                mFileUtil.WriteData(row, writes)
        else:
            result = "FAIL"
            testdata = "该节目不是少儿节目"
            tester = "huangqiaojun"
            writes["result"] = result
            writes["testdata"] = testdata
            writes["tester"] = tester
            mFileUtil.WriteData(row, writes)
            self.assertEqual(category,"少儿", "该节目不是少儿节目")
    def tearDown(self) -> None:
        mFileUtil.SaveBook()
        print("end")
if __name__=="__main__":
    unittest.main