from games.Lotto645 import Lotto645
from games.PowerballLottery import PowerballLottery
from games.LotteryGame import LotteryGame
from typing import Optional

# 게임 객체 생성을 담당하는 팩토리 클래스
class GameFactory:
    __game_map = {
        1: Lotto645,
        2: PowerballLottery
    }

    @classmethod
    def create_game(cls, game_choice: int) -> Optional[LotteryGame]:
        # 게임 선택 번호에 따라 게임 객체를 생성
        game_class = cls.__game_map.get(game_choice)

        if game_class is None:
            return None
        
        return game_class()
    
    @classmethod
    def register_game(cls, game_choice: int, game_class):
        cls.__game_map[game_choice] = game_class

    @classmethod
    def get_available_games(cls) -> dict:
        return cls.__game_map.copy()