from vendor import web
from vendor.web.contrib.template import render_jinja

urls = (
    '/', 'welcome',
    '/_add', 'add',
    '/_erase', 'erase',
    '/secret/(.+)','secret',
    '/author/(.+)', 'author',
    )

app = web.application(urls, globals())
render = render_jinja('templates')

from mongokit import MongoDocument
import datetime

class Secret(MongoDocument):
    db_name = 'keepmysecret'
    collection_name = 'secrets'
    structure = {
        'title' : unicode,
        'body' : unicode,
        'author' : unicode,
        'slug' : unicode,
        'date_created' : datetime.datetime
        }
        
    required_fields = ['title', 'author', 'body', 'slug']

class welcome:
    def GET(self):
        secrets = Secret().all()
        return render.index( messages = secrets )

class secret:
    def GET(self, slug):
        secret = Secret().one({ 'slug' : slug })
        return secret
    
    def create(self):
        pass

class author:
    def GET(self, author):
        secrets = Secret().all({ 'author' : author })
        return secrets

class add:
    def GET(self):
        secret = Secret( {
          'title':u'Hello, Dolly', 
          'body':u'Hello darling!', 
          'author':u'yaanno', 
          'slug':u'hello-dolly',
          'date_created':datetime.datetime.now(),
          } )
        secret.save()

class erase:
    def GET(self):
        secrets = Secret().all()
        for secret in secrets:
            secret.delete()

if __name__ == '__main__': app.run()
