from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def ind():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promo():
    countdown_list = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    return '</br>'.join(countdown_list)


@app.route('/bootstrap_sample')
def bootstrap():
    return f'''<!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        <link rel="stylesheet" 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
        crossorigin="anonymous">
        <title>Привет, Яндекс!</title>
      </head>
      <body>
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-6">
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                         alt="здесь должна была быть картинка, но не нашлась"> 
                    <div class="alert alert-secondary" role="alert">
                        Человечество вырастает из детства.<br>
                    </div>
                    <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.<br>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.<br>
                    </div>
                    <div class="alert alert-warning" role="alert">
                        И начнем с Марса!<br>
                    </div>
                    <div class="alert alert-danger" role="alert">
                        Присоединяйся!
                    </div>
                </div>
            </div>
        </div>
      </body>
    </html>'''


if __name__ == '__main__':
    app.run(port=8082, host='127.0.0.1')
