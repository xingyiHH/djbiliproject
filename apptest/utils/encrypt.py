import hashlib

def md5(data_string):
    from djbiliproject import settings
    obj=hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()

if __name__ == '__main__':
    print(md5("hhhh"))
