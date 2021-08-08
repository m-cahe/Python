from logging import debug
from flask import Flask, jsonify, request, render_template
import re

app = Flask(__name__)

log_succ = {"login":"success"}
log_fail = {"login":"fail"}


def id_chk(data):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"      #유효성검사
    if bool(re.match(reg, data)):   
        if data == "m@naver.com":
            print("아이디일치")
            return True
        else:
            print("아이디가 일치하지 않습니다")
            return False
    else:
        print('id는 이메일 형식으로 입력해주세요') 
        return False


def pw_chk(data):
    if data == "m":
        return True
    else:
        print("비밀번호가 일치하지 않습니다")
        return False

@app.route("/login")
def login():
    id = request.args.get('id')
    pw = request.args.get('pw')
    print("id = ", id, "pw = ", pw)
    
    if (id_chk(id) == True) and (pw_chk(pw)==True):
        return jsonify(log_succ)
    else:
        return jsonify(log_fail)

@app.route("/")
def basic():    
    return render_template('login.html')


if __name__ == '__main__':
    app.run('127.0.0.1','8080', debug=True)

#데코레이터: 같은 상황에서 함수만 바꿔써야 할 때 사용