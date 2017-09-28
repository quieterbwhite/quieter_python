# -*- coding=utf-8 -*-

from qiniu import Auth, put_file
from consts import AccessKey, SecretKey, BucketName, Expired


class QiNiu(object):

    def __init__(self):
        self.authed = Auth(AccessKey, SecretKey)

    def upload(self, data):
        """
        :param data:
                {
                    "filename":"",
                    "filepath":"",
                    "policy":{}
                }
        :return:
            ret
            info
        """

        filename = data["filename"]
        filepath = data["filepath"]
        policy   = data.get("policy", {})

        if policy:
            token = self.authed.upload_token(BucketName, filename, Expired, policy)
        else:
            token = self.authed.upload_token(BucketName, filename, Expired)

        ret, info = put_file(token, filename, filepath)

        return ret, info


def main():


    filename = "error.png"
    filepath = "/home/libo/work/camup_env/camup/static/seeds/error.png"

    data = {
        "filename":filename,
        "filepath":filepath,
        "policy":{}
    }

    qiniu = QiNiu()

    ret, info = qiniu.upload(data)

    print ret

    print info

if __name__ == '__main__':
    main()
