from conf_packages.settings_for_all import *


def getting_link(text_from_user):
    try:
        page_py = wiki_wiki.page(text_from_user.lower())
        return page_py
    except Exception as error:
        print(error)
        return error
