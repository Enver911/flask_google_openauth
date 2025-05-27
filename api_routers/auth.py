from flask import Blueprint, redirect, request, jsonify
from werkzeug.urls import urlsplit
from config.config import config_parser
import requests

router = Blueprint('auth', __name__)

client_id = config_parser.get('GOOGLE_CLIENT', 'client_id')
client_secret = config_parser.get('GOOGLE_CLIENT', 'client_secret')
redirect_uri = config_parser.get('GOOGLE_CLIENT', 'redirect_uri')

google_oauth2_api = config_parser.get('GOOGLE_API', 'google_oauth2_api')
user_token_api = config_parser.get('GOOGLE_API', 'user_token_api')
user_info_api = config_parser.get('GOOGLE_API', 'user_info_api')


@router.get('/oauth/google-oauth2/authentication')
def google_oauth2_authentication(*args, **kwargs):
    """Redirect to google oauth2 authentication api"""

    auth_url = (
        f'{google_oauth2_api}?client_id={client_id}'
        f'&redirect_uri={redirect_uri}'
        f'&response_type=code'
        f'&scope=openid%20email%20profile'
    )

    return redirect(auth_url)


@router.get(urlsplit(redirect_uri).path)
def google_oauth2_authorization(*args, **kwargs):
    """Callback after success google oauth2 authentication"""
    code = request.args.get('code')

    token_data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }

    response = requests.post(user_token_api, data=token_data)

    # authenticated user access token
    access_token = response.json().get('access_token')

    user_info = requests.get(user_info_api, headers={"Authorization": f"Bearer {access_token}"}).json()

    # then you can register or log in user with returned info and return some cookie or token
    return jsonify(user_info)
