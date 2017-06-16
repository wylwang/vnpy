# encoding: utf-8

from vnbtc38 import *

#----------------------------------------------------------------------
def testTrade():
    """测试交易"""
    accessKey = '2ed222e55ca2b8a33e8dc5a8678d8114'
    secretKey = '514555929ec1a39d368a4f3901ef343e699285a597addd9364a96b4d26b1ab3b'
    userId = '194440'
    
    # 创建API对象并初始化
    api = TradeApi()
    api.DEBUG = True
    api.init(accessKey, secretKey, userId)
    
    # 查询账户，测试通过
    api.getAccountInfo()
    
    # 查询委托，测试通过
    #api.getOrders()
    
    # 买入，测试通过
    #api.buy(7100, 0.0095)
    
    # 卖出，测试通过
    #api.sell(7120, 0.0095)
    
    # 撤单，测试通过
    #api.cancelOrder(3915047376L)
    
    # 查询杠杆额度，测试通过
    #api.getLoanAvailable()
    
    # 查询杠杆列表，测试通过
    #api.getLoans()
 
    # 阻塞
    input()    


#----------------------------------------------------------------------
def testData():
    """测试行情接口"""
    api = DataApi()
    
    api.init(0.5)
    
    # 订阅成交推送，测试通过
    api.subscribeTick(SYMBOL_BTCCNY)
    
    # 订阅报价推送，测试通过
    #api.subscribeQuote(SYMBOL_BTCCNY)

    # 订阅深度推送，测试通过
    #api.subscribeDepth(SYMBOL_BTCCNY, 1)

    # 查询K线数据，测试通过
    #data = api.getKline(SYMBOL_BTCCNY, PERIOD_1MIN, 100)
    print data
    
    input()
    
    
if __name__ == '__main__':
    
    testTrade()
    
    #testData()