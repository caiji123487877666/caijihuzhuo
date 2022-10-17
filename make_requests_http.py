'''

1.根据不同方法发送请求
2.发送内容动态化
'''
import requests


def make_http_requests(url, method, **kwargs):
    method = method.lower()

    return getattr(requests, method)(url=url, **kwargs)


if __name__ == '__main__':
    case = {
        'id': 1,
        'title': "注册成功，不带昵称和类型",
        'method': 'post',
        'url': 'http://api.lemonban.com/futureloan/member/register',
        'request_data': {"mobile_phone": "15873000001", "pwd": "12345678"},
        'expect_data': {"code": 0, "msg": "ok"},
        'headers': {"X-Lemonban-Media-Type": "lemonban.v1"}
    }
    res = make_http_requests(url=case['url'], method=case['method'],json=case['request_data'], headers=case['headers'])
    print(res.text)
    print(res.json())
