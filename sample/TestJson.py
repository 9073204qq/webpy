#python 3.6    
#蔡军生     
#http://blog.csdn.net/caimouse/article/details/51749579    
#
import web
import json

urls = (
    '/', 'index'
)

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))
app = MyApplication(urls, globals())


class index:
    def GET(self):
        pyDict = {'one':1,'two':2}
        web.header('Content-Type', 'application/json')
        return json.dumps(pyDict)

    
if __name__ == "__main__":
    app.run(port=8888)
