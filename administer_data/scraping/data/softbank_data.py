"""
((pref_id, area_id), area_name(店舗数)):{
    "店舗名": {
        class_name:
        phone_number:
        has_parking:
        is_barrier_free:
        address
    }
}
"""
data2 = {
    (('13', '131016'), '千代田区（4）'): {}, 
    (('13', '131024'), '中央区（5）'): {
        'ソフトバンク銀座': {
            'class_name': 'ソフトバンク銀座',
            'phone_number': '03-6252-3333',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都中央区銀座５丁目７番８号'
        }
    }, (('13', '131032'), '港区（7）'): {
        'ソフトバンク六本木': {
            'class_name': 'ソフトバンク六本木',
            'phone_number': '03-5775-5011',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都港区六本木４丁目９‐７ 三菱ＵＦＪ銀行六本木支店ビル１Ｆ'
        }
    }, (('13', '131041'), '新宿区（9）'): {
        'ソフトバンク新宿西口': {
            'class_name': 'ソフトバンク新宿西口',
            'phone_number': '03-3348-5811',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都新宿区西新宿１丁目１９‐５ 新宿幸容ビル'
        },
        'ソフトバンク神楽坂': {
            'class_name': 'ソフトバンク神楽坂',
            'phone_number': '03-5229-7150',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都新宿区神楽坂６丁目４７ 照井ビル１Ｆ'
        },
        'ソフトバンク高田馬場': {
            'class_name': 'ソフトバンク高 田馬場',
            'phone_number': '03-3209-7841',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都新宿区高田馬場２丁目１３‐２ Ｐｒｉｍｅｇａｔｅ１階'
        }
    }, (('13', '131059'), '文京区（2）'): {}, (('13', '131067'), '台東区（4）'): {
        'ソフトバンク浅草ＲＯＸ': {
            'class_name': 'ソフトバンク浅草ＲＯＸ',
            'phone_number': '03-5827-0430',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都台東区浅草１丁目２５‐ １５ 浅草ＲＯＸ １Ｆ'
        }
    }, (('13', '131075'), '墨田区（4）'): {
        'ソフトバンクアルカキット錦糸町': {
            'class_name': 'ソフトバンクアルカキット 錦糸町',
            'phone_number': '03-5610-7283',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都墨田区錦糸２丁目２‐１ アルカキット錦糸町８階'
        },
        'ソフトバンクオリナス錦糸町': {
            'class_name': 'ソフトバンクオリナス錦糸町',
            'phone_number': '03-5610-8830',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都墨田区太平４丁目２‐１オリナス２Ｆ'
        }
    }, (('13', '131083'), '江東区（9）'): {
        'ソフトバンクイトー ヨーカドー木場': {
            'class_name': 'ソフトバンクイトーヨーカドー木場',
            'phone_number': '03-6666-5290',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都江東区木場１丁目５‐３０ イトーヨーカドー木場店'
        },
        'ソフトバンクアリオ北砂': {
            'class_name': 'ソフトバンクアリオ北砂',
            'phone_number': '03-5665-0341',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都江東区北砂２丁目１７番地１号アリオ北砂２階'
        },
        ' ソフトバンクカメイドクロック': {
            'class_name': 'ソフトバンクカメイドクロック',
            'phone_number': '03-3636-6692',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都江東区亀戸６丁目３１‐６ カメイドクロック３Ｆ'
        }
    }, (('13', '131091'), '品川区（10）'): {
        'ソフトバンク大森': {
            'class_name': 'ソフトバンク大森',
            'phone_number': '03-3768-7390',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都品川区南大井６丁目２８‐１０'
        },
        'ソフトバンク阪急大井町ガーデン': {
            'class_name': 'ソフトバンク阪急大井町ガーデン',
            'phone_number': '03-3778-6400',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都品川区大井１丁目５０‐５阪急大井町ガーデン２階'
        },
        'ソフトバンク武蔵小山パルム': {
            'class_name': 'ソフトバンク武蔵小山パルム',
            'phone_number': '03-6426-9700',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都品川区小山３丁目２１‐１３武蔵小山パルムＡ棟'
        },
        'ソフトバンクパークシティ武蔵小山ザモール': {
            'class_name': 'ソフトバンクパークシティ武蔵小山ザモール',
            'phone_number': '03-5749-1122',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都品川区小山３丁目１５‐１ パークシティ武蔵小山ザモール１Ｆ'
        },
        'ソフトバンク目黒': {
            'class_name': 'ソフトバンク目黒',
            'phone_number': '03-3490-9561',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都品川区上大崎２丁目１８‐１６ 月乃ビル１階'
        }
    }, (('13', '131105'), '目黒区（5）'): {
        'ソフトバンク自由が丘南口': {
            'class_name': 'ソフトバンク自由が丘南口',
            'phone_number': '03-6891-6770',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都目黒区自由が丘１丁目８‐１ ミナミビル１Ｆ'
        },
        'ソフトバンク都立大学': {
            'class_name': 'ソフトバンク都立大学',
            'phone_number': '03-5731-0040',
            'has_parking': ' －',
            'is_barrier_free': '－',
            'address': '東京都目黒区平町１丁目２５‐１４ 右山ビル'
        },
        'ソフトバンク学芸大学': {
            'class_name': 'ソフトバンク学芸大学',
            'phone_number': '03-5768-5966',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都目黒区鷹番３丁目２０‐４ 山崎ビル１Ｆ'
        },
        'ソフトバンク中目黒': {
            'class_name': 'ソフトバンク中目黒',
            'phone_number': '03-3792-5831',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都目黒区上目黒１丁目２０‐５ 和田ビル１Ｆ'
        }
    }, (('13', '131113'), '大田区（11）'): {
        'ソフトバンク蒲田東急プラザ': {
            'class_name': 'ソフトバンク蒲田東急プラザ',
            'phone_number': '03-3733-5481',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都大田区西蒲田７丁 目６９‐１ 蒲田東急プラザ７Ｆ'
        },
        'ソフトバンク蒲田': {
            'class_name': 'ソフトバンク蒲田',
            'phone_number': '03-6715-9703',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都大田区蒲田４丁目１‐１ エクセルダイア蒲田ネクスト１Ｆ'
        }
    }, (('13', '131121'), '世田谷区（15）'): {
        'ソフトバンク桜新町': {
            'class_name': 'ソフトバンク桜新町',
            'phone_number': '03-5451-3011',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都世田谷区桜新町１丁目１５‐２０ サンライク桜新町１Ｆ'
        },
        'ソフトバンク成城学園': {
            'class_name': 'ソフトバンク成城学園',
            'phone_number': '03-3417-8181',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都世田谷区成城２丁目４０‐５ ヴェルドミール成城１Ｆ'
        },
        'ソフトバンク三軒茶屋': {
            'class_name': 'ソフトバンク三軒茶屋',
            'phone_number': '03-5486-7050',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都世田谷区太子堂４丁目３‐２ 三軒茶屋ビル１Ｆ'
        },
        'ソフトバンク三軒茶屋茶沢通り': {
            'class_name': 'ソフトバンク三軒茶屋茶沢通り',
            'phone_number': '03-5433-4191',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都世田谷区太子堂４丁目２９‐１ 萩原ビル１階'
        },
        'ソフトバンク下北沢': {
            'class_name': 'ソフトバンク下北沢',
            'phone_number': '03-6859-1100',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都世田谷区北沢２丁目１３‐７ 片野ビル１Ｆ、２Ｆ'
        },
        'ソフトバンク千歳烏山': {
            'class_name': 'ソフトバンク千歳烏山',
            'phone_number': '03-5314-6626',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都世田谷区南烏山４丁目１２‐５ 並木ビル１Ｆ'
        }
    }, (('13', '131130'), '渋谷区（6 ）'): {
        'ソフトバンク渋谷': {
            'class_name': 'ソフトバンク渋谷',
            'phone_number': '03-5459-6625',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都渋谷区宇田川町２７‐４ 喜山ビル'
        },
        'ソフトバンク表参道': {
            'class_name': 'ソフトバンク表参道',
            'phone_number': '03-6406-0711',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都渋谷区神宮前１丁目１３‐９ アルテカプラザ１Ｆ'
        },
        'ソフトバンク笹塚': {
            'class_name': ' ソフトバンク笹塚',
            'phone_number': '03-5302-3681',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都渋谷区笹塚２丁目１４‐１５ ヴェルト笹塚ツインビル１ １Ｆ'
        }
    }, (('13', '131148'), '中野区（4）'): {}, (('13', '131156'), '杉並区（7）'): {
        'ソフトバンク方南町駅前': {
            'class_name': 'ソフトバンク方南町駅前',
            'phone_number': '03-6867-8700',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都杉並区方南２丁目２１‐３ アコード方南ビル１階'
        },
        'ソフトバンク高円寺': {
            'class_name': 'ソフトバンク高円寺',
            'phone_number': '03-5929-1891',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都杉並区高円寺南４丁目７‐１０ 高円寺ビル１Ｆ'
        },
        'ソフトバンク阿佐ヶ谷': {
            'class_name': ' ソフトバンク阿佐ヶ谷',
            'phone_number': '03-5929-8617',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都杉並区阿佐谷南１丁目４７ ‐１２'
        },
        'ソフトバンク西荻窪': {
            'class_name': 'ソフトバンク西荻窪',
            'phone_number': '03-5303-1915',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都杉並区西荻北３丁目２‐７グロリアス西荻窪１Ｆ'
        },
        'ソフトバンク荻窪': {
            'class_name': 'ソフトバンク荻窪',
            'phone_number': '03-5347-4431',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都杉並区上荻１丁目１７‐１ シンフォニーシティ荻窪１階'
        }
    }, (('13', '131164'), '豊島区（8）'): {
        'ソフトバンク池袋東口駅前': {
            'class_name': 'ソフトバンク池袋東口駅前',
            'phone_number': '03-6384-7151',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都豊島区南池袋１丁目２６‐６Ｔｈｅ ＳＨ ｏｎｅ １Ｆ、２Ｆ'
        },
        'ソフトバンク池袋西口': {
            'class_name': 'ソフトバンク池袋西口',
            'phone_number': '03-5951-6790',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都豊島区西池袋１丁 目１６‐１０ 第２三笠ビル'
        },
        'ソフトバンク大塚': {
            'class_name': 'ソフトバンク大塚',
            'phone_number': '03-5961-3351',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都豊島区北大塚２丁目１６‐８ バロックコート大塚１０１号'
        },
        'ソフトバンク巣鴨': {
            'class_name': 'ソフトバンク 巣鴨',
            'phone_number': '03-5978-6613',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都豊島区巣鴨１丁目１８番８号 巣鴨東宝ビル１Ｆ'
        },
        'ソフトバンク駒込': {
            'class_name': 'ソフトバンク駒込',
            'phone_number': '03-5395-1023',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都豊島区駒込１丁目４２‐２ ライオンズマンション駒込駅前１０１'
        }
    }, (('13', '131172'), '北区（4）'): {
        'ソフトバンク王子駅前': {
            'class_name': 'ソフトバンク王子駅前',
            'phone_number': '03-6903-0375',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都北区王子２丁目３０‐３ ニッセイ王子ビル１階'
        },
        'ソフトバンク赤羽駅前': {
            'class_name': 'ソフトバンク赤羽駅前',
            'phone_number': '03-3903-5112',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都北区赤羽１丁目１６‐２ ＴＮ‐１ｓｔビル１階'
        }
    }, (('13', '131181'), '荒川区（4）'): {
        'ソフ トバンク日暮里': {
            'class_name': 'ソフトバンク日暮里',
            'phone_number': '03-5604-3551',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都荒川区西日暮里２丁目１９‐４ たちばなビル１・２Ｆ'
        }
    }, (('13', '131199'), '板橋区（7）'): {
        'ソフトバンク成増': {
            'class_name': 'ソフトバンク成増',
            'phone_number': '03-5967-7371',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都板橋区成増１丁目３１‐７ クリーンビル１Ｆ'
        },
        'ソフトバンク志村坂上': {
            'class_name': 'ソフトバンク志村坂上',
            'phone_number': '03-3967-4100',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都板橋区小豆沢２丁目１７‐７キャッスルマンション志村坂上 １階'
        },
        'ソフトバンク高島平': {
            'class_name': 'ソフトバンク高島平',
            'phone_number': '03-5922-6690',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都板橋区高島平８丁目４‐１２ ロイヤルステージ恵比寿１Ｆ'
        }
    }, (('13', '131202'), '練馬区（9）'): {
        'ソフトバンク練馬': {
            'class_name': 'ソフトバンク練馬',
            'phone_number': '03-5946-5077',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都練馬区豊玉北５丁目１７‐７ ネリマビル１Ｆ、Ｂ１Ｆ'
        },
        'ソフトバンク石神井公園': {
            'class_name': 'ソフトバンク石神井公園',
            'phone_number': '03-5923-0388',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都練馬区石神井町３丁目２５‐１ きくやビル１階'
        },
        'ソフトバンク大泉学園': {
            'class_name': 'ソフトバンク大泉学園',
            'phone_number': '03-5947-5336',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都練馬区東大泉１丁目３４‐１ 笹仙ビル１Ｆ'
        },
        'ソフトバンク光が丘': {
            'class_name': 'ソフトバ ンク光が丘',
            'phone_number': '03-5967-4171',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都練馬区光が丘５丁目１‐１ ＩＭＡ３Ｆ'
        }
    }, (('13', '131211'), '足立区（8）'): {
        'ソフトバンクアリオ西新井': {
            'class_name': 'ソフトバンクアリオ西新井',
            'phone_number': '03-5888-3133',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都足立区西新井栄町１丁目２０番１号 アリオ西新井２階'
        },
        'ソフトバンク綾瀬': {
            'class_name': 'ソフトバンク綾瀬',
            'phone_number': '03-5613-1886',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都足立区綾瀬３丁目５‐２０ 柏芳ビル参号館１Ｆ'
        },
        'ソフトバンク保木間': {
            'class_name': 'ソフトバンク保木間',
            'phone_number': '03-5851-0622',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都足立区保木間１丁目３３‐１７'
        },
        'ソフトバンク竹ノ塚': {
            'class_name': 'ソフトバンク竹ノ塚',
            'phone_number': '03-5831-1355',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都足立区竹の塚６丁目１２‐１１'
        }
    }, (('13', '131229'), '葛飾区（5）'): {
        'ソフトバンク新小岩': {
            'class_name': 'ソフトバンク新小岩',
            'phone_number': '03-5663-1790',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都葛飾区新小岩１丁目５０‐１ 新小岩Ｓビル１Ｆ'
        },
        'ソフトバンク青砥駅前': {
            'class_name': 'ソフトバンク青砥駅前',
            'phone_number': '03-5680-1125',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都葛飾区青戸３丁目３７‐１９'
        },
        'ソフトバンク亀有': {
            'class_name': 'ソフトバンク亀有',
            'phone_number': '03-5629-4661',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都葛飾区亀有３丁目３２‐８ 亀有３丁目ビル１階'
        }
    }, (('13', '131237'), '江戸川区（8）'): {
        'ソフトバンク西葛西': {
            'class_name': 'ソフトバンク西葛西',
            'phone_number': '03-5658-4251',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都江戸川区西葛西６丁目１３‐７ 第７山秀ビル２Ｆ'
        },
        'ソ フトバンク葛西': {
            'class_name': 'ソフトバンク葛西',
            'phone_number': '03-6808-0861',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都江戸川区東葛西６丁目１‐１２アビタシオン葛西１Ｆ'
        },
        'ソフトバンク船堀': {
            'class_name': 'ソフトバンク船堀',
            'phone_number': '03-5675-7405',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都江戸川区船堀３丁目５‐７ ＴＯＫＩビル１Ｆ'
        },
        'ソフトバンク瑞江': {
            'class_name': 'ソフトバンク瑞江',
            'phone_number': '03-6638-3731',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都江戸川区東瑞江１丁目２６ー１５ 瑞江ジーエスビル１Ｆ'
        },
        'ソフトバンク小岩昭和通り': {
            'class_name': 'ソフトバンク小岩昭和通り',
            'phone_number': '03-6892-2750',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都江戸川区南小岩７丁目２７ー２地場ビル１階'
        }
    }, (('13', '132012'), '八王子市（9）'): {
        'ソフ トバンクフォレストモール南大沢': {
            'class_name': 'ソフトバンクフォレストモール南大沢',
            'phone_number': '042-677-7773',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都八王子市南大沢２丁目２５ フォレストモール南大沢１階'
        },
        'ソフトバンク八王子': {
            'class_name': 'ソフトバ ンク八王子',
            'phone_number': '042-620-4161',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都八王子市中町５‐１０'
        },
        'ソフトバンク西八王子': {
            'class_name': 'ソフトバンク西八王子',
            'phone_number': '042-662-4651',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都八王子市千人町２丁目２０‐１デラパン西八王子駅前ビル１Ｆ'
        },
        'ソフトバンクｉｉａｓ高尾': {
            'class_name': 'ソフトバンクｉｉａｓ高尾',
            'phone_number': '042-673-4557',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都八王子市東浅川町５５０‐１ ｉｉａｓ高尾２Ｆ'
        }
    }, (('13', '132021'), '立川市（3）'): {
        'ソフトバンク立川南': {
            'class_name': 'ソフトバンク立川南',
            'phone_number': '042-528-8777',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都立川市柴崎町３丁目６‐１ 立川Ｎビル'
        },
        'ソフトバンクららぽーと立川立飛': {
            'class_name': 'ソフト バンクららぽーと立川立飛',
            'phone_number': '042-512-6771',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都立川市泉町９３５‐ １ ららぽーと立川立飛３０４０'
        }
    }, (('13', '132039'), '武蔵野市（4）'): {
        'ソフトバンク吉祥寺サンロード': {
            'class_name': 'ソフトバンク吉祥寺サンロード',
            'phone_number': '0422-21-7911',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都武蔵野市吉祥寺本町１丁目９‐８'
        },
        'ソフトバンクイトーヨーカドー武蔵境': {
            'class_name': 'ソフトバンクイトーヨーカドー武蔵境',
            'phone_number': '0422-33-5421',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都武蔵野市境南町２丁目３‐６ イトーヨーカドー武蔵境西館４階'
        }
    }, (('13', '132047'), '三鷹市（1）'): {
        'ソフトバンク三鷹': {
            'class_name': 'ソフトバンク三鷹',
            'phone_number': '0422-40-2200',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都三鷹市下連雀３丁目２７‐１３ 正栄ビル１Ｆ'
        }
    }, (('13', '132055'), '青梅市（1）'): {}, (('13', '132063'), '府中市（2）'): {
        'ソフトバンク府中': {
            'class_name': 'ソフトバンク府中',
            'phone_number': '042-362-0021',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': ' 東京都府中市宮町１丁目１００武蔵府中ル・シーニュ２階'
        }
    }, (('13', '132071'), '昭島市（1）'): {
        'ソフトバンクモリタウン昭島': {
            'class_name': 'ソフトバンクモリタウン昭島',
            'phone_number': '042-542-0972',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都昭島市田中町５６２‐１ モリタウン東館２Ｆ'
        }
    }, (('13', '132080'), '調布市（4）'): {
        'ソフトバンクホームズ仙川': {
            'class_name': 'ソフトバンクホームズ仙川',
            'phone_number': '03-5314-2195',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都調布市若葉町２丁目１‐７ ２Ｆ'
        },
        'ソフトバ ンクＢＲＡＮＣＨ調布': {
            'class_name': 'ソフトバンクＢＲＡＮＣＨ調布',
            'phone_number': '042-426-2218',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都調布市深大寺東町７丁目４７‐１ブランチ調布１階'
        }
    }, (('13', '132098'), '町田市（8）'): {
        'ソフトバンク南町田グランベリーパーク': {
            'class_name': 'ソフトバンク南町田グランベリーパーク',
            'phone_number': '042-788-7330',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都町田市鶴間３丁目４‐１'
        },
        'ソフトバンク成瀬': {
            'class_name': 'ソフトバンク成瀬',
            'phone_number': '042-706-8862',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都町田市南成瀬４丁目２‐４'
        },
        'ソフトバンク町田ジョルナ': {
            'class_name': 'ソフトバンク町田 ジョルナ',
            'phone_number': '042-710-6201',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都町田市原町田６丁目６‐１４ 町田ジョルナ１Ｆ'
        },
        'ソフトバンク町田駅前': {
            'class_name': 'ソフトバンク町田駅前',
            'phone_number': '042-710-0027',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都町田市原町田６丁目１１‐１１'
        },
        'ソフトバンク鶴川': {
            'class_name': 'ソフトバンク鶴川',
            'phone_number': '042-708-1922',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都町田市能ヶ谷２丁目１２‐５４ メゾンナツウメ１階'
        }
    }, (('13', '132101'), '小金井市（1）'): {
        'ソフトバンク武蔵小金井': {
            'class_name': 'ソフトバンク武蔵小金井',
            'phone_number': '042-386-6333',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都小金井市本町６丁目１４‐４５ｎｏｎｏｗａ武蔵小金井１階'
        }
    }, (('13', '132110'), '小平市（3）'): {
        ' ソフトバンク花小金井': {
            'class_name': 'ソフトバンク花小金井',
            'phone_number': '042-451-9530',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都小平市花小金井南町１丁目２７‐２２ Ｒ・Ｙビルディングサウス１Ｆ'
        }
    }, (('13', '132128'), '日野市（3）'): {
        'ソフトバンクイ オンモール多摩平の森': {
            'class_name': 'ソフトバンクイオンモール多摩平の森',
            'phone_number': '042-589-2888',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都日野市多摩平２丁目４番地１ ２Ｆ'
        }
    }, (('13', '132136'), '東村山市（3）'): {
        'ソフトバンク新秋津': {
            'class_name': 'ソフトバンク新秋津',
            'phone_number': '042-399-0071',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都東村山市秋津町５丁目１３ ‐５'
        }
    }, (('13', '132144'), '国分寺市（3）'): {
        'ソフトバンク国分寺': {
            'class_name': 'ソフトバンク国分寺',
            'phone_number': '042-328-1414',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都国分寺市本町４丁目１３‐５'
        }
    }, (('13', '132152'), '国立市（2）'): {
        'ソフトバンク国立': {
            'class_name': 'ソフトバンク国立',
            'phone_number': '042-501-2440',
            'has_parking': '－',
            'is_barrier_free': '－',
            'address': '東京都国立市東１丁目７‐１０ レジディア国立１階'
        }
    }, (('13', '132187'), '福生市（1）'): {}, (('13', '132195'), '狛江市（1）'): {}, (('13', '132209'), '東大和市（1）'): {
        'ソフトバンク東大和向原': {
            'class_name': 'ソフトバンク東大和向原',
            'phone_number': '042-590-0555',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都東大和市向原２丁目１‐１'
        }
    }, (('13', '132217'), '清瀬市（1）'): {
        'ソフトバンク清瀬': {
            'class_name': 'ソフトバンク清瀬',
            'phone_number': '042-492-5104',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都清瀬市元町１丁目８‐３５ アマルフィ'
        }
    }, (('13', '132225'), '東久留米市（2）'): {
        'ソフトバンク東久留米幸町': {
            'class_name': 'ソフトバンク東久留米幸町',
            'phone_number': '042-476-8721',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都東久留米市幸町５丁目５‐５ メゾンアイエス１Ｆ'
        }
    }, (('13', '132233'), '武蔵村山市（1）'): {}, (('13', '132241'), '多摩市（3）'): {
        'ソフトバンクグリナード永山': {
            'class_name': 'ソフトバンクグリ ナード永山',
            'phone_number': '042-311-3910',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都多摩市永山１丁目４ グリナード永山１号館２階'
        },
        'ソフトバンクココリア多摩センター': {
            'class_name': 'ソフトバンクココリア多摩センター',
            'phone_number': '042-355-6333',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都多摩市落合１丁目４６‐１ ココリア多摩センター２Ｆ'
        },
        'ソフトバンク聖蹟桜ヶ丘オー パ': {
            'class_name': 'ソフトバンク聖蹟桜ヶ丘オーパ',
            'phone_number': '042-311-2611',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都多摩市関戸４丁目７２番地 聖蹟桜ヶ丘ＯＰＡ５Ｆ'
        }
    }, (('13', '132250'), '稲城市（2）'): {
        'ソフトバンク矢野口': {
            'class_name': 'ソフトバンク矢野口',
            'phone_number': '042-370-7711',
            'has_parking': 'None',
            'is_barrier_free': '－',
            'address': '東京都稲城市矢野口６２９‐３ ｓｕｅｒｔｅ矢野口１階'
        },
        'ソフトバンク若葉台': {
            'class_name': 'ソフトバンク若葉台',
            'phone_number': '042-350-7277',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都稲城市若葉台２丁目４‐２ フレスポ若葉台２階'
        }
    }, (('13', '132276'), '羽村市（2）'): {
        'ソフトバンク羽村': {
            'class_name': 'ソフトバンク羽村',
            'phone_number': '042-569-8161',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都羽村市羽東１丁目２３‐２９'
        }
    }, (('13', '132284'), 'あきる野市（0）'): {}, (('13', '132292'), '西東京市（3）'): {
        'ソフトバンク田無アスタ': {
            'class_name': 'ソフトバンク田無アスタ',
            'phone_number': '042-466-7601',
            'has_parking': 'None',
            'is_barrier_free': '○',
            'address': '東京都西東京市田無町２丁目１‐１ アスタ２Ｆショッピングプラザ 田無アスタ'
        },
        'ソフトバンク保谷': {
            'class_name': 'ソフトバンク保谷',
            'phone_number': '042-438-7552',
            'has_parking': ' －',
            'is_barrier_free': '－',
            'address': '東京都西東京市東町３丁目１３‐２'
        },
        'ソフトバンクひばりヶ丘': {
            'class_name': 'ソフトバンクひばり ヶ丘',
            'phone_number': '042-439-7256',
            'has_parking': '－',
            'is_barrier_free': '○',
            'address': '東京都西東京市住吉町３丁目１０‐２５ ＨＩＢＡＲＩＴＯＷＥＲ１階'
        }
    }, (('13', '133035'), '西多摩郡瑞穂町（1）'): {}, 
    (('13', '133051'), '西多摩郡日の出町（1）'): {}, 
    (('13', '133078'), '西多摩郡檜原村（0）'): {}, 
    (('13', '133086'), '西多摩郡奥多摩町（0）'): {}, 
    (('13', '133612'), '大島町（0）'): {}, 
    (('13', '133621'), '利島村（0）'): {}, 
    (('13', '133639'), '新島村（0）'): {}, 
    (('13', '133647'), '神津島村（0）'): {}, 
    (('13', '133817'), '三宅村（0）'): {}, 
    (('13', '133825'), '御蔵島村（0）'): {}, 
    (('13', '134015'), '八丈町（0）'): {}, 
    (('13', '134023'), '青ヶ島村（0）'): {}, 
    (('13', '134210'), '小笠原村（0）'): {}
}

