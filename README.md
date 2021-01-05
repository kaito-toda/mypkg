# 1000を作る。
## 使用道具、環境
・ラズベリーパイ４  
・Ubuntu_20.04  
・ROS  

## 使用方法
ROSのセットアップが完了しているラズパイを用意する。  
srcディレクトリに移動。  
`git clone https://github.com/kaito-toda/mypkg.git`  
`roscore`  
`rosrun mypkg count.py &`  
`rosrun mypkg conver.py`  

## 動作
count.py: ランダムな1~100の数値を生成する。   
conver.py: 受け取った数値を足したり引いたりする処理を初期数値1から1000ピッタリになるまで繰り返す  
行った処理、現在の数値、試行回数が端末上に表示される。  
試行回数が100回、200回を超えると実行速度が上がる。  

## 動作の様子
<https://youtu.be/zwDeA9JCUw8>  
年始の暇つぶしにどうぞ。なかなか1000にたどり着かないらずぱい君が可愛く思えてくるかもしれません。  
