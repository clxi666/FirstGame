# 游戏脚本开始
define mc = Character("冯邓红", color="#100909")
define heroine = Character("豆刺腥", color="#100909")
define yujie = Character("雨姐", color="#100909")
define pangbai = Character("旁白", color="#100909")
define maodie = Character("耄耋", color="#100909")
# 定义背景图像
image bg library = "bg.jpg"
image bg cg = "cg.png"
image restraunt = "restraunt.png"
image 517 = "517.png"
image bed = "bed.png"


image man = "man.png"

#豆刺腥的图
image heroine normal = "character.png"
image heroine happy = "characterhappy.png"
image heroine close_eyes = "charactercloseeyes.png"
image heroine close_smile = "charactercloseeyessmile.png"
image dcxhuitou = "dcxhuitou.png"
image fish = "fish.png"

#冯邓红的图
image mc nomal = "nomalf.png"
image fdheat = "fdheat.png"
image hzh2 = "hzh2.png"
image hzhchayi = "hzhchayi.png"
image hzhdcx = "hzhdcx.png"
image fdhtaitou = "fdhtaitou.png"
image fdhcongmang = "fdhcongmang.png"
image fdhweisuo = "fdhweisuo.png"

#雨姐的图
image yujienomal = "yujienomal.png"
image yujiesweet = "yujiesweet.png"

#猫
image catnol = "cat.png"
image cathaqi = "cathaqi.png"
image catjugong = "catjugong.png"
image iphone17 = "iphone17.png"
image card = "card.png"
image fruit = "fruit.png"
# 定义音乐
define audio.library_bgm = "audio/music/bgm.mp3"
define audio.single_bgm = "audio/music/clown.mp3"
define audio.voice_bgm = "audio/music/voice.mp3"
define audio.walk_bgm = "audio/music/walk.mp3"
define audio.car = "audio/music/car.flac"
define over = "audio/music/over.mp3"
define out = "audio/music/out.mp3"
define aimei = "audio/music/aimei.mp3"
#定义全局变量

image mowan = "mowan.png"
image chengduluoli = "chengduluoli1.png"
image chengduluoli2 = "chengduluoli2.png"



label thestart:
    play music library_bgm fadein 2.0
    
    # 显示图书馆背景
    scene bg library with fade
    
    "一个安静的午后，我来到市立图书馆寻找参考资料。"
    "阳光透过巨大的玻璃窗洒在书架上，空气中弥漫着书香和宁静。"
    
    show heroine normal at right with dissolve
    
    "正当我在书架间穿梭时，一个身影吸引了我的注意。"
    "那是一个正在认真阅读的男孩，阳光勾勒出他专注的侧脸。"
    
    heroine "嗯...这本书的见解真是独特。"
    
    show mc nomal at left with dissolve
    mc "（他好像遇到了什么有趣的内容...）"
    
    # 主角不小心碰到书架
    "我试图从他身边经过，却不小心碰到了书架。"
    
    show heroine close_eyes at center
    heroine "啊！"
    
    "几本书从架子上掉了下来。"
    
    show heroine normal at right 
    heroine "没关系的，我来帮你捡。"
    
    show mc nomal at left with dissolve
    mc "真是抱歉！我太不小心了。"
    
    "我们同时蹲下捡书，手指不经意间触碰到一起。"
    
    show heroine close_smile at center
    heroine "啊..."
    
    show mc nomal at left with dissolve
    mc "对不起！"
    
    show heroine happy at center
    heroine "没关系。你也对文学类的书籍感兴趣吗？"
    
    show mc nomal at left with dissolve
    mc "是的，特别是古典文学。"
    
    heroine "真巧，我也是！"
    
    show heroine close_smile at right
    heroine "我正在读的这本《无能的丈夫》就是我最喜欢的作品之一。"
    
    mc "我也很喜欢。"
    
    # 对话选项
    menu:
        "你最喜欢书中的哪个角色？":
            jump ask_character

        "默默地看着他，觉得他很美":
            jump silent_admire