import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'senha123'
app.config['MYSQL_DATABASE_DB'] = 'ac'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('grava.html')

@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    email = request.form['email']
    endereco = request.form['endereco']

    if nome and email and endereco:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('insert into alunos (user_name, user_email, user_address) VALUES (%s, %s, %s)',(nome, email, endereco))
        conn.commit()

        return render_template('grava.html')

@app.route('/listar',methods=['POST', 'GET'])
def listar():

        conn = mysql.connect()
        cursor = conn.cursor()
        data = cursor.execute ('select user_name, user_email, user_address from alunos')
        data = cursor.fetchall()
        conn.commit()
        return render_template('lista.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)