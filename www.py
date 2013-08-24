from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
import darm
import os

STATIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
TEMPLT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask('darm', static_folder=STATIC, template_folder=TEMPLT)
Bootstrap(app)

app.config['BOOTSTRAP_USE_MINIFIED'] = True
app.config['BOOTSTRAP_USE_CDN'] = True
app.config['BOOTSTRAP_FONTAWESOME'] = True


def disasm(fn, instr):
    try:
        return str(fn(int(instr, 16)))
    except:
        return 'Invalid Instruction Encoding', 400


@app.route('/armv7/<instr>')
def armv7(instr):
    return disasm(darm.disasm_armv7, instr)


@app.route('/thumb/<instr>')
def thumb(instr):
    return disasm(darm.disasm_thumb, instr)


@app.route('/thumb2/<instr>')
def thumb2(instr):
    return disasm(darm.disasm_thumb2, instr)


@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
