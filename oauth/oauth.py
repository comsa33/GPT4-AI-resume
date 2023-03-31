import json
from flask import redirect, request
import requests

from data import settings


def auth_callback():
    error = request.args.get('error')
    if error:
        return f'Error: {error}'

    auth_code = request.args.get('code')
    state = request.args.get('state')

    if state != 'random_string_for_csrf_protection':
        return 'Invalid state'

    payload = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': settings.REDIRECT_URI,
        'client_id': settings.LINKEDIN_CLIENT_ID,
        'client_secret': settings.LINKEDIN_CLIENT_SECRET
    }
    response = requests.post(settings.TOKEN_URL, data=payload)
    response_data = response.json()

    if response.status_code != 200:
        return f'Error: {response_data}'

    access_token = response_data['access_token']

    # Get user's full profile information
    headers = {'Authorization': f'Bearer {access_token}'}
    profile_response = requests.get(settings.PROFILE_URL, headers=headers)

    if profile_response.status_code != 200:
        return f"Error fetching profile data: {profile_response.content}"

    profile_data = profile_response.json()

    return json.dumps(profile_data)
