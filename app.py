from vendor import web
from vendor.web.contrib.template import render_jinja

urls = (
    '/', 'welcome',
    '/add', 'add',
    '/erase', 'erase',
    '/_p/(.+)','post',
    '/_a/(.+)', 'author',
    )

app = web.application(urls, globals())
render = render_jinja('templates')

from mongokit import MongoDocument

class Post(MongoDocument):
    db_name = 'test'
    collection_name = 'tutorial'
    structure = {
        'title' : unicode,
        'body' : unicode,
        'author' : unicode,
        'slug' : unicode,
        }
    required_fields = ['title', 'author', 'body', 'slug']


class welcome:
    def GET(self):
        bp = Post().all()
        print bp
        return render.index( messages = bp )

class post:
    def GET(self, slug):
        p = Post().one({ 'slug' : slug })
        return p
    
    def create(self):
        pass

class author:
    def GET(self, author):
        a = Post().all({ 'author' : author })
        return a

class add:
    def GET(self):
        bp = Post( {'title':u'Hello, Dolly', 'body':u'Hello darling!', 'author':u'yaanno', 'slug':u'hello-dolly'} )
        '''
        bp['title'] = u'My post title'
        bp['body'] = u'My post body'
        bp['author'] = u'yaanno'
        '''
        bp.save()

class erase:
    def GET(self):
        posts = Post().all()
        for post in posts:
            post.delete()

if __name__ == '__main__': app.run()
