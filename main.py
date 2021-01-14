
from flask import Flask, request
import testscript

app = Flask(__name__)

mainpage = """
<form method="POST" action="runscript1">
    <input name="parameters">
    <input type="submit" value="RunScript1">
</form>
<form method="POST" action="runscript2">
    <input name="parameters">
    <input type="submit" value="RunScript2">
</form>
"""

@app.route('/')
def index():
    return mainpage

@app.route('/runscript1', methods=['POST'])
def runscript1():
    testscript.opennotepad()
    text = request.form['parameters']
    parameters = text.upper()
    return 'You opened notepad on the "server", and %s were the parameters supplied' % parameters

@app.route('/runscript2', methods=['POST'])
def runscript2():
    testscript.openwow()
    text = request.form['parameters']
    parameters = text.upper()
    return 'You opened wow on the "server", and %s were the parameters supplied' % parameters

if __name__ == "__main__":
    app.run()