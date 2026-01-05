# 숫자 기반 로터리 게임 클래스

import random
from typing import List
from .LotteryGame import LotteryGame
import logging

# 숫자 기반 복권
class NumberBasedLottery(LotteryGame):
    
    def __init__(self, name: str, ticket_price: int, 
                 min_number: int, max_number: int, 
                 numbers_to_pick: int, has_bonus: bool = False):
        
        # 로거 객체 직접 사용
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        
        if not self._logger.handlers:
            file_handler = logging.FileHandler(f"logs\\{__name__}.log", mode='w')
            #file_handler.setLevel(logging.INFO)

            log_formatter = logging.Formatter("%(funcname)s : %(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(log_formatter)
            self._logger.addHandler(file_handler)

        self._logger.info("숫자 기반 로터리 객체 생성") 
        super().__init__(name, ticket_price)
        self.min_number = min_number
        self.max_number = max_number
        self.numbers_to_pick = numbers_to_pick
        self.has_bonus = has_bonus
        
    # 랜덤 번호 생성하기
    def generate_random_numbers(self) -> List[int]:
        self._logger.info("랜덤 번호 생성하기")
        available_numbers = list(range(self.min_number, self.max_number + 1))
        return sorted(random.sample(available_numbers, self.numbers_to_pick))
    
    # 일치하는 번호 개수 계산
    def count_matches(self, user_numbers: List[int], drawn_numbers: List[int]) -> int:
        self._logger.info("일치하는 번호 개수 계산")
        return len(set(user_numbers) & set(drawn_numbers))
