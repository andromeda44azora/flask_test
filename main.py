from Flask import Flask, render_template

app = Flask('app')

@app.route('/')
def sakums():
    return "jsjsadjksdfjds"

if __name__ == '__main__':
    app.run(threaded=True, port = 5000)