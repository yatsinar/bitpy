from flask import Flask
bitpy = Flask(__name__)

@bitpy.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    bitpy.run()