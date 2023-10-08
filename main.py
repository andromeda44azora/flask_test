from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def sakums():
    return render_template('index.html')

@app.route('/sveiki', methods=["POST","GET"])
def sveiki():
    if request.method == "POST":
        vardins = request.form['vards']
        uzvardins = request.form['uzvards']
        return render_template('sveiki.html', vards = vardins, uzvards = uzvardins)
    return render_template('sveiki.html', vards = "", uzvards = "")

if __name__ == '__main__':
    app.run(threaded=True, port = 5000)