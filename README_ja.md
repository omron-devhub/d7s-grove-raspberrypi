# d7s-grove-raspberrypi
オムロン製センサ D7S を Raspberry Pi 3 Model B で評価する為のモジュールと、モジュールを利用する場合のサンプルプログラムです。

D7S は世界最小クラスの感震センサです。  
地震の大きさを表す震度階級とも相関性の高いSI値を採用することで、より震度階級に即した高精度な地震判定が可能です。  
I2Cインターフェースでセンサ内の地震関連情報の取得も可能です。

## 言語
- [英語](./README.md)
- [日本語](./README_ja.md)

## 概要
- grove_d7s.py  
D7S から GrovePi+ 経由でデータを取得するためのドライバモジュールです。

- sample_d7s.py  
ドライバモジュール経由で取得したデータをコンソール上で確認できるサンプルプログラムです。

- sample_gui_d7s.py  
ドライバモジュール経由で取得したデータをグラフで可視化して確認できるサンプルプログラムです。

***デモ:***  
sample_gui_d7s.py を実行すると以下のようなグラフを確認することができます。  

![Graph_D7S](Graph_D7S.png)

## インストール方法
1. 事前に依存関係のあるソフトウェアをインストールして下さい。  
    [依存関係](#link)
2. ターミナルを開き、次のコマンドを実行します。  
    ```
    $ mkdir omron_sensor
    $ cd omron_sensor
    $ git clone https://github.com/omron-devhub/d7s-grove-raspberrypi.git
    ```

## 使い方
サンプルプログラムを動作させる手順です。

-  sample_d7s.py  
ターミナルを開き、次のコマンドを実行します。  
    ```
    $ cd omron_sensor
    $ sudo python3 sample_d7s.py
    ```
- sample_gui_d7s.py  
ターミナルを開き、次のコマンドを実行します。  
    ```
    $ cd omron_sensor
    $ sudo python3 sample_gui_d7s.py
    ```
## <a name="link"></a>依存関係
d6t-grove-raspberrypi には次に挙げるソフトウェアとの依存関係があります。
- [Python3](https://www.python.org/)
- [GrovePi+](http://wiki.seeedstudio.com/GrovePi_Plus/)
- [matplotlib](https://matplotlib.org/)
- [smbus2](https://pypi.org/project/smbus2/)

## ライセンス
Copyright (c) OMRON Corporation. All rights reserved.

このリポジトリはMITライセンスの下でライセンスされています。
