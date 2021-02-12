from secrets import token_urlsafe


class Config:
    SECRET_KEY = token_urlsafe(32)
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'


class Production(Config):
    WTF_CSRF_SECRET_KEY = token_urlsafe(32)
    WTF_CSRF_ENABLED = True
    DEBUG = False
    FLASK_DEBUG_DISABLE_STRICT = True
    BOOTSTRAP_CDN_FORCE_SSL = True


class Debug(Config):
    WTF_CSRF_ENABLED = False
    DEBUG = True
    TESTING = True
