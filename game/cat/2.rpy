# 定义图片
image lvxing = "lvxing.jpg"
image business = "business.jpg"
image mai = "mai.png"
image red = "red.jpg"

# 人物
image fdhxiao = "fdhxiao.png"
image maodiemaimeng = "maodiemaimeng.png"


define happy = "audio/music/happy.mp3"
define qiaomen = "audio/music/qiaomen.mp3"
define zhuang = "audio/music/zhuang.mp3"


label cata:
    stop music
    mc "如果有一天我变得很有钱~"
    mc "我的第一选择不是去环游世界"
    mc "躺在世界最大最软的沙发里"
    mc "吃了就睡，醒了再吃一年~~~"
    mc "……"
    scene 517 with fade
    "冯邓红躺在寝室的床上哼着歌"
    show fdhtaitou at left with dissolve
    mc "怎么花掉这笔钱呢？"
    mc "环游世界,来场孤独的旅行？"
    show lvxing at Transform(center,zoom = 0.5,xpos = 0.5,ypos = 0.1) with Dissolve(0.5)
    mc "……"
    hide lvxing with Dissolve(1.0)
    mc "创业投资，创建一个属于自己的商业帝国？"
    show business at Transform(center,zoom = 0.5,xpos = 0.5,ypos = 0.1) with Dissolve(0.5)
    mc "…………"
    hide business with Dissolve(1.0)
    mc "还是大卖特卖，男人再富也要卖？"
    show mai at right with dissolve
    mc "………………"
    hide mai with Dissolve(1.0)
    pause 1.0
    hide fdhtaitou
    show fdhxiao at left with dissolve
    play music happy
    "冯邓红发出傻气的奸笑声"
    mc "小孩子才做选择，我都想要"
    mc "嘻嘻~~~"
    pause 1.0
    stop music
    mc "管他呢，反正我不用上学了"
    hide fdhxiao
    show fdhcongmang at left with dissolve
    "冯邓红带着纸，到床上睡去"
    scene black with fade
    "…………"
    jump maolaile

label maolaile:
    play sound qiaomen fadein 0.5
    "咚咚咚……"
    "咚咚咚…………"
    stop music
    "冯邓红被两道敲门声惊醒了"
    scene 517 with fade
    mc "谁啊"
    show fdhtaitou at left with dissolve
    "冯邓红很不情愿地去开门"
    "……"
    pause 1.0
    play music over fadein 0.5
    show catnol at Transform(center,zoom = 0.5,xpos = 0.7,ypos = 0.4)
    mc "!!!"
    mc "竟然是你！！"
    maodie "喵~这次来是想和你说件事的喵~"
    hide fdhtaitou
    show mc nomal at left with dissolve
    "冯邓红有点诧异"
    maodie "虽然说你是我的救命恩人喵~"
    maodie "但这钱也不能直接给你喵~"
    maodie "因为…………"
    maodie "这钱不是我的喵~"
    hide mc nomal
    show fdhxiao at left with dissolve
    mc "什么！！"
    mc "你说这钱不是你的？？？"
    hide fdhxiao
    show fdhcongmang at move
    "…………"
    "冯邓红一把抓住耄耋，"
    "像是愤怒"
    "又像是害怕"
    hide catnol
    "………………"
    hide fdhcongmang
    "……"
    show hzh2 at center
    pause 1.0
    show cathaqi at Transform(right,zoom = 0.5,xpos = 0.7,ypos = 0.4)
    "……"
    hide cathaqi
    show catnol at Transform(center,zoom = 0.5,xpos = 0.7,ypos = 0.4)
    "他的手像是在颤抖"
    mc"难不成是你偷的？？"
    "冯邓红气的咬牙切齿，却还是尽量压着声音说话"
    mc "你知道这样我有可能会坐牢吗？"
    hide catnol
    show maodiemaimeng at Transform(center,zoom = 0.5,xpos = 0.7,ypos = 0.4)
    maodie "恩人你别这么激动喵~"
    maodie "我不会害你的喵~"
    maodie "我其实是上帝"
    maodie "我现在需要你去帮我做一件事情，事成之后，这一个亿就完全属于你了"
    "耄耋的做了个wink，这事好久不做了，显得无比真诚"
    "冯邓红盯着耄耋的双眼，沉思了片刻"
    "似是接受了耄耋的话"
    "他把自己的人生全都设想了一遍"
    "有什么比金钱还重要呢？"
    "到底要不要接受耄耋的提议呢？"
    menu:
        "接受":
            
            hide hzh2
            show fdhtaitou at left
            mc"(钱不是万能的，但是……)"
            mc "(没有钱是万万不能的)"
            mc "(我要用钱重启我吊毛的人生！！)"
            jump jieshoumaodie
        "拒绝":
            mc "我觉得我可以靠自己在这个世界好好生存"
            mc "所以我不会接受你的提议！！"
            jump jujuemaodie


label jujuemaodie:
    scene black with fade
    "冯邓红揉揉眼睛"
    "……"
    "…………"
    "………………"
    scene bg cg with fade
    "回到了那天清晨"
    show mc nomal at Transform(left,zoom = 0.75,ypos = 0.5)

    mc "一只猫。。"
    show catnol at Transform(center,zoom = 0.5,xpos = 0.7,ypos = 0.4)
    play music car fadeout 0.5
    pause 1.0
    stop music fadeout 0.5
    mc"不好有车要过来了"
    "要不要去救它呢？"
    menu:
        "救":
            scene black with fade
            "……"
            mc "我不知道我为什么要做这样的决定"
            mc "不知道"
            mc "也许是对可爱生物的本能冲动"
            mc "也许只是一时兴起"
            mc "但是我"
            mc "…………"
            mc "并不后悔"
            play sound zhuang
            scene red with None
            pause 0.3
            scene black with None
            "……………………"
            mc "好痛！"
            mc "我好像撞大运了"
            "………………"
            mc "那只猫呢？"
            mc "我救到了吗？"
            mc "不好"
            mc "我的视野逐渐模糊了"
            mc "好冷"
            mc "动不了了"
            mc "我快要死了吗？"
            mc "可是我还有很多想做的事情没有做"
            mc "好不甘心！"
            mc "我还不想死"
            "冯邓红什么也看不到了"
            "也逐渐停止了呼吸"
            "…………"
            maodie "我其实不想这样的喵~"
            pangbai "冯邓红，卒"
            "解锁成就，草率的牺牲"
            "end"
            return
        "不救":
            mc"算了这本来也不关我的事"
            mc"随它去吧"
            hide catnol
            show cathaqi at right with dissolve
            "那辆车并没有减速"
            "………………"
            hide cathaqi
            "只是径直从耄耋的身上碾压过去"
            "耄耋原地去世"
            "被压成了猫饼"
            "卒"
            mc "有时候也得根据自身能力做判断啊"
            "解锁成就，无情的人"
        
            
