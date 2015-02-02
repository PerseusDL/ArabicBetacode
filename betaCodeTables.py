# The file includes three conversion tables.

# One-to-one transliteration for computational research
# - main principle: one Arabic character = one Latin character
# - understandable for Arabists, but has some unconventional symbols
betacodeTranslit = {
# Alphabet letters
    '_a' : 'ā', # alif
    'b'  : 'b', # bā’
    't'  : 't', # tā’
    '_t' : 'ṯ', # thā’
    '^g' : 'ǧ', # jīm
    'j'  : 'ǧ', # jīm
    '^c' : 'č', # chīm / Persian
    '*h' : 'ḥ', # ḥā’
    '.h' : 'ḥ', # ḥā’
    '_h' : 'ḫ', # khā’
    'd'  : 'd', # dāl
    '_d' : 'ḏ', # dhāl
    'r'  : 'r', # rā’
    'z'  : 'z', # zayn
    's'  : 's', # sīn
    '^s' : 'š', # shīn
    '*s' : 'ṣ', # ṣād
    '.s' : 'ṣ', # ṣād
    '*d' : 'ḍ', # ḍād
    '.d' : 'ḍ', # ḍād
    '*t' : 'ṭ', # ṭā’
    '.t' : 'ṭ', # ṭā’
    '*z' : 'ẓ', # ẓā’
    '.z' : 'ẓ', # ẓā’
    '`'  : 'ʿ', # ‘ayn
    '*g' : 'ġ', # ghayn
    '.g' : 'ġ', # ghayn
    'f'  : 'f', # fā’
    '*k' : 'ḳ', # qāf
    '.k' : 'ḳ', # qāf
    'q'  : 'ḳ', # qāf
    'k'  : 'k', # kāf
    'g'  : 'g', # gāf / Persian
    'l'  : 'l', # lām
    'm'  : 'm', # mīm
    'n'  : 'n', # nūn
    'h'  : 'h', # hā’
    'w'  : 'w', # wāw
    '_u' : 'ū', # wāw
    'y'  : 'y', # yā’
    '_i' : 'ī', # yā’
# Non-alphabetic letters
    '\'' : 'ʾ', # hamza
    '/a' : 'á', # alif maqṣūrah
    ':t' : 'ŧ', # tā’ marbūṭah
# Vowels
    '~a' : 'ã', # dagger alif
    'a'  : 'a', # fatḥah
    'u'  : 'u', # ḍammah
    'i'  : 'i', # kasrah
    }

# conventional US/LOC transliteration
translitLOC = {
# Alphabet letters
    'ā' : 'ā',  # alif
    'b' : 'b',  # bā’
    't' : 't',  # tā’
    'ṯ' : 'th', # thā’
    'ǧ' : 'j',  # jīm
    'č' : 'ch', # chīm / Persian
    'ḥ' : 'ḥ',  # ḥā’
    'ḫ' : 'kh', # khā’
    'd' : 'd',  # dāl
    'ḏ' : 'dh', # dhāl
    'r' : 'r',  # rā’
    'z' : 'z',  # zayn
    's' : 's',  # sīn
    'š' : 'sh', # shīn
    'ṣ' : 'ṣ',  # ṣād
    'ḍ' : 'ḍ',  # ḍād
    'ṭ' : 'ṭ',  # ṭā’
    'ẓ' : 'ẓ',  # ẓā’
    'ʿ' : 'ʿ',   # ‘ayn
    'ġ' : 'gh', # ghayn
    'f' : 'f',  # fā’
    'ḳ' : 'q',  # qāf
    'k' : 'k',  # kāf
    'g' : 'g',  # gāf / Persian
    'l' : 'l',  # lām
    'm' : 'm',  # mīm
    'n' : 'n',  # nūn
    'h' : 'h',  # hā’
    'w' : 'w',  # wāw
    'ū' : 'u',  # wāw
    'y' : 'y',  # yā’
    'ī' : 'i',  # yā’
# Non-alphabetic letters
    'ʾ' : 'ʾ',   # hamza
    'á' : 'ā',  # alif maqṣūrah
    'ŧ' : 'h',  # tā’ marbūṭah
# Vowels
    'ã' : 'ā',  # dagger alif
    'a' : 'a',  # fatḥah
    'u' : 'u',  # ḍammah
    'i' : 'i',  # kasrah
    }

# necessary for rendering searcheable lines
translitSearch = {
# Alphabet letters
    'ā' : 'a',  # alif
    'b' : 'b',  # bā’
    't' : 't',  # tā’
    'ṯ' : 'th', # thā’
    'ǧ' : 'j',  # jīm
    'č' : 'ch', # chīm / Persian
    'ḥ' : 'h',  # ḥā’
    'ḫ' : 'kh', # khā’
    'd' : 'd',  # dāl
    'ḏ' : 'dh', # dhāl
    'r' : 'r',  # rā’
    'z' : 'z',  # zayn
    's' : 's',  # sīn
    'š' : 'sh', # shīn
    'ṣ' : 's',  # ṣād
    'ḍ' : 'd',  # ḍād
    'ṭ' : 't',  # ṭā’
    'ẓ' : 'z',  # ẓā’
    'ʿ' : '',   # ‘ayn
    'ġ' : 'gh', # ghayn
    'f' : 'f',  # fā’
    'ḳ' : 'q',  # qāf
    'k' : 'k',  # kāf
    'g' : 'g',  # gāf / Persian
    'l' : 'l',  # lām
    'm' : 'm',  # mīm
    'n' : 'n',  # nūn
    'h' : 'h',  # hā’
    'w' : 'w',  # wāw
    'ū' : 'u',  # wāw
    'y' : 'y',  # yā’
    'ī' : 'i',  # yā’
# Non-alphabetic letters
    'ʾ' : '',   # hamza
    'á' : 'a',  # alif maqṣūrah
    'ŧ' : 'h',  # tā’ marbūṭah
# Vowels
    'ã' : 'a',  # dagger alif
    'a' : 'a',  # fatḥah
    'u' : 'u',  # ḍammah
    'i' : 'i',  # kasrah
    }
