# GroundServicesJP
## 概要 Overview
GroundServicesJP “GSJP”は、MicrosoftFlightSimulatorでの日本国内における空港の地上サービスや設備(GSE)を再現するために開始されたプロジェクトで、github.comを拠点とするオープンソースプロジェクトです。 

GSJPプロジェクトの4つの目標：  
1. 空港車両の配置、乗客の乗降経路設定、プッシュバック位置の設定、機体の停止位置設定をGSX Pro用プロファイルとして作成する (MSFS限定の機能) 。  
2. GSXを使用せずにプッシュバックをする方など、全ユーサー向けの~~プッシュバックマップ~~情報サイトを作成する。  
3. github.comのプロジェクトページを訪問することなく、GSJPにて作成されたプロファイルのダウンロードやアップデートを行えるソフトウェアの開発を行う(実装までしばらくお待ち下さい)。  
4. GSXの空港車両などを現実の塗装に合わせる(実装までしばらくお待ち下さい)。 

GroundServicesJP (GSJP) aims to improve Ground Services Equipment (GSE) in Japan on MSFS. The open-sourced project is hosted on github.com.  

The project has four objectives:  
1. GSX Pro profiles that include correct positioning of GSE vehicles, PAX Waypoints, pushback/stop locations. This feature is for MSFS only.  
2. ~~Pushback maps for all users (including ones who do not use GSX).~~ Provide pushback information for all users (including ones who do not use GSX).   
3. A software that organizes and updates various GSX profiles, so users do not have to come to github and download releases. This feature will come later.  
4. Updated GSX GSE vehicle textures to reflect the real condition. This feature will come later.

## 情報サイト Information Website
https://gsjp.info

## GSX Profiles
### Githubリポジトリへのリンク  Repository Link
https://github.com/GroundServicesJP/GroundServicesJP_GSXProfiles

### 必要アドオン Required Environment
- Microsoft Flight Simulator (MSFS 2020) 
- FSDreamTeam GSX Pro.  
- GSXプロファイルがサポートする空港アドオン Addon Airports the GSX profiles are supporting.

### ダウンロードとインストール  Download and Installation
現時点では、 https://github.com にあるファイルをダウンロードし、以下の手順でインストールしてください。  

1. GSXProのプロファイル(.ini) をインストールするため、`%AppData%\Virtuali\GSX\MSFS`を開きます。  

2. 同じ空港の古いプロファイル（自動生成されたプロファイル、ご自身で作成されたプロファイルなど）が既に存在している場合は、バックアップのうえ削除してください。  

3. `.ini`と`.py`ファイルを `%AppData%\Virtuali\GSX\MSFS` にペーストしてください。  

※`.ini`ファイル内のAFCAD.bglの書き込み欄は空欄のままで問題ありません。 

Currently, please download the newest release on https://github.com. To install the files, follow these steps:  
1. If you have old configuration files for the airport (either autogenerated, provided by us, or other creators), please backup and delete.  
2. Move the `.ini`and `.py` files to `%AppData%\Virtuali\GSX\MSFS`. There is no need to change AFCAD `.bgl` file path for MSFS GSX Pro version.

