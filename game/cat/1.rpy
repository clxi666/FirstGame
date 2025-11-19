label nosave:
    mc"算了这本来也不关我的事"
    mc"随它去吧"
    hide catnol
    show cathaqi at right with dissolve
    "那辆车并没有减速"
    "只是径直从耄耋的身上碾压过去"
    hide cathaqi
    "耄耋原地去世"
    "被压成了猫饼"
    "卒"
    mc "有时候也得根据自身能力做判断啊"
    "冯邓红走开了"
    jump end

transform move:
    offscreenleft
    linear 0.5 pos (0.9,0.8)


label save:
    "来不及多想"
    "冯邓红冲过去"
    "救一下"
    hide mc nomal
    show fdhcongmang at move
    "…………"
    hide catnol
    "………………"
    hide fdhcongmang
    "……"
    show hzh2 at center
    pause 1.0
    "冯邓红把他送到了路边上"
    show cathaqi at Transform(right,zoom = 0.5,xpos = 0.7,ypos = 0.4)
    maodie "哈————————"
    "汽车恰巧疾驰而过"
    "耄耋似乎意识到了什么"
    hide cathaqi
    show catnol at Transform(center,zoom = 0.5,xpos = 0.7,ypos = 0.4)
    "发出来咕噜咕噜的声音"
    "虽然冯邓红也知道猫听不懂人话"
    "但是…………"
    mc"我其实只是想救你罢了"
    maodie"那这么说你是我的救命恩人了"
    hide catnol
    show catjugong at Transform(center,zoom = 0.5,xpos = 0.7,ypos = 0.4)
    "耄耋对着冯邓红鞠了一躬"
    pause 1.0
    hide catjugong
    show catnol at Transform(center,zoom = 0.5,xpos = 0.7,ypos = 0.4)
    hide hzh2
    show hzhchayi at center with dissolve
    mc "你你你... 你怎么会说话！"
    "冯邓红吓得双腿一软，‘噗通’一声瘫坐在路边的草地上，手指着小猫，说话都打了结，眼睛瞪得溜圆。"
    "小猫慢悠悠地直起身，又对着他欠了欠身，嘴角仿佛噙着笑意：‘这是个秘密。’"
    "话音刚落，它纵身一跃，灵巧地跳进旁边的灌木丛里，只留下一阵轻微的枝叶响动，眨眼间就没了踪影，仿佛刚才的一切都是幻觉。"
    hide catnol with Dissolve(1.0)
    mc "（会说话的猫... 我没看错吧？刚才那一下，真是救了个‘大人物’？）"
    "冯邓红愣在原地好半天，才哆哆嗦嗦地爬起来，拍了拍身上的草屑，心还在砰砰狂跳。他望着小猫消失的方向，满脑子都是问号，却也没敢追进去。"
    jump end

