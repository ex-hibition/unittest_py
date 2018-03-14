import unittest
import sample
import datetime as dt

# -- テストケースはunittest.TestCaseのサブクラスとして作成する
class TestSample(unittest.TestCase):

  # -- テストの初期設定
  def setUp(self):
    # -- テスト対象クラスのインスタンスつくる
    self.calc = sample.DateCalculation("20180314")
    # -- 比較対象日付をdate型でつくる
    self.comp_date = dt.datetime.strptime("20180212", '%Y%m%d')

  # -- テスト実施
  def test_calc_before_days(self):
    self.assertEqual(self.calc.calc_before_days("30"), self.comp_date)


if __name__ == "__main__":
    unittest.main()
