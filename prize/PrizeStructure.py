# 상금 구조 클래스

from typing import List, Optional
from .PrizeRank import PrizeRank
import logging

# 상금 구조 관리
class PrizeStructure:
    
    def __init__(self):
        logging.basicConfig(filename="log/game_log.log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("상금 구조 객체 생성")
        self.prize_ranks: List[PrizeRank] = []
        self.total_pool = 0
        
    # 상금 등급 추가하기
    def add_rank(self, rank: PrizeRank):
        logging.debug("상금 순위 추가하기")
        self.prize_ranks.append(rank)
        # 등급순으로 정렬
        logging.debug("순위대로 정렬")
        self.prize_ranks.sort(key=lambda x: x.rank)
        
    # 특정 등급의 상금 얻기
    def get_prize(self, rank: int) -> int:
        logging.debug("특정 순위의 상금 확인")
        for prize_rank in self.prize_ranks:
            if prize_rank.rank == rank:
                return prize_rank.prize_amount
        return 0
    
    # 당첨자 수를 고려한 상금 계산 (추후 변동 상금 구현 시 사용)
    def calculate_prize(self, rank: int, winners_count: int = 1) -> int:
        logging.debug("당첨자 수를 고려한 상금 계산")
        base_prize = self.get_prize(rank)
        return base_prize
    
    # 상금 풀 업데이트
    def update_pool(self, amount: int):
        logging.debug("상금 풀 업데이트")
        self.total_pool += amount
        
    # 일치 개수와 보너스 당첨 여부로 등수 찾기
    def find_rank(self, match_count: int, has_bonus: bool = False) -> Optional[int]:
        logging.debug("일치 개수와 보너스 당첨 여부로 등수 찾기")
        for prize_rank in self.prize_ranks:
            if prize_rank.check_criteria(match_count, has_bonus):
                return prize_rank.rank
        return None
    
    # 인스턴스의 출력 양식
    def __repr__(self):
        ranks_str = "\n".join([str(rank) for rank in self.prize_ranks])
        logging.debug(f"상금 구조:\n{ranks_str}")
        return f"상금 구조:\n{ranks_str}"
