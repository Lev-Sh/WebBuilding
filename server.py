from flask import Flask

app = Flask(__name__)

text = 'Человечество вырастает из детства.Человечеству мала одна планета.Мы сделаем обитаемыми безжизненные пока планеты.И начнем с Марса!Присоединяйся!'


@app.route('/promotion')
def promotion():
    return '!<br><br>'.join('.<br><br>'.join(text.split('.')).split('!'))


@app.route('/promotion_image')
def promotion_image():
    with open('hmain.html', 'r', encoding='utf-8') as file:
        data = file.read().replace('\n', '')
    return data


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
