from flask import Flask,render_template,request
from score import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    student_name = request.form['student_name'] # 接收表单中的姓名
    student_num  = request.form['student_num']  # 接收表单中的考生号
    html_str = get_score(xm=student_name,ksh=student_num)
    data = parse_page_detail(html_str)
    return render_template('result.html', score=data[3::2])

if __name__ == '__main__':
    app.run(debug=True)
