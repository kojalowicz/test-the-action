from flask import request, Flask
goodbye = Flask(__name__)
@goodbye.route('/')
def goodbye_world():
    return 'Goodbye World '
if __name__ == '__main__':
    goodbye.run(debug=True, host='0.0.0.0')
