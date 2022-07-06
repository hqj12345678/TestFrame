#index,title,playsource,category,result,TestData,tester
from config import setting
import configparser,openpyxl,requests
class TestCaseData():
    def __init__(self):
        #self.filepath= settings.TestCasePath
        self.filepath=setting.TestCase_Path
        conn=configparser.ConfigParser()
        conn.read(setting.Config_Path, encoding="utf-8")
        self.url=conn.get("RequestData","url")
        self.book=openpyxl.Workbook()
    def GetAllTestCase(self):
        sheet = self.book.create_sheet(title="少儿模式", index=0)
        sheet.cell(row=1, column=1, value="index")
        sheet.column_dimensions["A"].width = 14
        sheet.cell(row=1, column=2, value="title")
        sheet.column_dimensions["B"].width = 60
        sheet.cell(row=1, column=3, value="playsource")
        sheet.column_dimensions["C"].width = 14
        sheet.cell(row=1, column=4, value="category")
        sheet.column_dimensions["D"].width = 14
        sheet.cell(row=1, column=5, value="result")
        sheet.column_dimensions["E"].width = 24
        sheet.cell(row=1, column=6, value="TestData")
        sheet.column_dimensions["F"].width =60
        sheet.cell(row=1, column=7, value="tester")
        sheet.column_dimensions["G"].width = 24
        n=2
        print(self.url)
        try:
            headers={
                "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
            }
            resp = requests.get(url=self.url,headers=headers)
            if resp.status_code==200:
                resp_json=resp.json()
                #print(resp_json)
                if len(resp_json)!=0:
                    contents=resp_json["content"]
                    #print(contents)
                    if len(contents)!=0:
                        for content in contents:
                            #print(content)
                            items=content["items"]
                            if len(items)!=0:
                                for item in items:
                                    #print(item)
                                    title=item["title"]
                                    playSource=item["playSource"]
                                    category=item["category"]
                                    print("category:"+category+",title:"+title)
                                    sheet.cell(row=n,column=1,value="index_"+str(n-1))
                                    sheet.cell(row=n,column=2,value=title)
                                    sheet.cell(row=n,column=3,value=playSource)
                                    sheet.cell(row=n,column=4,value=category)
                                    n+=1
                            else:
                                print("items为空")
                    else:
                        print("contents为空")
                else:
                    print("resp_json为空")
            else:
                print("request fail,code:"+str(requests.status_codes))
        except Exception as e:
            print("request error,error:"+str(e))
        self.book.save(self.filepath)
        print("保存成功")

TestCaseData().GetAllTestCase()
