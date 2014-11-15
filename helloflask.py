from flask import Flask, request
app = Flask(__name__)
app.debug = True   # need this for autoreload as and stack trace


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

@app.route('/hello')
def hello_form():
    if 'firstname' in request.args:
        return sendPage(request.args['firstname'])
    else:
        return sendForm()

def sendForm():
    return '''
    <html>
      <body>
          <form method='get'>
              <label for="myname">Enter Your Name</label>
              <input id="myname" type="text" name="firstname" value="Nada" />
              <input type="submit">
          </form>
      </body>
    </html>
    '''

def sendPage(name):
    return '''
    <html>
      <body>
        <h1>Hello {0}</h1>
      </body>
    </html>
    '''.format(name)

if __name__ == '__main__':
   app.run()
