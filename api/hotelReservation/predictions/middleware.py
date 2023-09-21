# ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True