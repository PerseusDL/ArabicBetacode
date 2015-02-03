# Arabic betaCode

The idea of **betaCode** is borrowed from the Classicists who developed ["a method of representing, using only ASCII characters, characters and formatting found in ancient Greek texts"](http://en.wikipedia.org/wiki/Beta_Code). Although both Windows and Mac OS now support Arabic there are still many issues with the available methods. In particular, it is difficult to keep track of fully vocalized texts, since most fonts either render *ḥarakāt* invisible, or do not render them properly. **betaCode** can help to make typing fully-vocalized Arabic texts possible and easy on any machine and render it into various transliteration conventions (although, of course, there should be one to rule them all) and into Arabic script (scroll below for examples). 

**betaCode** is first converted into a one-to-one transliteration scheme (the one to rule them all), which combines one-to-one transliteration conventions from major academic transliteration schemes. Such scheme is necessary, since none of the existing academic transliteration schemes (American/Library of Congress, British, French, German) allow to represent Arabic text unambiguously for computational purposes. Arabic **betaCode** transliteration can be then converted into any transliteration conventions. At the moment the following schemes are implemented (not yet fully):

* Library of Congress Romanization of Arabic
* Simplified transliteration (essentially, LOC but with diacritics removed)
* Arabic script (*hamzaŧ* orthography rules are not implemented yet)

**NB:** The current **betaCode** is inspired by, and is therefore quite similar to, the [arabTex scheme](http://www2.informatik.uni-stuttgart.de/ivi/bs/research/arab_e.htm).

## Basic principles:
Every Arabic letter is betaCoded with its one-letter equivalent (thus pulling from different academic transliteration schemes),
preceded (if necessary) with a technical symbol that is similar to a diacritical mark in the transliterated version. Thus, most common symbols are as follows:

* **\_** (underscore), if letter can be transliterated with *macron*/*breve* below or above (ā, ṯ, ḫ, ḏ, ū, ī)
* **.** (period), or  <b>\*</b> (asterisk), if letter can be transliterated transliterated with *dot* below or above (ḥ, ṣ, ḍ, ṭ, ẓ, ġ, ḳ)
* **^** (caret), if letter can be transliterated with *caron* (ǧ, š)
* plus some new combinations (scroll down for the complete table)

## Examples 

## betaCode example
```
.kul huwa all~ahu_ a.hadu.n all~ahu_ al-.samadu_ lam yalid wa-lam y_ulad wa-lam yakun lahu kufu'a.n a.hadu.n

wa-.k_amat `_amma:t+u_ Ba.gd_ada_ li-yusallima al-_hal_ifa:ta_ al-Man.s_ura_ `al/a ruj_u`i-hi min al-K_ufa:ti_

al-.hamdu li-Ll~ahi 
```


## betacodeToTranslit() - betaCode converted to one-to-one translit system (used for conversion into all other)
```
ḳul huwa allãhu aḥaduȵ allãhu al-ṣamadu lam yalid wa-lam yūlad wa-lam yakun lahu kufuʾaȵ aḥaduȵ

wa-ḳāmat ʿāmmaŧu Baġdāda li-yusallima al-ḫalīfaŧa al-Manṣūra ʿalá ruǧūʿi-hi min al-Kūfaŧi

al-ḥamdu li-Llãhi
```

## betacodeToSearch() - betaCode converted to simplified transliteration suitable for search/alphabetization
```
qul huwa allah ahad allah al-samad lam yalid wa-lam yulad wa-lam yakun lahu kufuan ahad

wa-qamat ammat Baghdad li-yusallima al-khalifa al-Mansur ala rujui-hi min al-Kufa

al-hamdu li-Llahi
```

## betacodeToLOC() - betaCode converted to the Library of Congress scheme
```
qul huwa allāh aḥad allāh al-ṣamad lam yalid wa-lam yulad wa-lam yakun lahu kufuʾ aḥad

wa-qāmat ʿāmmat Baghdād li-yusallima al-khalifa al-Manṣur ʿalā rujuʿi-hi min al-Kufa

al-ḥamdu li-Llāhi
```

### betacodeToArabic() - betaCode converted to Arabic (*hamzaŧ* orthography rules are not implemented yet)
```
قُلْ هُوَ ﭐلـلّٰـهُ أَحَدٌ ﭐلـلّٰـهُ ﭐلصَّمَدُ لَمْ يَلِدْ وَلَمْ يُولَدْ وَلَمْ يَكُنْ لَهُ كُفُءً أَحَدٌ

وَقَامَتْ عَامَّةُ بَغْدَادَ لِيُسَلِّمَ ﭐلْخَلِيفَةَ ﭐلْمَنْصُورَ عَلى رُجُوعِهِ مِنْ ﭐلْكوفَةِ

ﭐلْحَمْدُ لِـلّٰـهِ
```

## Some additional rules/principles

* vowel case endings add "_", i.e.:
	* ``` f_i al-kit_abi_ ```, but not:
	* ``` f_i al-kit_abi.n ``` (all *tanwīn kasr* and *tanwīn ḍamm* will be automatically removed from transliterated versions)
* attached prepositions/conjunctions must be separated with "-", i.e.:
	* ``` bi-Llahi_ ```
	* ``` fa-_dahaba_ ```
* *tāʾ marbūṭaŧ*: add "+" after *tāʾ marbūṭaŧ*, if the first word of *iḏāfaŧ*
	* ``` `_amma:t+u Ba.gd_ada ```, but:
	* ``` al-`_amma:tu f_i Ba.gd_ada ```
* some more to be added...


## betaCode and One-To-One Transliteration

| betacode | translit | Arabic |
|----------|-----------------|---------------|
| **\_a** | ā | *alif* |
| **b** | b | *bā’* |
| **t** | t | *tā’* |
| **\_t** | ṯ | *thā’* |
| **^g, j** | ǧ | *jīm* |
| **^c** | č | *chīm / Persian* |
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
| **g** | g | *gāf / Persian* |
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
| **:t** | ŧ | *tā’ marbūṭaŧ* (add "+", if the first word of *iḏāfaŧ*) |

## Vowels

| **betacode** | translit | Arabic |
|----------|-----------------|---------------|
| **~a** | ã | *dagger alif* |
| **a** | a | *fatḥaŧ* |
| **u** | u | *ḍammaŧ* |
| **i** | i | *kasraŧ* |
| **^n, .n, \_n, \*n** | ȵ | *n of tanwīn* |