label gift:
    scene black with fade
    pause 1.0
    scene 517 with fade
    play music over fadeout 1.0 
    pangbai "接下来的几天，冯邓红的寝室门口，开始接连出现让他意想不到的‘谢礼’。"
    pangbai "第一天清晨，冯邓红刚推开寝室门，就看到门口放着一个湿漉漉的网袋，里面装着一条活蹦乱跳的鲤鱼，鱼鳃还在一张一合。网袋上贴着一张白色纸条，用毛笔字工工整整地写着‘冯邓红收’。"
    show mc nomal at left with dissolve
    pause 1.5
    mc "（这... 是那只哈基米送的？送条活鱼是什么操作？）"
    show fish at Transform(center,zoom = 0.5,xpos = 0.5,ypos = 0.4) with Dissolve(0.5)
    "冯邓红看着那条扑腾的鱼哭笑不得，自己既不会杀鱼也不想养，干脆提着网袋跑到学校的人工池塘边，把鱼轻轻放回了水里。"
    mc "去吧去吧，回到你的地盘好好活着，下次可别再随便躺马路中间了。"
    scene black with fade
    pause 0.8
    scene 517 with fade
    pangbai "第二天傍晚，冯邓红下课后回到寝室，门口又多了一个保鲜盒。打开一看，里面装着精致的剩饭和切成小块的新鲜水果，还带着点温热，纸条依然是‘冯邓红收’。"
    mc "（这次是吃的？看着还挺干净...）"
    show mc nomal at left with dissolve
    pause 1.5
    show fruit at Transform(center,zoom = 0.5,xpos = 0.5,ypos = 0.4) with Dissolve(0.5)
    "寝室里的室友闻到香味都围了过来，冯邓红也没多想，大方地把东西分给了大家。"
    mc "来，兄弟们，尝尝这‘神秘投喂’，味道还不错。"
    "室友们吃得不亦乐乎，一边吃一边起哄，猜是哪个暗恋他的女生送的，冯邓红只能笑着打哈哈，心里却清楚，这多半还是那只哈基米的‘手笔’。"
    scene black with fade
    pause 0.8
    scene 517 with fade
    "第三天，惊喜直接升级。冯邓红刚睡醒，就被室友的惊呼吵醒。"
    show mc nomal at left with dissolve
    pause 1.5
    show iphone17 at Transform(center,zoom = 0.5,xpos = 0.7,ypos = 0.4) with Dissolve(0.5)
    "寝室门口的地板上，静静躺着一部崭新的 iPhone 17，黄色的机身闪着光，一看就价值不菲。手机背面贴着一张小纸条，除了‘冯邓红收’，还写着一串六位数字的密码。"
    "冯邓红拿起手机仔细一看，发现机身有轻微的使用痕迹，像是别人用过的二手机。"
    hide mc nomal
    show fdhtaitou at left with dissolve
    mc "（iPhone 17？这猫也太神通广大了吧...）"
    "他试着用纸条上的密码解锁，竟然一下就打开了。看着手机里干净的界面，冯邓红犹豫了一下 —— 毕竟是来路不明的东西，自己用着不踏实。"
    "琢磨了半天，他想起室友常说的转转回收，干脆抱着试一试的心态，把手机寄了过去。没想到几天后，回收款到账的短信弹了出来，整整 8888 元！"
    mc "我去！真的到账了,8888 块！"
    "冯邓红看着手机银行里的余额，眼睛都亮了，室友们凑过来一看，顿时炸开了锅，纷纷追问他是不是中了奖。"
    pause 0.7
    scene black with fade
    pause 0.8
    scene 517 with fade
    show fdhtaitou at left with dissolve
    pangbai "第四天，真正的‘重磅惊喜’来了。冯邓红刚走到寝室门口，就看到地上放着一张黑色的银行卡，卡片上贴着一张小纸条，依旧是‘冯邓红收’，下面还写着一串密码。"
    "前三次的经历已经让他有了心理准备，但看到银行卡的瞬间，冯邓红还是忍不住心跳加速。他揣着银行卡，揣着满心的忐忑和期待，一路跑到学校附近的 ATM 机。"
    "插卡、输密码，屏幕上跳出余额的那一刻，冯邓红的眼睛都直了 —— 一串长长的数字，后面跟着好几个零，整整一个小目标！"
    show card at Transform(center,zoom = 0.5,xpos = 0.5,ypos = 0.4) with Dissolve(0.5)
    mc "我的妈呀... 一、一个小目标？！"
    "他盯着屏幕看了足足半分钟，确认自己没有数错零，突然觉得头晕目眩，差点一头栽倒在 ATM 机前，嘴角却控制不住地往上扬，开心得快要昏厥过去。"
    mc "我这是... 要走上人生巅峰了？！"
    "他紧紧攥着银行卡，手心全是汗，脑子里已经开始畅想未来的生活：再也不用为生活费发愁，能买喜欢的东西，能带着室友们吃大餐，甚至还能支持自己想做的事..."
    pangbai "阳光透过 ATM 机的玻璃窗照进来，落在冯邓红兴奋得发红的脸上。那只神秘的黑猫，用一份份离奇的谢礼，彻底打乱了他原本平淡的生活。"
    pangbai "只是，这突如其来的巨额财富背后，真的没有代价吗？那只说话的哈基米，又藏着怎样的秘密？冯邓红的人生巅峰，真的会这么轻易到来吗？"
    pause 2.0
    stop music fadeout 0.5
    scene black with fade
    jump cata