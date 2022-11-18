# 目次
<details>
<summary>目次</summary>

- [目次](#目次)
- [実装方針](#実装方針)
- [教室情報(class_infos)のAPI](#教室情報class_infosのapi)
  - [インスタンスの形式](#インスタンスの形式)
    - [各フィールド概要](#各フィールド概要)
  - [Endpoint URLs](#endpoint-urls)
  - [`/class_infos/`](#class_infos)
    - [GET](#get)
    - [POST(おそらくエラー出る)、未実装](#postおそらくエラー出る未実装)
  - [`/class_infos/<uuid>/`](#class_infosuuid)
    - [GET](#get-1)
    - [PUT(おそらくエラー)](#putおそらくエラー)
    - [DELETE](#delete)
- [教室評価(reviews)のAPI](#教室評価reviewsのapi)
  - [インスタンスの形式](#インスタンスの形式-1)
    - [各フィールド概要](#各フィールド概要-1)
  - [Endpoint URLs](#endpoint-urls-1)
  - [`/reviews/`](#reviews)
    - [GET](#get-2)
    - [POST](#post)
  - [`/reviews/<uuid>/`](#reviewsuuid)
    - [GET](#get-3)
    - [PUT](#put)
    - [DELETE](#delete-1)
- [講義開催情報(lec_infos)のAPI](#講義開催情報lec_infosのapi)
  - [インスタンスの形式](#インスタンスの形式-2)
    - [各フィールド概要](#各フィールド概要-2)
  - [Endpoint URLs](#endpoint-urls-2)
  - [`/lec_infos/`](#lec_infos)
    - [GET](#get-4)
    - [POST(うごきそう)](#postうごきそう)
  - [`/lec_infos/<uuid>/`](#lec_infosuuid)
    - [GET](#get-5)
    - [PUT(おそらくエラー)](#putおそらくエラー-1)
    - [DELETE](#delete-2)
- [講義日付(lec_infos/date)のAPI](#講義日付lec_infosdateのapi)
  - [インスタンスの形式](#インスタンスの形式-3)
    - [各フィールド概要](#各フィールド概要-3)
  - [Endpoint URLs](#endpoint-urls-3)
  - [`/lec_infos/<uuid:lec_infos>/date/`](#lec_infosuuidlec_infosdate)
    - [GET](#get-6)
    - [POST](#post-1)
  - [`/lec_infos/<uuid:lec_infos>/date/<uuid:date>/`](#lec_infosuuidlec_infosdateuuiddate)
    - [GET](#get-7)
    - [PUT](#put-1)
    - [DELETE](#delete-3)
- [その他のインスタンスについて](#その他のインスタンスについて)
  - [講義(lecture)インスタンス](#講義lectureインスタンス)

</details>

# 実装方針
店舗経営者や店舗検索をする利用者からの投稿があるかどうかに着目してどの機能を実装するかどうかの指針にしました。  
教室情報(classinfo)や講義開催情報(lecinfos)、講義日付(lec_infos/date)は経営者、教室評価(reviews)は検索利用者を想定しました。
基本的に展開した状態で渡された方が扱いやすいという前提で構造を考えました。

# 教室情報(class_infos)のAPI
関連情報詰め込みまくってるので長いです。

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
        "pref_id": 14,
        "city_id": 1,
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
        <講義(lecture)インスタンス>,
        <講義(lecture)インスタンス>,
        <講義(lecture)インスタンス>
    ],
    "lec_infos": [
        <講義開催情報(lec_infos)インスタンス>,
        <講義開催情報(lec_infos)インスタンス>,
        <講義開催情報(lec_infos)インスタンス>
    ],
    "reviews": [
        <教室評価(reviews)インスタンス>,
        <教室評価(reviews)インスタンス>,
        <教室評価(reviews)インスタンス>
    ]
}
```
<details>
<summary>インスタンス詳細まで表示</summary>

```json
{
    "id": "12345678-1234-5678-1234-567812345678",
    "class_name": "皇居",
    "organizer": {
        "org_id": 1,
        "org_name": "個人"
    },
    "city": {
        "pref_id": 14,
        "city_id": 1,
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
        // 講義(lecture)インスタンス
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
        // 講義開催情報(lec_infos)インスタンス
        {
            "id": "00000000-0000-0000-0000-000000000000",
            "lecture": {
                "lec_id": 1,
                "lecture_content": "lec1 python",
                "is_target_old": false
            },
            "which_class_held": "12345678-1234-5678-1234-567812345678",
            "is_personal_lec": false,
            "is_iphone": true,
            "can_select_date": false,
            "created": "2022-10-23T14:22:12.938000Z",
            "updated": "2022-10-29T14:37:03.797000Z",
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
            ]
        }
    ],
    "reviews": [
        // 教室評価(reviews)インスタンス
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
</details>

### 各フィールド概要
`id`：教室情報(class_infos)のuuid  

`class_name`：教室の名称  

`organizer`： 教室を開いてる団体、三大キャリアとか、個人とか  

`city`：教室が存在する地域の情報
> `pref_id`：県のID
> 
> `city_id`：街のID
> 
> `prefecture`：県の名称
> 
> `city_name`：街の名称


`phone_number`：str型、教室の電話番号  

`address`：住所

`evaluation`：いいねボタンの評価数

`price`：教室の価格

`site_url`：教室のwebサイトのURL

`created`：教室情報の作成日時

`updated`：教室情報の最新更新日時、紐づいた講義の予定などの更新から最新の日時を返す

`lecture`：教室が扱っている講義インスタンスのリスト  
> `lec_id`：lectureのid(連番)
> 
> `lecture_content`：講義の名称、タグとか分類のようなもの
> 
> `is_target_old`：高齢者向けか否か、bool値


`lec_infos`：教室が扱う講義開催情報(lec_infos)インスタンスのリスト、教室が扱う開催予定などがこれにあたる
> 詳しくは[講義開催情報(lec_infos)のAPI](#講義開催情報lec_infosのapi) を参照



`reviews`：教室に付いた教室評価(reviews)インスタンスのリスト
> 詳しくは[教室評価(reviews)のapi](#教室評価reviewsのapi) を参照

## Endpoint URLs
- [`/class_infos/`](#class_infos)
- [`/class_infos/<uuid>/`](#class_infosuuid)

## `/class_infos/`
### GET
上記の教室情報(class_infos)のインスタンスのリストを返す

### POST(おそらくエラー出る)、未実装
上記の教室情報(class_infos)のインスタンスを追加作成する  
organizer, city, lectureをidから指定できるようにしたい。  

最低限の送信例を書きたい気持ちはある
```json
/* 例 */
{
    "class_name": "",
    "organizer": <organizerインスタンス>,
    "phone_number": "",
    "city": {
        "prefecture": <prefectureインスタンス>,
        "city_name": ""
    },
    "address": "",
    "lecture": [],
    "evaluation": 0,
    "price": 0,
    "site_url": ""
}
```


## `/class_infos/<uuid>/`
patchは実装してるのかしてないのかよくわからないです。すまん。
### GET
\<uuid\>の教室情報(class_infos)インスタンスを返す

### PUT(おそらくエラー)
\<uuid\>の教室情報(class_infos)インスタンスを更新する

### DELETE
\<uuid\>の教室情報(class_infos)インスタンスを削除する


[目次へ](#目次)

# 教室評価(reviews)のAPI
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
### 各フィールド概要
`rev_id`：教室評価(reveiews)のuuid  

`class_info_id`：評価対象になる教室のid (教室情報(class_infos))  

`author`：評価の投稿者名  

`faves`：いいねボタンの評価数  

`review_text`：評価の本文  


## Endpoint URLs
- [`/reviews/`](#reviews)
- [`/reviews/<uuid>/`](#reviewsuuid)

## `/reviews/`

### GET
教室評価(reveiews)のインスタンスのリストを返す

### POST
教室評価(reveiews)のインスタンスを追加作成する  

必須の指定項目は`class_info_id`と`review_text`の二つ  
`class_info_id`は実在する教室情報(class_infos)の`id`を、`review_text`は空文字以外を指定してください。

インスタンス上に存在する`rev_id`, `author`, `faves`はjsonから省略した形で送信しても補完されます 

最低限の送信例
```json
{
    "class_info_id": "12345678-1234-5678-1234-567812345678",
    "review_text": "nice!"
}
```
上記三つは省略された場合、`rev_id`はuuidの自動生成、`author`には`"no name"`が、`faves`は `0` がデフォルトで設定される  

`rev_id`はformとかにデフォルトで生成したものを渡すようにしたつもりですがフロントの実装で役に立つかは不明、ピンとこなければ読み飛ばしてください
> [参考drf公式docs](https://www.django-rest-framework.org/api-guide/fields/#initial)


## `/reviews/<uuid>/`
patchは実装してるのかしてないのかよくわからないです。すまん。
### GET
\<uuid\>の教室評価(reveiews)インスタンスを返す

### PUT
\<uuid\>の教室評価(reveiews)インスタンスを更新する
```json
{
    "rev_id": "f45b58bf-7ba9-4864-a204-dccaab856a7d",
    "class_info_id": "c935a1d2-5f30-417f-81a0-e9294c2752cb",
    "author": "no name",
    "faves": 0,
    "review_text": "a\nは改行として認識されませんでした。"
}
```

### DELETE
\<uuid\>の教室評価(reveiews)インスタンスを削除する

[目次へ](#目次)

# 講義開催情報(lec_infos)のAPI
## インスタンスの形式
```json

{
    "id": "c51ec2f8-306e-4a4d-b516-cfc55125744c",
    "lecture": {
        "lec_id": 1,
        "lecture_content": "lec1 python",
        "is_target_old": false
    },
    "which_class_held": "d1013537-a869-4d1c-a444-513f6d3be5d9",
    "is_personal_lec": false,
    "is_iphone": true,
    "can_select_date": false,
    "created": "2022-10-23T14:22:12.938000Z",
    "updated": "2022-11-13T02:16:07.745946Z",
    "schedules": [
        // 講義日付(lec_infosdate)インスタンス
        {
            "id": "34bd1208-3b81-4861-9328-51b53d7c61b2",
            "lec_info_id": "c51ec2f8-306e-4a4d-b516-cfc55125744c",
            "date": "2022-10-23T14:32:50Z",
            "updated": "2022-10-23T14:32:54.981000Z"
        },
        {
            "id": "d2c002de-4a19-4675-91c4-a2191132af4a",
            "lec_info_id": "c51ec2f8-306e-4a4d-b516-cfc55125744c",
            "date": "2022-10-31T12:00:00Z",
            "updated": "2022-10-23T14:37:03.797000Z"
        }
    ]
}
```
### 各フィールド概要
`id`：講義開催情報(lec_infos)のid  

`lecture`：対象となる講義インスタンス  
> `lec_id`：lectureのid(連番)
> 
> `lecture_content`：講義の名称、タグとか分類のようなもの
> 
> `is_target_old`：高齢者向けか否か、bool値

`which_class_held`：開催元となる教室(教室情報(class_infos))のid  

`is_personal_lec`：個人向けの講義か否か、bool値  

`is_iphone`：iphoneの講座か否か、bool値  

`can_select_date`：日程が選べるタイプの講義か否か、bool値  

`created`：作成日時  

`updated`：最新更新日時、以下のschedulesと講義開催情報の更新日時
を比較して最新のものを返す  

`schedules`：講義日付(lec_infosdate)インスタンスのリスト、読み取り専用。追加、更新が行いたい場合は下記リンクへ  
> 詳しくは[講義日付(lec_infos/date)のAPI](#講義日付lec_infosdateのapi) を参照

## Endpoint URLs
- [`/lec_infos/`](#lec_infos)
- [`/lec_infos/<uuid>/`](#lec_infosuuid)

## `/lec_infos/`
### GET
講義開催情報(lec_infos)のインスタンスのリストを返す

### POST(うごきそう)
```json
{
    "lecture": {
        "lec_id": 2
    },
    "which_class_held": "d1013537-a869-4d1c-a444-513f6d3be5d9",
    "is_personal_lec": false,
    "is_iphone": false,
    "can_select_date": false
}
```
講義開催情報(lec_infos)のインスタンスを追加作成する  
既にその教室情報(class_infos)の講義について講義開催情報(lec_infos)のインスタンスが存在する場合、それを取得して返す。(任意の教室の講義に対して、講義開催情報は1対1)  

`schedules`は読み取り専用なのでここから追加、更新などはできない。  
講義日付(lec_infosdate)を紐づけたい場合は[講義日付(lec_infos/date)のAPI](#講義日付lec_infosdateのapi) を参照

`id`は(同様に読み取り専用で? (どうするか悩み中))、新規作成の場合はランダム生成のuuidに、既存のインスタンスを返す場合は既存のuuidをそのまま返す仕様になっている。  
しかし、矛盾が起こるuuidの指定をされた場合にどのような動作をするかよくわからないのでjsonは指定しない形でPOSTすることを推奨

## `/lec_infos/<uuid>/`
### GET
\<uuid\>の講義開催情報(lec_infos)インスタンスを返す

### PUT(おそらくエラー)
\<uuid\>の講義開催情報(lec_infos)インスタンスを更新する

### DELETE
\<uuid\>の講義開催情報(lec_infos)インスタンスを削除する



[目次へ](#目次)

# 講義日付(lec_infos/date)のAPI
## インスタンスの形式
```json
{
    "id": "34bd1208-3b81-4861-9328-51b53d7c61b2",
    "lec_info_id": "c51ec2f8-306e-4a4d-b516-cfc55125744c",
    "date": "2023-04-01T00:00:00Z",
    "updated": "2022-11-13T03:03:01.192665Z"
}
```
### 各フィールド概要
`id`：講義日付(lec_infos/date)のid  

`lec_info_id`：日付を持たせる対象の講義開催情報(lec_infos)のid

`date`：講義が実施される日時  

`updated`：最終更新日時  

## Endpoint URLs
- [`/lec_infos/<uuid:lec_infos>/date/`](#lec_infosuuidlec_infosdate)
- [`/lec_infos/<uuid:lec_infos>/date/<uuid:>/`](#lec_infosuuidlec_infosdateuuid)

## `/lec_infos/<uuid:lec_infos>/date/`
### GET
講義日付(lec_infos/date)インスタンスのリストを返す

### POST
講義日付(lec_infos/date)インスタンスを追加作成する  
```json
{
    "id": "389e6737-8a11-479f-9eca-d33352c669fe",
    "lec_info_id": "c51ec2f8-306e-4a4d-b516-cfc55125744c",
    "date": "2022-10-31T12:00:00Z"
}
```
`updated`は自動更新なので省略されます。

## `/lec_infos/<uuid:lec_infos>/date/<uuid:date>/`
### GET
`id`が`<uuid:date>`の講義日付(lec_infos/date)インスタンスを返す

### PUT
講義日付(lec_infos/date)インスタンスを更新する  
形式はPOSTと同様

### DELETE
講義日付(lec_infos/date)インスタンスを削除する


[目次へ](#目次)

# その他のインスタンスについて
## 講義(lecture)インスタンス
`lec_id`：lectureのid(連番)

`lecture_content`：講義の名称、タグとか分類のようなもの

`is_target_old`：高齢者向けか否か、bool値

管理者から追加することを想定しているため、URLの割り当てなし  
`lecture_content`と`is_target_old`は読み取り専用


[目次へ](#目次)
