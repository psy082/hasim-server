# hasim-server
하심 서비스를 위한 서버

<<<<<<< HEAD
서버에 사용된 웹 프레임워크
==============================

[Flask는 Python으로 작성된 웹 프레임워크이다.] (http://flask.pocoo.org/) Flask는 document에서 자신을 microframework라고 설명한다. 서버에서 핵심적으로 필요한 서비스는 제공하지만(routing과 html rendering과 같은) 데이터베이스의 선택이나 보안 모듈과 같은 웹 어플리케이션을 구성하는 세부 요소는 개발자에게 맡겨져 있다. 이 덕분에 Flask는 짧은 시간에 간단한 구현만으로도 서비스를 시작할 수 있다는 장점이 있는 반면 장고와는 다르게 개발자가 설정해야 할 부분이 많다는 단점도 있다. 다행히도 Flask에서는 서버 구성 모듈들의 확장을 위한 Flask-확장 모듈들을 제공한다.(여느 Python 모듈들과 마찬가지로 간단하게 import하여 사용이 가능하다.) 예를 들어, hasim 서비스에서 데이터베이스로 선택한 MongoDB의 경우 flask-pymongo 모듈을 사용하여 MongoDB와 연결하여 사용할 수 있다. hasim 서비스는 100명 이내의 사용자를 가정한 서비스이고 제공해야 할 서비스도 간단한 데이터 읽기와 쓰기에 불과하기 때문에 무거운 다른 웹 프레임워크가 아닌 Flask를 사용하였다.

Flask는 Python 웹 어플리케이션 표준인 WSGI(Web Server Gateway Interface)에 맞춰 작성된 toolkit인 [Werkzeug] (https://palletsprojects.com/p/werkzeug/)와 동적인 웹페이지로 렌더링 해주는 template engine인 [Jinja2] (http://jinja.pocoo.org/)를 기반으로 작성되었다. (Flask, Werkzeug, jinja2 모두 Python 언어를 기반으로 오픈소스 프로젝트를 진행하는 pocoo라는 팀의 결과물이다.) 따라서 API작성 시 WSGI에 대한 공부는 유용하며, html 문서 작성시에도 Jinja2에 대한 지식이 있으면 더 효율적이고 간결하게 데이터를 표현할 수 있다.
=======
서버에 사용된 웹 프레임워크 : Flask
==============================

[Flask는 Python으로 작성된 웹 프레임워크이다.](http://flask.pocoo.org/) Flask는 document에서 자신을 microframework라고 설명한다. 서버에서 핵심적으로 필요한 서비스는 제공하지만(routing과 html rendering과 같은) 데이터베이스의 선택이나 보안 모듈과 같은 웹 어플리케이션을 구성하는 세부 요소는 개발자에게 맡겨져 있다. 이 덕분에 Flask는 짧은 시간에 간단한 구현만으로도 서비스를 시작할 수 있다는 장점이 있는 반면 장고와는 다르게 개발자가 설정해야 할 부분이 많다는 단점도 있다. 다행히도 Flask에서는 서버 구성 모듈들의 확장을 위한 Flask-확장 모듈들을 제공한다.(여느 Python 모듈들과 마찬가지로 간단하게 import하여 사용이 가능하다.) 예를 들어, hasim 서비스에서 데이터베이스로 선택한 MongoDB의 경우 flask-pymongo 모듈을 사용하여 MongoDB와 연결하여 사용할 수 있다. hasim 서비스는 100명 이내의 사용자를 가정한 서비스이고 제공해야 할 서비스도 간단한 데이터 읽기와 쓰기에 불과하기 때문에 무거운 다른 웹 프레임워크가 아닌 Flask를 사용하였다.

Flask는 Python 웹 어플리케이션 표준인 WSGI(Web Server Gateway Interface)에 맞춰 작성된 toolkit인 [Werkzeug](https://palletsprojects.com/p/werkzeug/) 와 동적인 웹페이지로 렌더링 해주는 template engine인 [Jinja2](http://jinja.pocoo.org/)를 기반으로 작성되었다. (Flask, Werkzeug, jinja2 모두 Python 언어를 기반으로 오픈소스 프로젝트를 진행하는 pocoo라는 팀의 결과물이다.) 따라서 API작성 시 WSGI에 대한 공부는 유용하며, html 문서 작성시에도 Jinja2에 대한 지식이 있으면 더 효율적이고 간결하게 데이터를 표현할 수 있다.




>>>>>>> origin/master
