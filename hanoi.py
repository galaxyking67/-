"汉诺塔游戏攻略"
def move(f, to):
	global i
	print("第%d步："%i +f+" 移动到 "+to)
	i+=1
def hanoi(n, x, y, z):
	if n == 1:
		# print(x, '移动到', z)
		move(x,z)
	else:
		hanoi(n-1, x, z, y)
		# print(x,'移动到', z)
		move(x,z)
		hanoi(n-1, y , x, z)


while True:
	i = 1
	inp = input('请输入汉诺塔的层数：')
	if inp.isdigit():

		n = int(inp)
		if not n>0:
			print("请输入大于0的数字")
		
		else:
			hanoi(n, "1", "2", "3")
			print("一共需要%d步"%(i-1))
	else:
		print("游戏结束！")
		break