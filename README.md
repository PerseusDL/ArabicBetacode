# Arabic betaCode

 Although both Windows and Mac OS now support Arabic, it is still quite difficult to type and edit Arabic texts. In particular, it is extremely difficult to edit and manipulate fully vocalized texts, since most fonts either render “short vowels” (*ḥarakāt*) invisible, or do not render them properly. Moreover, because of the “stacking,” i.e. when “short vowels” are placed on top of each other, it becomes impossible to edit texts, one is forced to delete and re-type, rather then to edit (and still, because of visual issues, there is no guarantee that all the letters and “short vowels” are actually in the right order). **betaCode** can help to make typing fully-vocalized Arabic texts possible and easy on any machine and render it into various transliteration conventions and into Arabic script (scroll below for examples). 

**betaCode** is first converted into a one-to-one transliteration scheme (the one to rule them all), which combines one-to-one transliteration conventions from major academic transliteration schemes. Such scheme is necessary, since none of the existing academic transliteration schemes (American/Library of Congress, British, French, German) allow to represent Arabic text unambiguously for computational purposes. Arabic **betaCode** transliteration can be then converted into any transliteration conventions. At the moment the following schemes are implemented (not yet fully):

* Library of Congress Romanization of Arabic
* Simplified transliteration (essentially, LOC but with diacritics removed)
* Arabic script (*hamzaŧ* orthography rules are not implemented yet)

