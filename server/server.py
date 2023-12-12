from flask import Flask, request
from transformers import pipeline

# ham gen_text 
model = "exampleDeploy\model\LaMini-111M"
pipe = pipeline("text-generation", model=model)
def gen_text(input_prompt):
    out_put = pipe(input_prompt)[0]['generated_text']
    return out_put


app = Flask(__name__)

# phuong thuc post
@app.route('/process_text', methods=['POST'])
def process_text():
    if request.method == 'POST':
        # Lấy dữ liệu được gửi lên từ người dùng
        user_text = request.form.get('text')  
        user_text = str(user_text)
        out = gen_text(user_text)
    return out

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='6868')
