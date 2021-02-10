from flask import Flask, request
import pymysql

app = Flask(__name__)

@app.route("/")
def hello():
    html = '''
    <h1>Login</h1>
    <form method="post" action="/login">
        <p>ID: <input type="text" name="id"></p>
        <p>PW: <input type="text" name="pw"></p>
        <p><input type="submit" value="Submit"></p>
    </form>
    '''
    return html
    
@app.route("/login", methods=['GET', 'POST'])
# get을 쓰면 주소에 input 내용이 보이고, post를 쓰면 안보임!

def login():
    '''
    # get : .args. / post : .form. 이 부분 차이점
    id = request.args.get('id')
    pw = request.args.get('pw')
    print('id is', id)
    print('pw is', pw)
    '''
    
    # post
    id = request.form.get('id')
    pw = request.form.get('pw')
    db = pymysql.connect(
                    host='127.0.0.1',
                    port=3306,
                    user='web',
                    passwd='webpw',
                    db='sue',
                    charset='utf8'
                    )
    cursor = db.cursor()
    sql = "SELECT pw FROM user WHERE id='" + id + "'"
    # sql 구문을 str으로 넣어준다.
    # 중간의 id는 python의 request.form.get('id')의 str 값
    print(sql)
    cursor.execute(sql)
    # sql 구문을 실행한다-는 뜻
    dbpw = cursor.fetchone()[0]
    # db에서 가져온 것 중 첫번째 값 / 슬라이싱 안해주면 리스트 형태로 나옴.
    if pw == dbpw: return 'good login'
    else: return 'no pw'
   
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=80, debug=True)