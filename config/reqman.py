import requests


class Req:
    """
    执行接口测试主体类
    """
    def __init__(self, headers=None, cookies=None):
        if cookies is None:
            cookies = dict()
        if headers is None:
            headers = dict()
        self.headers = headers
        self.cookies = cookies
        self.req = requests.Session()
        self.temp = dict()  # 存放response数据json内容
        self.content = dict()  # 存放新数据

    def request(self, data, **kwargs):
        self.use(data)
        print("请求数据：" + str(data))
        res = self.req.request(method=data['method'], url=data['url'],
                               data=data['data'], cookies=self.cookies,
                               headers=self.headers, **kwargs)
        if not self.cookies and res.cookies is not None:
            for i in res.cookies.items():
                self.cookies[i[0]] = i[1]

        if hasattr(res, 'json'):
            self.temp = res.json()
            print("response数据: " + str(self.temp))
            self.save(data)
            print('存放的数据' + str(self.content))
        return res

    def update_data(self, data):
        """
        此方法废弃、
        "keyword": ['two=one']
        """
        temp = {}
        if 'keyword' in data.keys():
            for i in data['keyword']:
                if '=' in i:
                    k, v = i.split('=')
                    if v in self.temp.keys():
                        temp[k] = self.temp[v]
        return temp

    def modify(self, data):
        """
            此方法废弃
        """
        if 'save' in data.keys() and data['save']:
            for i in data['save']:
                if i in self.temp.keys():
                    self.content[i] = self.temp[i]
        if 'use' in data.keys() and data['use']:
            for j in data['use'].keys():
                data['data'][j] = self.temp[data['use'][j]]

    def save(self, data):
        """
        保存本次请求响应中需要在下次使用的数据
        """
        if 'save' in data.keys() and data['save']:
            for i in data['save']:
                if i in self.temp.keys():
                    self.content[i] = self.temp[i]

    def use(self, data):
        """
            使用上此请求响应保存的数据、更新到下次请求中
        """
        if 'use' in data.keys() and data['use']:
            for j in data['use'].keys():
                data['data'][j] = self.temp[data['use'][j]]


if __name__ == '__main__':

    data2 = [
        {"method": "post", "url": "http://yapi.demo.qunar.com/api/user/login",
         "data": {"email": "2360150005@qq.com", "password": "12345678"}, 'save': ['errmsg'], 'use': {}},

        {"method": "get", "url": "http://yapi.demo.qunar.com/api/user/find?id=78431", "data": {
            'msg': '哈哈' },
         'save': [], 'use': {'msg': 'errmsg'}}
    ]

    req2 = Req()
    for i2 in data2:
        res2 = req2.request(i2)


#