data = {(('13', '131016'), '千代田区（4）'): {}, (('13', '131032'), '港区（7）'): {'ソフトバンク六本木': {'class_name': 'ソフトバンク六本木', 'phone_number': '03-5775-5011', 'has_parking': '－', 'is_barrier_free': '○', 'address': '東京都港区六本木４丁目９‐７ 三菱ＵＦＪ銀行六本木支店ビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T248/?cid=tpsk_191119_mobile'}}, (('13', '131024'), '中央区（5）'): {'ソフトバンク銀座': {'class_name': 'ソフトバンク銀座', 'phone_number': '03-6252-3333', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都中央区銀座５丁目７番８号', 'site_url': 'https://www.softbank.jp/shop/search/detail/TD31/?cid=tpsk_191119_mobile'}}, (('13', '131059'), '文京区（2）'): {}, (('13', '131067'), '台東区（4）'): {'ソフトバン ク浅草ＲＯＸ': {'class_name': 'ソフトバンク浅草ＲＯＸ', 'phone_number': '03-5827-0430', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都台東区浅草１丁目２５‐１５ 浅草ＲＯＸ １Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T168/?cid=tpsk_191119_mobile'}}, (('13', '131075'), '墨田区（4）'): {'ソフトバンクアルカキット錦糸町': {'class_name': 'ソフトバン クアルカキット錦糸町', 'phone_number': '03-5610-7283', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都墨田区錦糸２丁目２‐１ アルカキット錦糸町８階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T159/?cid=tpsk_191119_mobile'}, 'ソフトバンクオリナス錦糸町': {'class_name': 'ソフ トバンクオリナス錦糸町', 'phone_number': '03-5610-8830', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都墨田区太平４丁目２‐１オリナス ２Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/TH10/?cid=tpsk_191119_mobile'}}, (('13', '131041'), '新宿区（9）'): {'ソフトバンク新宿西口': {'class_name': 'ソフトバンク新宿西口', 'phone_number': '03-3348-5811', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都新宿区西新宿１丁 目１９‐５ 新宿幸容ビル', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1G5/?cid=tpsk_191119_mobile'}, 'ソフトバンク神楽坂': {'class_name': 'ソフトバンク神楽坂', 'phone_number': '03-5229-7150', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都新宿区神楽坂６丁目４７ 照井ビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1G0/?cid=tpsk_191119_mobile'}, 'ソフトバンク高田馬場': {'class_name': 'ソフトバンク高田馬場', 'phone_number': '03-3209-7841', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都新宿区高田馬場２丁目１３‐２ Ｐｒｉｍｅｇａｔｅ１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T132/?cid=tpsk_191119_mobile'}}, (('13', '131083'), '江東区（9）'): {'ソフトバンクイトーヨーカドー木場': {'class_name': 'ソフトバンクイトーヨーカドー木場', 'phone_number': '03-6666-5290', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都江東区木場１丁目５‐３０ イトーヨーカドー木場店', 'site_url': 'https://www.softbank.jp/shop/search/detail/TH87/?cid=tpsk_191119_mobile'}, 'ソフトバンクアリオ北 砂': {'class_name': 'ソフトバンクアリオ北砂', 'phone_number': '03-5665-0341', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都江東区北砂２丁目１７番地１号アリオ北砂２階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T2E3/?cid=tpsk_191119_mobile'}, 'ソフトバンクカメイドクロック': {'class_name': 'ソフトバンクカメイドクロック', 'phone_number': '03-3636-6692', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都江東区亀戸６丁目３１‐６ カメイドクロック３Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T131/?cid=tpsk_191119_mobile'}}, (('13', '131091'), '品川 区（10）'): {'ソフトバンク大森': {'class_name': 'ソフトバンク大森', 'phone_number': '03-3768-7390', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都品川区南大井６丁目２８‐１０', 'site_url': 'https://www.softbank.jp/shop/search/detail/T120/?cid=tpsk_191119_mobile'}, 'ソフトバンク阪急大井町ガーデン': {'class_name': 'ソフトバンク阪急大井町ガーデン', 'phone_number': '03-3778-6400', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都品川区大井１丁目５０‐５阪急大井町ガーデン２階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T119/?cid=tpsk_191119_mobile'}, 'ソフトバンク武蔵小山パルム': {'class_name': 'ソフトバンク武蔵小山パルム', 'phone_number': '03-6426-9700', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都品川区小山３丁目２１‐１３武蔵小山パルムＡ棟', 'site_url': 'https://www.softbank.jp/shop/search/detail/TH90/?cid=tpsk_191119_mobile'}, 'ソフトバンクパークシティ武蔵小山ザモール': {'class_name': 'ソフトバンクパークシティ武蔵小山ザモール', 'phone_number': '03-5749-1122', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都品川区小山３丁目１５‐１ パークシティ武蔵小山ザモール１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1A0/?cid=tpsk_191119_mobile'}, 'ソフトバンク目黒': {'class_name': 'ソフトバンク目 黒', 'phone_number': '03-3490-9561', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都品川区上大崎２丁目１８‐１６ 月乃ビル１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T175/?cid=tpsk_191119_mobile'}}, (('13', '131105'), '目黒区（5）'): {'ソフトバンク自由が丘南口': {'class_name': 'ソフトバンク自由が丘南口', 'phone_number': '03-6891-6770', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都目黒区自由が丘１丁目８‐ １ ミナミビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1V3/?cid=tpsk_191119_mobile'}, 'ソフトバンク都立大学': {'class_name': 'ソフトバンク都立大学', 'phone_number': '03-5731-0040', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都目黒区平町１丁目２５‐１４ 右山ビル', 'site_url': 'https://www.softbank.jp/shop/search/detail/TD05/?cid=tpsk_191119_mobile'}, 'ソフトバンク学芸大学': {'class_name': 'ソフトバンク学芸大学', 'phone_number': '03-5768-5966', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都目黒区鷹番３丁目２０‐４ 山崎ビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T145/?cid=tpsk_191119_mobile'}, 'ソフトバンク中目黒': {'class_name': 'ソフトバンク中目黒', 'phone_number': '03-3792-5831', 'has_parking': '－', 'is_barrier_free': '○', 'address': '東京都目黒区上目黒１丁目２０‐５ 和田ビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T176/?cid=tpsk_191119_mobile'}}, (('13', '131113'), '大田区（11）'): {'ソフトバンク蒲田東急プラザ': {'class_name': 'ソフトバンク蒲田東急プラザ', 'phone_number': '03-3733-5481', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都大田区西蒲田７丁目６９‐１ 蒲田東急プラザ７Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T187/?cid=tpsk_191119_mobile'}, 'ソフトバンク蒲田': {'class_name': 'ソフトバンク蒲田', 'phone_number': '03-6715-9703', 'has_parking': '－', 'is_barrier_free': '○', 'address': '東京都大田区蒲田４丁目１‐１ エクセルダイア蒲田ネクスト１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/TH79/?cid=tpsk_191119_mobile'}}, (('13', '131130'), '渋谷区（6）'): {'ソフトバンク渋谷': {'class_name': 'ソフトバンク渋谷', 'phone_number': '03-5459-6625', 'has_parking': '－', 'is_barrier_free': '○', 'address': '東京都渋谷区宇田川町２７‐４ 喜山ビル', 'site_url': 'https://www.softbank.jp/shop/search/detail/T198/?cid=tpsk_191119_mobile'}, 'ソフト バンク表参道': {'class_name': 'ソフトバンク表参道', 'phone_number': '03-6406-0711', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都渋谷区神宮前１丁目１３‐９ アルテカプラザ１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1D3/?cid=tpsk_191119_mobile'}, 'ソフトバンク笹塚': {'class_name': 'ソフトバンク笹塚', 'phone_number': '03-5302-3681', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都渋谷区笹塚２丁目１４‐ １５ ヴェルト笹塚ツインビル１ １Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T196/?cid=tpsk_191119_mobile'}}, (('13', '131148'), '中野区（4）'): {}, (('13', '131121'), '世田谷区（15）'): {'ソフトバンク桜新町': {'class_name': 'ソフトバンク桜新町', 'phone_number': '03-5451-3011', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都世田谷区桜新町１丁目１５‐２０ サンライク桜新町１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1V4/?cid=tpsk_191119_mobile'}, 'ソフトバンク成城学園': {'class_name': 'ソフトバンク成城学園', 'phone_number': '03-3417-8181', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都世田谷区成城２丁目４０‐５ ヴェルドミール成城１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T118/?cid=tpsk_191119_mobile'}, 'ソフトバンク三軒茶屋': {'class_name': 'ソフ トバンク三軒茶屋', 'phone_number': '03-5486-7050', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都世田谷区太子堂４丁目３‐２ 三軒茶屋ビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T144/?cid=tpsk_191119_mobile'}, 'ソフトバンク三軒茶屋茶沢通り': {'class_name': 'ソフトバン ク三軒茶屋茶沢通り', 'phone_number': '03-5433-4191', 'has_parking': '－', 'is_barrier_free': '○', 'address': '東京都世田谷区太子堂４丁目２９‐１ 萩原ビル１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1I3/?cid=tpsk_191119_mobile'}, 'ソフトバンク下北沢': {'class_name': 'ソフトバンク下北沢', 'phone_number': '03-6859-1100', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都世田谷区北沢２丁目１３‐７ 片野ビル１Ｆ、２Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T178/?cid=tpsk_191119_mobile'}, 'ソフトバンク千歳烏山': {'class_name': 'ソフトバンク千歳烏山', 'phone_number': '03-5314-6626', 'has_parking': '－', 'is_barrier_free': '○', 'address': '東京都世田谷区南烏山４丁目１２‐５ 並木ビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T111/?cid=tpsk_191119_mobile'}}, (('13', '131156'), '杉並区（7）'): {'ソフトバンク方南町駅前': {'class_name': 'ソフトバンク方南町駅前', 'phone_number': '03-6867-8700', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都杉並区方南２丁目２１‐３ アコード方南ビル１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/TD45/?cid=tpsk_191119_mobile'}, 'ソフトバンク高円寺': {'class_name': 'ソフトバンク高円寺', 'phone_number': '03-5929-1891', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都杉並区高円寺南４丁目７‐１０ 高円寺ビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T138/?cid=tpsk_191119_mobile'}, 'ソフトバンク阿佐ヶ谷': {'class_name': 'ソフトバンク阿佐ヶ谷', 'phone_number': '03-5929-8617', 'has_parking': '－', 'is_barrier_free': '○', 'address': '東京都杉並区阿佐谷南１丁目４７‐１２', 'site_url': 'https://www.softbank.jp/shop/search/detail/T189/?cid=tpsk_191119_mobile'}, 'ソフトバンク西荻窪': {'class_name': 'ソフトバンク西荻窪', 'phone_number': '03-5303-1915', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都杉並区西荻北３丁目２‐７グロリアス西荻窪１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1L8/?cid=tpsk_191119_mobile'}, 'ソフトバンク荻窪': {'class_name': 'ソフトバンク荻 窪', 'phone_number': '03-5347-4431', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都杉並区上荻１丁目１７‐１ シンフォニーシティ荻窪１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T182/?cid=tpsk_191119_mobile'}}, (('13', '131164'), '豊島区（8）'): {'ソフトバンク池袋東口駅前': {'class_name': 'ソフトバンク池袋東口駅前', 'phone_number': '03-6384-7151', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都豊島区南池袋 １丁目２６‐６Ｔｈｅ ＳＨ ｏｎｅ １Ｆ、２Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/TJ01/?cid=tpsk_191119_mobile'}, 'ソフトバンク池袋西 口': {'class_name': 'ソフトバンク池袋西口', 'phone_number': '03-5951-6790', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都豊島区西池袋１丁目１６‐１０ 第２三笠ビル', 'site_url': 'https://www.softbank.jp/shop/search/detail/T195/?cid=tpsk_191119_mobile'}, 'ソフトバンク大塚': {'class_name': 'ソフトバンク大塚', 'phone_number': '03-5961-3351', 'has_parking': '－', 'is_barrier_free': '○', 'address': '東京都豊島区北大塚２丁目１６‐８ バロックコート大塚１０１号', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1A3/?cid=tpsk_191119_mobile'}, 'ソフトバンク巣鴨': {'class_name': 'ソフトバンク 巣鴨', 'phone_number': '03-5978-6613', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都豊島区巣鴨１丁目１８番８号 巣鴨東宝ビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1B9/?cid=tpsk_191119_mobile'}, 'ソフトバンク駒込': {'class_name': 'ソフトバンク駒込', 'phone_number': '03-5395-1023', 'has_parking': '－', 'is_barrier_free': '○', 'address': '東 京都豊島区駒込１丁目４２‐２ ライオンズマンション駒込駅前１０１', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1A2/?cid=tpsk_191119_mobile'}}, (('13', '131181'), '荒川区（4）'): {'ソフトバンク日暮里': {'class_name': 'ソフトバンク日暮里', 'phone_number': '03-5604-3551', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都荒川区西日暮里２丁目１９‐４ たちばなビル１・２Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T160/?cid=tpsk_191119_mobile'}}, (('13', '131172'), '北区（4）'): {'ソフトバンク王子 駅前': {'class_name': 'ソフトバンク王子駅前', 'phone_number': '03-6903-0375', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都北区王子２丁目３０‐３ ニッセイ王子ビル１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/TD43/?cid=tpsk_191119_mobile'}, 'ソフトバンク赤羽駅前': {'class_name': 'ソフトバンク赤羽駅前', 'phone_number': '03-3903-5112', 'has_parking': '－', 'is_barrier_free': '○', 'address': '東京都北区赤羽１丁目１６‐２ ＴＮ‐１ｓｔビル１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/TD20/?cid=tpsk_191119_mobile'}}, (('13', '131199'), '板橋区（7）'): {'ソフトバ ンク成増': {'class_name': 'ソフトバンク成増', 'phone_number': '03-5967-7371', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都板橋区成増１丁目３１‐７ クリーンビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T181/?cid=tpsk_191119_mobile'}, 'ソフトバンク志村坂上': {'class_name': 'ソフトバンク志村坂上', 'phone_number': '03-3967-4100', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都板橋区小豆沢２丁目１７‐ ７キャッスルマンション志村坂上 １階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1O3/?cid=tpsk_191119_mobile'}, 'ソフトバンク高島平': {'class_name': 'ソフトバンク高島平', 'phone_number': '03-5922-6690', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都板橋区高島平８丁目４‐１ ２ ロイヤルステージ恵比寿１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1Q9/?cid=tpsk_191119_mobile'}}, (('13', '131202'), '練馬区（9）'): {'ソフトバンク練馬': {'class_name': 'ソフトバンク練馬', 'phone_number': '03-5946-5077', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都練馬区豊玉北５丁目１７‐７ ネリマビル１Ｆ、Ｂ１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T101/?cid=tpsk_191119_mobile'}, 'ソフトバンク 石神井公園': {'class_name': 'ソフトバンク石神井公園', 'phone_number': '03-5923-0388', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都練馬区石神井町３丁目２５‐１ きくやビル１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1O8/?cid=tpsk_191119_mobile'}, 'ソフトバンク大泉学園': {'class_name': 'ソフトバンク大泉学園', 'phone_number': '03-5947-5336', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都練馬区東大泉１丁目 ３４‐１ 笹仙ビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/TD15/?cid=tpsk_191119_mobile'}, 'ソフトバンク光が丘': {'class_name': 'ソフトバンク光が丘', 'phone_number': '03-5967-4171', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都練馬区光が丘５丁目１‐１ ＩＭＡ３Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T183/?cid=tpsk_191119_mobile'}}, (('13', '131211'), '足立区（8）'): {'ソフトバンクアリオ西新井': {'class_name': 'ソフトバンクアリオ西新井', 'phone_number': '03-5888-3133', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都足立区西新井栄 町１丁目２０番１号 アリオ西新井２階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1L2/?cid=tpsk_191119_mobile'}, 'ソフトバンク綾瀬': {'class_name': 'ソフトバンク綾瀬', 'phone_number': '03-5613-1886', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都足立区綾瀬３丁目５‐２０ 柏芳ビル参号館１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1J8/?cid=tpsk_191119_mobile'}, 'ソフトバンク保木間': {'class_name': 'ソフトバン ク保木間', 'phone_number': '03-5851-0622', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都足立区保木間１丁目３３‐１７', 'site_url': 'https://www.softbank.jp/shop/search/detail/TG77/?cid=tpsk_191119_mobile'}, 'ソフトバンク竹ノ塚': {'class_name': 'ソフトバンク竹ノ塚', 'phone_number': '03-5831-1355', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都足立区竹の塚６丁目１２‐１１', 'site_url': 'https://www.softbank.jp/shop/search/detail/T191/?cid=tpsk_191119_mobile'}}, (('13', '131229'), '葛飾区（5）'): {'ソフトバンク新小岩': {'class_name': 'ソフトバンク新小岩', 'phone_number': '03-5663-1790', 'has_parking': 'None', 'is_barrier_free': '○', 'address': ' 東京都葛飾区新小岩１丁目５０‐１ 新小岩Ｓビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T124/?cid=tpsk_191119_mobile'}, 'ソフトバンク 青砥駅前': {'class_name': 'ソフトバンク青砥駅前', 'phone_number': '03-5680-1125', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都葛飾区青戸３丁目３７‐１９', 'site_url': 'https://www.softbank.jp/shop/search/detail/T100/?cid=tpsk_191119_mobile'}, 'ソフトバンク亀有': {'class_name': 'ソフト バンク亀有', 'phone_number': '03-5629-4661', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都葛飾区亀有３丁目３２‐８ 亀有３丁目ビル１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T193/?cid=tpsk_191119_mobile'}}, (('13', '132012'), '八王子市（9）'): {'ソフトバンクフォレストモ ール南大沢': {'class_name': 'ソフトバンクフォレストモール南大沢', 'phone_number': '042-677-7773', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都八王子市南大沢２丁目２５ フォレストモール南大沢１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1L0/?cid=tpsk_191119_mobile'}, ' ソフトバンク八王子': {'class_name': 'ソフトバンク八王子', 'phone_number': '042-620-4161', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都八王子市中町５‐１０', 'site_url': 'https://www.softbank.jp/shop/search/detail/T106/?cid=tpsk_191119_mobile'}, 'ソフトバンク西八王子': {'class_name': ' ソフトバンク西八王子', 'phone_number': '042-662-4651', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都八王子市千人町２丁目２０‐１デラ パン西八王子駅前ビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T108/?cid=tpsk_191119_mobile'}, 'ソフトバンクｉｉａｓ高尾': {'class_name': 'ソフトバンクｉｉａｓ高尾', 'phone_number': '042-673-4557', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都八王子市東浅川町５５０‐１ ｉｉａｓ高尾２Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/TD50/?cid=tpsk_191119_mobile'}}, (('13', '131237'), '江戸川区（8）'): {'ソフトバンク西葛西': {'class_name': 'ソフトバンク西葛西', 'phone_number': '03-5658-4251', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都江戸川区西葛西６丁目１３‐７ 第７山秀ビル２Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T140/?cid=tpsk_191119_mobile'}, 'ソフトバンク葛西': {'class_name': 'ソフトバンク葛西', 'phone_number': '03-6808-0861', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都江戸川区東葛西６丁目１‐ １２アビタシオン葛西１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1V2/?cid=tpsk_191119_mobile'}, 'ソフトバンク船堀': {'class_name': 'ソ フトバンク船堀', 'phone_number': '03-5675-7405', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都江戸川区船堀３丁目５‐７ ＴＯＫＩビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T139/?cid=tpsk_191119_mobile'}, 'ソフトバンク瑞江': {'class_name': 'ソフトバンク瑞江', 'phone_number': '03-6638-3731', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都江戸川区東瑞江１丁目２６ー１５瑞江ジーエスビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T172/?cid=tpsk_191119_mobile'}, 'ソフトバンク小岩昭和通り': {'class_name': 'ソフトバンク小岩昭和通り', 'phone_number': '03-6892-2750', 'has_parking': '－', 'is_barrier_free': '○', 'address': '東京都江戸川区南小岩７丁目２７ー２地場ビル１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/TG16/?cid=tpsk_191119_mobile'}}, (('13', '132021'), '立川市（3）'): {'ソフトバンク立川南': {'class_name': 'ソフトバンク立川南', 'phone_number': '042-528-8777', 'has_parking': '－', 'is_barrier_free': '○', 'address': '東京都立川市柴崎町３丁目６‐１ 立川Ｎビル', 'site_url': 'https://www.softbank.jp/shop/search/detail/T123/?cid=tpsk_191119_mobile'}, 'ソフトバンクららぽーと立川立飛': {'class_name': 'ソフトバンクららぽーと立川 立飛', 'phone_number': '042-512-6771', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都立川市泉町９３５‐１ ららぽーと立川立飛３０４０', 'site_url': 'https://www.softbank.jp/shop/search/detail/TG99/?cid=tpsk_191119_mobile'}}, (('13', '132039'), '武蔵野市（4）'): {'ソフトバンク吉祥寺サンロ ード': {'class_name': 'ソフトバンク吉祥寺サンロード', 'phone_number': '0422-21-7911', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都武蔵野市吉祥寺本町１丁目９‐８', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1J3/?cid=tpsk_191119_mobile'}, 'ソフトバンクイトーヨーカドー武蔵境': {'class_name': 'ソフトバンクイトーヨーカドー武蔵境', 'phone_number': '0422-33-5421', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都武蔵野市境南町２丁目３‐６ イトーヨーカドー武蔵境西館４階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T150/?cid=tpsk_191119_mobile'}}, (('13', '132055'), '青梅市（1）'): {}, (('13', '132047'), '三鷹市（1）'): {'ソフトバンク三鷹': {'class_name': 'ソフトバンク三鷹', 'phone_number': '0422-40-2200', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都三鷹市下連雀３丁目２７‐１３ 正栄ビル１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T137/?cid=tpsk_191119_mobile'}}, (('13', '132063'), '府中市（2）'): {'ソフトバンク府中': {'class_name': 'ソフトバンク府中', 'phone_number': '042-362-0021', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都府中市宮町１丁目１００武蔵府中ル・シーニュ２階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T152/?cid=tpsk_191119_mobile'}}, (('13', '132071'), '昭島市（1）'): {'ソフトバンクモリタウン昭島': {'class_name': 'ソフト バンクモリタウン昭島', 'phone_number': '042-542-0972', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都昭島市田中町５６２‐１ モリタウン東館２Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T103/?cid=tpsk_191119_mobile'}}, (('13', '132080'), '調布市（4）'): {'ソフトバンクホー ムズ仙川': {'class_name': 'ソフトバンクホームズ仙川', 'phone_number': '03-5314-2195', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都調布市若葉町２丁目１‐７ ２Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/TH99/?cid=tpsk_191119_mobile'}, 'ソフトバンクＢＲＡＮＣＨ調布': {'class_name': 'ソフトバンクＢＲＡＮＣＨ調布', 'phone_number': '042-426-2218', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都調布市深大寺 東町７丁目４７‐１ブランチ調布１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1I4/?cid=tpsk_191119_mobile'}}, (('13', '132101'), '小金井市（1）'): {'ソフトバンク武蔵小金井': {'class_name': 'ソフトバンク武蔵小金井', 'phone_number': '042-386-6333', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都小金井市本町６丁目１４‐４５ｎｏｎｏｗａ武蔵小金井１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T148/?cid=tpsk_191119_mobile'}}, (('13', '132110'), '小平市（3）'): {'ソフトバンク花小金井': {'class_name': 'ソフトバンク花小金井', 'phone_number': '042-451-9530', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都小平市花小金井南町１ 丁目２７‐２２ Ｒ・Ｙビルディングサウス１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1O2/?cid=tpsk_191119_mobile'}}, (('13', '132128'), '日野市（3）'): {'ソフトバンクイオンモール多摩平の森': {'class_name': 'ソフトバンクイオンモール多摩平の森', 'phone_number': '042-589-2888', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都日野市多摩平２丁目４番地 １ ２Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T147/?cid=tpsk_191119_mobile'}}, (('13', '132098'), '町田市（8）'): {'ソフトバンク南町田グランベリーパーク': {'class_name': 'ソフトバンク南町田グランベリーパーク', 'phone_number': '042-788-7330', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都町田市鶴間３丁目４‐１', 'site_url': 'https://www.softbank.jp/shop/search/detail/TH95/?cid=tpsk_191119_mobile'}, 'ソフトバンク成瀬': {'class_name': 'ソフトバンク成瀬', 'phone_number': '042-706-8862', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都町田市南成瀬４丁目２‐４', 'site_url': 'https://www.softbank.jp/shop/search/detail/TG28/?cid=tpsk_191119_mobile'}, 'ソフトバンク町田ジョルナ': {'class_name': 'ソフトバンク町田 ジョルナ', 'phone_number': '042-710-6201', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都町田市原町田６丁目６‐１４ 町田ジョルナ１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T110/?cid=tpsk_191119_mobile'}, 'ソフトバンク町田駅前': {'class_name': 'ソフトバンク町田駅前', 'phone_number': '042-710-0027', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都町田市原町田６丁目１１‐１１', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1F2/?cid=tpsk_191119_mobile'}, 'ソフトバンク鶴 川': {'class_name': 'ソフトバンク鶴川', 'phone_number': '042-708-1922', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都町田市能ヶ谷２丁目１２‐５４ メゾンナツウメ１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/TD21/?cid=tpsk_191119_mobile'}}, (('13', '132136'), '東村山市（3）'): {'ソフトバンク新秋津': {'class_name': 'ソフトバンク新秋津', 'phone_number': '042-399-0071', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都東村山市秋津町５丁目１３‐５', 'site_url': 'https://www.softbank.jp/shop/search/detail/TD14/?cid=tpsk_191119_mobile'}}, (('13', '132144'), '国分寺市（3）'): {'ソフトバンク国分寺': {'class_name': 'ソフトバンク国分寺', 'phone_number': '042-328-1414', 'has_parking': '－', 'is_barrier_free': '○', 'address': '東京都国分寺市本町４丁目１３‐５', 'site_url': 'https://www.softbank.jp/shop/search/detail/T155/?cid=tpsk_191119_mobile'}}, (('13', '132187'), ' 福生市（1）'): {}, (('13', '132195'), '狛江市（1）'): {}, (('13', '132152'), '国立市（2）'): {'ソフトバンク国立': {'class_name': 'ソフトバンク国立', 'phone_number': '042-501-2440', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都国立市東１丁目７‐１０ レジディア国立１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T190/?cid=tpsk_191119_mobile'}}, (('13', '132209'), '東大和市（1）'): {'ソフトバンク東大和向原': {'class_name': 'ソフトバンク東大和向原', 'phone_number': '042-590-0555', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都東大和市向原２丁目１‐１', 'site_url': 'https://www.softbank.jp/shop/search/detail/TG83/?cid=tpsk_191119_mobile'}}, (('13', '132225'), '東久留米市（2）'): {'ソフトバンク東久留米幸町': {'class_name': 'ソフトバンク東久留米幸町', 'phone_number': '042-476-8721', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都東久留米市幸町５丁目５‐５ メゾンアイエス１Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1M2/?cid=tpsk_191119_mobile'}}, (('13', '132233'), '武蔵村山市（1）'): {}, (('13', '132217'), '清瀬市（1）'): {'ソフトバンク清瀬': {'class_name': 'ソフトバンク清瀬', 'phone_number': '042-492-5104', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都清瀬市元町１丁目８‐３５ アマルフ ィ', 'site_url': 'https://www.softbank.jp/shop/search/detail/TD17/?cid=tpsk_191119_mobile'}}, (('13', '132250'), '稲城市（2）'): {'ソフトバンク矢野口': {'class_name': 'ソフトバンク矢野口', 'phone_number': '042-370-7711', 'has_parking': 'None', 'is_barrier_free': '－', 'address': '東京都稲城市矢野口６２９‐ ３ ｓｕｅｒｔｅ矢野口１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1I8/?cid=tpsk_191119_mobile'}, 'ソフトバンク若葉台': {'class_name': 'ソフトバンク若葉台', 'phone_number': '042-350-7277', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都稲城市若葉台２丁目４‐２ フレスポ若葉台２階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1E3/?cid=tpsk_191119_mobile'}}, (('13', '132276'), '羽村市（2）'): {'ソフトバンク羽村': {'class_name': 'ソフトバンク羽村', 'phone_number': '042-569-8161', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都羽村市羽東１丁目２ ３‐２９', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1Q6/?cid=tpsk_191119_mobile'}}, (('13', '132241'), '多摩市（3）'): {'ソフトバンクグリ ナード永山': {'class_name': 'ソフトバンクグリナード永山', 'phone_number': '042-311-3910', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都多摩市永山１丁目４ グリナード永山１号館２階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1G7/?cid=tpsk_191119_mobile'}, 'ソフトバンクココ リア多摩センター': {'class_name': 'ソフトバンクココリア多摩センター', 'phone_number': '042-355-6333', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都多摩市落合１丁目４６‐１ ココリア多摩センター２Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1B7/?cid=tpsk_191119_mobile'}, 'ソフトバンク聖蹟桜ヶ丘オーパ': {'class_name': 'ソフトバンク聖蹟桜ヶ丘オーパ', 'phone_number': '042-311-2611', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都多摩市関戸４丁目７２番地 聖蹟桜ヶ丘ＯＰＡ５Ｆ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T149/?cid=tpsk_191119_mobile'}}, (('13', '133035'), '西多摩郡瑞穂町（1）'): {}, (('13', '133051'), '西多摩郡日の出町（1）'): {}, (('13', '132292'), '西東京市（3）'): {'ソフトバンク 田無アスタ': {'class_name': 'ソフトバンク田無アスタ', 'phone_number': '042-466-7601', 'has_parking': 'None', 'is_barrier_free': '○', 'address': '東京都西東京市田無町２丁目１‐１ アスタ２Ｆショッピングプラザ 田無アスタ', 'site_url': 'https://www.softbank.jp/shop/search/detail/T174/?cid=tpsk_191119_mobile'}, 'ソフトバンク保谷': {'class_name': 'ソフトバンク保谷', 'phone_number': '042-438-7552', 'has_parking': '－', 'is_barrier_free': '－', 'address': '東京都西東京市東町３丁目１３‐２', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1J1/?cid=tpsk_191119_mobile'}, 'ソフトバンクひばりヶ丘': {'class_name': 'ソフトバンクひばりヶ丘', 'phone_number': '042-439-7256', 'has_parking': ' －', 'is_barrier_free': '○', 'address': '東京都西東京市住吉町３丁目１０‐２ ５ ＨＩＢＡＲＩＴＯＷＥＲ１階', 'site_url': 'https://www.softbank.jp/shop/search/detail/T1C1/?cid=tpsk_191119_mobile'}}}




