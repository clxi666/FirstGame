# achievement_gallery.rpy
screen achievement_gallery():
    tag menu
    
    default current_filter = "all"
    
    frame:
        xfill True
        yfill True
        background Solid("#2a2a2a")
        
        vbox:
            xfill True
            yfill True
            spacing 20
            
            text "成就系统" size 36 color "#fff" xalign 0.5
            
            # 调试信息
            text f"总成就数: {achievements.get_total_count()}, 已解锁: {achievements.get_unlocked_count()}" size 14 color "#ff0" xalign 0.5
            
            hbox:
                xalign 0.5
                spacing 50
                
                vbox:
                    text "总进度":
                        size 16
                        color "#ccc"
                    text "[achievements.get_unlocked_count()]/[achievements.get_total_count()]":
                        size 24
                        color "#fff"
                        xalign 0.5
                
                vbox:
                    text "完成度":
                        size 16
                        color "#ccc"
                    text "[int(achievements.get_completion_percentage())]%":
                        size 24
                        color "#fff"
                        xalign 0.5
                
                vbox:
                    text "成就点数":
                        size 16
                        color "#ccc"
                    text "[achievements.get_total_points()]":
                        size 24
                        color "#ffd700"
                        xalign 0.5
            
            hbox:
                xalign 0.5
                spacing 20
                
                if current_filter == "all":
                    textbutton "全部成就":
                        action SetScreenVariable("current_filter", "all")
                        background "#4CAF50"
                else:
                    textbutton "全部成就":
                        action SetScreenVariable("current_filter", "all")
                        background "#666"
                
                if current_filter == "unlocked":
                    textbutton "已解锁":
                        action SetScreenVariable("current_filter", "unlocked")
                        background "#4CAF50"
                else:
                    textbutton "已解锁":
                        action SetScreenVariable("current_filter", "unlocked")
                        background "#666"
                
                if current_filter == "locked":
                    textbutton "未解锁":
                        action SetScreenVariable("current_filter", "locked")
                        background "#4CAF50"
                else:
                    textbutton "未解锁":
                        action SetScreenVariable("current_filter", "locked")
                        background "#666"
            
            frame:
                xalign 0.5
                xsize 1000
                ysize 500
                background Solid("#1a1a1a")
                
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    yfill True
                    
                    vbox:
                        spacing 15
                        xfill True
                        
                        if achievements.get_total_count() == 0:
                            text "没有注册任何成就" size 20 color "#f00" xalign 0.5 yalign 0.5
                        else:
                            $ display_count = 0
                            for achievement_id, achievement in achievements.achievements.items():
                                $ should_show = True
                                
                                if current_filter == "unlocked" and not achievement["unlocked"]:
                                    $ should_show = False
                                elif current_filter == "locked" and achievement["unlocked"]:
                                    $ should_show = False
                                elif achievement.get("hidden", False) and not achievement["unlocked"]:
                                    $ should_show = False
                                
                                if should_show:
                                    $ display_count += 1
                                    use achievement_item(achievement)
                            
                            if display_count == 0:
                                text "没有成就可显示" size 18 color "#f00" xalign 0.5
            
            # 测试按钮
            # hbox:
            #     xalign 0.5
            #     spacing 10
            #     textbutton "测试解锁单身" action Function(achievements.force_unlock, "single")
            #     textbutton "测试解锁萝莉" action Function(achievements.force_unlock, "luoli")
            #     textbutton "测试解锁上帝" action Function(achievements.force_unlock, "god")
            #     textbutton "重置所有成就" action Function(achievements.reset_all_achievements)
            
            # textbutton "返回":
            #     action Return()
            #     xalign 0.5
            textbutton "返回":
                action If(main_menu, true=ShowMenu("main_menu"), false=Return())
                xalign 0.5

screen achievement_item(achievement):
    $ is_unlocked = achievement.get("unlocked", False)
    $ achievement_icon = achievement.get("icon", "achievement_default.png")
    
    frame:
        xsize 900
        background Solid("#333" if is_unlocked else "#222")
        padding (20, 15)
        
        hbox:
            spacing 20
            
            # 图标区域 - 显示成就图片
            frame:
                xsize 80
                ysize 80
                background Solid("#4CAF50" if is_unlocked else "#666")
                
                # 直接显示成就图标图片
                add achievement_icon:
                    size (80, 80)
                    xalign 0.5
                    yalign 0.5
            
            # 信息区域
            vbox:
                spacing 5
                xfill True
                
                # 标题
                if is_unlocked:
                    text achievement["title"]:
                        size 20
                        color "#fff"
                        bold True
                else:
                    text achievement["title"]:
                        size 20
                        color "#888"
                        bold True
                
                # 描述
                if is_unlocked or not achievement.get("hidden", False):
                    if is_unlocked:
                        text achievement["description"]:
                            size 16
                            color "#ccc"
                    else:
                        text achievement["description"]:
                            size 16
                            color "#666"
                else:
                    text "？？？？？？":
                        size 16
                        color "#666"
                
                # 状态和点数
                hbox:
                    spacing 20
                    if is_unlocked:
                        text "✅ 已解锁":
                            color "#4CAF50"
                            size 14
                    else:
                        text "❌ 未解锁":
                            color "#f44336"
                            size 14
                    
                    if achievement.get("points", 0) > 0:
                        text "⭐ [achievement['points']]点数":
                            color "#ffd700"
                            size 14