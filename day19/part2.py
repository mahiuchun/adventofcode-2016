from collections import deque

INP = 3014603

mid = (INP + 1) // 2
top = deque(range(1, mid+1))
bot = deque(range(mid+1, INP+1))

while len(top) > 1:
    if len(top) > len(bot):
        top.pop()
    else:
        bot.popleft()
    x = top.popleft()
    bot.append(x)
    x = bot.popleft()
    top.append(x)
print(top[0])
