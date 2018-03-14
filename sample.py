import datetime as dt

# -- クラスつくる
class DateCalculation:

  # -- コンストラクタ
  def __init__(self, yyyymmdd):
    self.target_date = dt.datetime.strptime(yyyymmdd, "%Y%m%d")
    
  # -- mm日前を計算するメソッド
  def calc_before_days(self, mm):
    calc_date = self.target_date - dt.timedelta(days=+int(mm))
    return calc_date

if __name__ == '__main__':
  # -- 調整日数
  days = "30"
  # -- インスタンスつくる
  calc = DateCalculation("20180314")
  # -- メソッド実行
  calc_date = calc.calc_before_days(days)
  # -- アトリビュート取得
  target_date = calc.target_date
  # -- 画面出力
  print(target_date, "の", days, "日前は", calc_date,"です。")
