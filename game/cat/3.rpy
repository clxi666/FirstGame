

define xindian = "audio/music/xindian.mp3"
define di = "audio/music/di.mp3"

image hospital = "bingfang.jpg"



label jieshoumaodie:
    mc "我同意帮你做事"
    maodie"那太好啦喵~"
    hide maodiemaimeng
    show cathaqi at right with dissolve
    maodie "哈————————"
    stop music
    "…………"
    scene black with fade
    "空间中存在的BGM的戛然而止"
    "风不再流淌，生物不再生长，时间就此凝固，连光都停止了传播..."
    "世界像只剩下虚无黑暗的空间，只有我和猫咪存在于此。"
    show fdhtaitou at left with dissolve
    mc "这是怎么回事？！"
    pause 0.3
    mc "（奇怪...我明明喊出了声，却听不到自己的声音？）"
    mc "（难道是我耳朵聋了？！）"
    show catnol at Transform(center,zoom = 0.5,xpos = 0.7,ypos = 0.4)
    maodie "不用担心，我只是将你带入了一个空间，在这里，我们可以用意识交流。"
    mc "意识交流？这么牛掰？"
    maodie "是的。"
    mc "那你说吧，要让我做什么？"
    maodie "我需要你帮我做出‘上帝的选择’。我确实是上帝不假，变成猫是为了实现一个女孩的心愿：她想遇见一只猫。"
    mc "啊？为啥你要亲自变成猫？你可是上帝欸，随便丢一只猫猫让她遇见不就好了？"
    maodie "那当然不行，因为随便一只猫是不会听我话的，更不会听她的话。让别人听话的方式有很多，但让自己听话最可靠保险。你不需要知道这么多，只需做出选择就行。"
    mc "行"
    "虽然冯邓红不了解前因后果"
    "但是他也不好多问什么"
    jump hospital



label hospital:
    scene hospital at Transform(size=(config.screen_width, config.screen_height), fit="cover")
    show mc nomal at left with dissolve
    show catnol at Transform(center,zoom = 0.5,xpos = 0.7,ypos = 0.4)
    "周围场景瞬间转变，一猫一人来到了一家医院的病房。"
    play music xindian fadein 0.5
    "病房整洁宽敞，是个单间，中间的病床上躺着一位中年男子——头发光亮整洁，脸上没有痘痘或痘印，看着是个注重仪表的有钱人。"
    maodie "你现在可以决定他的生死。那一个亿是他的私人财产，他死后将无人接管，因为他无亲无故。我可以让你接手这笔钱，前提是你使用上帝的能力让他死亡。"

    # 第一个选项分支
    menu:
        "让他死":
            jump choice_kill
        "不！我做不到":
            jump choice_refuse
        "寻问男子的情况":
            jump choice_ask



label choice_kill:
    mc "这男子看起来也活不了多久了，不如让他痛痛快快地走，他的遗产就由我来继承吧！"
    pause 0.5
    stop music
    play music di
    pause 1.0
    stop music
    "病床旁的心律机‘嘀——’地一声停止了跳动。"
    
    "周围十分安静，没有人发现：这一刻，一条鲜活的生命被所谓的‘上帝’抹去。"
    "他走得很宁静，好似睡了一个很长、很长、很长的觉......"
    
    scene bg cg with dissolve 
    show fdhtaitou at left with dissolve
    "时空转变，我和猫回到了初见的那一天——"
    "但不同的是，我见到的不是躺在马路中间的活猫，而是一摊脑浆爆开的猫尸体。"
    show card at Transform(center,zoom = 0.5,xpos = 0.5,ypos = 0.4) with Dissolve(0.5)
    "那只猫已经被车压死，尸体旁有一张黑卡，就是那只猫之前给我的那张！"


    menu:
        "上去捡起那张黑卡":
            jump choice_pick_card
        "直接走掉，远离这里":
            jump choice_leave





label choice_pick_card:
    "一个声音""你可真贪！杀人是要偿命的！那只猫就是你！"
    "一个声音" "你给老子进局子吧！死刑！死刑！！！"

    return



label choice_leave:
    "一个声音""人都杀了你还不要钱？！也给老子去死吧！"
    "冯邓红突然脑袋一晕，倒在了地上，再也没有起来。"
    "他的肉体死亡了，精神却被带到了新的空间。"
    "一个声音" "上一任上帝死了，那就由你来当这一任上帝吧。你要为自己赎罪，不得超生！"
    "达成成就，赎罪的上帝"
    return


label choice_refuse:
    mc "不行！我不能随便决定别人的生死！这太荒唐了！"
    maodie "（沉默片刻）看来你和之前的‘选择者’不一样。"
    return


label choice_ask:
    mc "他到底是什么人？为什么会无亲无故？"
    maodie "他是那个‘想遇见猫的女孩’的父亲——当年他抛弃了女孩和她的母亲，导致女孩抑郁多年，唯一的心愿就是‘遇见一只温暖的猫’。"

    return