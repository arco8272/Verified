from flask import Flask,jsonify
import requests
from flask import Flask
app = Flask(__name__)

@app.route('/arcoikka/id=<int:pk>')
def hello_world(pk):

    cookies = {
        'ajax': '0',
        'token': 'hOadPuyHfcLmInGeWASQz0jJK2k3b8Bsi16YlF4vwoTDNUqXg95MrCpx7EVZRt63173339512',
        'numberOfRequests': '2',
    }

    headers = {
        'Host': 'instaup.marsapi.com',
        'Agent': 'OPPO:23:PECM30',
        'Crc': '5070437774/24551372/3838819788415185973',
        'Api_key': 'ABCXYZ123TEST',
        'Nagent': '869390048632298/02:00:00:00:00:00/-1123815807/828b3d25b56bed31/92893157623399229622/null',
        'Threads': '0',
        'Dsl': 'fe7ed4f6',
        'Lng': 'en',
        'Cnt': 'unknown',
        'Special-User': '0',
        'Versionname': '18.3.0',
        'Market': 'Global',
        'Aj': '0',
        'Version': '137',
        'Enmarket': 'EnglishWebPayment',
        'Uid': '63173339512',
        'Create_at': 'November 18, 2023',
        'Access': 'c560772c33e0d6e790c43537e514821d',
        'Pkg': 'f2c6d7a5b030a1542f7eb589d5013340',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Content-Length': '66',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'okhttp/3.12.1',
        'Connection': 'close',
        # 'Cookie': 'ajax=0; token=hOadPuyHfcLmInGeWASQz0jJK2k3b8Bsi16YlF4vwoTDNUqXg95MrCpx7EVZRt63173339512; numberOfRequests=2',
    }

    data = {
        'user_name': 'instafol99_',
        'market': 'EnglishWebPayment',
        'user_id': f'{pk}',
    }

    response = requests.post(
        'https://instaup.marsapi.com/get_likes/user/coins',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    ).json()
    return f"created by aszuts Instagram Sh4y6m\n {response}"
