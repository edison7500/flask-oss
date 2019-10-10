# flask-oss

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/51fdde18650c4a50a33cc909d820b02f)](https://www.codacy.com/manual/edison7500/flask-oss?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=edison7500/flask-oss&amp;utm_campaign=Badge_Grade)

flask stroage use **aliyun-oss** 


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

#check file in oss
oss.exists_file('<your filename>')

#download file from oss
oss.get_file('<your filename in oss>')

#remove file from oss
oss.del_file('<your filename in oss>')
```