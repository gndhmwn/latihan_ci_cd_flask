from flask import Flask


app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Hello World'

@app.route('/nama')
def nama():
    return 'Ganda Himawan'

#@app.route('/alamat')
#def alamat():
#    return 'Medan Marelan'

if __name__ == '__main__':
    app.run()
