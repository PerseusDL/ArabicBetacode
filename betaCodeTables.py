# Including some variations (*h and .h --- are the same)
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

# From Wikipedia
"""
Arabic letters usage in Literary Arabic
Name	Translit	Value (IPA)	Contextual forms	Isolated
Final	Medial	Initial
alif	ā /  ’  (also  ʾ  )	various,
including /aː/ [a]	ـا	ـا	ا	ا
bā’	b	/b/
(sometimes /p/ in loanwords)[b]	ـب	ـبـ	بـ	ب
tā’	t	/t/	ـت	ـتـ	تـ	ت
thā’	th (also ṯ )	/θ/	ـث	ـثـ	ثـ	ث
jīm	j (also ǧ, g)	[d͡ʒ] ~ [ʒ] ~ [ɡ] [c]	ـج	ـجـ	جـ	ج
ḥā’	ḥ	/ħ/	ـح	ـحـ	حـ	ح
khā’	kh (also ḫ, ḵ )	/x/	ـخ	ـخـ	خـ	خ
dāl	d	/d/	ـد	ـد	د	د
dhāl	dh (also ḏ )	/ð/	ـذ	ـذ	ذ	ذ
rā’ / rāy / rays	r	/r/	ـر	ـر	ر	ر
zayn / zāy / zā’	z	/z/	ـز	ـز	ز	ز
sīn	s	/s/	ـس	ـسـ	سـ	س
shīn	sh (also š )	/ʃ/	ـش	ـشـ	شـ	ش
ṣād	ṣ	/sˤ/	ـص	ـصـ	صـ	ص
ḍād	ḍ	/dˤ/	ـض	ـضـ	ضـ	ض
ṭā’	ṭ	/tˤ/	ـط	ـطـ	طـ	ط
ẓā’	ẓ	[ðˤ] ~ [zˤ]	ـظ	ـظـ	ظـ	ظ
‘ayn	 ‘  (also  ʿ  )	/ʕ/	ـع	ـعـ	عـ	ع
ghayn	gh (also ġ, ḡ )	/ɣ/
(sometimes /ɡ/ in loanwords)[c]	ـغ	ـغـ	غـ	غ
fā’	f	/f/
(sometimes /v/ in loanwords)[b]	ـف	ـفـ	فـ	ف [d]
qāf	q	/q/
(sometimes /ɡ/ in loanwords)[c]	ـق	ـقـ	قـ	ق [d]
kāf	k	/k/
(sometimes /ɡ/ in loanwords)[c]	ـك	ـكـ	كـ	ك
gāf	g	/g/	ـگ	ـگـ	گـ	گ
lām	l	/l/	ـل	ـلـ	لـ	ل
mīm	m	/m/	ـم	ـمـ	مـ	م
nūn	n	/n/	ـن	ـنـ	نـ	ن
hā’	h	/h/	ـه	ـهـ	هـ	ه
wāw	w / ū / aw	/w/, /uː/, /aw/,
sometimes /u/, /o/, and /oː/ in loanwords	ـو	ـو	و	و
yā’	y / ī / ay	/j/, /iː/, /aj/,
sometimes /i/, /e/, and /eː/ in loanwords	ـي	ـيـ	يـ	ي [e]
"""
