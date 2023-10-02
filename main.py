from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def sakums():
    return render_template('index.html')

@app.route('/sveiki')
def sveiki():
    visi_vardi = ['lapsene', 'Katrīne', 'pasaule']
    return render_template('sveiki.html', vards = visi_vardi)

if __name__ == '__main__':
    app.run(threaded=True, port = 5000)