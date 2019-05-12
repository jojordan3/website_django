use_ssl: false

django_env:
    DJANGO_SETTINGS_MODULE: website_wagtail.settings.production
    HOST_NAME: jazminleon.com
    DB_USER: xgbeuybg
    DB_PASSWD: 'qfhy49e22tz8'
    DB_HOST: localhost
    DB_NAME: website_wagtail_db 
    EMAIL_HOST: 'email_host'
    EMAIL_FROM: 'support@chrisdev.com'
    EMAIL_USER: 'email_user'
    EMAIL_PASSWD: 'email_passwd'
    DJANGO_ADMIN_USER: 'jleon1521'
    DJANGO_ADMIN_EMAIL: 'admin@host.com' 
    DJANGO_ADMIN_PASSWD: 'hwt0cr2qhqav'
