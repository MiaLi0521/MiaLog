"""
用来存储各种辅助函数
>> urljoin('https://www.jianshu.com','https://www.baidu.com/p/2ea7a063223')
>> 'https://www.baidu.com/p/2ea7a063223'
说明第二个URL为外部URL
>> urljoin('https://www.jianshu.com','/p/2ea7a063223')
>> 'https://www.jianshu.com/p/2ea7a063223'
说明第二个URL为内部URL
"""
from flask import request, redirect, url_for
from urllib.parse import urljoin, urlparse


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def redirect_back(default='blog.index', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))
