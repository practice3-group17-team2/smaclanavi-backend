# 目次
- [目次](#目次)
- [教室情報(class_infos)のAPI](#教室情報class_infosのapi)
  - [インスタンスの形式](#インスタンスの形式)
  - [URL](#url)
    - [`/class_infos/`](#class_infos)
    - [http methodについて](#http-methodについて)
    - [`/class_infos/<uuid>`](#class_infosuuid)
    - [http methodについて](#http-methodについて-1)
- [教室評価(reviews)のAPI](#教室評価reviewsのapi)
  - [インスタンスの形式](#インスタンスの形式-1)
  - [URL](#url-1)
    - [`/reviews/`](#reviews)
    - [http methodについて](#http-methodについて-2)
    - [`/class_infos/<uuid>`](#class_infosuuid-1)
    - [http methodについて](#http-methodについて-3)
- [講義開催情報(lec_infos)のAPI](#講義開催情報lec_infosのapi)
- [講義日付(lec_infos/date)のAPI](#講義日付lec_infosdateのapi)


# 教室情報(class_infos)のAPI
## インスタンスの形式
```json
{
    "id": "12345678-1234-5678-1234-567812345678",
    "class_name": "皇居",
    "organizer": {
        "org_id": 1,
        "org_name": "個人"
    },
    "city": {
        "prefecture": "東京都",
        "city_name": "千代田区"
    },
    "phone_number": "123-4567-8910",
    "address": "東京都千代田区千代田1番1号",
    "evaluation": 0,
    "price": 10000,
    "site_url": "https://www.kunaicho.go.jp/",
    "created": "1868-01-01T00:00:00.000000Z",
    "updated": "2021-07-14T00:00:00.000000Z",
    "lecture": [
        {
            "lec_id": 1,
            "lecture_content": "lec1 python",
            "is_target_old": false
        },
        {
            "lec_id": 2,
            "lecture_content": "lec2 html, css",
            "is_target_old": true
        }
    ],
    "lec_infos": [
        {
            "id": "00000000-0000-0000-0000-000000000000",
            "lecture": {
                "lec_id": 1,
                "lecture_content": "lec1 python",
                "is_target_old": false
            },
            "which_class_held": "12345678-1234-5678-1234-567812345678",
            "schedules": [
                {
                    "id": "11111111-1111-1111-1111-51b53d7c61b2",
                    "date": "2022-10-23T14:32:50Z",
                    "updated": "2022-10-23T14:32:54.981000Z"
                },
                {
                    "id": "22222222-4a19-4675-91c4-a2191132af4a",
                    "date": "2022-10-31T12:00:00Z",
                    "updated": "2022-10-29T14:37:03.797000Z"
                }
            ],
            "is_personal_lec": false,
            "is_iphone": true,
            "can_select_date": false,
            "created": "2022-10-23T14:22:12.938000Z",
            "updated": "2022-10-29T14:37:03.797000Z"
        }
    ],
    "reviews": [
        {
            "rev_id": "33333333-2026-fcbb-d730-79a13d39c173",
            "class_info_id": "12345678-1234-5678-1234-567812345678",
            "author": "user1",
            "faves": 0,
            "review_text": "nice!"
        },
        {
            "rev_id": "44444444-2026-fcbb-d730-79a13d39c173",
            "class_info_id": "12345678-1234-5678-1234-567812345678",
            "author": "user2",
            "faves": 0,
            "review_text": "awesome!"
        }
    ]
}
```
それぞれについての説明  
`id`：教室情報(class_info)のuuid  

`class_name`：教室の名称  

`organizer`：
- 教室を開いてる団体、三大キャリアとか、個人とか  

`phone_number`：str型、教室の電話番号  

`city`：存在するエリアの情報

- `prefecture`：  
prefectureクラスのインスタンス、県の名称
  
- `city_name`：街の名称

`address`：住所

`lecture`：扱っている講義

`evaluation`：いいねボタンの評価数

`price`：教室の価格

`site_url`：教室のwebサイトのURL

`reviews`：教室に付いた教室評価(reviews)インスタンスのリスト

## URL
### `/class_infos/`
### http methodについて
> ### get
> 教室情報(class_infos)のインスタンスのリストを返す
> ### post
> 教室情報(class_infos)のインスタンスを追加作成する  
> 
> 最低限の送信例
> ```json
> {
>     "class_name": "",
>     "organizer": <organizerインスタンス>,
>     "phone_number": "",
>     "city": {
>         "prefecture": <prefectureインスタンス>,
>         "city_name": ""
>     },
>     "address": "",
>     "lecture": [],
>     "evaluation": 0,
>     "price": 0,
>     "site_url": ""
> }
> ```


### `/class_infos/<uuid>`
### http methodについて
> patchは実装してるのかしてないのかよくわからないです。すまん。
> ##### get
> \<uuid\>の教室情報(class_info)インスタンスを返す
> ##### put
> \<uuid\>の教室情報(class_info)インスタンスを更新する
> ##### delete
> \<uuid\>の教室情報(class_info)インスタンスを削除する



# 教室評価(reviews)のAPI
- post時、authorはデフォルトで`no name`が設定されるようになっている。
- もし`""(空文字)`でpostされたとしても`no name`が設定される
## インスタンスの形式
```json
{
    "rev_id": "2de04071-2026-fcbb-d730-79a13d39c173",
    "class_info_id": "12345678-1234-5678-1234-567812345678",
    "author": "user1",
    "faves": 0,
    "review_text": "nice!"
}
```
それぞれについての説明  
`id`：教室情報(class_info)のuuid  

`class_name`：教室の名称  

`organizer`：
- 教室を開いてる団体、三大キャリアとか、個人とか  

## URL
### `/reviews/`
### http methodについて
> ### get
> 教室情報(class_infos)のインスタンスのリストを返す
> ### post
> 教室情報(class_infos)のインスタンスを追加作成する  
> 
> 最低限の送信例
> ```json
> {
>     "class_name": "",
>     "organizer": <organizerインスタンス>,
>     "phone_number": ""
> }
> ```


### `/class_infos/<uuid>`
### http methodについて
> patchは実装してるのかしてないのかよくわからないです。すまん。
> #### get
> \<uuid\>の教室情報(class_info)インスタンスを返す
> #### put
> \<uuid\>の教室情報(class_info)インスタンスを更新する
> #### delete
> \<uuid\>の教室情報(class_info)インスタンスを削除する

# 講義開催情報(lec_infos)のAPI
# 講義日付(lec_infos/date)のAPI

