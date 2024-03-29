#560 - 用lambda选出最快的记录; 
#本节作业：最慢的记录实现作为作业；用for循环的方式实现功能
import random
import sys
import time #时间模块

guess_limit = int(sys.argv[1]) #最多猜测次数
scores = [] #战绩

cycle = 0 #第几轮
while(True):
	cycle += 1
	answer = random.randint(1,1)
	is_right = False 
	begin_time = time.time()
	#while:根据一个判断条件；for是循环一个已知的列表 
	for i in range(guess_limit):
		guess = int(input('我想好了1个1-10之间的数字，你猜是几？')) 
		if(answer == guess):
			is_right = True
			break;
		elif(guess > answer):
			print('太大了', end='，')
		else:
			print('太小了', end='，')

		if(i < guess_limit-1):
			print('请继续猜：')

	#处理结果
	if(is_right):
		print('你猜对了！👌')
	else:
		print('你用完了猜测次数，你失败了❌')
	end_time = time.time()
	used_time = end_time - begin_time #用了多少时间
	used_time = round(used_time, 2) #保留两位小数
	print(f'共用时{used_time}秒')

	#保存战绩
	scores.append((cycle, is_right, used_time))
	best_score = min(scores, key=lambda x:x[2] if x[1] else 9999)
	print('=========战绩============')
	for _cycle, _is_right, _used_time in scores:
		label = '✌️ ' if(_is_right) else '❌ '
		best_label = '👄' if(_cycle == best_score[0] and best_score[1]) else '' #设定最好的标记
		print(f'{_cycle}轮，{label}，{_used_time}{best_label}')
	print('========================')

	con = input('要继续玩，输入y，否则直接回车：')
	if(con != 'y'):
		print('886...')
		break #退出游戏






