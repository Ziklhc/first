# 输入辣度等级，输出建议描述  
level = int(input("请选择辣度等级（1-5）："))  
if level == 1:  
    print("推荐：清汤锅（适合儿童）")  
elif 2 <= level <= 3:  
    print("推荐：鸳鸯锅（兼顾各地口味）")  
elif 4 <= level <= 5:  
    print("推荐：九宫格老火锅（重庆本地人最爱）")  
else:  
    print("输入错误！")  
a=level*0.5
print(a)