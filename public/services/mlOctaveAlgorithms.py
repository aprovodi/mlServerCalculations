#! /usr/bin/env python
 
import logging
import pytave
import os
import sys

#sys.path.append(os.getcwd() + "/kMeans")
 
class Service:
    def callMethod(self, msg):
        curPath = sys.path[0]
	logFilePath = curPath + "/contactjson.txt"
        logging.basicConfig(filename=logFilePath, level=logging.DEBUG)
        logging.debug("OLDLoading contact service")
        outputPictureName = "picturem.png"
        pytave.feval(0, "addpath", curPath)
        pytave.feval(0, "addpath", curPath + "/kMeans")
        pytave.feval(0, "addpath", curPath + "/pytave")
        outputPicture = curPath + "/kMeansPictures/" + outputPictureName
        pytave.feval(0, "exec", curPath + "/kMeansPictures/" + msg, outputPicture)

###TODO: implement compression algorithm here in order to put logging information during running
#	A = pytave.feval(1, "imread", '/home/aprovodi/simpleserver/VLayouts/output/services/bird_small.png')

#	B = A[0] / 255.0 # Divide by 255 so that all values are in the range 0 - 1
#	os.mkdir("/home/aprovodi/simpleserver/VLayouts/temp/zhopa")
#	pytave.feval(1, "imwrite", B, "/home/aprovodi/simpleserver/VLayouts/temp/picture.jpg")
#	result = curPath + "/kMeansPictures/" + msg
        return outputPictureName
 
 
if __name__ == '__main__':
    # this is if JSONService.py is run as a CGI
    from jsonrpc.cgihandler import handleCGIRequest
    handleCGIRequest(Service())
else:
    # this is if JSONService.py is run from mod_python:
    # rename .htaccess.mod_python to .htaccess to activate,
    # and restart Apache2
    from jsonrpc.apacheServiceHandler import handler
