
from flask import Flask, redirect, url_for, request, Response
import dutapi_fun

app = Flask(__name__)

@app.route('/account', methods=['GET', 'POST'])
def account():
    sType = request.args.get('type')
    try:
        if sType == None:
            return Response('Bad request!', status=400, mimetype='text/html; charset=utf-8')
        elif sType.lower() == 'login':
            if request.method == 'POST':
                return dutapi_fun.Login(request.args.get('user'), request.args.get('pass'))
        elif sType.lower() == 'logout':
            if request.method == 'POST':
                return dutapi_fun.Logout(request.args.get('sid'))
        elif sType.lower() == 'subjectschedule':
            if request.method == 'POST':
                return dutapi_fun.SubjectSchedule(request.args.get('sid'), request.args.get('year'), request.args.get('semester'), request.args.get('insummer'))
        elif sType.lower() == 'subjectfee':
            if request.method == 'POST':
                return dutapi_fun.SubjectFee(request.args.get('sid'), request.args.get('year'), request.args.get('semester'), request.args.get('insummer'))
        elif sType.lower() == 'accinfo':
            if request.method == 'POST':
                return dutapi_fun.GetAccInfo(request.args.get('sid'))
        else:
            return Response('Bad request!', status=400, mimetype='text/html; charset=utf-8')
    # If something went wrong, will return back to homepage.
    except Exception as err:
        print(err)
        return Response('Internal Server Error!', status=500, mimetype='text/html; charset=utf-8')
 
@app.route('/news', methods=['GET'])
def getNews():
    sType = request.args.get('type')
    page = request.args.get('page')
    if request.method == 'GET':
        return dutapi_fun.GetNews(sType, page)

@app.route('/utils', methods=['GET'])
def getUtils():
    sType = request.args.get('type')
    sTypeWeek = request.args.get('week')
    try:
        if request.method == 'GET':
            if sType == None or len(sType) == 0:
                raise Exception("Invalid value!")
            elif sType.lower() == 'weekrange':
                return dutapi_fun.GetWeekRange(sTypeWeek)
            else:
                raise Exception("No arguments provided.")
    except Exception as err:
        print(err)
        return Response('Internal Server Error!', status=500, mimetype='text/html; charset=utf-8')
          
@app.route('/')
def index():
    return Response("DUTAPI", status=200, mimetype="text/html; charset=utf-8")

if __name__ == '__main__':
    app.run()
