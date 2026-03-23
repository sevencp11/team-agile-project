
class Room:
    def __init__(self, name, description, items=None, exits=None):
        self.name = name
        self.description = description
        self.items = items or []
        self.exits = exits or {}

class Player:
    def __init__(self):
        self.current_room = None
        self.inventory = []

def create_rooms():
    """创建游戏房间"""
    # 定义房间
    entrance = Room("入口", "你站在城堡入口处，前方是走廊", ["钥匙"])
    corridor = Room("走廊", "一条长长的走廊，两边有门", ["火把"])
    treasure_room = Room("宝藏室", "房间里闪闪发光，有很多宝物", ["金币"])
    
    # 设置房间连接
    entrance.exits = {"北": corridor}
    corridor.exits = {"南": entrance, "东": treasure_room}
    treasure_room.exits = {"西": corridor}
    
    return entrance, corridor, treasure_room

def main():
    print("=== 文字冒险游戏 ===")
    
    # 初始化游戏
    entrance, corridor, treasure_room = create_rooms()
    player = Player()
    player.current_room = entrance
    
    print(f"欢迎来到 {player.current_room.name}！输入 'help' 查看命令")
    
    while True:
        cmd = input("\n请输入命令: ").strip().lower().split()
        
        if not cmd:
            continue
            
        action = cmd[0]
        
        # 退出游戏
        if action == "exit":
            print("已退出游戏。")
            break
            
        # 查看帮助
        elif action == "help":
            print("可用命令：")
            print("  look - 查看当前房间")
            print("  move [方向] - 移动 (方向：北/南/东/西)")
            print("  take [物品] - 拿走物品")
            print("  inventory - 查看背包")
            print("  exit - 退出游戏")
            
        # 查看房间
        elif action == "look":
            room = player.current_room
            print(f"\n【{room.name}】")
            print(room.description)
            if room.items:
                print(f"可见物品：{', '.join(room.items)}")
            else:
                print("这里没有什么可拿的。")
            print(f"出口：{', '.join(room.exits.keys())}")
            
        # 移动
        elif action == "move" or action == "go":
            if len(cmd) < 2:
                print("请指定方向，如：move 北")
                continue
            direction = cmd[1]
            room = player.current_room
            if direction in room.exits:
                player.current_room = room.exits[direction]
                print(f"你向{direction}移动，来到了 {player.current_room.name}")
            else:
                print("那个方向没有出口。")
                
        # 拿走物品
        elif action == "take":
            if len(cmd) < 2:
                print("请指定物品，如：take 钥匙")
                continue
            item = cmd[1]
            room = player.current_room
            if item in room.items:
                room.items.remove(item)
                player.inventory.append(item)
                print(f"你拿起了 {item}")
            else:
                print("这里没有这个物品。")
                
        # 查看背包
        elif action == "inventory" or action == "bag":
            if player.inventory:
                print(f"背包物品：{', '.join(player.inventory)}")
            else:
                print("背包是空的。")
                
        else:
            print(f"未知命令：{action}，输入 'help' 查看帮助")

if __name__ == "__main__":
    main()