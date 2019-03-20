# hasim-server
하심 서비스를 위한 서버

서버에 사용된 웹 프레임워크
==============================

[Flask는 Python으로 작성된 웹 프레임워크이다.] (http://flask.pocoo.org/) Flask는 document에서 자신을 microframework라고 설명한다. 서버에서 핵심적으로 필요한 서비스는 제공하지만(routing과 html rendering과 같은) 데이터베이스의 선택이나 보안 모듈과 같은 웹 어플리케이션을 구성하는 세부 요소는 개발자에게 맡겨져 있다. 이 덕분에 Flask는 짧은 시간에 간단한 구현만으로도 서비스를 시작할 수 있다는 장점이 있는 반면 장고와는 다르게 개발자가 설정해야 할 부분이 많다는 단점도 있다. 다행히도 Flask에서는 서버 구성 모듈들의 확장을 위한 Flask-확장 모듈들을 제공한다.(여느 Python 모듈들과 마찬가지로 간단하게 import하여 사용이 가능하다.) 예를 들어, hasim 서비스에서 데이터베이스로 선택한 MongoDB의 경우 flask-pymongo 모듈을 사용하여 MongoDB와 연결하여 사용할 수 있다. hasim 서비스는 100명 이내의 사용자를 가정한 서비스이고 제공해야 할 서비스도 간단한 데이터 읽기와 쓰기에 불과하기 때문에 무거운 다른 웹 프레임워크가 아닌 Flask를 사용하였다.


Dependency
==================
│
├─ Flask 1.0.2
├─ Flask-PyMongo 2.2.0 
├─ Jinja 2 2.10
├─ Werkzeug 0.14.1
└─ pymongo 3.7.2
