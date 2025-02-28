"from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    services = [
        {
            'title': 'Chat Tool',
            'description': 'Ultimate Facebook Messages sender tool.',
            'image': 'static/images/convo.jpg',
            'link': '/service/chat'
        },
        {
            'title': 'Comments Tool',
            'description': 'Facebook Post Comments Tool By Cookies.',
            'image': 'static/images/post.jpg',
            'link': '/service/post'
        },
        {
            'title': 'Comments Tool V2',
            'description': 'Facebook Post Comments Tool v2 By Tokens.',
            'image': 'static/images/postv2.jpg',
            'link': '/service/postv2'
        },
        {
            'title': '2FA Live',
            'description': 'Get OTP Code Live using 2FA Live.',
            'image': 'static/images/2fa.jpg',
            'link': '/service/2fa'
        },
        {
            'title': 'Checker Tool',
            'description': 'Check Multiple Tokens, Cookies, Multiple ID\'s using Checker Tool.',
            'image': 'static/images/checker.jpg',
            'link': '/service/checker'
        },
        {
            'title': 'Token Extractor',
            'description': 'Profile & Page Token Extractor using Cookies.',
            'image': 'static/images/token.jpg',
            'link': '/service/token'
        }
    ]
    return render_template('index.html', services=services)
if __name__ == '__main__':
    app.run(debug=True)"
 https://chat.two.ai/#:~:text=Script%20(app.py)-,from,-flask
