__author__ = 'sara'

from comm import BaseTest
from comm import get_url
from time import sleep
from comm import my_assert
import test_set.btcchina.bsnsCommon as bcomm


class TestTrade(BaseTest):

    def setUp(self):
        BaseTest.setUp(self)
        self.driver.get(get_url("homepage"))
        bcomm.login(self.user.get("email"), self.user.get("password"))

    def test_trade_btc(self):
        self.driver.get(get_url("trade"))
        sleep(3)
        before_orders = self.get_open_orders()

        print("======>before_orders :%s" %before_orders)
        self.buy()
        after_orders = self.get_open_orders()
        print("======>after_orders :%s" % after_orders)
        self.check_result(before_orders, after_orders, "购买btc")
        before_orders = self.get_open_orders()
        self.sell()
        after_orders = self.get_open_orders()
        print("======>after_orders :%s" % after_orders)
        self.check_result(before_orders, after_orders, "出售btc")

    def test_trade_ltc(self):
        self.driver.get(get_url("trade_ltc"))
        sleep(3)
        before_orders = self.get_open_orders()
        self.buy()
        after_orders = self.get_open_orders()
        self.check_result(before_orders, after_orders, "购买ltc")
        before_orders = self.get_open_orders()
        self.sell()
        after_orders = self.get_open_orders()
        self.check_result(before_orders, after_orders, "出售ltc")

    def buy(self):
        self.get_element("trade", "buy_price").send_keys("1")
        self.get_element("trade", "buy_amount").send_keys("1")
        self.get_element("trade", "buy_transpassword").send_keys(self.user.get("trans_password"))
        sleep(1)
        self.get_element("trade", "buy_btn").click()
        sleep(3)

    def sell(self):
        self.get_element("trade", "sell_price").send_keys("10000")
        self.get_element("trade", "sell_amount").send_keys("0.001")
        self.get_element("trade", "sell_transpassword").send_keys(self.user.get("trans_password"))
        sleep(1)
        self.get_element("trade", "sell_btn").click()
        sleep(3)

    def get_open_orders(self):
        return len(self.get_elements("trade", "open_orders_table_tr"))

    def check_result(self, before_orders, after_orders, msg):
        sleep(2)
        if after_orders-3 == before_orders:
            with my_assert(msg):
                self.assertEqual(1, 1)
            # open_order_title = self.get_element("trade", "open_orders_title")
            # sleep(4)
            # self.driver.execute("arguments[0].scrollIntoView()", open_order_title)
            sleep(4)
            self.get_element("trade", "cancle_first_orders_table_tr").click()
            sleep(4)

    def tearDown(self):
        self.driver.get(get_url("homepage"))
        bcomm.logout()
