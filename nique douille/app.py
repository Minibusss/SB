from flask import Flask, g, render_template, jsonify
import sqlite3

app = Flask(__name__, 
            template_folder='D:\\Travail\\Projets\\Shrodingerbox\\Test',
            static_folder='D:\\Travail\\Projets\\Shrodingerbox\\Test')

DATABASE = r'D:\Travail\Projets\Shrodingerbox\Test\vrai_base.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data')
def get_data():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM emil")  
    data = cursor.fetchall()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

