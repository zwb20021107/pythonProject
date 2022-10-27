class Game:
    top_socore = 0;

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help(self):
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(self):
        print("当前最高分为: %d" %Game.top_socore)


    def start_game(self):
        print("%s开始玩游戏" %self.player_name)


js = Game("小明")

Game.show_top_score()
js.start_game()
