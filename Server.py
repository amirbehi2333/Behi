import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/message', methods=['POST'])
def api_message():
    user_message = request.json.get('message', '')

    # یک پاسخ ساده به عنوان نمونه
    if "سلام" in user_message:
        bot_reply = f"سلام بهنوش عزیز 🌸 چطوری؟"
    elif "حال من بده" in user_message:
        bot_reply = "می‌دونم سخته ولی من اینجام کنارت ❤️ با هم حلش می‌کنیم."
    else:
        bot_reply = f"بهنوش جان، من همیشه اینجام برات ✨"

    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
