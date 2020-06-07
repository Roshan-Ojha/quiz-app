from flask import Flask,redirect,render_template,request,jsonify
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='Roshan Ojha'
app.config['MYSQL_PASSWORD']='qwerty12345'
app.config['MYSQL_DB']='quiz'

mysql=MySQL(app)

@app.route('/')
def add():
    return render_template('question.html')

@app.route('/store',methods=['GET','POST'])
def store():
    if request.method=='POST':
        question=request.form.get('question')
        opt_i=request.form.get('opt_i')
        opt_ii=request.form.get('opt_ii')
        opt_iii=request.form.get('opt_iii')
        opt_iv=request.form.get('opt_iv')
        answer=request.form.get('answer')

        cur=mysql.connection.cursor()
        cur.execute("""INSERT INTO QuestionAnswer(question,opt_i,opt_ii,opt_iii,opt_iv,correct) 
                        VALUES(%s,%s,%s,%s,%s,%s)""",

                        (question,
                        opt_i,
                        opt_ii,
                        opt_iii,
                        opt_iv,
                        answer)
                    )

        mysql.connection.commit()
        cur.close()
        print(opt_iii)
        print(question,opt_iv,answer)
        return jsonify("")

if __name__=='__main__':
    app.run(debug=True)