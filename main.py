from flask import Flask, render_template, redirect, request
import psycopg2

app = Flask(__name__)


def add():
    if request.method == 'post':
        u_id = request.form.get('u_id')
        surname = request.form.get('surname')
        name = request.form.get('name')
        otc = request.form.get('otc')
        phone = request.form.get('phone')
    connection = psycopg2.connect(dbname="PZ",
                                  user="postgres",
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432")
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO main VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')""".format(u_id, surname,
                                                                                            name, otc, phone))
    connection.commit()
    connection.close()


@app.route('/', methods=['post', 'get'])
def base():
    connection = psycopg2.connect(dbname="PZ",
                                  user="postgres",
                                  password="123",
                                  host="127.0.0.1",
                                  port="5432")
    cursor = connection.cursor()
    cursor.execute("SELECT * from main;")
    list_users = cursor.fetchall()
    return render_template('index.html', list_users=list_users)


if __name__ == '__main__':
    app.run(debug=True)