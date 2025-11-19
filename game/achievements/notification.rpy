# notification.rpy  -- Ren'Py 7 可用
screen ach_popup(ach):
    zorder 2000
    frame:
        xalign 0.5 yalign 0.1
        background Solid("#000000aa")
        padding (20,10)
        hbox:
            spacing 15
            add ach.icon_unlocked
            vbox:
                text "[ach.title!q]" size 24 bold True
                if not ach.hidden or ach.unlocked:
                    text "[ach.desc!q]" size 18
    timer 1.5 action Hide("ach_popup")   # 1.5 秒后自己消失