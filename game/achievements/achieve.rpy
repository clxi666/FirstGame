# achievements_core.rpy
init python:
    import datetime
    import json
    import os
    
    class AchievementSystem:
        def __init__(self):
            self.achievements = {}
            # 确保 persistent 数据正确初始化
            if not hasattr(persistent, 'unlocked_achievements') or persistent.unlocked_achievements is None:
                persistent.unlocked_achievements = set()
            if not hasattr(persistent, 'achievement_stats') or persistent.achievement_stats is None:
                persistent.achievement_stats = {}
            print("✅ 成就系统类初始化完成")
            print(f"🔍 初始解锁成就: {persistent.unlocked_achievements}")
        
        def register_achievement(self, achievement_id, title, description, condition_func, icon=None, hidden=False, points=0):
            # 安全地检查解锁状态
            if persistent.unlocked_achievements is None:
                persistent.unlocked_achievements = set()
                
            is_unlocked = achievement_id in persistent.unlocked_achievements
            
            self.achievements[achievement_id] = {
                "id": achievement_id,
                "title": title,
                "description": description,
                "condition": condition_func,
                "icon": icon or "achievement_default.png",
                "hidden": hidden,
                "unlocked": is_unlocked,
                "unlock_time": None,
                "points": points
            }
            print(f"✅ 注册成就: {title} (解锁状态: {is_unlocked})")
        
        def unlock_achievement(self, achievement_id):
            if achievement_id in self.achievements:
                achievement = self.achievements[achievement_id]
                if not achievement["unlocked"]:
                    achievement["unlocked"] = True
                    achievement["unlock_time"] = datetime.datetime.now()
                    
                    # 确保 persistent 数据不是 None
                    if persistent.unlocked_achievements is None:
                        persistent.unlocked_achievements = set()
                    
                    # 保存到 persistent 数据
                    persistent.unlocked_achievements.add(achievement_id)
                    
                    print(f"🎉 解锁成就: {achievement['title']}")
                    print(f"💾 已保存到持久化数据: {list(persistent.unlocked_achievements)}")
                    
                    # 显示弹窗
                    renpy.show_screen("achievement_popup", achievement)
                    
                    # 播放音效
                    try:
                        renpy.play("audio/achievement.mp3", channel="sound")
                    except:
                        print("⚠️ 成就音效文件不存在")
                    
                    renpy.restart_interaction()
                    return True
                else:
                    print(f"ℹ️ 成就已解锁: {achievement_id}")
                    return True
            else:
                print(f"❌ 成就不存在: {achievement_id}")
                return False
        
        def force_unlock(self, achievement_id):
            return self.unlock_achievement(achievement_id)
        
        def get_unlocked_count(self):
            # 安全地从 persistent 数据获取
            if persistent.unlocked_achievements is None:
                persistent.unlocked_achievements = set()
            return len(persistent.unlocked_achievements)
        
        def get_total_count(self):
            return len(self.achievements)
        
        def get_completion_percentage(self):
            total = self.get_total_count()
            unlocked = self.get_unlocked_count()
            if total == 0:
                return 0
            return (unlocked / total) * 100
        
        def get_total_points(self):
            total = 0
            # 安全地遍历 persistent 数据
            if persistent.unlocked_achievements is None:
                persistent.unlocked_achievements = set()
                
            for achievement_id in persistent.unlocked_achievements:
                achievement = self.achievements.get(achievement_id)
                if achievement:
                    total += achievement.get("points", 0)
            return total
        
        def reset_all_achievements(self):
            """重置所有成就状态"""
            persistent.unlocked_achievements = set()
            for achievement in self.achievements.values():
                achievement["unlocked"] = False
                achievement["unlock_time"] = None
            renpy.restart_interaction()
            print("🔄 所有成就已重置")
        
        def initialize(self):
            """初始化成就系统"""
            # 确保 persistent 数据正确初始化
            if persistent.unlocked_achievements is None:
                persistent.unlocked_achievements = set()
                
            print(f"🎯 成就系统初始化完成: {self.get_total_count()}个成就, {self.get_unlocked_count()}个已解锁")
            print(f"📂 持久化成就数据: {list(persistent.unlocked_achievements)}")

# 创建全局实例
default achievements = AchievementSystem()

# ==================== 成就注册部分 ====================
# 在游戏启动时注册成就
label before_main_menu:
    python:
        print("🚀 在游戏启动时注册成就...")
        
        # 注册所有成就
        achievements.register_achievement("single", "单身之神", "错过所有的姻缘", lambda: False, "asingle.png", points=10)
        achievements.register_achievement("luoli", "你在湖工商只算个萝莉", "告白被成都萝莉截胡", lambda: False, "aluoli.png", points=30)
        achievements.register_achievement("cg_collector", "收藏家", "收集所有CG图片", lambda: False, "achievement_collector.png", points=40)
        achievements.register_achievement("out", "见异思迁", "同时勾搭多个角色", lambda: False, "aout.png", hidden=True, points=50)
        achievements.register_achievement("die", "草率的牺牲", "第二次选择救耄耋，被创死了", lambda: False, "die.png", points=25)
        achievements.register_achievement("god", "赎罪的上帝", "代替别人成为上帝", lambda: False, "god.png", points=25)
        achievements.register_achievement("wuqing", "无情的人", "放弃救耄耋", lambda: False, "wuqing.png", points=25)
        
        print(f"🎉 成就注册完成！总共 {achievements.get_total_count()} 个成就")
    return