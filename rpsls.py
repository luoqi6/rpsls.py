#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：罗琦
日期：2020.4.16
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):   
	if name == "石头":
		return 0
	elif name == "史波克":
		return 1
	elif name == "纸":
		return 2
	elif name == "蜥蜴":
		return 3
	elif name == "剪刀":
		return 4
	else:
		print("Error: No Correct Name")

def number_to_name(number):
	if number in range(0,5):
			if number == 0:
				return "石头"
			elif number == 1:
				return "史波克"
			elif number == 2:
				return "纸"
			elif number == 3:
				return "蜥蜴"
			elif number == 4:
				return "剪刀"
			else:
				print("Error: No Correct Name")  


def rpsls(player_choice):
	if player_choice!="石头" and player_choice!="剪刀" and player_choice!="蜥蜴" and player_choice!="史波克" and player_choice!="纸":#输入不正确的游戏对象时，屏幕输出Error: No Correct Name
		print("Error: No Correct Name")
	else:#输入正确的游戏对象
		print("--------") # 输出"-------- "进行分割
		print("您的选择为",player_choice)
		player_number = name_to_number(player_choice)  # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
		comp_number = random.randrange(0,5)    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
		comp_choice = number_to_name(comp_number)# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
		print("计算机选择为",comp_choice) # 在屏幕上显示计算机选择的随机对象
		if comp_number-player_number>2 or comp_number-player_number==(-1) or comp_number-player_number==(-2) :# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
			print("您赢了！")
		elif player_number - comp_number == 0:
			print("您和计算机出的一样呢")
		else:
			print("计算机赢了")# 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”



# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


