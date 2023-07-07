
import dutapi
from flask import Flask, redirect, url_for, request, Response
import json

# Login
def Login(username: str, password: str):
    repText = None
    repCode = 200
    repType = "text/html; charset=utf-8"
    token = dutapi.GenerateSessionID()
    if username != None and password != None:
        repText = dutapi.Login(token, username, password)
        repCode = 200
        if repText['logged_in'] == False:
            repCode = 401
        repText = json.dumps(repText, ensure_ascii=False).encode('UTF-8')
        repType = "application/json" 
    else:
        repText = 'Bad request!'
        repCode = 400
    return Response(repText, status=repCode, mimetype=repType)

# Logout
def Logout(sessionid: str):
    repText = None
    repCode = 200
    repType = "text/html; charset=utf-8"
    if sessionid != None:
        repText = dutapi.Logout(sessionid)
        if repText['logged_in'] == True:
            repCode = 401
        repText = json.dumps(repText, ensure_ascii=False).encode('UTF-8')
        repType = "application/json"   
    else:
        repText = 'Bad request!'
        repCode = 400
    return Response(repText, status=repCode, mimetype=repType)

# Subject schedule
def SubjectSchedule(sessionid: str, year: int, semester: int, insummer: int):
    repText = None
    repCode = 200
    repType = "application/text"
    if sessionid != None and year != None and semester != None and insummer != None:
        if dutapi.IsLoggedIn(sessionid)['logged_in'] == True:
            repText = json.dumps(dutapi.GetSubjectSchedule(sessionid, year, semester, True if insummer == 1 else False), ensure_ascii=False).encode('UTF-8')
            repCode = 200
            repType = "application/json"            
        else:
            repText = "Unauthorized"
            repCode = 401
    else:
        repText = 'Bad request!'
        repCode = 400
    return Response(repText, status=repCode, mimetype=repType)

# Subject fee
def SubjectFee(sessionid: str, year: int, semester: int, insummer: int):
    repText = None
    repCode = 200
    repType = "text/html; charset=utf-8"
    if sessionid != None and year != None and semester != None and insummer != None:
        if dutapi.IsLoggedIn(sessionid)['logged_in'] == True:
            repText = json.dumps(dutapi.GetSubjectFee(sessionid, year, semester, True if insummer == 1 else False), ensure_ascii=False).encode('UTF-8')
            repCode = 200
            repType = "application/json"            
        else:
            repText = "Unauthorized"
            repCode = 401
    else:
        repText = 'Bad request!'
        repCode = 400
    return Response(repText, status=repCode, mimetype=repType)

def GetAccInfo(sessionid: str):
    repText = None
    repCode = 200
    repType = "text/html; charset=utf-8"
    if sessionid != None:
        if dutapi.IsLoggedIn(sessionid)['logged_in'] == True:
            repText = json.dumps(dutapi.GetAccountInformation(sessionid), ensure_ascii=False).encode('UTF-8')
            repCode = 200
            repType = "application/json"            
        else:
            repText = "Unauthorized"
            repCode = 401
    else:
        repText = 'Bad request!'
        repCode = 400
    return Response(repText, status=repCode, mimetype=repType)

# Get news
def GetNews(type: dutapi.NewsType, page: int):
    repText = None
    repCode = 200
    repType = "application/text"
    try:
        if (type == None) or (type.lower() != "global" and type.lower() != "subjects"):
            repText = "Bad request!"
            repCode = 400
        else:
            if (page == None) or (page.isdigit() == False):
                page = 1
            else:
                page = int(page)
                if page < 1: page = 1
            repText = json.dumps(dutapi.GetNews(dutapi.NewsType.Global if type.lower() == "global" else dutapi.NewsType.Subjects, page), ensure_ascii=False).encode('UTF-8')
            repType = "application/json"
    except:
        repText = 'Internal Server Error!'
        repCode = 500
    finally:
        return Response(repText, status=repCode, mimetype=repType)    

def GetWeekRange(type: str):
    repText = None
    repCode = 200
    repType = "application/json"
    if type == None or len(type) == 0:
        raise Exception("Invalid value!")
    elif type.lower() == "current":
        repText = dutapi.GetCurrentWeek()
        repType = "application/text"
        return Response(repText, status=repCode, mimetype=repType)
    elif type.lower() == "week":
        repText = dutapi.SCHOOLYEAR_START
        repType = "application/json"
        return Response(repText, status=repCode, mimetype=repType)
