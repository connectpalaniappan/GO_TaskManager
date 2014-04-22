import os

import json

def runAddCurl(data,path):
    a = os.system('curl --silent -H "Content-Type: application/json" --data @'+ data+' http://localhost:8080/task/add > '+path)
    return

def runListAllCurl(path):
    a = os.system('curl --silent -H "Content-Type: application/json" http://localhost:8080/task/list > '+path)
    return
	
def runListIdCurl(id,path):
    a = os.system('curl --silent -H "Content-Type: application/json" http://localhost:8080/task/'+ id +' > '+path)
    return
	
def runUpdateCurl(data,id,path):
    a = os.system('curl --silent -H "Content-Type: application/json" --data @'+ data+' http://localhost:8080/task/'+id+'> '+path)
    return

def runDeleteCurl(data,id,path):
    a = os.system('curl --silent -H "Content-Type: application/json" --data @'+ data+' http://localhost:8080/task/delete/'+id+'> '+path)
    return
	
	
def compareJson(expectedPath, newPath):
    return json.load(open(expectedPath)) == json.load(open(newPath))

	
if __name__ == '__main__':
    newPath = "1.json"
    expectedPath = "expected_add.json"
    runAddCurl("data.json",newPath)
    if compareJson(newPath,expectedPath):
        print "Add 1 :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "Add 1 :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath	
    newPath = "2.json"
    expectedPath = "expected_listall.json"
    runListAllCurl(newPath)
    if compareJson(newPath,expectedPath):
        print "List All :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "List All :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath
    newPath = "3.json"
    expectedPath = "expected_list1.json"
    runListIdCurl("1",newPath)
    if compareJson(newPath,expectedPath):
        print "List 1 :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "List 1 :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath
    newPath = "4.json"
    expectedPath = "expected_add1.json"
    runAddCurl("data1.json",newPath)
    if compareJson(newPath,expectedPath):
        print "Add 2 :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "Add 2 :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath
    newPath = "5.json"
    expectedPath = "expected_add2.json"
    runAddCurl("data2.json",newPath)
    if compareJson(newPath,expectedPath):
        print "Add 3 :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "Add 3 :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath
    newPath = "6.json"
    expectedPath = "expected_add3.json"
    runAddCurl("data3.json",newPath)
    if compareJson(newPath,expectedPath):
        print "Add 4 :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "Add 4 :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath
    newPath = "7.json"
    expectedPath = "expected_add4.json"
    runAddCurl("data4.json",newPath)
    if compareJson(newPath,expectedPath):
        print "Add 5 :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "Add 5 :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath
    newPath = "8.json"
    expectedPath = "expected_update1.json"
    runUpdateCurl("data4.json","1",newPath)
    if compareJson(newPath,expectedPath):
        print "Update 1 :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "Update 1 :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath
    newPath = "9.json"
    expectedPath = "expected_list11.json"
    runListIdCurl("1",newPath)
    if compareJson(newPath,expectedPath):
        print "List 1 :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "List 1 :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath
    newPath = "10.json"
    expectedPath = "expected_update2.json"
    runUpdateCurl("data4.json","2",newPath)
    if compareJson(newPath,expectedPath):
        print "Update 2 :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "Update 2 :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath
    newPath = "11.json"
    expectedPath = "expected_list12.json"
    runListIdCurl("2",newPath)
    if compareJson(newPath,expectedPath):
        print "List 2 :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "List 2 :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath
    newPath = "12.json"
    expectedPath = "expected_listall1.json"
    runListAllCurl(newPath)
    if compareJson(newPath,expectedPath):
        print "List All :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "List All :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath
    newPath = "13.json"
    expectedPath = "expected_delete1.json"
    runDeleteCurl("data4.json","1",newPath)
    print "Delete 1"
    newPath = "13.json"
    expectedPath = "expected_list13.json"
    runListIdCurl("1",newPath)
    if compareJson(newPath,expectedPath):
        print "List 1 :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "List 1 :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath
    newPath = "14.json"
    expectedPath = "expected_listall2.json"
    runListAllCurl(newPath)
    if compareJson(newPath,expectedPath):
        print "List All :: Test Case Passed :: Actual="+newPath+" :: Expected="+expectedPath
    else : 
        print "List All :: Test Case Failed :: Actual="+newPath+" :: Expected="+expectedPath