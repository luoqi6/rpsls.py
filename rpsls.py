#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����
���ڣ�2020.4.16
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):   
	if name == "ʯͷ":
		return 0
	elif name == "ʷ����":
		return 1
	elif name == "ֽ":
		return 2
	elif name == "����":
		return 3
	elif name == "����":
		return 4
	else:
		print("Error: No Correct Name")

def number_to_name(number):
	if number in range(0,5):
			if number == 0:
				return "ʯͷ"
			elif number == 1:
				return "ʷ����"
			elif number == 2:
				return "ֽ"
			elif number == 3:
				return "����"
			elif number == 4:
				return "����"
			else:
				print("Error: No Correct Name")  


def rpsls(player_choice):
	if player_choice!="ʯͷ" and player_choice!="����" and player_choice!="����" and player_choice!="ʷ����" and player_choice!="ֽ":#���벻��ȷ����Ϸ����ʱ����Ļ���Error: No Correct Name
		print("Error: No Correct Name")
	else:#������ȷ����Ϸ����
		print("--------") # ���"-------- "���зָ�
		print("����ѡ��Ϊ",player_choice)
		player_number = name_to_number(player_choice)  # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
		comp_number = random.randrange(0,5)    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
		comp_choice = number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
		print("�����ѡ��Ϊ",comp_choice) # ����Ļ����ʾ�����ѡ����������
		if comp_number-player_number>2 or comp_number-player_number==(-1) or comp_number-player_number==(-2) :# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
			print("��Ӯ�ˣ�")
		elif player_number - comp_number == 0:
			print("���ͼ��������һ����")
		else:
			print("�����Ӯ��")# ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�



# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


