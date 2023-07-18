sde = float(input('请输入全年应税所得额：')) #全年应纳税所得额

sl = 0 #税率
sskcs = 0 #速算扣除数
if sde > 960000:
    sl = 0.45
    sskcs = 181920
elif sde > 660000 and sde <= 960000:
    sl = 0.35
    sskcs = 85920
elif sde > 420000 and sde <= 660000:
    sl = 0.30
    sskcs = 52920
elif sde > 300000 and sde <= 420000:
    sl = 0.25
    sskcs = 31920
elif sde > 144000 and sde <= 300000:
    sl = 0.20
    sskcs = 16920
elif sde > 36000 and sde <= 144000:
    sl = 0.10
    sskcs = 2520
else:
    sl = 0.03
    sskcs = 0

se = sde * sl - sskcs #计算税额
print('全年应纳税所得额：',sde)
print('适用税率：{:.2%}'.format(sl))
print('速算扣除数：', sskcs)
print('全年应纳税金额：', se)
print('综合税率：{:.2%}'.format(se/sde))
