from bottle import route, run, template


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/')
def real_index():
    return "Hello Tareque"


run(host='localhost', port=8080)
