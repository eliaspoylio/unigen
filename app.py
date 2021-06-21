from flask import Flask,render_template,request
import blocks
import asyncio
 
app = Flask(__name__)
 
@app.route('/', methods = ['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        orig = request.form['Url']
        unicodeData = blocks.converToUnicode(orig)
        return render_template('form.html', orig = orig, unicodeData = unicodeData)
 
 
if __name__ == "__main__":
    app.run()