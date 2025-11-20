screen achievement_popup(achievement):
    zorder 1000
    modal False
    
    frame:
        xalign 0.02
        yalign 0.02
        xsize 400
        background Solid("#000c")
        padding (20, 20)
        
        at transform:
            alpha 0.0
            linear 0.5 alpha 1.0
            pause 3.0
            linear 0.5 alpha 0.0
        
        hbox:
            spacing 15
            
            # 成就图标 - 保持原来的样式
            add achievement["icon"]:
                size (128, 128)
                yalign 0.5
            
            vbox:
                spacing 5
                
                # 成就标题
                text "成就解锁!":
                    color "#ffd700"
                    size 36
                    bold True
                
                text achievement["title"]:
                    color "#fff"
                    size 40
                    bold True
                
                text achievement["description"]:
                    color "#ccc"
                    size 28
                    xsize 280
    
    timer 4.0 action Hide("achievement_popup")

