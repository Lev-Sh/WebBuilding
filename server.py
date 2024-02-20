from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return  render_template('base.html', title=title)
@app.route('/list_prof/<type_list>')
def list_prof(type_list):
    result = []
    with open('profesions.txt', 'w' ,encoding='utf-8') as f:
        result = list(map(lambda x: x.rstrip(), f.read().split('*')))
    params = {
        'proffessions': result,
        'title': 'Список проффесий',
        'type_list': type_list
    }
    return render_template('list_prof.html', **params)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
