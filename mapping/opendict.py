import webbrowser


DICTS = {"zdict": "http://www.zdic.net/hans/",
         "tw": "https://stroke-order.learningweb.moe.edu.tw/charactersQueryResult.do?words=",
         "moedict": "https://www.moedict.tw/",
         "arch": "https://www.archchinese.com/chinese_english_dictionary.html?find="}


def open_dict(url, char):
    """ Open a chinese dictionary on the default web browser to see the stroke order
        of a character

    Parameters
    ----------
    url : str
        Url to a chinese dictionary/stroke order page or
        a key to a default dictionary defined in DICTS
    char : str
        Character to open on the  dictionary

    """
    if url == None:
        return
    elif url not in DICTS.keys():
        webbrowser.open(url + char)
    else:
        webbrowser.open(DICTS[url] + char)
    return
    
