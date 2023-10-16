from flask import Flask, request
import requests
import dns.resolver


app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_request():
    # 获取请求的Cookie
    cookies = request.cookies

    # 检查Cookie是否包含键名为'a'，且值包含"j8.rip"
    if 'a' in cookies and 'j8.rip' in cookies['a']:
        a_value = cookies['a']
        
        target_url = "http://{}".format(a_value[1:])

        print(target_url)
        responses_data = requests.get(target_url)
        print(responses_data)
        
        return "good"
    else:
        return 'not good'

if __name__ == '__main__':
    app.run()