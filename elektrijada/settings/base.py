# -*- coding: utf-8 -*-
"""
Django settings for embassy project.
"""
from django.conf.global_settings import STATICFILES_FINDERS, TEMPLATE_CONTEXT_PROCESSORS
from django.core.urlresolvers import reverse_lazy
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

SECRET_KEY = 'dev_key_uV|56/2554#Y^y$'

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'bootstrapform',
    'tinymce',
    'compressor',
    'endless_pagination',
    'django_extensions',
    'django_reset',

    'django.contrib.admin',

    'elektrijada',
    'zivotopis',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'elektrijada.urls'

WSGI_APPLICATION = 'elektrijada.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'sqlite.db'),
    }
}

# Internationalization

LANGUAGE_CODE = 'hr-hr'
# LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Zagreb'
USE_I18N = True
USE_L10N = True
DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y H:i'
DATE_INPUT_FORMATS = ('%d.%m.%Y', '%d.%m.%Y.',)
DATETIME_INPUT_FORMATS = ('%d.%m.%Y %H:%M', '%d.%m.%Y. %H:%M')
USE_TZ = True

# Static, media files (CSS, JavaScript, Images)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

SITE_ID = 1

SESSION_COOKIE_AGE = 1209600    # two weeks in seconds

# Every RequestContext will contain a variable request, required for admin dashboard
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)

# Custom settings

GRAPPELLI_ADMIN_TITLE = '<a href="/">Elektrijada</a>'
GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

# Main FileBrowser Directory 'uploads/'. Leave empty in order to browse all from MEDIA_ROOT
FILEBROWSER_DIRECTORY = 'uploads/'
FILEBROWSER_DIRECTORY = ''
FILEBROWSER_DEFAULT_SORTING_BY = 'filename_lower'

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (60px)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (140px)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (300px)', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (460px)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (680px)', 'width': 680, 'height': '', 'opts': ''},
}
# Versions available within the Admin-Interface.
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'big', 'large']
# Which Version should be used as Admin-thumbnail.
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'

FILEBROWSER_SELECT_FORMATS = {
    'File': ['Folder', 'Document'],
    'Image': ['Folder', 'Image'],
    'Media': ['Video', 'Sound'],
    'Document': ['Document'],
    # for TinyMCE we can also define lower-case items
    'image': ['Image'],
    'file': ['Folder', 'Image', 'Document'],
}

# tinymce settings, add/remove buttons and so on
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_resizing': True,
    'plugins': 'table,contextmenu,paste,autoresize,media,lists,style',
    # 'height': 600,
    # 'width': 800,
    'theme_advanced_buttons1': ('formatselect,style,bold,italic,underline,separator,bullist,separator,outdent,'
                                'indent,separator,undo,redo'),
    'theme_advanced_buttons2': 'cleanup,code,separator,lists,pasteword,table,contextmenu,media,style,image,link',
    # 'theme_advanced_buttons3': '',
}

LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')
LOGIN_REDIRECT_URL = '/'

ENDLESS_PAGINATION_PER_PAGE = 20
ENDLESS_PAGINATION_DEFAULT_CALLABLE_ARROWS = False
ENDLESS_PAGINATION_NEXT_LABEL = u'»'
ENDLESS_PAGINATION_PREVIOUS_LABEL = u'«'
