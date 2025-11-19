# 成就系统 - 全局版，屏幕可直接调用
init -999 python:
    persistent.ach_unlocked = persistent.ach_unlocked or set()
    persistent.ach_progress = persistent.ach_progress or {}

init python:
    class Achievement(object):
        def __init__(self, key, title, desc, hidden=False, stat_max=1,
                     icon_unlocked="ach_unlocked.png", icon_locked="ach_locked.png"):
            self.key = key
            self.title = title
            self.desc = desc
            self.hidden = hidden
            self.stat_max = stat_max
            self.icon_unlocked = icon_unlocked
            self.icon_locked = icon_locked

        @property
        def unlocked(self):
            return self.key in persistent.ach_unlocked

        def progress(self):
            if self.stat_max == 1:
                return (1 if self.unlocked else 0, 1)
            now = persistent.ach_progress.get(self.key, 0)
            return (now, self.stat_max)

        def grant(self):
            if self.unlocked:
                return
            persistent.ach_unlocked.add(self.key)
            renpy.show_screen("ach_popup", ach=self)
            renpy.pause(1.25)
            renpy.hide_screen("ach_popup")

        def add_progress(self, n=1):
            if self.unlocked:
                return
            now = persistent.ach_progress.get(self.key, 0) + n
            persistent.ach_progress[self.key] = now
            if now >= self.stat_max:
                self.grant()

    ACH_REGISTRY = {}

    def register(ach):
        ACH_REGISTRY[ach.key] = ach

    def get(key):
        return ACH_REGISTRY.get(key)

    def unlocked_count():
        return len(persistent.ach_unlocked)

    def total_count():
        return len(ACH_REGISTRY)

    def all_achievements():
        return ACH_REGISTRY.values()


