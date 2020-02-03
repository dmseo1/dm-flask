from flask import Flask, render_template, request  # Flask라는 클래스를 불러올 것
                                          # render_template: 보여지게 하는 데 필요한 것들을 모아놓음
from data import Articles
from flask_mysqldb import MySQL
import pymysql


app = Flask(__name__) # 5000번 포트에 앱 실행
# app.debug = True ;  app.run() 메소드 안에 debug=True 옵션을 주는 것과 동일하다


# mysql 을 위한 setting
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_PASSWORD'] = '1234'
# app.config['MYSQL_DB'] = 'myflaskapp'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# msms = MySQL(app)

# mysql 을 위한 setting 2
db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='myflaskapp', charset='utf8')
cursor = db.cursor()

data1 = cursor.execute("INSERT INTO users(name, email, username, password) VALUES('seo', 'dmseo@llit.kr', '동민', '1234')")
print(data1)



garaData = Articles()
print(garaData[0]['title'])

@app.route('/') # decorate(장식자). 바로 밑에 함수를 붙여주면 그것이 실행된다.
def hello() :
    data1 = cursor.execute("INSERT INTO users(name, email, username, password) VALUES('seo', 'dmseo@llit.kr', '동민', '1234')")
    print(data1)
    # cur = msms.connection.cursor()
    # cur.execute("INSERT INTO users(name, email, username, password, register_date) VALUES ('a','b','c','d',NOW())");
    # msms.connection.commit()
    # cur.close()

    return render_template('home.html')
    

@app.route('/user/<name>')
def user(name) :
    return render_template('user.html', data=name)

@app.route('/about')
def about() :
    return render_template('about.html')

@app.route('/articles')
def articles() :
    return render_template('articles.html', articles=garaData)

@app.route('/articles/<string:id>')
def read_article(id) :
    return render_template('read_article.html', id=int(id), article=garaData)


if __name__  == "__main__": #이 파일이 직접적으로 호출되었을 때에만 실행하도록 한다. (이 py 파일이 import 되어 사용될 경우 호출되지 않는다)
    app.run(debug=True)
    #debug=True : 디버그 모드 실행. 파일 전체를 재실행하는 듯 (근거: A가 두 번 출력). 개발할 때는 debug 모드를 on(True)으로 두자
