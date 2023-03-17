# **LittleLemon**
## **API Endpoints To Test**

Below are the API endpoints or paths that you can use to test out the APP
* `/api/` (Static Index HTML page)
* `/api/bookings` [POST, GET]
* `/api/menu`  [POST, GET]
* `/api/menu/id` [GET, PATCH, PUT] (id as Primary Key)
* `/api/users` [GET] (requires admin authentication)
* `/auth/users` [GET]
* `/auth/users/me` [GET] (requires authentication)
* `/auth/token/login` [POST] (login, username & password)
* `/auth/token/logout` (logout)
* `/auth/** other routes from djoser such as reset password, activate, e.t.c

<br>

### **Some helpful commands**

If you want to run this app locally you can use the below commands:
<br>

* Migrate the database first

        python manage.py migrate
* Star the server

        python manage.py runserver

For more commands check the Makefile for reference