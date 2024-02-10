from flask import Flask

app = Flask(__name__)

text = 'Человечество вырастает из детства.Человечеству мала одна планета.Мы сделаем обитаемыми безжизненные пока планеты.И начнем с Марса!Присоединяйся!'


@app.route('/promotion')
def promotion():
    return '!<br><br>'.join('.<br><br>'.join(text.split('.')).split('!'))



@app.route('/image_mars')
def image_mars():
    return '<h1>Жди нас, Марс!</h1></br><img scr="images/mars_vremya.png" alt="mars_image lol"></br><p>Вот она какая, красная планета.</p>'


@app.route('/promotion_image')
def image_marss():
    with open('hmain.html', 'r', encoding='utf-8') as file:
        data = file.read().replace('\n', '')
    return data


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
