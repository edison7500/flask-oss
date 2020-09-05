# flask-oss

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/51fdde18650c4a50a33cc909d820b02f)](https://www.codacy.com/manual/edison7500/flask-oss?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=edison7500/flask-oss&amp;utm_campaign=Badge_Grade)
[![GitHub license](https://img.shields.io/github/license/edison7500/flask-oss.svg)](https://github.com/edison7500/flask-oss/blob/master/LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

flask storage use **aliyun-oss** 


## flask config

```
OSS_ACCESS_KEY_ID       = '<your oss key>'
OSS_SECRET_ACCESS_KEY   = '<your oss secret>'
OSS_ENDPOINT            = '<your oss endpoint>'
OSS_BUCKET_NAME         = '<your oss bucket name>'
```

## How to use 
```.python
from flask import Flask
from flask_oss import FlaskOSS

app = Flask(__name__)
oss = FlaskOSS(app)

#upload file to oss
oss.put_file('<your filename>', 'file data')

#upload file to oss
oss.put_file_by_path('<your filename>', '<your filepath>')

#check file in oss
oss.exists_file('<your filename>')

#download file from oss
oss.get_file('<your filename in oss>')

#remove file from oss
oss.del_file('<your filename in oss>')
```
