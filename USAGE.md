# DUTAPI_Heroku - Usage

## Table of contents
- [Base URL](#base-url)
- [Get News](#get-news)
- [Account](#account)
  - [Login](#login)
  - [Logout](#logout)
  - [Get subjects schedule](#get-subjects-schedule)
  - [Get subjects fee](#get-subjects-fee)
  - [Get account information](#get-account-information)

## Base URL
- https://dutapi.herokuapp.com


## Get news
global - Thông báo chung or subject - Thông báo lớp học phần

```
[GET] /news
```

Parameters:
- type: News type (global/subject).
- page (optional): News page.

Returns:
- If "type" isn't provided, will return 400 Bad Request.
- If "page" is missing or invaild, will follow default (1) and continue.
- If successful, will return 200 and list of news.

Examples:
```
/news?type=global&page=1
```

[Go to TOC](#table-of-contents)

## Account

### Login
```
[POST] /account?type=login
```

Parameters:
- user: User account (here is student ID)
- pass: User password

Returns:
- If "user" or "pass" is missing, will return 400 Bad Request.
- If isn't logged in, will return 401.
- If successful, will return 200 and SessionID in json.

Examples:
```
/account?type=login&user=123456789&pass=9876554321
```

[Go to TOC](#table-of-contents)

### Logout
```
[POST] /account?type=logout
```

Parameters:
- sid: Session ID.

Returns:
- Will return 200 and login state.
- If no "sid", will return 400 Bad Request.
- This won't detect valid or invaild "sid".

Examples:
```
/account?type=logout&sid=48239r78293urjd23
```

[Go to TOC](#table-of-contents)

### Get subjects schedule
```
[POST] /account?type=subjectschedule
```

Parameters:
- sid: Session ID.
- year: Current schoolyear.
- semester: Current semseter.
- insummer: If your subject schedule is in summer, give it 1.

Returns:
- If one of parameters above is missing, will return 400 Bad Request.
- If "sid" not logged in, will return 401.
- If successful, will return 200 and subjects schedule.

Examples:
```
/account?type=subjectschedule?sid=48239r78293urjd23&year=20&semester=2&insummer=0
```

[Go to TOC](#table-of-contents)

### Get subjects fee
```
[POST] /account?type=subjectfee
```

Parameters:
- sid: Session ID.
- year: Current schoolyear.
- semester: Current semseter.
- insummer: If your subject schedule is in summer, give it 1.

Returns:
- If one of parameters above is missing, will return 400 Bad Request.
- If "sid" not logged in, will return 401.
- If successful, will return 200 and subjects fee.

Examples:
```
/account?type=subjectfee?sid=48239r78293urjd23&year=20&semester=2&insummer=0
```

[Go to TOC](#table-of-contents)

### Get account information
```
[POST] /account?type=accinfo
```

Parameters:
- sid: Session ID.


Returns:
- If one of parameters above is missing, will return 400 Bad Request.
- If "sid" not logged in, will return 401.
- If successful, will return 200 and account information.

Examples:
```
/account?type=accinfo?sid=48239r78293urjd23
```
