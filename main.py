from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('HTML/index.html')

@app.route('/school')
def school():
    return render_template('HTML/school.html')

@app.route('/cv')
def cv():
    return render_template('HTML/cv.html')

@app.route('/knowledge')
def knowledge():
    return render_template('HTML/knowledge.html')

if __name__ == '__main__':
    app.run(debug=True)
