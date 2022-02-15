





def OriginDataAnls(origin_data):
    num = 0
    index = 1

    for i in range(16):
        dig = int.from_bytes(origin_data[num+2:num+4], 'little', signed=False)
        dot = int.from_bytes(origin_data[num:num+2], 'little', signed=False)
        fly_time = round(dig + dot/65535,5)
        num += 4
        index += 1
        # total.cell(count,index).value = fly_time
    for i in range(16):
        pulse_wid = round(int.from_bytes(origin_data[num:num+1], 'little', signed=False)/127,3)
        num += 1
        index += 1
        # total.cell(count,index).value = pulse_wid
    for i in range(8):
        timeDiff = int.from_bytes(origin_data[num:num+4], 'little', signed=True)
        num += 4
        index += 1
        # total.cell(count,index).value = timeDiff
    for i in range(4):
        state = int.from_bytes(origin_data[num:num+1], 'little', signed=False)
        num += 1
        index += 1
        # total.cell(count,index).value = state
    for i in range(2):
        flowstate = int.from_bytes(origin_data[num:num+2], 'little', signed=False)
        num += 2
        index += 1
        # total.cell(count,index).value = flowstate
    for i in range(4):
        waveTime = int.from_bytes(origin_data[num:num+2], 'little', signed=False)
        num += 2
        index += 1
        # total.cell(count,index).value = waveTime
    for i in range(4):
        averagetimeDiff = int.from_bytes(origin_data[num:num+4], 'little', signed=True)
        num += 4
        index += 1
        # total.cell(count,index).value = averagetimeDiff
    for i in range(8):
        waveTime = int.from_bytes(origin_data[num:num+2], 'little', signed=False)
        num += 2
        index += 1
        # total.cell(count,index).value = waveTime
    for i in range(8):
        refWaveTime = int.from_bytes(origin_data[num:num+2], 'little', signed=False)
        num += 2
        index += 1
        # total.cell(count,index).value = refWaveTime

    flowrate = int.from_bytes(origin_data[num:num+4], 'little', signed=False)
    num += 4
    index += 1
    # total.cell(count,index).value = flowrate

    for i in range(5):
        flowtotal = int.from_bytes(origin_data[num:num+4], 'little', signed=False)
        num += 4
        index += 1
        # total.cell(count,index).value = flowtotal

    bjgc = int.from_bytes(origin_data[num:num+2], 'little', signed=False)
    num += 2
    index += 1
    # total.cell(count,index).value = bjgc

    ckgc = int.from_bytes(origin_data[num:num+2], 'little', signed=False)
    num += 2
    index += 1
    # total.cell(count,index).value = ckgc


    temp = round(int.from_bytes(origin_data[num:num+2], 'little', signed=False)/100,2)
    num += 2
    index += 1
    # total.cell(count,index).value = temp


    a2 = int.from_bytes(origin_data[num:num+1], 'little', signed=False)
    a3 = a2 & 0x80
    a4 = (a2 >> 6) & 0x01
    a5 = (a2 >> 5) & 0x01
    a6 = a2 & 0x1F
    if a6 >= 16 and a6 <= 31:
        a6 = a6 - 32
    if a4 == 1:
        a6 += 20
    if a5 == 1:
        a6 -= 20
    a1 = a6
    if a3 == 0:
        a7 = '↑'
        a8 = 0
    else:
        a7 = '↓'
        a8 = 1
    temp1 = a7 +str(a1)
    num += 1
    index += 1
    # total.cell(count,index).value = temp1


    temp2 = int.from_bytes(origin_data[num:num+1], 'little', signed=False)
    num += 1
    index += 1
    # total.cell(count,index).value = temp2