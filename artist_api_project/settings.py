# artist_api_project/settings.py

INSTALLED_APPS = [
    # ...
    'rest_framework',
    'rest_framework.authtoken',
    'artist_api',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