**NB:** The idea of **betaCode** is borrowed from the Classicists who developed ["a method of representing, using only ASCII characters, characters and formatting found in ancient Greek texts"](http://en.wikipedia.org/wiki/Beta_Code). The current **betaCode** is inspired by, and is therefore quite similar to, the [arabTex scheme](http://www2.informatik.uni-stuttgart.de/ivi/bs/research/arab_e.htm).

## Basic principles of *betaCode*:
Every Arabic letter is betaCoded with its one-letter equivalent (thus pulling from different academic transliteration schemes),
preceded (if necessary) with a technical symbol that is similar to a diacritical mark in the transliterated version. Thus, most common symbols are as follows:

* **\_** (underscore), if letter can be transliterated with *macron*/*breve* below or above (ā, ṯ, ḫ, ḏ, ū, ī)
* **.** (period), or  <b>\*</b> (asterisk), if letter can be transliterated transliterated with *dot* below or above (ḥ, ṣ, ḍ, ṭ, ẓ, ġ, ḳ)
* **^** (caret), if letter can be transliterated with *caron* (ǧ, š)
* plus some new combinations (scroll down for the complete table)

## Running the converter
* clone the repository
* save texts that must be transliterated (i.e., the text is in English, but has some Arabic terms that must be transliterated) into “./to\_translit” (follow the format of given in the example file).
* save texts that must be fully transliterated or/and converted into Arabic script (i.e., the entire texts is in Arabic) into “./to_arabic/” (follow the format given in the example file).
* run the script “\_generateBetaCode.py”.
* converted texts (in all available modes of conversion) will be automatically added after the betaCoded texts.
* if you need to make any changes, edit your initial betaCoded text and run the script again, converted results will be replaced with updated versions.

## betaCode and One-To-One Transliteration

| betacode | translit | Arabic letter |
|----------|-----------------|---------------|
| **\_a** | ā | *alif* |
| **b** | b | *bā’* |
| **t** | t | *tā’* |
| **\_t** | ṯ | *thā’* |
| **^g, j** | ǧ | *jīm* |
| **\*h, .h** | ḥ | *ḥā’* |
| **\_h** | ḫ | *khā’* |
| **d** | d | *dāl* |
| **\_d** | ḏ | *dhāl* |
| **r** | r | *rā’* |
| **z** | z | *zayn* |
| **s** | s | *sīn* |
| **^s** | š | *shīn* |
| **\*s, .s** | ṣ | *ṣād* |
| **\*d, .d** | ḍ | *ḍād* |
| **\*t, .t** | ṭ | *ṭā’* |
| **\*z, .z** | ẓ | *ẓā’* |
| **`** | ʿ | *‘ayn* |
| **\*g, .g** | ġ | *ghayn* |
| **f** | f | *fā’* |
| **\*k, .k, q** | ḳ | *qāf* |
| **k** | k | *kāf* |
| **l** | l | *lām* |
| **m** | m | *mīm* |
| **n** | n | *nūn* |
| **h** | h | *hā’* |
| **w** | w | *wāw* |
| **\_u** | ū | *wāw* |
| **y** | y | *yā’* |
| **\_i** | ī | *yā’* |

## Non-alphabetic letters
| **betacode** | translit | Arabic |
|----------|-----------------|---------------|
| **'** | ʾ | *hamzaŧ* |
| **/a** | á | *alif maqṣūraŧ* |
| **:t** | ŧ | *tā’ marbūṭaŧ* |

## Vowels

| **betacode** | translit | Arabic |
|----------|-----------------|---------------|
| **~a** | ã | *dagger alif* |
| **a** | a | *fatḥaŧ* |
| **u** | u | *ḍammaŧ* |
| **i** | i | *kasraŧ* |
| **.n** | ȵ | *n of tanwīn* |
| **.a** | å | *silent alif* |
| **.w** | ů | *silent wāw* |

## Additional *betaCode* rules

* vowel case endings add "_", i.e.:
	* ``` f_i al-kit_abi_ ```, but not:
	* ``` f_i al-kit_abi.n ``` (all *tanwīn kasr* and *tanwīn ḍamm* will be automatically removed from transliterated versions)
* attached prepositions/conjunctions must be separated with "-", i.e.:
	* ``` bi-Llahi_ ```
	* ``` fa-_dahaba_ ```
* *tāʾ marbūṭaŧ*: add "+" after *tāʾ marbūṭaŧ*, if the first word of *iḏāfaŧ*
	* ``` `_amma:t+u Ba.gd_ada ```, but:
	* ``` al-`_amma:tu f_i Ba.gd_ada ```
* more to be added...


# Examples 

## betaCode into Arabic

NB: These are examples of converting betaCode to full transliteration and Arabic script. The very last paragraph showcases conversion of hamza in different positions.

```
q_ala 'ab_u Mas`_udi.n :: 'an_a qad sami`tu h~a_d_a min ras_uli All~ahi ( .sl`m )

.hadda_ta-n_a `Amru.w bnu R_afi`i.n , .hadda_ta-n_a `Abdu All~ahi bnu al-Mub_araki , `an Mu.hammadi bni 'is.h_aqa , `an Mu.hammadi bni ^Ga`fari.n , `an `Ubaydi All~ahi bni `Abdi All~ahi bni `Umara , `an 'Ab_i-hi , `ani al-nabiyyi ( .sl`m ) na.hwa-hu

'a_hbara-n_a Qutayba:tu q_ala , .hadda_ta-n_a Sufy_anu , `an Ya.hy/a bni Sa`_idi.n , `an 'Ab_i Bakri bni Mu.hammadi.n , `an `Umara bni `Abdi al-`Az_izi , `an 'Ab_i Bakri bni `Abdi al-Ra.hm~ani bni al-.H_ari_ti bni Hi^s_ami.n , `an 'Ab_i Hurayra:ta mi_tla-hu

Ta.hw_ilu al-.hamza:ti ( kalim_atu.n mufrada:tu.n )

'amru.n 'unsu.n 'insu.n '_im_anu.n
'_aya:tu.n '_amana mas'ala:tu.n sa'ala ra'su.n qur'_anu.n ta'_amara
_di'bu.n as'ila:tu.n q_ari'i-hi su'lu.n mas'_ulu.n
tak_afu'u-hu su'ila q_ari'i-hi _di'_abu.n ra'_isu.n
bu'isa ru'_ufu.n ra'_ufu.n su'_alu.n mu'arri_hu.n
abn_a'a-hu abn_a'u-hu abn_a'i-hi ^say'a.n _ha.t_i'a:tu.n
.daw'u-hu .d_u'u-hu .daw'a-hu .daw'i-hi mur_u'a:tu.n
'abn_a'i-hi bar_i'u-hu s_u'ila f_ilu.n f_annu.n f_unnu.n
s_a'ala fu'_adu.n ^surak_a'u-hu ri'_asa:tu.n tahni'a:tu.n
daf_a'a:tu.n .taff_a'a:tu.n ta'r_i_hu.n fa'ru.n
^say'u.n ^say'i.n ^say'a.n  .daw'u.n .daw'i.n .daw'a.n
juz'u.n  juz'i.n  juz'a.n mabda'u.n mabda'i.n mabda'a.n
naba'a q_ari'u.n tak_afu'u.n tak_afu'i.n tak_afu'a.n
abn_a'u abn_a'i abn_a'a jar_i'u.n maqr_u'u.n .daw'u.n ^say'u.n juz'u.n
`ulam_a'u al-`ulam_a'i al-`ulam_a'a `Amru.n.w wa-fa`al_u.a
```

