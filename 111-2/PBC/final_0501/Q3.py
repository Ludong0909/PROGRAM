input = input().split('+')

zh = ['零','一','二','三','四','五','六','七','八','九','十']


if len(input) == 2:
    # 帶分數
    dei = (input[0])
    son = ((input[1]).split('/')[0])
    mom = ((input[1]).split('/')[1])

    if len(dei) == 2:
        # 兩位數
        dei_zh10 = zh[int(dei[0])]
        if int(dei[0]) == 1:
            dei_zh10 = ''

        dei_zh1 = zh[int(dei[1])]
        dei_zh = dei_zh10 + '十' + dei_zh1
    else:
        # 一位數
        dei_zh = zh[int(dei)]

    if len(son) == 2:
        # 兩位數
        son_zh10 = zh[int(son[0])]
        if int(son[0]) == 1:
            son_zh10 = ''
        son_zh1 = zh[int(son[1])]
        son_zh = son_zh10 + '十' + son_zh1
    else:
        # 一位數
        son_zh = zh[int(son)]

    if len(mom) == 2:
        # 兩位數
        mom_zh10 = zh[int(mom[0])]
        if int(mom[0]) == 1:
            mom_zh10 = ''
        mom_zh1 = zh[int(mom[1])]
        mom_zh = mom_zh10 + '十' + mom_zh1
    else:
        # 一位數
        mom_zh = zh[int(mom)]

    print(dei_zh+'又'+mom_zh+'分之'+son_zh)
    

else:
    son = ((input[0]).split('/')[0])
    mom = ((input[0]).split('/')[1])


    if len(son) == 2:
        # 兩位數
        son_zh10 = zh[int(son[0])]
        if int(son[0]) == 1:
            son_zh10 = ''
        son_zh1 = zh[int(son[1])]
        son_zh = son_zh10 + '十' + son_zh1
    else:
        # 一位數
        son_zh = zh[int(son)]

    if len(mom) == 2:
        # 兩位數
        mom_zh10 = zh[int(mom[0])]
        if int(mom[0]) == 1:
            mom_zh10 = ''
        mom_zh1 = zh[int(mom[1])]
        mom_zh = mom_zh10 + '十' + mom_zh1
    else:
        # 一位數
        mom_zh = zh[int(mom)]

    print(mom_zh+'分之'+son_zh)