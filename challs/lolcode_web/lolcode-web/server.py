from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def process():
    request_data = request.get_json()
    lol_code= request_data['lol-code']
    lol_file = open("/tmp/h.lol", "w")
    lol_file.write(lol_code)
    lol_file.close()

    process = subprocess.Popen(['./lci', '/tmp/h.lol'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if (stdout == b''):
        return stderr
    else:
        return stdout

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
