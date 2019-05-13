---
use_ssl: false
django_env:
    SECRET_KEY: 'vOf6iVRhpjjMQaMrp/VlAIr0Mqsh31g145IMDXa0ePolkBaFiBCrdcl8DEMc5EVci+ret8XA9H2mvTmaYfpHtQ'
    DJANGO_SETTINGS_MODULE: website_wagtail.settings.production
    HOST_NAME: staging.jazminleon.com
    DB_USER: xgbeuybg
    DB_PASSWD: Infinity0802
    DB_HOST: 12.0.0.1
    DB_NAME: website_wagtail_db 
    EMAIL_HOST: 'smtp.gmail.com'
    EMAIL_FROM: 'noreply@jazminleon.com'
    EMAIL_USER: 'jazmin@jazminleon.com'
    EMAIL_PASSWD: 'PawPaw378'
    DJANGO_ADMIN_USER: 'jleon1521'
    DJANGO_ADMIN_PASSWD: 'KMLLCAa@0802'

