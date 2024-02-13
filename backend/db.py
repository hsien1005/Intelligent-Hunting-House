import json
from flask_cors import CORS
import pymongo
from bson import json_util
from model import Room, MyFavorite, MyHistory,MyFilter
import logging
def connectMongo():
     #  MongoDB atlas
    myclient = pymongo.MongoClient('mongodb://127.0.0.1:27017') 
    mydb = myclient['IOT_DB']  
    mycol = mydb['room']  
    myfavorite = mydb['favorite']
    myhistory = mydb['history']
    myfilter = mydb['filter']
    return {'mycol': mycol, 'myfavorite': myfavorite, 'myhistory': myhistory, 'myfilter': myfilter}

def getMongo():
    mycol = connectMongo()['mycol']

    # myquery = {"id": '64698523ea65f4f95d15d10a'}   
    mydoc = mycol.find({})    
    
    dataList = []
    for x in mydoc:
        
        x = json.loads(json_util.dumps(x))
        # logging.warn(x)
        dataList.append(x)
        # print(x)
        # return x
    return dataList
# class Room:
#     def __init__(self,name, type , roomType ,money, address,zone, img_list, area):
#         self.name = name
#         self.type = type
#         self.roomType = roomType
#         self.money = money  
#         self.address = address  
#         self.zone = zone
#         self.img_list = img_list  
#         self.area = area 
#     def to_dict(self):
#             return {
#                 "name":self.name,
#                 "type":self.type,
#                 "roomType":self.roomType,
#                 "money": self.money,
#                 "address": self.address,
#                 "zone":self.zone,
#                 "img_list": self.img_list,
#                 "area": self.area
#             }
def InsertMongo(name,type,roomType,money,address,zone,img_list,area):
    mycol = connectMongo()['mycol']
    room = Room(name=name,type=type,roomType=roomType,money=money, address=address,zone=zone, img_list=img_list, area=area)
    room_dict = room.to_dict() 
    post_id = mycol.insert_one(room_dict).inserted_id
    if(post_id != None):
        return "successful"
    else:
        return "error"
    # print (post_id) # if ObjectId('...') then successful!

def InsertFilter(moneyMax,moneyMin,address):
    mycol = connectMongo()['myfilter']
    filter = MyFilter(moneyMax=moneyMax,moneyMin=moneyMin,address=address)
    filter_dict = filter.to_dict() 
    post_id = mycol.insert_one(filter_dict).inserted_id
    if(post_id != None):
        return "successful"
    else:
        return "error"

def InsertHistory(person,room):
    mycol = connectMongo()['myhistory']
    history = MyHistory(person=person,room=room)
    history_dict = history.to_dict() 
    post_id = mycol.insert_one(history).inserted_id
    if(post_id != None):
        return "successful"
    else:
        return "error"
    
def InsertFavorite(person,room):
    mycol = connectMongo()['myfavorite']
    favorite = MyFavorite(person=person,room=room)
    favorite_dict = favorite.to_dict() 
    post_id = mycol.insert_one(favorite).inserted_id
    if(post_id != None):
        return "successful"
    else:
        return "error"

def deleteAllDocuments():
    mycol = connectMongo()['mycol']
    logging.warn("delete call")
    result = mycol.delete_many({})
    
    if result.deleted_count > 0:
        return "successful "
    else:
        return "error"
    
