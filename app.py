from flask import Flask, render_template, request, jsonify
from pymongo.mongo_client import MongoClient

app = Flask(__name__, template_folder='templates')


uri = "mongodb+srv://mohfaiz0504:mohfaiz543@cluster0.nmg1vs4.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
db = client["message_db"]
collection = db["collection"]



@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/send',methods=['POST'])
def send():
    if request.method == 'POST':
        
        text = request.get_json().get("val")
        text=text.split(" ")
        data_dic={"name":text[0],"email":text[1],"msg":text[2]}
        print(data_dic)
        collection.insert_one(data_dic)
        message={"message":"Message sent successfully"}
        return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)