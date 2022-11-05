from flask import  Flask, request, jsonify


app = Flask(__name__)

@app.route('/xyz',methods = ['GET','POST'])
def test():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify(str(result))



# @app.route('/db_mogo',methods = ['GET','POST'])
# def mongo_connect():
#     if(request.method=="POST"):
#         a = request.json['conn']
#         x = db.db_m_connect()
#         return jsonify(str(x))


if __name__ == '__main__':
    app.run()
