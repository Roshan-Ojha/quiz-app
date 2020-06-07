from flask import Flask,render_template,jsonify,request
from flask_mysqldb import MySQL
import random

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']="Roshan Ojha"
app.config['MYSQL_PASSWORD']="qwerty12345"
app.config['MYSQL_DB']='quiz'

mysql=MySQL(app)



@app.route('/')
def quiz():
    global da,answer_list,correct_list,question_list,c
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM QuestionAnswer")
    data=cur.fetchall()
    mysql.connection.commit()
    cur.close()
    da=random.sample(data,len(data))
    question_list=[]
    answer_list=[]
    correct_list=[]
    c=0
    # print(da)
    return render_template('quiz.html',da=da)


@app.route('/check',methods=['GET','POST'])
def check():
    global c,question_list,answer_list,correct_list
    question=eval(request.form.get('question_no'))
    answer=eval(request.form.get('answer'))
    question_list.append(da[question][0])
    answer_list.append(da[question][answer])
    correct_list.append(da[question][5])
    if da[question][answer]==da[question][5]:
        print("True")
        c=c+1
    else:
        print("Flase")
    # print(da[question][0])
    # print(da[question][answer])
    # print(da)

    return jsonify({'data':da})

@app.route('/result')
def result():
    print(c)
    print(question_list)
    return jsonify({'c':c,'attempts':question_list,'answered':answer_list,'correct':correct_list})

if __name__=='__main__':
    app.run(debug=True)