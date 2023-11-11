from flask import Flask,request,redirect,url_for,render_template,abort


app = Flask(__name__)


# @app.before_request
# def check_locale():
#     path = request.path
#     if '.' not in path and path not in ('/','/en','/fr','/404'):
#         abort(404)
    

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/<lang>')
def home(lang):
    return render_template('home.html',lang=lang)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.post('/clicked')
def clicked():
    for e in dir(request):
        print(e)
    print()
    print(request.method)

    return '<h1>clicked</h1>'


if __name__=='__main__':
    app.run('localhost',3000,debug=True)