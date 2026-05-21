from flask import g, request, make_response, redirect
from .translations import SUPPORTED_LANGS, DEFAULT_LANG, RTL_LANGS, LANG_NAMES
from .translations import t as _t, tdb as _tdb

COOKIE_NAME = 'roloband_lang'


def init_i18n(app):
    @app.route('/set-lang/<lang>')
    def set_lang(lang):
        if lang not in SUPPORTED_LANGS:
            lang = DEFAULT_LANG
        referrer = request.referrer or '/'
        resp = make_response(redirect(referrer))
        resp.set_cookie(COOKIE_NAME, lang, max_age=60 * 60 * 24 * 365, samesite='Lax')
        return resp

    @app.before_request
    def detect_lang():
        lang = request.cookies.get(COOKIE_NAME, DEFAULT_LANG)
        if lang not in SUPPORTED_LANGS:
            lang = DEFAULT_LANG
        g.lang = lang
        g.is_rtl = lang in RTL_LANGS

    @app.context_processor
    def inject_i18n():
        lang = getattr(g, 'lang', DEFAULT_LANG)

        def translate(key):
            return _t(key, lang)

        def translate_db(text):
            return _tdb(text, lang)

        return {
            't':            translate,
            'tdb':          translate_db,
            'current_lang': lang,
            'is_rtl':       getattr(g, 'is_rtl', False),
            'supported_langs': SUPPORTED_LANGS,
            'lang_names':   LANG_NAMES,
        }
