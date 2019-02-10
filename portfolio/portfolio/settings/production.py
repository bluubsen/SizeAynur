from .base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "anyurotyakmaz",
        "USER": "aynur",
        "PASSWORD": "s8231823812h3h",
        "HOST": "127.0.0.1",
        "PORT": "",
    }
}

FILE_UPLOAD_PERMISSIONS = 0o644

ALLOWED_HOSTS = ["aynurotyakmaz.com", "www.aynurotyakmaz.com"]

ADMINS = [('Dylan Peter Hayward', "dylanpeterhayward@gmail.com")]
SERVER_EMAIL = '"Mr. Robot" <serverbot@transmitter-berlin.de>'

FABRIC = {
    "DEPLOY_TOOL": "rsync",  # Deploy with "git", "hg", or "rsync"
    "SSH_USER": "dylan",  # VPS SSH username
    "HOSTS": ["188.166.22.191"],  # The IP address of your VPS
    "DOMAINS": ["aynurotyakmaz.com",
                "www.aynurotyakmaz.com"],
    "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
    "LOCALE": "en_US.UTF-8",  # Should end with ".UTF-8"
    "DB_PASS": "asku873FF!mnopABBA",  # Live database password
    "ADMIN_LOGIN": "dylan",  # Custom settings entry.
    "ADMIN_PASS": "sj9878243GKK$$$mniqq",  # Live admin user password
}
