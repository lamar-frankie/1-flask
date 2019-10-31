from programs import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello from Python'

@app.route('/frank')
def frank():
    return 'Hello Frank!'
