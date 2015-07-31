__author__ = 'jakerosenberg'
from flask import Flask
from flask import request
from flask import render_template



app = Flask(__name__)

@app.route('/')
def my_form():
    return """
        <!DOCTYPE html>
        <html lang="en">
        
        <body>
        <h1>UVPD Intensity Thing</h1>
        
        <form action="/input" method="POST">
        Protein Sequence: <br>
        <input type="text" name="seq" size = "200%"> <br>
        TIC Intensity: <br>
        <input type = "text" name = "intensity"><br>
        Paste Qual Browser Output: <br>
        <textarea name="qual_output" cols="40" rows="40"></textarea> <br>
        
        <input type="submit" name="my-form" value="Send">
        </form>
        </body>
        </html>
        """

@app.route('/input', methods=['POST'])
def my_form_post():
    seq = request.form['seq']
    int = request.form['intensity']
    qual= request.form['qual_output']
    dtext = qual.split("\n")
    peaksdict = {}
    
    for line in dtext:
        ln = line.split('\t')
        try:
            peaksdict[float(ln[0])] = float(ln[1])
        except ValueError:
            pass
        except IndexError:
            pass




return str(sum(k for k in peaksdict))




if __name__ == '__main__':
    app.run()