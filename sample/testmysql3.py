#python 3.6    
#蔡军生     
#http://blog.csdn.net/caimouse/article/details/51749579    
#
import web

urls = (
    '/', 'index',
    '/add', 'add'
)


app = web.application(urls, globals())
render = web.template.render('templates/')
db = web.database(dbn='mysql', host='127.0.0.1', port=3308,
                  db='forum', user='root', pw='12345678',
                  driver = 'mysql.connector')

class index:
    def GET(self):
       email = db.select('mintest')
       return render.index1(email)        
    
class add:
    def POST(self):
        i = web.input()
        n = db.insert('mintest', email=i.title, NAME='name-' + i.title)
        raise web.seeother('/')
    
if __name__ == "__main__":
    app.run()
