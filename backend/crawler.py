#有可能載下來的是JSON格式的資料，還要做測試
#JSON {}:字典 []:列表
import urllib.request as req
import json
import math
from db import InsertMongo
from db import deleteAllDocuments
def crawler_591():
    deleteAllDocuments()
    data_list = []
    ## find all data ##############################
    url = "https://rent.591.com.tw/home/search/rsList?is_format_data=1&is_new_list=1&type=1&region=2&totalRows=743&recom_community=1&firstRow=0"
    request = req.Request(url, headers={
        "User-Agent": "",
        "X-Csrf-Token": "",
        "Cookie": ""
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    data = json.loads(data)
    all_data = data["records"]
    pages = math.floor(int(all_data)/30)
    # print(pages)
    ###############################################

    for page in range(0,2):
        url = "https://rent.591.com.tw/home/search/rsList?is_format_data=1&is_new_list=1&type=1&region=2&totalRows=743&recom_community=1&firstRow="+str(page*30)
        request = req.Request(url, headers={
            "User-Agent": "",
            "X-Csrf-Token": "",
            "Cookie": ""
        })
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")

        data = json.loads(data)
        # print(data)
        posts = data["data"]["data"]
        print(len(posts))
        # print(posts[0])
        # page = 0
        for key in range(0,len(posts)):
            individual_data = []
            post = posts[key]
            # print(str(num)+'：' + post["title"] + post["price"])
            individual_data.append(post["title"])
            individual_data.append(post["kind_name"])
            if "room_str" in post and post["room_str"] != "":
                individual_data.append(post["room_str"])
            else:
                individual_data.append('')
            
            
            individual_data.append(post["price"])
            # print(post["photo_list"])
            #照片資料為list 有可能為空list(need to check)
            data = post["photo_list"]
            if data:
                # 取得第一筆資料
                individual_data.append(data)
            else:
                print("列表為空")
                individual_data.append('')
            # print(len(data))
            individual_data.append(post["section_name"])
            individual_data.append(post["location"])
            individual_data.append(post["area"])

            data_list.append(individual_data)
            InsertMongo(individual_data[0],individual_data[1],individual_data[2],individual_data[3],individual_data[6],individual_data[5],individual_data[4],individual_data[7])
    return data_list

def crawler_5168():
    data_list = []

    ## find all data ##############################
    url = "https://rent.houseprice.tw/ws/list/%E5%9F%BA%E9%9A%86%E5%B8%82_city/"
    request = req.Request(url, headers={
        "User-Agent": "",
        "Cookie": ""
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        
    data = json.loads(data)
    pages = data["pa"]["totalPageCount"]
    ###############################################
    for page in range(1,3):
        url = "https://rent.houseprice.tw/ws/list/%E5%9F%BA%E9%9A%86%E5%B8%82_city/?p="+str(page)
        request = req.Request(url, headers={
            "User-Agent": "",
            "Cookie": ""
        })
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")

        data = json.loads(data)
        # print(data)
        posts = data["webRentCaseGroupingList"]
        # print(len(posts))
        # print(posts[0])
        # page = 0
        for key in range(0,len(posts)):
            individual_data = []
            data = []
            post = posts[key]
            # print(str(num)+'：' + post["title"] + post["price"])
            individual_data.append(post["caseName"]) #房型
            individual_data.append(post["rentPurPoseName"]) #住家類型
            #rooms information 
            roominfo = ""
            rm = post["rm"]
            if rm:
                roominfo+=(str(int(rm))+"房")
            livingRm = post["livingRm"]
            if livingRm:
                roominfo+=(str(int(livingRm))+"廳")
            bathRm = post["bathRm"]
            if bathRm:
                roominfo+=(str(int(bathRm))+"衛")
            individual_data.append(roominfo) # 詳細房型
            individual_data.append(str(int(post["caseFromList"][0]["totalPrice"]))) #價錢
    #         # print(post["photo_list"])
    #         #照片資料為list 有可能為空list(need to check)
            img_data = []
            data = post["imageFileList"] 
            if data:
                # 取得第一筆資料
                image = data[0]["casePicUrl"]
                # print(image)
                if image[-3:] != "jpg":
                    if image[-4:] == "jpeg":
                        image = image[:-4]
                        image += "jpg"
                    elif image[-3:] == "png":
                        continue
                    else:
                        image += ".jpg"
                img_data.append(image) #圖片列表
                individual_data.append(img_data)
            else:
                print("列表為空")
                individual_data.append('')
            individual_data.append(post["district"]) #區域
            individual_data.append(post["simpAddress"]) #住址
            individual_data.append(str(post["buildPin"])) #坪數
            print(individual_data)
            InsertMongo(individual_data[0],individual_data[1],individual_data[2],individual_data[3],individual_data[6],individual_data[5],individual_data[4],individual_data[7])
            data_list.append(individual_data)
    return data_list

crawler_591()
crawler_5168()