## BETACODE#TO#ONE#TO#ONE###

ḳāla ʾabū Masʿūdiȵ :: ʾanā ḳad samiʿtu hãḏā min rasūli Allãhi ( ṣlʿm )

ḥaddaṯa-nā ʿAmruů bnu Rāfiʿiȵ , ḥaddaṯa-nā ʿAbdu Allãhi bnu al-Mubāraki , ʿan Muḥammadi bni ʾisḥāḳa , ʿan Muḥammadi bni Ǧaʿfariȵ , ʿan ʿUbaydi Allãhi bni ʿAbdi Allãhi bni ʿUmara , ʿan ʾAbī-hi , ʿani al-nabiyyi ( ṣlʿm ) naḥwa-hu

ʾaḫbara-nā Ḳutaybaŧu ḳāla , ḥaddaṯa-nā Sufyānu , ʿan Yaḥyá bni Saʿīdiȵ , ʿan ʾAbī Bakri bni Muḥammadiȵ , ʿan ʿUmara bni ʿAbdi al-ʿAzīzi , ʿan ʾAbī Bakri bni ʿAbdi al-Raḥmãni bni al-Ḥāriṯi bni Hišāmiȵ , ʿan ʾAbī Hurayraŧa miṯla-hu

Taḥwīlu al-ḥamzaŧi ( kalimātuȵ mufradaŧuȵ )

ʾamruȵ ʾunsuȵ ʾinsuȵ ʾīmānuȵ
ʾāyaŧuȵ ʾāmana masʾalaŧuȵ saʾala raʾsuȵ ḳurʾānuȵ taʾāmara
ḏiʾbuȵ asʾilaŧuȵ ḳāriʾi-hi suʾluȵ masʾūluȵ
takāfuʾu-hu suʾila ḳāriʾi-hi ḏiʾābuȵ raʾīsuȵ
buʾisa ruʾūfuȵ raʾūfuȵ suʾāluȵ muʾarriḫuȵ
abnāʾa-hu abnāʾu-hu abnāʾi-hi šayʾaȵ ḫaṭīʾaŧuȵ
ḍawʾu-hu ḍūʾu-hu ḍawʾa-hu ḍawʾi-hi murūʾaŧuȵ
ʾabnāʾi-hi barīʾu-hu sūʾila fīluȵ fānnuȵ fūnnuȵ
sāʾala fuʾāduȵ šurakāʾu-hu riʾāsaŧuȵ tahniʾaŧuȵ
dafāʾaŧuȵ ṭaffāʾaŧuȵ taʾrīḫuȵ faʾruȵ
šayʾuȵ šayʾiȵ šayʾaȵ  ḍawʾuȵ ḍawʾiȵ ḍawʾaȵ
ǧuzʾuȵ  ǧuzʾiȵ  ǧuzʾaȵ mabdaʾuȵ mabdaʾiȵ mabdaʾaȵ
nabaʾa ḳāriʾuȵ takāfuʾuȵ takāfuʾiȵ takāfuʾaȵ
abnāʾu abnāʾi abnāʾa ǧarīʾuȵ maḳrūʾuȵ ḍawʾuȵ šayʾuȵ ǧuzʾuȵ
ʿulamāʾu al-ʿulamāʾi al-ʿulamāʾa ʿAmruȵů wa-faʿalūå
```

## TRANSLIT#TO#ARABIC#SCRIPT##

```
قَالَ أَبُو مَسْعُودٍ :: أَنَا قَدْ سَمِعْتُ هٰذَا مِنْ رَسُولِ ﭐلـلّٰـهِ ( صْلْعْمْ )

