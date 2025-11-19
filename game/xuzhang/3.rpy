label end:
    
    mc "有点饿了，去食堂逛逛吧"
    scene black with fade
    pause 0.5
    scene restraunt with fade
    play music voice_bgm fadein 0.5
    "食堂里很热闹"
    mc "买点什么吃一吃呢？"
    menu:
        "湘味套餐":
            pass
        "朱家小馆":
            pass
        "瑞膳鱼粉":
            pass
        "量贩自助":
            pass
    pause 1.0
    show fdheat at left with dissolve
    "冯邓红找好位置，坐了下来"
    mc "这食堂，吃来吃去就那几样，一点意思没有。"
    mc "人还那么多，排队难等"
    mc "没劲，难受"
    "冯邓红埋头吃起晚饭"
    pause 0.5
    "此时，一位面容姣好，又高又壮的女孩从冯邓红面前经过"
    "那时，他正大口大口吃着饭，"
    "却猛然停下来，"
    "他嗅到了一股非常带派的味道"
    hide fdheat
    "抬头"
    show fdhtaitou at left with dissolve
    "那个女孩在他对桌坐了下来"
    show yujienomal at right with dissolve
    "冯邓红认出了她"
    "那是他的同班同学————雨姐"
    "雨姐刚刚上完体育课"
    menu:
        "向她询问体育课的情况":
            $ yujiemark = 1
            $ mark =  check_marks()
            if mark:
                return
            jump ask
        "假装没看见她":
            mc "我和她也并不熟"
            mc "假装没看到她吧"
            "冯邓红加快了吃饭的速度"
            "……"
            "吃完后，他很快便离开了"
            if dcxmark==1:
                jump classroom
            elif maodiemark == 1:
                jump gift
            else:
                jump Single_Line
        "向他告白":
            hide yujienomal
            show chengduluoli1 at Transform(center,zoom = 0.5,xpos = 0.7,ypos = 0.4)with dissolve
            "成都萝莉""好的，宝贝"
            jump chengduluolia


label panduan:


label chengduluolia:
    scene black with fade
    play music aimei
    "……………………"
    mc"有的时候，幸福来得就是这么突然"
    mc"你永远无法猜到他会以什么样的形式来到"
    scene bed at Transform(size=(config.screen_width, config.screen_height), fit="cover") with fade
    show chengduluoli2 at left with dissolve
    "成都萝莉""❤️❤️❤️宝贝快来❤️❤️❤️"
    show hzhchayi at right with dissolve
    mc "（这不是我想要的😭😭😭😭😭）"
    scene black with fade
    mc"但是…………"
    stop music
    mc"这样好像也不错"
    "冯邓红堕落了"
    "解锁成就，你在湖工商只能算个萝莉！"
    pangbai"告白怎么还被截胡了呢"
    "end"
    return



label Single_Line:
    play music single_bgm fadein 1.0

    scene black with fade

    pangbai "你已经连续错过了几段姻缘"
    
    pangbai "旁白都看不下去了"

    pangbai "你是豆刺腥本人吧，这么菜"
    scene bg cg with dissolve
    show hzh2 at center
    pangbai "我现在要借助上帝的力量把你永远变成豆刺腥，哈哈哈"
    pause 2.0
    hide hzh2
    show hzhchayi at right
    mc "不，不要啊，变成豆刺腥在517和狗有什么区别，"
    mc "不，我不想要这样！我不想被栓门口！"
    scene black with fade
    pause 2.0
    scene bg cg with dissolve
    "冯邓红缓缓睁开双眼"
    show hzhdcx at center
    "发现自己真的变成了豆刺腥"
    pangbai "你就以这个姿态活一辈子吧哈哈哈哈"
    pangbai "哈哈哈哈哈"
    mc "我的一切都毁了"
    scene black with fade
    "达成成就，单身之神。"
    "是不是哪里走错了呢？好好想想吧"
    "end"
    return