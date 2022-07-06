#index,title,playsource,category,result,TestResult,tester
import pytest
from data import FileUtil
from database import mongodata
mFileUtil=FileUtil.FileUtil()
datas=mFileUtil.ReadData("少儿模式")
class TestApi():
    def setup_class(self):
        print("start")
        self.mongodata=mongodata.SearchMongo()
    @pytest.mark.parametrize("data",datas)
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
                assert(1==0)
            else:
                result = "PASS"
                testdata = "库中存在该节目"
                tester = "huangqiaojun"
                writes["result"] = result
                writes["testdata"] = testdata
                writes["tester"] = tester
                mFileUtil.WriteData(row, writes)
                assert(res==True)
        else:
            result = "FAIL"
            testdata = "该节目不是少儿节目"
            tester = "huangqiaojun"
            writes["result"] = result
            writes["testdata"] = testdata
            writes["tester"] = tester
            mFileUtil.WriteData(row, writes)
            assert(category=="少儿")
    def teardown_class(self) -> None:
        mFileUtil.SaveBook()
        print("end")
