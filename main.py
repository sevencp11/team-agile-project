# 极简命令式引擎（满足任务3要求）
def main():
    print("=== 敏捷开发控制台引擎 ===")
    while True:
        cmd = input("请输入命令 (help 查看帮助, exit 退出): ").strip().lower()
        if cmd == "exit":
            print("已退出程序。")
            break
        elif cmd == "help":
            print("可用命令：help | exit | list | add")
        elif cmd == "list":
            print("[列表] 当前无任务")
        elif cmd == "add":
            task = input("请输入任务内容：")
            print(f"[添加] 成功添加任务：{task}")
        else:
            print(f"[错误] 未知命令：{cmd}")

if __name__ == "__main__":
    main()