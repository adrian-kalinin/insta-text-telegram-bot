all_characters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890'

antispam = str.maketrans(all_characters, 'абвгдeёжзийклmнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯаbсdefghijklmnорqrstuvwхyzАВСDЕFGНIJКLМNОРQRSТUVWХYZ01234567890')

dictionary = {
    'Инᴄᴛᴀᴦᴩᴀʍ': str.maketrans(all_characters, 'ᴀбʙᴦдᴇёжɜийᴋᴧʍнᴏᴨᴩᴄᴛуɸхцчɯщъыь϶юяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯᴀʙᴄdᴇfghijᴋlʍnᴏᴩqrsᴛuvwхyzАВСDЕFGНIJКLМNОРQRSТUVWХYZ01234567890'),
    'Инᥴᴛᥲᴦρᥲⲙ': str.maketrans(all_characters, 'ᥲδʙᴦдᥱёжᤋᥙᥔκ᧘ⲙн᧐ᥰρᥴᴛуɸ᥊цчɯщъыь϶юяАБВ𐌲ДЕЁЖЗИЙ𐌺𐌡𐌑𐋏𐌏𐌿Р𑀝ТУФ𐌗ЦԿШЩЪЫЬЭЮЯᥲδᥴɗᥱfgɦijκᥣⲙᥒ᧐ρqrsᴛᥙ᥎ᥕ᥊yᤁAB𑀝𑀥EFᏵ𐋏IJ𐌺𑀉𐌑𐌽𐌏PQR𐍃T𐌵VWXYZ01234567890'),
    'Ⳙⲏⲥⲧⲁⲅⲣⲁⲙ': str.maketrans(all_characters, 'ⲁⳝⲃⲅⲇⲉⲉⲯⳅυύⲕⲗⲙⲏⲟⲡⲣⲥⲧⲩⲫⲭцⳡⲱⳃъыьэюяⲀⳜⲂⲄⲆⲈⲈⲮⳄⳘЙⲔⲖⲘⲎⲞⲠⲢⲤⲦⲨⲪⲬЦⳠⲰⳂЪЫЬЭЮЯⲁⲃⲥⲇⲉϝⳋⲏⲓⳗⲕⳑⲙⲛⲟⲣqʀⲋⲧυⳳⲱⲭⲩⲍⲀⲂⲤⲆⲈϜⳒⲎⲒⳖⲔⳐⲘⲚⲞⲢQRⲊⲦⳘⳲⲰⲬⲨⲌ01234567890'),
    'Ͷϰϲταӷραϻ': str.maketrans(all_characters, 'αδɞӷɠεεѫӡμύӄλϻϰσηρϲτγϕχҵɥωψƅɩƅ϶બꤎΑҔΒӶ𑀐ξξѪӠͶӢӃΛϺΗΟꢒϷ𑀝ͲሃΦӼЏϤΨΨᏖ℔ᏏϿѤ𐍉αϸϲɗεϝɠɦʝʆӄɭϻησρϙɾʂʈμѵω𑀌γʐΑΒ𑀝ƊξϜƓΗ𑀡ͿӃLϺƝΟϷϘɌЅͲƲѴŴΧϒζ01234567890'),
    'υʜсταⲅραɱ': str.maketrans(all_characters, 'αɓɞⲅ∂ϱɛжʒυύκⲗɱʜσηρсτƴϕχʯɥɯɰъыь϶юяαɓɞⲅ∂ϱɛжʒυύκⲗɱʜσηρсτƴϕχʯɥɯɰъыь϶юяαɓϲ∂ϱƒɠɧɩʝƙɭɱɳσρʠɼѕʈυνѡχƴʑαɓϲ∂ϱƒɠɧɩʝƙɭɱɳσρʠɼѕʈυνѡχƴʑ01234567890'),
    'υⲏς੮ɑɾƿɑⲙ': str.maketrans(all_characters, 'ɑઠɞɾ∂૯દжਡυύκʌⲙⲏ૦ηƿς੮ƴɸⲭц૫ਘਘъыь϶юяɑઠɞɾ∂૯દжਡυύκʌⲙⲏ૦ηƿς੮ƴɸⲭц૫ਘਘъыь϶юяɑᑲςᑯ૯⨍ɢⲏɪᴊκʟⲙⲛ૦ƿવʀઽ੮υνਘⲭⲩⲍɑᑲςᑯ૯⨍ɢⲏɪᴊκʟⲙⲛ૦ƿવʀઽ੮υνਘⲭⲩⲍ01234567890'),
    '𐌵ઞꤍተꤌ꤅рꤌ𐌼': str.maketrans(all_characters, 'ꤌꤒꤐ꤅მꤕꤢ𐌟उꤣ꤇ӄ𐌻𐌼ઞ꤀ꤙрꤍተγϕ𑀋ꤟપω൰𑀨ખ𑀨ᤋળꤎ𐌀চ𐌱Г𑀥ΣΣ𐌟ን𐌵𐌵𐌺𐌡𐌑𐋏𐌏𐌿ᕈ𑀗𐌕𐍅𐌘𐌗ԱԿ𐌸𐌸ሄልራ𐌄𐌝𐌓ꤌꤐꤍꤤꤕકɠꤖ꤯ʆӄ꤈𐌌ꤙ꤀ρᱧ꤅᥉𑀱ս꤂ꤗ𑀋γꤘ𐌀𐌱𑀗𑀥Σ𐍆Ᏽ𐋏𐌆𐌋𐌺𑀉𐌑𐌽𐌏ᕈዓ𐍂𐍃𐌕𐌵𐠨ᱦ𐌗𐍅𐌔01234567890'),
    '𐌍Н𐌂𐌕𐌀𐌐𐌛𐌀𐌑': str.maketrans(all_characters, '𐌀Б𐌁𐌐д𐌄𐌄𐌟ᕒ𐌍𐌍𐌊𐌡𐌑Н𐌏П𐌛𐌂𐌕𐍔𐌘𐌗ЦЧШЩ𐌜𐌉𐌜𐌴𐌝𐌓𐌀Б𐌁𐌐д𐌄𐌄𐌟ᕒ𐌍𐌍𐌊𐌡𐌑Н𐌏П𐌛𐌂𐌕𐍔𐌘𐌗ЦЧШЩ𐌜𐌉𐌜𐌴𐌝𐌓𐌀𐌁𐌂Ɗ𐌄𐌅GH𐌉𐌋𐌊L𐌑N𐌏𐌛𐌒𐌓𐍃𐌕U𐌖W𐌗𐍔𐌔𐌀𐌁𐌂Ɗ𐌄𐌅GH𐌉𐌋𐌊L𐌑N𐌏𐌛𐌒𐌓𐍃𐌕U𐌖W𐌗𐍔𐌔01234567890'),
    '𐌵Н𐌾𐍄𐌳𐌲ᖘ𐌳𐌼': str.maketrans(all_characters, '𐌳𐍱𐌱𐌲𐍚𐌴𐌴𐌟ᕒ𐌵𐌵𐌺𐌻𐌼Н𐌏𐍀ᖘ𐌾𐍄𐍟𐌘𐍇ц𐍁𐍦𐍦ЪЫЬЭ𐌹𐌓𐌳𐍱𐌱𐌲𐍚𐌴𐌴𐌟ᕒ𐌵𐌵𐌺𐌻𐌼Н𐌏𐍀ᖘ𐌾𐍄𐍟𐌘𐍇ц𐍁𐍦𐍦ЪЫЬЭ𐌹𐌓𐌳𐌱𐌾D𐌴𐍆GH𐌹𐍡𐌺𐍰𐌼𐌽𐌏ᖘQ𐍂𐍃𐍄𐌵𐍛𐍪𐍇𐍟𐍐𐌳𐌱𐌾D𐌴𐍆GH𐌹𐍡𐌺𐍰𐌼𐌽𐌏ᖘQ𐍂𐍃𐍄𐌵𐍛𐍪𐍇𐍟𐍐01234567890'),
    'ᱢዘꤍተ𐌳𐌲ᱞ𐌳ᱬ': str.maketrans(all_characters, '𐌳ऊଓ𐌲ᱚꤕꤕ𐌟ንᱢᱢઝᱤᱬዘᱛᱴᱞꤍተሃ𐌘𐌗Ա𐌍ᱦᱷᱠᱟᱩ𑁌ᱵ𐌓𐌳ऊଓ𐌲ᱚꤕꤕ𐌟ንᱢᱢઝᱤᱬዘᱛᱴᱞꤍተሃ𐌘𐌗Ա𐌍ᱦᱷᱠᱟᱩ𑁌ᱵ𐌓𐌳ଓꤍᱚꤕፑ᱙ዘ𐌉𐌋ઝ𑀉ᱬ𐌽ᱛᱞᱧ𐍂Ⴝተ𐌵𐌖ᱦ𐌗𐍅ᱮ𐌳ଓꤍᱚꤕፑ᱙ዘ𐌉𐌋ઝ𑀉ᱬ𐌽ᱛᱞᱧ𐍂Ⴝተ𐌵𐌖ᱦ𐌗𐍅ᱮ01234567890'),
    'ሀዘርፐልታየልጠ': str.maketrans(all_characters, 'ልፔፎታሏይይሦንሀህኸበጠዘዐከየርፐነዋጰህሃሠሡፘፊሪጓሬጸልፔፎታሏይይሦንሀህኸበጠዘዐከየርፐነዋጰህሃሠሡፘፊሪጓሬጸልፎርሏይፑፘዘፗጋኸረጠበዐየዓዩናፐሀህሠጰሃጓልፎርሏይፑፘዘፗጋኸረጠበዐየዓዩናፐሀህሠጰሃጓ01234567890'),
    '༥ℵངᜎℷ۲ཥℷཀ': str.maketrans(all_characters, 'ℷཏཋ۲ℶ٤٤ᜈ༣༥༥۴۸ཀℵ٥กཥངᜎལཆ྾པལཡཔເ༁เཟཁཐℷཏཋ۲ℶ٤٤ᜈ༣༥༥۴۸ཀℵ٥กཥངᜎལཆ྾པལཡཔເ༁เཟཁཐℷཋངℶ٤ச۹ℵ༏ง۴༨ཀก٥ཥ۶۲༦ᜎ༥۷ཡ྾ལའℷཋངℶ٤ச۹ℵ༏ง۴༨ཀก٥ཥ۶۲༦ᜎ༥۷ཡ྾ལའ01234567890'),
    'ນห໒รคເ༩คຕ': str.maketrans(all_characters, 'คธദເລ౿౿ณзນม๙ภຕหഠກ༩໒รຯ୫྾บഴພຟ๒ຫ๖ອശศคธദເລ౿౿ณзນม๙ภຕหഠກ༩໒รຯ୫྾บഴພຟ๒ຫ๖ອശศคദ໒ລ౿ச໑ล୲ຽ๙ℓຕກഠ༩າཞຣรບ୶໖྾ຯຂคദ໒ລ౿ச໑ล୲ຽ๙ℓຕກഠ༩າཞຣรບ୶໖྾ຯຂ01234567890'),
    'Џʜҁϯѧґⱀѧʍ': str.maketrans(all_characters, 'ѧѣʙґđєҽѫӡџӣκʌʍʜѳπⱀҁϯƴѻχҵӌɯѱƀӀƀ϶ѥᴙѦѢƁҐΔΣҼѪӠЏӢҞΛᛖⴼѲ∏ƤҀϮƳѺӼҴӋƜѰƀӀƀƎѤꯌѧƀҁđєӻƍђϊɉҟƖʍƞѳⱀǫɍƽϯυⱱѡχƴⱬѦƁҀΔΣӺǤⴼΪɈҞⱢᛖƝѲƤǪƦƼϮƲѴѠӼƳⱫ01234567890'),
    'ИϰɕᎿɑɾ℘ɑɱ': str.maketrans(all_characters, 'ɑҕɞɾϫɛⅇҗʓϞӥκλɱϰσπ℘ɕᎿγȹℵцʮɯɰҍ℩ƅəюᴙᎯҔᏰℾϪ℮ℰᏯℨИҊӃᏁℳℋᎾℿ⅌ℭƬᎽɸℵЦᏎƜᏇᏖ℔Ꮟ℈ᎾЯɑᎴɕⅆɛƒℊℏⅈⅉƙℓɱɳσ℘ǫɼʂᎿʋɤѡℵℽʑᎯᏰℭⅅ℮ℱᏩℋᏐℐӃℒℳℕᎾ⅌ℚℜᏕƬƲᏉᏔℵᎽℤ01234567890'),
    'ꪊꪦ૮ꫂꪋટƿꪋꪑ': str.maketrans(all_characters, 'ꪋꪉଓટꪖꫀꫀઋꪅꪊꪌઝꪒꪑꪦ᥆ꪀƿ૮ꫂꪗફꪎꪍꪩꪝꪡꪶꪨꪶꪮꪓꪯꪋꪉଓટꪖꫀꫀઋꪅꪊꪌઝꪒꪑꪦ᥆ꪀƿ૮ꫂꪗફꪎꪍꪩꪝꪡꪶꪨꪶꪮꪓꪯꪋଓ૮ᦔꫀᠻꪮꫝꪱ᧒ઝꪶꪑꪀ᥆ƿꪺꪚઽꫂꪊꪜꪝꪎꪗᤁꪋଓ૮ᦔꫀᠻꪮꫝꪱ᧒ઝꪶꪑꪀ᥆ƿꪺꪚઽꫂꪊꪜꪝꪎꪗᤁ01234567890'),
    'ᜤᜨᢗᝨᝯᥬᜣᝯᜰ': str.maketrans(all_characters, 'ᝯᠪẞᥬ᠗ᠻᠻᜫᜢᜤᜬᜥ᠕ᜰᜨᝪᥒᜣᢗᝨ𐍟ᥗᝣᜮᝄ𐍦ɰᕹᒈᖯᢖᠣᠫᝯᠪẞᥬ᠗ᠻᠻᜫᜢᜤᜬᜥ᠕ᜰᜨᝪᥒᜣᢗᝨ𐍟ᥗᝣᜮᝄ𐍦ɰᕹᒈᖯᢖᠣᠫᝯẞᢗ᠗ᠻᠮ᠖ᜨᜧ𐌋ᜥ᠘ᜰᜬᝪᜣ᠑ᜠ𐍃ᝨᝀᜱᜦᝣ𐍟𐌔ᝯẞᢗ᠗ᠻᠮ᠖ᜨᜧ𐌋ᜥ᠘ᜰᜬᝪᜣ᠑ᜠ𐍃ᝨᝀᜱᜦᝣ𐍟𐌔01234567890'),
    'ひꤊ᥌რձᤇթձო': str.maketrans(all_characters, 'ձნᤜᤇმᤉᤉ𐌟ვսմҟ᥈ოꤊჿიթ᥌რყჶ᥊ևվաաს᥏᥇϶დꤎ𐌀ゟßՐの𑁗𑁗𐌟ՅひびҞへ𐌌みՕႶԹႺႵႸႴ𐌢ԱԿሠሡႪႦႦ𑁌ሬମձճ᥌ძᤉӻᤚჩ𐌠ʆҟ꤈ოከჿթգᤇ᥉էս᥎ᤐ᥊ყᤁ𐌀ßႺの𑁗Բ𐌾みፗ𑀮ҞԼՊ𐌽ՕԹႳՔჽႵႮ꣗ሠ𐌢Ⴤ𑁞01234567890'),
    'ⵍⴼⵎⵜѦⵤᎮѦᗑ': str.maketrans(all_characters, 'ѦⵒɃⵤⵠⵟⵉⵅᕒⵍⵍҞⴷᗑⴼⵔगᎮⵎⵜᖿⵀⵋⵡⵖᗐƜѢѣѣⴺⵚⴳѦⵒɃⵤⵠⵟⵉⵅᕒⵍⵍҞⴷᗑⴼⵔगᎮⵎⵜᖿⵀⵋⵡⵖᗐƜѢѣѣⴺⵚⴳѦɃⵎⵠⵟƑGⴼⵊɈҞȽᗑƝⵔᎮⵕⴽⵢⵜƲⴸᏔⵋᖿƵѦɃⵎⵠⵟƑGⴼⵊɈҞȽᗑƝⵔᎮⵕⴽⵢⵜƲⴸᏔⵋᖿƵ01234567890'),
    'ᛋᚺᛈᛠᚣᛚᚹᚣᛖ': str.maketrans(all_characters, 'ᚣƃᛒᛚᚦᛊᛊᛯƷᛋᛪᛕᚳᛖᚺᛜᚢᚹᛈᛠᚴᛰᚷᛮⰍᚠᚡᚧᚦᚦᛘᚿᛟᚣƃᛒᛚᚦᛊᛊᛯƷᛋᛪᛕᚳᛖᚺᛜᚢᚹᛈᛠᚴᛰᚷᛮⰍᚠᚡᚧᚦᚦᛘᚿᛟᚣᛒᛈᚦᛊᚫᛩᚻᛨᛇᛕᚳᛖᚺᛜᚹᛟᚱᛢᛠᛘᛉᚠᚷᚴZᚣᛒᛈᚦᛊᚫᛩᚻᛨᛇᛕᚳᛖᚺᛜᚹᛟᚱᛢᛠᛘᛉᚠᚷᚴZ01234567890'),
    'ꈤꍬꊐꉢꁲ꒕ꉣꁲꂵ': str.maketrans(all_characters, 'ꁲꃥꃃ꒕ꅓꂅꏁꁘ꒱ꈤꈣꂪꀊꂵꍬꏿꊮꉣꊐꉢꌦꂈꉧꈥꃏꅐꁁꀲꎪꎪꎆꂼꋪꁲꃥꃃ꒕ꅓꂅꏁꁘ꒱ꈤꈣꂪꀊꂵꍬꏿꊮꉣꊐꉢꌦꂈꉧꈥꃏꅐꁁꀲꎪꎪꎆꂼꋪꁲꃃꊐꅓꂅꊰꁅꍬꀤꀭꂪ꒒ꂵꊮꏿꉣꐎꉸꌗꉢꏵꏝꅐꉧꌦꏣꁲꃃꊐꅓꂅꊰꁅꍬꀤꀭꂪ꒒ꂵꊮꏿꉣꐎꉸꌗꉢꏵꏝꅐꉧꌦꏣ01234567890'),
    'ᑌᕼᐸᖶᗅᒥᕈᗅᗑ': str.maketrans(all_characters, 'ᗅᘪᗽᒥᐃᗕᓬᗗᕒᑌᕫᏦᐱᗑᕼᗜᑎᕈᐸᖶᖿᙉ᙭ᕰᔦᗐᗖᘪᒈᘤᗒᘗᖆᗅᘪᗽᒥᐃᗕᓬᗗᕒᑌᕫᏦᐱᗑᕼᗜᑎᕈᐸᖶᖿᙉ᙭ᕰᔦᗐᗖᘪᒈᘤᗒᘗᖆᗅᗽᐸᐃᗕᖴᎶᕼᔫJᏦᒪᗑᑎᗜᕈᕴᖇᔑᖶᕰᐯᗐ᙭ᖿᘔᗅᗽᐸᐃᗕᖴᎶᕼᔫJᏦᒪᗑᑎᗜᕈᕴᖇᔑᖶᕰᐯᗐ᙭ᖿᘔ01234567890'),
    'ᑌᕼᙅᙢᗣᒋᖘᗣᗰ': str.maketrans(all_characters, 'ᗣᘜᙖᒋᗪᙓᕧᙧᙐᑌᕫᏦᙁᗰᕼᗝᑎᖘᙅᙢᎽᙨⵋᘈᔦᗯᘺᕹᕠᖚᑓᕡᖆᗣᘜᙖᒋᗪᙓᕧᙧᙐᑌᕫᏦᙁᗰᕼᗝᑎᖘᙅᙢᎽᙨⵋᘈᔦᗯᘺᕹᕠᖚᑓᕡᖆᗣᙖᙅᗪᙓᖴᘜᕼᖗᒍᏦᒐᗰᘉᗝᖘᘯᖇᔕᙢᑌᐯᙡⵋᎽᘔᗣᙖᙅᗪᙓᖴᘜᕼᖗᒍᏦᒐᗰᘉᗝᖘᘯᖇᔕᙢᑌᐯᙡⵋᎽᘔ01234567890'),
    'ᑌᕼᑕᎢᗩᒥᑭᗩᗰ': str.maketrans(all_characters, 'ᗩᘕᗷᒥᗞᗴᗴᙧᗱᑌᑧᖉᐱᗰᕼᓂᑎᑭᑕᎢᖿᗼ᙭ᘈᔦᙎᘺᘶᒈᖚᕭᘗᖆᗩᘕᗷᒥᗞᗴᗴᙧᗱᑌᑧᖉᐱᗰᕼᓂᑎᑭᑕᎢᖿᗼ᙭ᘈᔦᙎᘺᘶᒈᖚᕭᘗᖆᗩᗷᑕᗞᗴᖴᎶᕼᏆᒍᏦᏞᗰᑎᓂᑭᑫᖇᔑᎢᑌᐯᗯ᙭ᎩᔐᗩᗷᑕᗞᗴᖴᎶᕼᏆᒍᏦᏞᗰᑎᓂᑭᑫᖇᔑᎢᑌᐯᗯ᙭Ꭹᔐ01234567890'),
    'ᑌᕼᑕᎢᕕᒋᖘᕕᕬ': str.maketrans(all_characters, 'ᕕᘜᗷᒋᗋᘓᕧᙧᗱᑌᑧᖉᐱᕬᕼᓂᑎᖘᑕᎢᖿᗼ᙭ᕰᔦᙎᙡᕹᕠᖚᕭᕡᖆᕕᘜᗷᒋᗋᘓᕧᙧᗱᑌᑧᖉᐱᕬᕼᓂᑎᖘᑕᎢᖿᗼ᙭ᕰᔦᙎᙡᕹᕠᖚᕭᕡᖆᕕᗷᑕDᘓᖴᘜHᓵᖙᖉᒐᕬᑎᓂᖘᖗRᔕᎢᑌᕓᗯ᙭ᖿᘔᕕᗷᑕDᘓᖴᘜHᓵᖙᖉᒐᕬᑎᓂᖘᖗRᔕᎢᑌᕓᗯ᙭ᖿᘔ01234567890'),
    '나⼶ㄈ亇闩⼚ㄗ闩⽖': str.maketrans(all_characters, '闩万乃⼚刀乇乇⺢㇋나나片入⽖⼶口兀ㄗㄈ亇丫中乂凵ㄐ山⼬ㄊ也ムヲ扣牙闩万乃⼚刀乇乇⺢㇋나나片入⽖⼶口兀ㄗ亡亇丫中乂凵ㄐ山⼬ㄊ也ムヲ扣牙闩乃ㄈ刀乇下彑⼶⻈亅片乚⽖力口ㄗ디尺丂亇凵ム山乂丫乙闩乃亡刀乇下彑⼶工亅片乚⽖力口ㄗ디尺丂亇凵ム山乂丫乙01234567890'),
    '丩什仁个丸⽧ヤ丸从': str.maketrans(all_characters, '丸⽯书⽧亼乜せ⽶乡丩나长⼈从什⼞介ヤ仁个丫兎⽗凵ㄐ丗冚ㄊ乩ムヌ仂乆丸⽯书⽧亼乜せ⽶乡丩나长⼈从什⼞介ヤ仁个丫兎⽗凵ㄐ丗冚ㄊ乩ムヌ仂乆丸书仁亼乜ﾁ乌什亻丿长乚从九⼞ヤ⽈刄与个凵ム丗⽗丫之丸书仁亼乜ﾁ乌什亻丿长乚从九⼞ヤ⽈刄与个凵ム丗⽗丫之01234567890'),
    'ℐ𝓃𝓈𝓉𝒶ℊ𝓇𝒶𝓂': str.maketrans(all_characters, '𝒶𝒷𝓋ℊ𝒹ℯ𝓎𝓏𝒽𝓏𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓇𝓈𝓉𝓊𝒻𝒽𝓉𝒸𝒽𝓈𝒽𝓈𝓎𝓎𝓎𝒜ℬ𝒱𝒢𝒟ℰ𝒴𝒵𝒽𝒵ℐ𝒥𝒦ℒℳ𝒩𝒪𝒫ℛ𝒮𝒯𝒰ℱℋ𝒯𝒞𝒽𝒮𝒽𝒮𝒴𝒴𝒴𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵01234567890'),
    '𝓘𝓷𝓼𝓽𝓪𝓰𝓻𝓪𝓶': str.maketrans(all_characters, '𝓪𝓫𝓿𝓰𝓭𝓮𝔂𝔃𝓱𝔃𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓻𝓼𝓽𝓾𝓯𝓱𝓽𝓬𝓱𝓼𝓱𝓼𝔂𝔂𝔂𝓐𝓑𝓥𝓖𝓓𝓔𝓨𝓩𝓱𝓩𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓡𝓢𝓣𝓤𝓕𝓗𝓣𝓒𝓱𝓢𝓱𝓢𝓨𝓨𝓨𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩01234567890'),
    '𝔗𝔫𝔰𝔱𝔞𝔤𝔯𝔞𝔪': str.maketrans(all_characters, '𝔞𝔟𝔳𝔤𝔡𝔢𝛾𝔷𝔥𝔷𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔯𝔰𝔱𝔲𝔣𝔥𝔱𝔠𝔥𝔰𝔥𝔰𝛾𝛾𝛾𝔄𝔅𝔙𝔊𝔇𝔈ϒℨ𝔥ℨ𝔗𝔍𝔎𝔏𝔐𝔑𝔒𝔓ℜ𝔖ℑ𝔘𝔉ℌℑℭ𝔥ℭ𝔥ℭϒϒϒ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝛾𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌ𝔗𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖ℑ𝔘𝔙𝔚𝔛ϒℨ01234567890'),
    '𝕿𝖓𝖘𝖙𝖆𝖌𝖗𝖆𝖒': str.maketrans(all_characters, '𝖆𝖇𝖛𝖌𝖉𝖊𝛄𝖟𝖍𝖟𝖎𝖎𝖐𝖑𝖒𝖓𝖔𝖕𝖗𝖘𝖙𝖚𝖋𝖍𝖙𝖈𝖍𝖘𝖍𝖘𝛄𝛄𝛄𝕬𝕭𝖁𝕲𝕯𝕰𝚼𝖅𝖍𝖅𝕿𝕴𝕶𝕷𝕸𝕹𝕺𝕻𝕽𝕾𝕴𝖀𝕱𝕳𝕴𝕮𝖍𝕾𝖍𝕾𝚼𝚼𝚼𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝛄𝖟𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕿𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕴𝖀𝖁𝖂𝖃𝚼𝖅01234567890'),
    '𝖨𝗇𝗌𝗍𝖺𝗀𝗋𝖺𝗆': str.maketrans(all_characters, '𝖺𝖻𝗏𝗀𝖽𝖾𝗒𝗓𝗓𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗋𝗌𝗍𝗎𝖿𝗁𝗍𝗁𝗌𝗁𝗌𝖼𝗁𝗒𝗒𝗒𝖠𝖡𝖵𝖦𝖣𝖤𝖸𝖹𝖹𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖱𝖲𝖳𝖴𝖥𝖧𝖳𝖢𝖲𝗁𝖲𝖼𝗁𝖸𝖸𝖸𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹01234567890'),
    '𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺': str.maketrans(all_characters, '𝗮𝗯𝘃𝗴𝗱𝗲𝘆𝘇𝘇𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗿𝘀𝘁𝘂𝗳𝗵𝘁𝗰𝗵𝘀𝗵𝗰𝗵𝘆𝘆𝘆𝗔𝗕𝗩𝗚𝗗𝗘𝗬𝗭𝗭𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗥𝗦𝗧𝗨𝗙𝗛𝗧𝗖𝗵𝗦𝗵𝗦𝗰𝗬𝗬𝗬𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭01234567890'),
    '𝐼𝑛𝑠𝑡𝑎𝑔𝑟𝑎𝑚': str.maketrans(all_characters, '𝑎𝑏𝑣𝑔𝑑𝑒𝑦𝑧𝑧𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑟𝑠𝑡𝑢𝑓ℎ𝑡𝑐ℎℎ𝑠𝑐ℎ𝑦𝑦𝑦𝐴𝐵𝑉𝐺𝐷𝐸𝑌𝑍𝑍𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑅𝑆𝑇𝑈𝐹𝐻𝑇𝐶ℎℎ𝑆𝑐ℎ𝑌𝑌𝑌𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍01234567890'),
    '𝑰𝒏𝒔𝒕𝒂𝒈𝒓𝒂𝒎': str.maketrans(all_characters, '𝒂𝒃𝒗𝒈𝒅𝒆𝒚𝒛𝒛𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒓𝒔𝒕𝒖𝒇𝒉𝒕𝒄𝒉𝒉𝒔𝒄𝒉𝒚𝒚𝒚𝑨𝑩𝑽𝑮𝑫𝑬𝒀𝒁𝒁𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑹𝑺𝑻𝑼𝑭𝑯𝑻𝑪𝒉𝒉𝑺𝒄𝒉𝒀𝒀𝒀𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁01234567890'),
    '𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖': str.maketrans(all_characters, '𝚊𝚋𝚟𝚐𝚍𝚎𝚢𝚣𝚣𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚛𝚜𝚝𝚞𝚏𝚑𝚝𝚌𝚑𝚑𝚜𝚌𝚑𝚢𝚢𝚢𝙰𝙱𝚅𝙶𝙳𝙴𝚈𝚉𝚉𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚁𝚂𝚃𝚄𝙵𝙷𝚃𝙲𝚑𝚑𝚂𝚌𝚑𝚈𝚈𝚈𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉01234567890'),
    '𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦': str.maketrans(all_characters, '𝐚𝐛𝐯𝐠𝐝𝐞𝐲𝐳𝐳𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐫𝐬𝐭𝐮𝐟𝐡𝐭𝐜𝐡𝐡𝐬𝐜𝐡𝐲𝐲𝐲𝐀𝐁𝐕𝐆𝐃𝐄𝐘𝐙𝐙𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐑𝐒𝐓𝐔𝐅𝐇𝐓𝐂𝐡𝐒𝐒𝐜𝐡𝐘𝐘𝐘𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙01234567890'),
    '𝕀𝕟𝕤𝕥𝕒𝕘𝕣𝕒𝕞': str.maketrans(all_characters, '𝕒𝕓𝕧𝕘𝕕𝕖𝕪𝕫𝕫𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕣𝕤𝕥𝕦𝕗𝕙𝕥𝕤𝕙𝕤𝕙𝕔𝕙𝕪𝕪𝕪𝔸𝔹𝕍𝔾𝔻𝔼𝕐ℤℤ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℝ𝕊𝕋𝕌𝔽ℍ𝕋𝕤ℂ𝕊𝕙𝕊𝕙𝕐𝕐𝕐𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ01234567890'),
    'Ｉｎｓｔａｇｒａｍ': str.maketrans(all_characters, 'ａｂｖｇｄｅｙｚｚｉｊｋｌｍｎｏｐｒｓｔｕｆｈｔｈｓｈｓｃｈｙｙｙＡＢＶＧＤＥＹＺＺＩＪＫＬＭＮＯＰＲＳＴＵＦＨＴＣＳｈＳｃｈＹＹＹａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ01234567890'),
    'ɪɴsᴛᴀɢʀᴀᴍ': str.maketrans(all_characters, 'ᴀʙᴠɢᴅᴇʏᴢᴢɪᴊᴋʟᴍɴᴏᴘʀsᴛᴜғʜᴛsʜsʜsʜʏʏʏᴀʙᴠɢᴅᴇʏᴢᴢɪᴊᴋʟᴍɴᴏᴘʀsᴛᴜғʜᴛsʜsʜsʜʏʏʏᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ01234567890'),
    'ⒾⓃⓈⓉⒶⒼⓇⒶⓂ️': str.maketrans(all_characters, 'ⒶⒷⓋⒼⒹⒺⓎⓏⓏⒾⒿⓀⓁⓂ️ⓃⓄⓅⓇⓈⓉⓊⒻⒽⓉⒽⓈⒽⒽⓎⓎⓎⒶⒷⓋⒼⒹⒺⓎⓏⓏⒾⒿⓀⓁⓂ️ⓃⓄⓅⓇⓈⓉⓊⒻⒽⓉⒽⓈⒽⒽⓎⓎⓎⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂ️ⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂ️ⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ01234567890'),
    '🅘🅝🅢🅣🅐🅖🅡🅐🅜': str.maketrans(all_characters, '🅐🅑🅥🅖🅓🅔🅨🅩🅩🅘🅙🅚🅛🅜🅝🅞🅟🅡🅢🅣🅤🅕🅗🅣🅗🅒🅗🅢🅒🅗🅨🅨🅨🅐🅑🅥🅖🅓🅔🅨🅩🅩🅘🅙🅚🅛🅜🅝🅞🅟🅡🅢🅣🅤🅕🅗🅣🅗🅒🅗🅢🅒🅗🅨🅨🅨🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩01234567890'),
    '🄸🄽🅂🅃🄰🄶🅁🄰🄼': str.maketrans(all_characters, '🄰🄱🅅🄶🄳🄴🅈🅉🅉🄸🄹🄺🄻🄼🄽🄾🄿🅁🅂🅃🅄🄵🄷🅃🄷🅂🄷🅂🄲🄷🅈🅈🅈🄰🄱🅅🄶🄳🄴🅈🅉🅉🄸🄹🄺🄻🄼🄽🄾🄿🅁🅂🅃🅄🄵🄷🅃🄷🅂🄷🅂🄲🄷🅈🅈🅈🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉01234567890'),
    'ⓘⓝⓢⓣⓐⓖⓡⓐⓜ': str.maketrans(all_characters, 'ⓐⓑⓥⓖⓓⓔⓘⓩⓩⓘⓨⓚⓛⓜⓝⓞⓟⓡⓢⓣⓤⓕⓗⓣⓢⓗⓢⓗⓢⓒⓨⓨⓨⓐⓑⓥⓖⓓⓔⓘⓩⓩⓘⓨⓚⓛⓜⓝⓞⓟⓡⓢⓣⓤⓕⓗⓣⓢⓗⓢⓗⓢⓒⓨⓨⓨⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ01234567890'),
    '⁰¹²³⁴⁵⁶⁷⁸⁹': str.maketrans(all_characters, 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ⁰¹²³⁴⁵⁶⁷⁸⁹⁰'),
    '₀₁₂₃₄₅₆₇₈₉': str.maketrans(all_characters, 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ₀₁₂₃₄₅₆₇₈₉₀'),
    '⓪①②③④⑤⑥⑦⑧⑨': str.maketrans(all_characters, 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ⓪①②③④⑤⑥⑦⑧⑨⓪'),
    '⓿➊➋➌➍➎➏➐➑➒': str.maketrans(all_characters, 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ⓿➊➋➌➍➎➏➐➑➒⓿'),
    '𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫': str.maketrans(all_characters, 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢'),
    '𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵': str.maketrans(all_characters, 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬'),
    '𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿': str.maketrans(all_characters, 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶'),
    '𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗': str.maketrans(all_characters, 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎'),
    '𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡': str.maketrans(all_characters, 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘'),
    '０１２３４５６７８９': str.maketrans(all_characters, 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ０１２３４５６７８９０')
}


def translate_instagram(user_input: str):
    lines = user_input.split('\n')
    text = ''

    for line in lines:
        if len(line) > 2:
            if line.startswith('..'):
                text += '⠀⠀' + line[2:]

            elif line.startswith(',,'):
                count = 10 - len(line) // 4
                text += '⠀ ' * count + line[2:]

            else:
                text += line

            text += '\n'

        elif line == '':
            text += '⠀\n'

        else:
            text += line

    return text
