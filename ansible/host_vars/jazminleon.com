use_ssl: false
le_admin_email: jazmin@jazminleon.com
django_env:
    DJANGO_SETTINGS_MODULE: website_wagtail.settings.production
    HOST_NAME: jazminleon.com
    DB_USER: xgbeuybg_jazminleon
    DB_PASSWD: 'Infinity0802'
    DB_HOST: 12.0.0.1
    DB_NAME: xgbeuybg_jazminleon_db 
    EMAIL_HOST: 'smtp.gmail.com'
    EMAIL_FROM: 'noreply@jazminleon.com'
    EMAIL_USER: 'jazmin@jazminleon.com'
    EMAIL_PASSWD: 'PawPaw378'
    DJANGO_ADMIN_USER: 'jleon1521'
    DJANGO_ADMIN_EMAIL: 'jazmin@jazminleon.com' 
    DJANGO_ADMIN_PASSWD: 'KMLLCAa@0802'
