from flask import Flask, render_template

app = Flask(__name__)

# 假資料庫，實際應用中需替換為真實資料庫
data = [
    {"name": "產品1", "category": "類別A", "price": "$100"},
    {"name": "產品2", "category": "類別B", "price": "$200"},
    {"name": "產品3", "category": "類別A", "price": "$150"}
]

@app.route('/')
def index():
    return render_template('test.html', data=data)

# if __name__ == '__main__':
#     app.run(debug=True)   