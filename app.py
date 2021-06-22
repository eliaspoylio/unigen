from flask import Flask,render_template,request
import blocks
import asyncio
 
app = Flask(__name__)
 
@app.route('/', methods = ['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        origUrl = request.form['url']
        origCols = request.form['cols']
        origScale = request.form['scale']
        error = None
 
        if not origUrl or not origUrl.strip():
            error = 'Url is missing'
        if not origCols or not origCols.strip():
            error = 'Number of columns is missing'
        if not origScale or not origScale.strip():
            error = 'Scale is missing'
        if error:
            return render_template('form.html', error = error)

        unicodeData = blocks.converToUnicode(origUrl, int(origCols), float(origScale))
        return render_template('form.html', orig = origUrl, unicodeData = unicodeData)
 
 
if __name__ == "__main__":
    app.run()