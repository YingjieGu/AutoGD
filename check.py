import requests,json

# 填写pushplus微信消息推送
sckey = 'ec626523407844e58e95f13bf7e65156'
# 填入glados账号对应cookie
# cookie = 'koa:sess=eyJ1c2VySWQiOjM3MzEyNywiX2V4cGlyZSI6MTcxNTEzNDA5MTEwMCwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=l8ZT4Ynxrlxic6jSWwBTg4lMNbE; __stripe_mid=24cab017-308c-4a6a-9663-c02b9a45db2e569594; _gid=GA1.2.595094798.1691480132; _ga=GA1.2.1940575413.1681177047; _ga_CZFVKMNT9J=GS1.1.1691564232.23.0.1691564232.0.0.0'
cookie = "_gid=GA1.2.590902005.1691659888; koa:sess=eyJ1c2VySWQiOjM3MzEyNywiX2V4cGlyZSI6MTcxNzU4MDE5MTA0OSwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=sTPg8ASynovzyslB6ZkE_qgJ1hE; _ga=GA1.1.2041549777.1691659887; _ga_CZFVKMNT9J=GS1.1.1691659887.1.1.1691661051.0.0.0"


def start():
    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
   # print(res)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        #print(time)
        #发送微信通知消息
        requests.get('http://www.pushplus.plus/send?token=' + sckey + '&title=' + mess + '&content=' + time + 'days left!')
    else:
        requests.get('http://www.pushplus.plus/send?token=' + sckey + '&title=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()
