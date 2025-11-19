label ask_character:
    show heroine happy at right
    heroine "我喜欢带入苦主，这样有种被牛的快感。"
    heroine "你呢？有特别喜欢的角色吗？"
    
    show mc nomal at left with dissolve
    mc "我是老吃家，比较喜欢带入女主，他的坚韧很打动我。"
    
    show heroine close_smile at right
    heroine "确实...每个人都能在书中找到自己的影子。"
    jump continue_conversation

label silent_admire:
    show heroine close_eyes at center
    "我静静地注视着她，阳光在他的脸间跳跃。"
    "他专注谈论书籍的样子，让我不禁有些入迷。"
    
    show heroine close_smile at right
    heroine "怎么了？我脸上有什么吗？"
    
    show mc nomal at left with dissolve
    mc "啊，没有...只是觉得男人也可以这样美丽吗。"
    
    show heroine happy at center
    heroine "谢谢...你真是个有趣的人。"
    jump continue_conversation

label continue_conversation:
    show heroine normal at right
    heroine "说起来，我经常在这里看书，还是第一次遇到同样喜欢古典文学的人。"
    
    mc "我也是第一次遇到这么懂文学的男生。"
    
    # 重要选择 - 决定是否触发CG
    menu:
        "鼓起勇气邀请他一起喝咖啡":
            $ dcxmark = 1
            jump invite_coffee
            
        "只是礼貌地道别":
            jump say_goodbye

label invite_coffee:
    show heroine close_eyes at center
    heroine "诶？现在吗？"
    
    show mc nomal at left with dissolve
    mc "是的，图书馆楼下就有一家不错的咖啡厅。"
    mc "我们可以继续讨论刚才的话题..."
    
    show heroine close_smile at right
    heroine "..."
    
    show heroine happy at center
    heroine "好啊，我很乐意。"
    
    # 触发CG场景
    stop music fadeout 1.0
    scene black with fade
    play music library_bgm fadein 1.0
    
    "我们收拾好书籍，一起走向图书馆门口。"
    "在夕阳的余光中，我们的影子被拉得很长..."
    
    # 显示特殊CG
    scene bg cg  with dissolve
    pause 2.0
    
    heroine "今天真的很开心能遇到你。"
    mc "我也是...希望以后还能一起讨论书籍。"
    
    show heroine close_smile at center with dissolve
    heroine "嗯，一定会的。"
    
    "就这样，一次偶然的邂逅，开启了一段美好的缘分..."
    
    jump cat

label say_goodbye:
    show heroine normal at center
    heroine "时间不早了，我该回去了。"
    
    mc "好的，很高兴认识你。"
    
    show heroine happy at center
    heroine "明天晚上我们继续在这里见面"
    
    mc "我会的"
    
    "我们互相道别，他抱着书离开了图书馆。"
    "虽然有些遗憾，但这次邂逅依然让我心中充满了温暖..."
    stop music fadeout 2.0
    scene black with fade
    "我们的图书馆邂逅，就这样画上了句号..."
    jump cat

label cat:
    stop music
    scene black with fade
    "…………"
    "清晨"
    scene bg cg with fade
    show mc nomal at Transform(left,zoom = 0.75,ypos = 0.5)
    play music walk_bgm fadeout 2.0
    "冯邓红在散步"
    mc"阳光暖暖的，很舒服"
    "他贪婪地吮吸着清新的空气"
    "到达马路边上"
    "一团奇怪的东西躺在马路中间"
    "冯邓红揉揉眼睛"
    stop music fadeout 0.5
    "……"
    "…………"
    "………………"
    show catnol at Transform(center,zoom = 0.5,xpos = 0.7,ypos = 0.4)
    mc"一只猫？"
    "为什么有猫躺在马路中间"
    play music car fadeout 0.5
    pause 1.0
    stop music fadeout 0.5
    mc"不好有车要过来了"
    mc"小心"
    "要不要去救它呢？"
    menu:
        "救":
            $ maodiemark = 1
            $ mark = check_marks()
            if mark:
                return
            jump save
        "不救":
            jump nosave