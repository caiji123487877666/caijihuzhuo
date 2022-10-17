import requests
from make_requests_http import make_http_requests

# 发送请求
case = {
    'id': 1,
    'title': "注册成功，不带昵称和类型",
    'method': 'post',
    'url': 'http://api.lemonban.com/futureloan/member/register',
    'request_data': {"mobile_phone": "15873009901", "pwd": "12345678"},
    'expect_data': {"code": 0, "msg": "ok"},
    'headers': {"X-Lemonban-Media-Type": "lemonban.v1"}
}

# if case['method'] == 'post':
#     try:
#         response = requests.get(url=case['url'], json=case['request_data'], headers=case['headers'])
#     except Exception as e:
#         raise e
# elif case['method'] == 'GET':
#     pass
# elif case['method'] == 'put':
#     pass

response = make_http_requests(url=case['url'], method=case['method'],json=case['request_data'], headers=case['headers'])
# 判断与请求是否一致
# 状态码是否一致
if response.status_code == 200:
    print('‘请求发送更成功')
else:
    raise AssertionError('请求失败，状态码为{}'.format(response.status_code))
'''
如果响应的格式是json格式，有一个json方法可以将json转换为python对象
'''
res_data = response.json()
if res_data['code'] == case['expect_data']['code']:
    print('code断言成功')
else:
    raise AssertionError('code断言失败，错误的msg为{}'.format(res_data['code']))
if res_data['msg'] == case['expect_data']['msg']:
    print('msg断言成功')
else:
    raise AssertionError('msg断言失败，错误的msg为{}'.format(res_data['msg']))
# assert res_data['msg'] == case['expect_data']['msg']
