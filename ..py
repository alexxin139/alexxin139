import requests
token = "cd418c735f05ae975ce8480b8e0e0ca578b81e277904f8f061286f1798200a61e009bca7d93ec3051bae27181afcdd56"
geturl =f'"https://a1.fanbook.cn/api/bot/{token}/getme"'
xinxi = requests.get(url=geturl)
print(xinxi)
#result = requests.get(url=f'http://1.117.76.68:5000/bot/sm?token={token}&chatid=595164589499731968&text=114514')
#print(result.text)