from flask import Flask, render_template
import darm
import os

STATIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
TEMPLT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask('darm', static_folder=STATIC, template_folder=TEMPLT)


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


@app.route('/download')
def download():
    return render_template('download.html')


@app.route('/docs')
def docs():
    return render_template('docs.html')


@app.route('/contributors')
def contributors():
    return render_template('contributors.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
