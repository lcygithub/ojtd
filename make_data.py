#!/usr/bin/env python
import sys
import os
dirname = "testdata/"
for i in range(5):
    for j in range(1,5):
        if(not os.path.exists("testdata/"+str(j))):
            os.mkdir("testdata/"+str(j))
        else:
            pass
        fp = open("testdata/" + str(j) + "/" + str(i) + ".in", "w+")
        fp.write("1 2")
        fp.close()
        fp = open("testdata/" + str(j) + "/" + str(i) + ".out", "w+")
        fp.write("3\n")
        fp.close()
