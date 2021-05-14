from flask import Flask, render_template, jsonify, request, redirect
from flask.helpers import url_for
from instamojo_wrapper import Instamojo

app = Flask(__name__)
api = Instamojo(api_key='test_cbbc6adf6c2d6eb9ed78a4fa289',
                auth_token='test_6a8d674054ab057ae04632524cf', endpoint='https://test.instamojo.com/api/1.1/')


@ app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        response = api.payment_request_create(
            amount='5000',
            purpose='Covid19 Relief',
            send_email=True,
            email="sunny.shankar44@gmail.com",
            redirect_url=url_for('verification', _external=True),
        )
        return redirect(response['payment_request']['longurl'])

    return render_template('index.html')


@app.route('/verification')
def verification():
    return render_template('verification.html')


if __name__ == '__main__':
    app.run(debug=True)
