#python 3.6  
#蔡军生   
#http://blog.csdn.net/caimouse/article/details/51749579  
#  
import web

urls = (
    '/(.*)', 'index'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
    def GET(self, name):
        i = web.input(name=None)
        return render.index(i.name)
    

if __name__ == "__main__":
    app.run()
