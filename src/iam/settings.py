import os
import environ

from pathlib import Path


env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=list,
)
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'rest_framework',
    'djoser',
    'oauth2_provider',
    'social_django',
    'drf_yasg',

    'core',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "iam.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "iam.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")


# Auth-related settings

AUTH_USER_MODEL = 'core.User'

SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['user_id']
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['email']

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

# https://python-social-auth.readthedocs.io/en/latest/pipeline.html#pipeline
SOCIAL_AUTH_PIPELINE = (
    'core.pipeline.check_user_allowed',
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'core.pipeline.associate_by_user_id',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('GOOGLE_OAUTH2_KEY')
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('GOOGLE_OAUTH2_SECRET')
# SOCIAL_AUTH_FACEBOOK_KEY = env('FACEBOOK_KEY')
# SOCIAL_AUTH_FACEBOOK_SECRET = env('FACEBOOK_SECRET')
# SOCIAL_AUTH_TWITTER_KEY = env('TWITTER_KEY')
# SOCIAL_AUTH_TWITTER_SECRET = env('TWITTER_SECRET')
# SOCIAL_AUTH_INSTAGRAM_KEY = env('INSTAGRAM_KEY')
# SOCIAL_AUTH_INSTAGRAM_SECRET = env('INSTAGRAM_SECRET')
# SOCIAL_AUTH_SPOTIFY_KEY = env('SPOTIFY_KEY')
# SOCIAL_AUTH_SPOTIFY_SECRET = env('SPOTIFY_SECRET')
# SOCIAL_AUTH_SOUNDCLOUD_KEY = env('SOUNDCLOUD_KEY')
# SOCIAL_AUTH_SOUNDCLOUD_SECRET = env('SOUNDCLOUD_SECRET')
# SOCIAL_AUTH_TWITCH_KEY = env('TWITCH_KEY')
# SOCIAL_AUTH_TWITCH_SECRET = env('TWITCH_SECRET')
# SOCIAL_AUTH_TUMBLR_KEY = env('TUMBLR_KEY')
# SOCIAL_AUTH_TUMBLR_SECRET = env('TUMBLR_SECRET')
# SOCIAL_AUTH_PINTEREST_KEY = env('PINTEREST_KEY')
# SOCIAL_AUTH_PINTEREST_SECRET = env('PINTEREST_SECRET')
