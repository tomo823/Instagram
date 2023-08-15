import requests
import json
import datetime
from pprint import pprint


def basic_info():
    # 初期
    config = dict()
    # 【要修正】アクセストークン
    config["access_token"]         = 'EAACbKTgHjzMBO2TTm7SiyjeBQKIZASNGaZAJujyynZBxdZBoYooZBGVcoSxqOh1feVbkm1g6nzDDmZCIZBNectvsIAFZBMGZAcAD2C23yBPFggq8nDdknUCHnwDY4NAIGWrDXY82bNKdcRJYZAF6UlYaozgoxPaOuU5ZBs3BifEivkYscsYpnwZAJ69mbZCBB'
    # 【要修正】アプリID
    config["app_id"]               = '170601335983923'
    # 【要修正】アプリシークレット
    config["app_secret"]           = '88b7d8b3e346944c35b8a5d19b00d7e5'
    # 【要修正】インスタグラムビジネスアカウントID
    config['instagram_account_id'] = "648247127274918"
    # 【要修正】グラフバージョン
    config["version"]              = 'v17.0'
    # 【修正不要】graphドメイン
    config["graph_domain"]         = 'https://graph.facebook.com/'
    # 【修正不要】エンドポイント
    config["endpoint_base"]        = config["graph_domain"]+config["version"] + '/'
    # 出力
    return config



# APIリクエスト用の関数
def InstaApiCall(url, params, request_type):
    
    # リクエスト
    if request_type == 'POST' :
        # POST
        req = requests.post(url,params)
    else :
        # GET
        req = requests.get(url,params)
    
    # レスポンス
    res = dict()
    res["url"] = url
    res["endpoint_params"]        = params
    res["endpoint_params_pretty"] = json.dumps(params, indent=4)
    res["json_data"]              = json.loads(req.content)
    res["json_data_pretty"]       = json.dumps(res["json_data"], indent=4)
    
    # 出力
    return res



def get_user_media_stats(params, ig_user_name):
    """
    ***********************************************************************************
    【APIのエンドポイント】
    "https://graph.facebook.com/v14.0/17841405309211844?fields=business_discovery.username('ig_username'){followers_count,media_count}&access_token={access-token}"
    ***********************************************************************************
    """
    
    # エンドポイントに送付するパラメータ
    Params = dict()
    Params['user_id']      = params['instagram_account_id']
    Params['access_token'] = params['access_token']
    Params['fields']       = 'business_discovery.username(' + ig_username + '){followers_count,media_count,media{comments_count,like_count}}'
    # エンドポイントURL
    url = params['endpoint_base'] + Params['user_id']
    # 出力
    return InstaApiCall(url, Params, 'GET')



# 【要修正】インスタグラムユーザー名を指定！
ig_username = 'bizco_careerup'

# リクエストパラメータ
params      = basic_info()                                # リクエストパラメータ
response    = get_user_media_stats(params, ig_username)   # レスポンス

# 出力
pprint(response)