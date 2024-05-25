from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']

        if (username == "arthur"):
            return render_template('main.html', username=username)
        else:
            return render_template('newuser.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)