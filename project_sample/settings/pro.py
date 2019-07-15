import json
from .default import *


DEBUG = False

with open(REPOSITORY_ROOT + "/config/auth.json") as auth_file:
    AUTH_TOKENS = json.load(auth_file)

DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': "projectsample",
          'HOST': AUTH_TOKENS['mysql']['host'],
          'PORT': AUTH_TOKENS['mysql']['port'],
          'USER': AUTH_TOKENS['mysql']['user'],
          'PASSWORD': AUTH_TOKENS['mysql']['password'],
      }
}
