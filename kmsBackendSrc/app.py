from flask import Flask,request,session,jsonify,url_for,send_from_directory
import os,json
import utils,threading,time

global output
output = False
BASEDIR="./config"
COMMANDS=['start','stop','restart']

fileLists = list(os.walk(BASEDIR))[0][2]
nameLists = [fileName.split('.')[0].lower() for fileName in fileLists]
app = Flask(__name__)
app.secret_key =os.urandom(4)
config = utils.config()

def login_check():
    if not session.get('admin'):
        return False
    else:
        return True


@app.route('/')
def hello_world():
    return '没啥软用的主页'


@app.route("/login",methods=['POST'])
def login():
    passwordlist = config.get("password").split("\n")
    if request.form.get("password") in passwordlist:
        session['admin'] = True
        return jsonify(state=True,message="登录成功")
    else:
        session['admin'] = False
        return jsonify(state=False,message="密码错误")

@app.route("/content/<part>",methods=['POST','GET'])
def content(part):
    if request.method == "GET":
        if 'password' in part.lower():
            if login_check():
                return jsonify(status=True,content=config.get(part))
            else:
                return jsonify(status=False,message="login required")
        if (part.lower() not in nameLists) or ('password' in part.lower()):
            return jsonify(status=False,message="param not defined or the file not exits")
        else:
            return jsonify(status=True,content=config.get(part))
    if request.method == "POST":
        if login_check():
            form = request.form
            if not form.get('content'):
                return jsonify(status=False,message="Content required")
            else:
                config.set(part,form.get('content'))
                return jsonify(status=True,message="Update successfully")
        else:
            return jsonify(status=False, message="login required")

@app.route("/control",methods=['POST'])
def control():
    if login_check():
        data = request.get_json()
        if not data:
            return jsonify(status=False,message="action required")
        if data.get('action') not in COMMANDS:
            return jsonify(status=False,message="commmad not allowed")
        else:
            os.system("touch /mnt/log/"+data['action'])
            return jsonify(status=True,message=data['action']+' successfully')
    else:
        return jsonify(status=False, message="login required")


@app.route("/logs")
def log():
    if login_check():
        utils.logParser()
        items = os.popen("tail -n10 /mnt/log/parsedLogs")
        data = items.readlines()
        for i in range(len(data)):
            data[i] = json.loads(data[i])
        os.system("rm /mnt/log/logs")
        return jsonify(data)

    else:
        return jsonify(status=False, message="login required")

@app.route("/status")
def status():
    check = threading.Thread(target=task,args=("./scripts/vlmcs_check vlmcsd",))
    check.start()
    time.sleep(0.1)
    return jsonify(status=output)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

def task(cmd=None):
    global output
    if cmd:
        if os.system(cmd) == 0:
            output = True
        else:
            output = False


if __name__ == '__main__':
    app.run(host="0.0.0.0")

