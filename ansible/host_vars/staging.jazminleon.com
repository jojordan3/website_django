---
use_ssl: false
django_env:
    SECRET_KEY: your_secret_key 
    DJANGO_SETTINGS_MODULE: website_wagtail.settings.production
    HOST_NAME: staging.jazminleon.com
    DB_USER: django
    DB_PASSWD: change_db_password!!!
    DB_HOST: localhost
    DB_NAME: website_wagtail_db 
    EMAIL_HOST: 'email_host'
    EMAIL_FROM: 'support@chrisdev.com'
    EMAIL_USER: 'email_user'
    EMAIL_PASSWD: 'email_passwd'
    DJANGO_ADMIN_USER: jleon1521
    DJANGO_ADMIN_PASSWD: 'your_admin_password'

