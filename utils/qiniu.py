# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_file, etag
import uuid

# 需要填写你的 Access Key 和 Secret Key
access_key = 'JQ9Gq0DM69NJFrpkPUPxuWD8e8DtJ0vZz9EEoe7P'
secret_key = 'Kipl3z76-zg3so06XJkekmJFHSkjI9cxKpgBwQLb'
# 构建鉴权对象
q = Auth(access_key, secret_key)
# 要上传的空间
bucket_name = 'xfysjxcx'
# 上传到七牛后保存的文件名
key = 'qrcode/images/' + str(uuid.uuid1())


# 生成上传 Token，可以指定过期时间等


# 要上传文件的本地路径
def uploader(url):
    localfile = url
    fullname = key + '.' + url.split('.')[-1]
    print(type)
    token = q.upload_token(bucket_name, fullname, 3600)
    ret, info = put_file(token, fullname, localfile)
    print(info)
    assert ret['key'] == fullname
    assert ret['hash'] == etag(localfile)
    return fullname