حَدَّثَنَا عَمْرُو بْنُ رَافِعٍ ، حَدَّثَنَا عَبْدُ ﭐلـلّٰـهِ بْنُ ﭐلْمُبَارَكِ ، عَنْ مُحَمَّدِ بْنِ إِسْحَاقَ ، عَنْ مُحَمَّدِ بْنِ جَعْفَرٍ ، عَنْ عُبَيْدِ ﭐلـلّٰـهِ بْنِ عَبْدِ ﭐلـلّٰـهِ بْنِ عُمَرَ ، عَنْ أَبِيهِ ، عَنِ ﭐلنَّبِيِّ ( صْلْعْمْ ) نَحْوَهُ

أَخْبَرَنَا قُتَيْبَةُ قَالَ ، حَدَّثَنَا سُفْيَانُ ، عَنْ يَحْيٰى بْنِ سَعِيدٍ ، عَنْ أَبِي بَكْرِ بْنِ مُحَمَّدٍ ، عَنْ عُمَرَ بْنِ عَبْدِ ﭐلْعَزِيزِ ، عَنْ أَبِي بَكْرِ بْنِ عَبْدِ ﭐلرَّحْمٰنِ بْنِ ﭐلْحَارِثِ بْنِ هِشَامٍ ، عَنْ أَبِي هُرَيْرَةَ مِثْلَهُ

تَحْوِيلُ ﭐلْحَمْزَةِ ( كَلِمَاتٌ مُفْرَدَةٌ )

أَمْرٌ أُنْسٌ إِنْسٌ إِيمَانٌ
آيَةٌ آمَنَ مَسْأَلَةٌ سَأَلَ رَأْسٌ قُرْآنٌ تَآمَرَ
ذِئْبٌ أَسْئِلَةٌ قَارِئِهِ سُؤْلٌ مَسْؤُولٌ
تَكَافُؤُهُ سُئِلَ قَارِئِهِ ذِئَابٌ رَئِيسٌ
بُئِسَ رُؤُوفٌ رَؤُوفٌ سُؤَالٌ مُؤَرِّخٌ
أَبْنَاءَهُ أَبْناؤُهُ أَبْنائِهِ شَيْئًا خَطِيئَةٌ
ضَوْءُهُ ضُوؤُهُ ضَوْءَهُ ضَوْئِهِ مُرُوءَةٌ
أَبْنائِهِ بَرِيؤُهُ سُوئِلَ فِيلٌ فَانٌّ فُونٌّ
سَاءَلَ فُؤَادٌ شُرَكاؤُهُ رِئَاسَةٌ تَهْنِئَةٌ
دَفَاءَةٌ طَفّاءَةٌ تَأْرِيخٌ فَأْرٌ
شَيْءٌ شَيْءٍ شَيْئًا  ضَوْءٌ ضَوْءٍ ضَوْءًا
جُزْءٌ  جُزْءٍ  جُزْءًا مَبْدَأٌ مَبْدَأٍ مَبْدَأً
نَبَأَ قَارِئٌ تَكَافُؤٌ تَكَافُؤٍ تَكَافُؤًا
أَبْناءُ أَبْناءِ أَبْناءَ جَريءٌ مَقْروءٌ ضَوْءٌ شَيْءٌ جُزْءٌ
عُلَماءُ ﭐلْعُلَماءِ ﭐلْعُلَماءَ عَمْرٌو وَفَعَلُوا
```

## betaCode into Translit
