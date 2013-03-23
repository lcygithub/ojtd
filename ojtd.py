#!/usr/bin/env python
import os
import sys
import json

testdata = []
for dir in os.listdir("testdata"):
    dic = {"pid": int(dir), "special": 0, "data": []}
    testdata.append(dic)
    for file_count in range(len(os.listdir("testdata/"+dir))/2):
        tout = open("testdata/"+dir+"/"+str(file_count)+".out","r")
        tin = open("testdata/"+dir+"/"+str(file_count)+".in","r")
        dic["data"].append({"out": tout.read(),"in":tin.read()})
        tout.close()
        tin.close()
testdata = json.dumps(testdata)
ctestdata = open("tdjson", "w")
ctestdata.write(testdata)
ctestdata.close()
    