from flask import Flask, render_template, request, redirect, url_for
from werkzeug import secure_filename
import os
from main import locatePlate

#app = Flask(__name__, static_url_path="", static_folder="static/images")
app = Flask(__name__)

app.secret_key = 'thisisasecretekey'    
app.config['UPLOAD_FOLDER'] = 'static/images'


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        f = request.files['photo']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        
        #model prediction   
        locatePlate(f.filename)
        res_img="static/images/o_"+f.filename
        text_out='PLATE NUMBER'
        return render_template('result.html', img_name=res_img, text_name=text_out)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)