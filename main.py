from flask import Flask, render_template
from datetime import datetime  #дата и время сейчас
import requests
import jinja2


app = Flask(__name__) # Объект flask с аргументом _name_


@app.route('/') #декоратор - страница сайта - home page\first page - http://localhost:5000/
def index():
    return render_template('index.html',name = "MAxon",project_name= 100)    #render_template отвечает за подключение HTML страницы

@app.route('/about')  # еще одна страница сайта с адресом  http://localhost:5000/___все что после слеша
def second_page(): 
    return 'Информация о нас'  # можно подключить по примерц выше свою страницу html

@app.route('/albums/<int:album_number>/<song_number>')# пример динамического адреса, <converter:variable_name> с изменением типа данных
def songs(album_number,song_number):
    return "The{} album, and {} musician performer.".format(album_number,song_number)

@app.route('/jinja')
def jinjas():
    return render_template(
        "jinja.html",
        m = 300)     

@app.route("/eye.svg")   
def icon():
    
    return "Здесь должно быть фото eye.png" 

if __name__ == "__main__":  #
    # Launch the Flask dev server
    app.run(host="localhost", debug=True) # параметры запуска\ .run - запускает сервер   http://localhost:5000/  debug=False or True отвечает за видимость ошибок на странице html users