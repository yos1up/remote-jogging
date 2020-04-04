[日本語はこちら](#日本語版説明)

# remote-jogging

Enjoy jogging (or silent-jogging) at home with Joy-Con and Google Street View

![demo](https://raw.githubusercontent.com/yos1up/remote-jogging/master/misc/demo.gif)

## Requirements

- a Joy-Con(L)

- a Leg Strap for Ring Fit Adventure

- macOS

- Python >=3.7

- Follownig Python libraries (You can install them by pip)

    - hidapi

    - joycon-python

    - pyautogui

## Usage

1. Pair a Joy-Con(L) to Mac

    - https://www.tomsguide.com/us/use-joy-cons-on-pc-mac,news-25419.html

2. Attach the Joy-Con(L) to the Leg Strap and wrap it around your thigh

    - https://en-americas-support.nintendo.com/app/answers/detail/a_id/47744/~/how-to-attach%2Fdetach-the-joy-con-to-the-ring-con-and-leg-strap-accessories#DT:t1-q1a2EP:t1-q1a2-c

3. Open Google Street View with your browser and go to anywhere

4. `python main.py`

5. Let your view go forward once, by clicking [the button shown over the street](https://github.com/yos1up/remote-jogging/blob/master/misc/sv.png), then make sure that your view goes forward every time you press the up-arrow key

6. Enjoy jogging or silent-jogging (= light-squatting)

    - The developper is enjoying with silent-jogging actually, and hasn't tried to do with (normal) jogging. So normal jogging is not tested. If this program does not work well with jogging, please try silent-jogging instead.
    
    
    
----

# 日本語版説明

Joy-Con とストリートビューで在宅ジョギング（または在宅サイレントジョギング）

![demo](https://raw.githubusercontent.com/yos1up/remote-jogging/master/misc/demo.gif)

## Requirements

- ジョイコン(L)

- 「リングフィットアドベンチャー」のレッグバンド

- macOS

- Python >=3.7

- 以下の Python ライブラリ（pip でインストールできます）

    - hidapi

    - joycon-python

    - pyautogui
    
## 使い方

1. Joy-Con(L) を Mac とペアリングする

    - http://shobi-ec.sakura.ne.jp/%E3%82%B8%E3%83%A7%E3%82%A4%E3%82%B3%E3%83%B3%E3%82%92mac%E3%83%87%E3%83%90%E3%82%A4%E3%82%B9%E3%81%AB/

2. Joy-Con(L) をレッグバンドに取り付けて太ももに装着する

    - https://support.nintendo.co.jp/app/answers/detail/a_id/36632

3. Google ストリートビューをブラウザで開き，好きな地点に移動する．

4. `python main.py` 

5. [道路上に表示される矢印ボタン](https://github.com/yos1up/remote-jogging/blob/master/misc/sv.png)をクリックして，ストリートビューの画面を一度前進させる．そのあと，上キーを押すたびにストリートビューの画面がさらに前進することを確認する

6. ジョギングを開始する．もしくはサイレントジョギング（= 軽いスクワット）を開始する．

    - 開発者はサイレントジョギングで走っています．普通のジョギングで試したことはありません．もし普通のジョギングでうまく動かない場合は，サイレントジョギングを試してみてください．
