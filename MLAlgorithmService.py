from pyjamas import DOM, Window
from pyjamas.JSONService import JSONProxy
import pyjamas.gmaps.Utils
import kMeans
import time

class MLAlgorithmJSONProxy(JSONProxy):
    def __init__(self):
        ## services/mloctavealgorithms.py counts from output folder
        JSONProxy.__init__(self, "services/mlOctaveAlgorithms.py", ["callMethod","test"])
 
class MLAlgorithmService:
    def __init__(self, callback):
        self.callback = callback
        self.proxy = MLAlgorithmJSONProxy()
 
    def test(self):
        self.proxy.test(self)
 
    def callMethod(self,cmd):
        a = self.proxy.callMethod(cmd, self)
 
    def onRemoteResponse(self, response, request_info):        
#        Window.alert(dir(request_info))
#        Window.alert(request_info.method)
#        Window.alert(request_info.handler)
#        time.sleep( 3 )
        Window.alert("inside MLAlgorithmService: compression is done")
        self.callback.loadImage(response)

#        if request_info.method == "callMethod":
#            self.callback.showStatus(""" Called method %s and response %s """ % (request_info.method,response))
#        else:
#            self.callback.showStatus(""" REQ METHOD = %s RESP %s """ % (request_info.method,response)) 
 
    def onRemoteError(self, code, errobj, request_info):
        Window.alert("inside MLAlgorithmService: onRemoteError")
        Window.alert(request_info)
        message = errobj['message']
        Window.alert(message)
        if code != 0:
            self.callback.showStatus("HTTP error %d: %s" % (code, message))
        else:
            json_code = errobj['code']
            self.callback.showStatus("JSONRPC Error %s: %s" % (json_code, message))
