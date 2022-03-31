
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ziyis.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')

@app.route("/book", methods=["POST"])
def book_post():
    url_receive = request.form['url_give']
    url2_receive = request.form['url2_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive,url2_receive, headers=headers)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']


    doc = {
        'title':title,
        'image': image,
        'star':star_receive,
        'comment':comment_receive,
        'url2':url2_receive
    }


    db.book.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})

@app.route("/book", methods=["GET"])
def book_get():
    book_list=list(db.book.find({},{'_id':False}))
    return jsonify({'book':book_list})



if __name__ == '__main__':
   app.run('0.0.0.0', port=8001, debug=True)