from flask import Flask,render_template,request,jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World'

@app.route('/test')
def  test():
    return  render_template('test.html')
    
@app.route('/partialupdate/<int:userid>', methods=['POST'])
def partial_update(userid):
    try:
        # fetch the user, perform the updates and commit
        return jsonify(success=1)
    except Exception:
        return jsonify(success=0)
if __name__ == '__main__':

    app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run()