from flask import Flask, render_template,request,jsonify
app = Flask(__name__)


from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ziyis.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_post():
   title_receive = request.form['title_give']
   thumbnail_receive=request.form['thumbnail_give']

   doc = {
      'title':'슬기로운'
   }
   db.book.insert_one(doc)

   return jsonify({'msg': '저장 완료!'})


@app.route('/book', methods=['GET'])
def book_get():
   title_receive = request.args.get('title_give')
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})



if __name__ == '__main__':
   app.run('0.0.0.0',port=1000,debug=True)
