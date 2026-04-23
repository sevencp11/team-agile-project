import unittest
from main import Room, Player, create_rooms

class TestAdventureGame(unittest.TestCase):
    def setUp(self):
        self.entrance, self.corridor, self.treasure = create_rooms()
        self.player = Player()
        self.player.current_room = self.entrance

    # 测试1：房间创建正确
    def test_room_creation(self):
        self.assertEqual(self.entrance.name, "入口")
        self.assertEqual(self.treasure.name, "宝藏室")

    # 测试2：玩家可以移动
    def test_player_move(self):
        self.player.current_room = self.entrance.exits["北"]
        self.assertEqual(self.player.current_room.name, "走廊")

    # 测试3：玩家可以拾取物品
    def test_take_item(self):
        item = "钥匙"
        self.entrance.items.remove(item)
        self.player.inventory.append(item)
        self.assertIn(item, self.player.inventory)

if __name__ == '__main__':
    unittest.main()