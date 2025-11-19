# init python:
#     # 1. 变量
#     store.dcxmark    = 0
#     store.yujiemark  = 0
#     store.maodiemark = 0
#     store.out_triggered = False

#     # 2. 纯逻辑函数
#     def jiantinga():
#         if store.out_triggered:
#             return
#         cnt = store.dcxmark + store.yujiemark + store.maodiemark
#         if cnt >= 2:
#             store.out_triggered = True
#             renpy.jump("out")          # 注意：用 renpy.jump，不是裸写 jump

#     # 3. 挂到每次交互结束后
#     config.interact_callbacks.append(jiantinga)


# 1. 定义全局变量
default dcxmark = 0
default maodiemark = 0
default yujiemark = 0

init python:
    def check_marks():
        cnt = store.dcxmark + store.maodiemark + store.yujiemark
        if cnt >= 2:
            renpy.call_in_new_context("out")   # 官方 API，立即切换
            return True
        return False
