# -*- coding=utf-8 -*-


from __future__ import print_function

import oss2
from consts import AccessKeyId, AccessKeySecret, BucketName, Endpoint
from camup.services.com_service import ComService

class Osss(object):

    def __init__(self, resid=0, table_name=""):
        self.auth = oss2.Auth(AccessKeyId, AccessKeySecret)
        self.service = oss2.Service(self.auth, Endpoint)
        self.bucket = oss2.Bucket(self.auth, Endpoint, BucketName)
        self.resid = resid
        self.table_name = table_name
        self.percent = -1

    def bucket_list(self):
        """ bucket 列表

        :return:
            bucket_name_list list bucket　名字列表
        """

        bucket_name_list = [b.name for b in oss2.BucketIterator(self.service)]
        print("bucket_name_list: {0}".format(bucket_name_list))
        return bucket_name_list

    def bucket_create(self, bucket_name):
        """ 创建 bucket
        :param bucket_name:
        :return:
        """

        bucket = oss2.Bucket(self.auth, Endpoint, bucket_name)
        bucket.create_bucket()

    def upload(self, data):
        """　上传

        :param data:
                {
                    "filename" : "filename",
                    "filepath" : "/path/to/file"
                }
        :return:
            rate int
        """

        result = self.bucket.put_object_from_file(data["filename"], data["filepath"], progress_callback=self.percentage)

        print("http status: {0}".format(result.status))
        print("request_id: {0}".format(result.request_id))
        print("etag: {0}".format(result.etag))
        print("headers: {0}".format(result.headers))

    def percentage(self, consumed_bytes, total_bytes):
        """ 获取上传进度

        :param consumed_bytes:
        :param total_bytes:
        :return:
            rate int 进度值
        """

        rate = 0
        if total_bytes:
            rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
            #print("\r{0}%".format(rate), end="")
            if rate != self.percent:
                self.percent = rate
                if self.percent % 2 == 0:
                    rate_percent = "{0}%".format(rate)
                    print("percent: {0}".format(self.percent))
                    ComService.handle_upload_progress(self.resid, self.table_name, rate_percent)


def main():

    filename = "Koala.jpg"
    filepath = "/home/libo/work/camup_env/camup/static/seeds/Koala.jpg"

    data = {
        "filename":filename,
        "filepath":filepath
    }

    osss = Osss()

    osss.bucket_list()

    osss.upload(data)


if __name__ == '__main__':
    main()
