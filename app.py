from flask import Flask, request, redirect, render_template
import string
import random

app = Flask(__name__)
url_map = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_code = generate_short_code()
        url_map[short_code] = original_url
        return render_template('index.html', short_code=short_code)
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_url(short_code):
    original_url = url_map.get(short_code)
    if original_url:
        return redirect(original_url)
    else:
        return 'URL not found', 404

if __name__ == '__main__':
    app.run(debug=True)
