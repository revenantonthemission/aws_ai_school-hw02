# 추첨 기계 클래스

import random
import logging
from typing import List, Optional

# 번호 추첨 기계
class DrawingMachine:
    
    def __init__(self, min_number: int, max_number: int, numbers_to_draw: int, has_bonus: bool = False):
        # 로거 객체 직접 사용
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        
        if not self._logger.handlers:
            file_handler = logging.FileHandler(f"logs\\{__name__}.log", mode='w')
            #file_handler.setLevel(logging.INFO)

            log_formatter = logging.Formatter("%(funcname)s : %(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(log_formatter)
            self._logger.addHandler(file_handler)

        self._logger.info("로또 추첨 기계 객체 생성")
        self.min_number = min_number
        self.max_number = max_number
        self.numbers_to_draw = numbers_to_draw
        self.has_bonus = has_bonus
        self.last_drawn_numbers: List[int] = []
        self.last_bonus_number: Optional[int] = None
    
    # 기본 번호 추첨
    def draw_numbers(self) -> List[int]:
        self._logger.info("기본 번호 추첨")
        available_numbers = list(range(self.min_number, self.max_number + 1))
        self.last_drawn_numbers = sorted(random.sample(available_numbers, self.numbers_to_draw))
        return self.last_drawn_numbers.copy()
    
    # 보너스 번호 추첨
    def draw_bonus(self) -> Optional[int]:
        self._logger.info("보너스 번호 추첨")
        if not self.has_bonus:
            return None
        
        # 이미 추첨된 번호를 제외한 번호 중에서 선택
        self._logger.debug("이미 추첨된 번호를 제외한 번호 중에서 선택")
        available_numbers = [n for n in range(self.min_number, self.max_number + 1)
                           if n not in self.last_drawn_numbers]
        self.last_bonus_number = random.choice(available_numbers)
        return self.last_bonus_number
    
    # 추첨 기계 초기화
    def reset(self):
        self._logger.info("추첨 기계 초기화")
        self.last_drawn_numbers = []
        self.last_bonus_number = None
    
    # 인스턴스의 출력 양식
    def __repr__(self):
        self._logger.debug(f"DrawingMachine({self.min_number}-{self.max_number}, draw {self.numbers_to_draw}, bonus: {self.has_bonus})")
        return (f"DrawingMachine({self.min_number}-{self.max_number}, draw {self.numbers_to_draw}, bonus: {self.has_bonus})")
