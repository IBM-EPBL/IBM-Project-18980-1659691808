from flask import Flask,redirect
app=Flask(__name__)
@app.route('/')
def home():
    return "welcome to flask"
@app.route('/courses')
def courses():
    return "courses"
@app.route('/admin')
def admin():
    return redirect('/')
@app.route('/Department')
def Department():
    return "Department"
if __name__=='__main__':
    app.run(debug=True)