### サポートされている空港とProfileバージョン  Supported Airports and Version
Google Map: https://www.google.com/maps/d/u/3/edit?mid=1qhnhZHAZv8GJ76quQZC9RZpLdB4ASFI&usp=sharing
| プロファイル名 Profile Name▼ | 空港 Airport           | シーナリー作者 Scenery Creator | バージョン Version | リリース日/アップデート日 Release/Update Date |
| -----------                | -----------           | -----------                   | -----------                    | ----------- |
| rjbd-tsuji.ini/.py          | 南紀白浜 Nanki-Shirahama (RJBD) | Tsujiさん                      | Ver 1.0                       | 2024/09/08 Released |
| rjbe-kaze.ini/.py          | 神戸 Kobe (RJBE) | KAZEさん                      | Ver 1.0                       | 2024/06/01 Released |
| rjcb-alois.ini/.py          | 帯広 Obihiro (RJCB)   | Aloisさん                      | Ver 1.3                       | 2025/01/27 Updated |
| rjck-karuchie.ini/.py          | 釧路 Kushiro (RJCK)   | karuchieさん                      | Ver 1.1                       | 2024/02/03 Updated |
| rjcm-gaochan_alois_rip.ini/.py            | 女満別 Memanbetsu (RJCM) | GAOCHANさん<br>Aloisさん<br>RIPさん      | Ver 1.0                | 2024/05/18 Released  |
| rjcn-alois.ini/.py          | 中標津 Nakashibetsu (RJCN)   | Aloisさん                      | Ver 1.1                       | 2025/03/22 Released |
| rjeb-alois_marin_karuchie.ini/.py | 紋別 Monbetsu (RJEB)   | Aloisさん<br>Marinさん<br>Karuchieさん                      | Ver 1.0                       | 2024/02/24 Released |
| rjec-mfsg.ini/.py          | 旭川 Asahikawa (RJEC)   | MFSG                     | Ver 1.0                       | 2024/02/18 Updated |
| rjer-g15_marin.ini/.py <br> rjer-g15_v2.ini/.py         | 利尻 Rishiri (RJER)   | G15 (v1)/Marinさん  <br>  Gate15Scenery (v2)    | Ver 1.0 <br>  Ver 1.0                     | 2024/02/17 Released <br> 2024/06/01 Released|
| rjff-snjsim.ini/.py        | 福岡 Fukuoka (RJFF) | SNJSIM                          | Ver 1.2                        | 2025/01/27 Updated |
| rjfr-mfsg.ini              | 北九州 Kitakyushu (RJFR) | MFSG                          | Ver 1.0                        | 2024/01/28 Released |
| rjft-keisim.ini/.py   <br> rjft-snjsim.ini/.py        | 熊本 Kumamoto (RJFT) | Keisimさん  <br>   SNJSIM      | Ver 1.0                | 2025/03/09 Released |
| rjoa-kaze.ini/.py              | 広島 Hiroshima (RJOA) | KAZEさん                          | Ver 1.2                       | 2024/02/24 Updated |
| rjoi-permille.ini/.py            | 岩国 Iwakuni (RJOI) | permilleさん                          | Ver 1.0                | 2024/05/18 Released  |
| rjok-mfsg.ini/.py            | 高知 Kochi (RJOK) | MFSG                         | Ver 1.0                             | 2024/02/17 Released |
| rjoo-kado.ini/.py            | 大阪国際 Osaka International (RJOO) | KADOさん                         | Ver 1.2            | 2024/05/18 Updated |
| rjot-kado.ini/.py            | 高松 Takamatsu (RJOT) | KADOさん                         | Ver 1.0                             | 2024/03/15 Released |
| rjsk-fssa.ini/.py              | 秋田 Akita (RJSK) | FSSA                          | Ver 1.4                           | 2025/03/09 Updated |
| rjsr-highmemfix.ini/.py              | 大館能代 Odate-Noshiro (RJSR) | Highmemfixさん                          | Ver 1.0                           | 2024/02/17 Released |
| rjss-kaze.ini/.py              | 仙台 Sendai (RJSS) | KAZEさん                          | Ver 1.0                           | 2024/09/20 Released |
| rjth-karuchie.ini/.py            | 八丈島 Hachijojima (RJTH) | karuchieさん                         | Ver 1.0                             | 2024/02/17 Released |
| rjtt-karuchie.ini/.py            | 東京国際（羽田） Tokyo International (Haneda) (RJTT) | kaurchieさん                          | Ver 1.1                | 2025/01/06 Updated |
| roah-mkstudios-gsjp.ini/.py            | 那覇 Naha (ROAH) | MK-STUDIOS                          | Ver 1.3                | 2025/03/09 Updated |
| roig-keisim.ini/.py            | 新石垣 New Ishigaki (ROIG) | Keisimさん                          | Ver 1.4                | 2025/01/27 Updated |



### ライセンス Licensing 
本リポジトリは、以下の作品を除き、GPLv3ライセンスを利用しています：
The majority of this repository is open-sourced with GPLv3 license, except for the following work: 

- rjoo-kado.ini/.py
- rjfr-mfsg.ini
- rjot-kado.ini/.py

上記の作品はMITライセンスを使用しています。The works above are licensed with MIT. 

GSJPプロジェクトのライセンスは、Githubリポジトリ内の `LICENSE.md` をご覧ください。  
Please refer to LICENSE.md on github.com in the github repository.  

### プロジェクトへの参加 Contributing
GSJPプロジェクトへ加入されたい方は、github.comにてリポジトリをForkし、Pull Request(PR)を作成してください。 

以下は、git VCSを使用せずにgithub.comでプロジェクトに参加するための簡単なフローです。 

Github.com内にて公開されているProfileを更新する、あるいは作成したProfileをアップロードする場合: 

If you would like to contribute, please fork the repository and make a pull request (PR).  

Here is a simple procedure on how to contribute on github without git VCS.  If you would like to add or edit an existing .ini file:  
1. リポジトリ (Repository) をForkする。Fork the repository.
   
   ![alt text](README_images/1.png)
2. ファイルアップロードを選択し、更新したファイルをアップロードする。この際、必ず自身のForkしたリポジトリ内で作業を行ってください。Have your edited file ready, select Upload files and upload. Make sure you are doing this in your own forked repository.
   
   ![alt text](README_images/2.png)
3. アップロードが完了したら、Pull Request(PR)を作成します。 Create a Pull Request (PR) after committing.
   
   ![alt text](README_images/3.png)
4. PRが、下の画像のように正しく設定されていることを確認してください。  Make sure the PR is set up correctly. Make sure the head repository is your repository and the branch for comparing contains files you would like to add/edit. Make sure the base repository is GroundServicesJP/GroundServicesJP_GSXProfiles and the base branch is main. Create the pull request and we will review it.
   
  ![alt text](README_images/4.png)

※ あなたが作成したファイルをgithubを通してアップロードできない場合、GSJPプロジェクトメンバーに直接ファイルを送っていただければ、プロジェクトメンバーが代理でアップロードを行い、更新の連絡を行います。 If you do not want to use github.com, please send us the files directly, and we will review and update them for you.

### プロジェクトメンバー Contributor List 
- ANA7875 (@ANA7875_fwc) 
- ろくまる (@60Kumaru)
- Sanrok (@sanrok_)
- RIN (@RIIIIIN3180)
- Legotatsu
- FUK_Driver (@FUK_Nob0525)
- Yuta (@Aobuta34)
- Takama (@B77W_JPN)
- ろぼたん (@robotaaaan)
