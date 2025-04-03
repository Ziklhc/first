# 输入货物重量和单价，自动计算总运费  
weight = float(input("请输入货物重量（kg）："))  
unit_price = float(input("请输入单价（元/kg）："))  
total = weight * unit_price  
print(f"总运费为：{total}元")  
money=float(input("请输入运费："))
if money>=100:money*=0.9
print(money)