label out:
    scene black with fade
    play music out fadein 0.5
    pause 0.5
    scene bg cg with fade
    show fdhtaitou at left with dissolve
    "我怎么突然被传送到这里来了"
    "……"
    "…………"
    "………………"
    show man at center with dissolve
    if dcxmark == 1 and yujiemark == 1:
        pangbai "有了豆刺腥，你居然还想勾搭雨姐"
    elif yujiemark == 1 and maodiemark == 1:
        pangbai "有了耄耋，你居然还想勾搭雨姐"
    else:
        pangbai"有了豆刺腥，居然还想勾搭耄耋"
    pangbai"简直猎奇"
    "和豆刺腥有的一比"
    pangbai"旁白都看不下去了"
    hide man
    hide fdhtaitou
    show hzh2 at center
    pangbai "简直就是个魔丸"
    pangbai "我现在要借助上帝的力量把你永远变成魔丸，哈哈哈"
    pause 2.0
    hide hzh2
    show hzhchayi at right
    "………"
    "………………"
    scene black with fade
    pause 2.0
    scene bg cg with dissolve
    "冯邓红缓缓睁开双眼"
    show mowan at center
    "他的身体已经完全不再是自己了"
    pangbai "你就以这个姿态活一辈子吧哈哈哈哈"
    pangbai "哈哈哈哈哈"
    mc "我的一切都毁了"
    scene black with fade
    "达成成就，见异思迁。"
    "end"
    return