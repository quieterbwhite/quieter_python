# -*- coding=utf-8 -*-
# Created Time: 2015年09月30日 星期三 16时08分17秒
# File Name: errors.py

'''
错误码定义

这个错误码文件会在所有 wedor 项目中使用
错误码第一位用来分类， 其他用来确定是该类下具体异常
分类:
    1:    系统异常
    2:    用户系统相关
    3:    图片处理相关
    4:    待添加
    N:    待添加
    9:    系统内部错误
'''

err_param = {'err_code':'10001'}

errs = {
    '-1'   : 'fail',
    '0'    : 'success',
    '10001': 'param missing',
    '10002': 'param type error',
    '10003': 'db error',
    '10004': 'empty',
    '10005': 'no updates',
    '10006': 'time out',
    '10007': 'not allowed',

    '20001': 'wrong username or password',
    '20002': 'user exists',
    '20003': 'user not exists',
    '20004': 'login error',
    '20005': 'login expired',
    '20006': 'staff not exists',
    '20007': 'invalid rights',

    '20008': 'no order found',
    '20009': 'no shop found',
    '20010': 'no object found',
    '20011': 'no price found',
    '20012': 'wrong user-agent',
    '20013': 'wrong order status',
    '20014': 'no available washing record found',
    '20015': 'cant cancel coupon cloth',
    '20016': 'incorrect amount or currency paid',
    '20017': 'wrong recharge sums',
    '20018': 'order cant modify',
    '20019': 'wrong get code',
    '20020': 'cant cancel the order',
    '20021': 'no recharge card found',
    '20022': 'invalid shop token',
    '20023': 'invalid area id',
    '20024': 'recharge failed',
    '20025': 'washing code error',
    '20026': 'packt process not found',
    '20027': 'wrong shop',

    '21001': 'wrong username or password',
    '21002': 'user exists',
    '21003': 'user not exists',
    '21004': 'login error',
    '21005': 'login expired',
    '21006': 'wrong verify code',
    '21007': 'wrong rights',
    '21008': 'no recharge card found',
    '21009': 'wrong rights',
    '21010': 'bind wechat failed',

    '22001': 'cant del the area',
    '22002': 'cant del the worker',

    '30200':u'操作执行成功',
    '30298':u'部分操作执行成功',
    '30400':u'请求报文格式错误',
    '30401':u'认证授权失败',
    '30404':u'资源不存在',
    '30405':u'请求方式错误',
    '30406':u'上传的数据CRC32校验错误',
    '30419':u'用户账号被冻结',
    '30478':u'镜像服务器出现异常',
    '30503':u'服务端不可用',
    '30504':u'服务端操作超时',
    '30579':u'上传成功但是回调失败',
    '30599':u'服务端操作失败',
    '30608':u'资源内容被修改',
    '30612':u'指定资源不存在或已被删除',
    '30614':u'目标资源已存在',
    '30630':u'已创建的空间数量达到上限，无法创建新空间',
    '30631':u'指定空间不存在',
    '30640':u'调用列举资源(list)接口时，指定非法的 marker 参数',
    '30701':u'在断点续传上传过程中，后续上传接收地址不正确或ctx信息已过期',

    '31001':u'拒绝访问',
    '31002':u'Bucket已经存在',
    '31003':u'Bucket不为空',
    '31004':u'实体过大',
    '31005':u'实体过小',
    '31006':u'文件组过大',
    '31007':u'文件Part不存在',
    '31008':u'文件Part过时',
    '31009':u'参数格式错误',
    '31010':u'Access Key ID不存在',
    '31011':u'无效的Bucket名字',
    '31012':u'无效的摘要',
    '31013':u'无效的Object名字',
    '31014':u'无效的Part',
    '31015':u'无效的part顺序',
    '31016':u'Logging操作中有无效的目标bucket',
    '31017':u'OSS内部发生错误',
    '31018':u'XML格式非法',
    '31019':u'不支持的方法',
    '31020':u'缺少参数',
    '31021':u'缺少内容长度',
    '31022':u'Bucket不存在',
    '31023':u'文件不存在',
    '31024':u'Multipart Upload ID不存在',
    '31025':u'无法处理的方法',
    '31026':u'预处理错误',
    '31027':u'发起请求的时间和服务器时间超出15分钟',
    '31028':u'请求超时',
    '31029':u'签名错误',
    '31030':u'用户的Bucket数目超过限制',

    '40001':u'价格不正确',

    '90001':u'子类必须实现父类的该方法',
}

oss_errs = {
    'AccessDenied':'31001',
    'BucketAlreadyExists':'31002',
    'BucketNotEmpty':'31003',
    'EntityTooLarge':'31004',
    'EntityTooSmall':'31005',
    'FileGroupTooLarge':'31006',
    'FilePartNotExist':'31007',
    'FilePartStale':'31008',
    'InvalidArgument':'31009',
    'InvalidAccessKeyId':'31010',
    'InvalidBucketName':'31011',
    'InvalidDigest':'31012',
    'InvalidObjectName':'31013',
    'InvalidPart':'31014',
    'InvalidPartOrder':'31015',
    'InvalidTargetBucketForLogging':'31016',
    'InternalError':'31017',
    'MalformedXML':'31018',
    'MethodNotAllowed':'31019',
    'MissingArgument':'31020',
    'MissingContentLength':'31021',
    'NoSuchBucket':'31022',
    'NoSuchKey':'31023',
    'NoSuchUpload':'31024',
    'NotImplemented':'31025',
    'PreconditionFailed':'31026',
    'RequestTimeTooSkewed':'31027',
    'RequestTimeout':'31028',
    'SignatureDoesNotMatch':'31029',
    'TooManyBuckets':'31030'
}














