# 당첨 순위 클래스

import logging

# 당첨 순위에 대한 정보를 관리하는 클래스
class PrizeRank:
 
    def __init__(self, rank: int, match_count: int, bonus_required: bool = False, 
                 prize_amount: int = 0):
        logging.basicConfig(filename="log/game_log.log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("당첨 순위 객체 생성")
        self.rank = rank
        self.match_count = match_count
        self.bonus_required = bonus_required
        self.prize_amount = prize_amount
        
    # 당첨 조건 확인하기
    def check_criteria(self, match_count: int, has_bonus: bool = False) -> bool:
        logging.debug("당첨 조건 확인")
        if self.match_count != match_count:
            return False
        if self.bonus_required and not has_bonus:
            return False
        return True
    
    # 인스턴스의 출력 양식
    def __repr__(self):
        bonus_str = " + 보너스" if self.bonus_required else ""
        logging.debug(f"Rank {self.rank}: {self.match_count}개 일치{bonus_str} - {self.prize_amount:,}원")
        return f"Rank {self.rank}: {self.match_count}개 일치{bonus_str} - {self.prize_amount:,}원"
