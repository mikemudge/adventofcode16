from collections import deque

with open('advent10') as f:
    lines = f.readlines()

    count = 0
    bots = {}
    startBot = None
    for line in lines:
        parts = line.strip().split()
        if parts[0] == 'bot':
            botId = parts[1]
            bot = bots.get(botId, {'values': set([])})
            bot['id'] = botId
            # 2 gives, 3 low, 4 to, 5 bot/output
            if parts[5] == 'bot':
                lowBotId = parts[6]
                bot['lowId'] = lowBotId
            else:
                bot['lowOutput'] = parts[6]
            # 7 and, 8 high, 9 to, 10 bot/output
            if parts[10] == 'bot':
                highBotId = parts[11]
                bot['highId'] = highBotId
            else:
                bot['highOutput'] = parts[11]
        else:
            # value
            value = int(parts[1])
            # 2 goes, 3 to, 4 bot
            botId = parts[5]

            bot = bots.get(botId, {'values': set([])})
            bot['id'] = botId
            bot['values'].add(value)
            if len(bot['values']) == 2:
                startBot = bot
        bots[botId] = bot

    print startBot
    bot = None
    outputs = {}
    queue = deque([startBot])
    while True:
        if not queue:
            break
        curBot = queue.popleft()
        print 'moving', curBot
        highValue = max(curBot['values'])
        lowValue = min(curBot['values'])
        highId = curBot.get('highId')
        lowId = curBot.get('lowId')
        botId = curBot.get('id')
        if lowValue == 17 and highValue == 61:
            print botId, lowValue, highValue
            winner = botId

        if lowId:
            if lowValue in bots[lowId]['values']:
                pass
                # print 'Already in the values', lowId, lowValue
            else:
                bots[lowId]['values'].add(lowValue)
                queue.append(bots[lowId])
        else:
            outputs[curBot.get('lowOutput')] = lowValue
            pass
            # print 'Output'

        if highId:
            if highValue in bots[highId]['values']:
                pass
                # print 'Already in the values', highId, highValue
            else:
                bots[highId]['values'].add(highValue)
                queue.append(bots[highId])
        else:
            outputs[curBot.get('highOutput')] = highValue
            pass
            # print 'Output'
    print winner, bots[winner]
    print outputs
    print outputs['0'], outputs['1'], outputs['2']
    print outputs['0'] * outputs['1'] * outputs['2']
