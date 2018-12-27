from flask import Flask, request
from werkzeug import secure_filename
from MyQR import myqr
import os
import base64
import utils.qiniu
app = Flask(__name__)

root = os.getcwd()
@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        print(request.args.get('name'))
        return 'Hello World!'
    else:
        #print(request.form['name'])
        print(request.files['file'])
        f = request.files['file']

        #print base64.b64encode(imageFile.read())
        filename = secure_filename(f.filename)
        filetype = f.content_type
        f.save(root+'/static/images/' + filename)

        myqr.run(
            words='http://www.baidu.com',
            version=10,
            level='H',
            picture=root+'/static/images/' + filename,
            colorized=True,
            contrast=1.5,
            brightness=1.6,
            save_name=filename,
            save_dir=root+'/static/images/'
        )
        #image = open(root+'/static/images/' + filename, "rb")
        backurl  = utils.qiniu.uploader(root + '/static/images/' + filename)
        # 将数据写到本地的方法
        # with open(root+'/static/images/' + filename, "rb") as f:
        #     base64_data = base64.b64encode(f.read())
        #
        # backstr = 'data:'+filetype+';base64,'+base64_data.decode()
        # print(backstr)
        return backurl


if __name__ == '__main__':
    #app.debug = True
    #app.host = '0.0.0.0'
    #app.port = 8090
    app.run(port=8080, host='0.0.0.0')
