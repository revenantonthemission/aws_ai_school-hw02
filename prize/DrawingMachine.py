# 추첨 기계 클래스

import random
import logging
from typing import List, Optional

# 번호 추첨 기계
class DrawingMachine:
    
    def __init__(self, min_number: int, max_number: int, numbers_to_draw: int,
                 has_bonus: bool = False):
        logging.basicConfig(filename="log/game_log.log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("로또 추첨 기계 객체 생성")
        self.min_number = min_number
        self.max_number = max_number
        self.numbers_to_draw = numbers_to_draw
        self.has_bonus = has_bonus
        self.last_drawn_numbers: List[int] = []
        self.last_bonus_number: Optional[int] = None
    
    # 기본 번호 추첨
    def draw_numbers(self) -> List[int]:
        logging.debug("기본 번호 추첨")
        available_numbers = list(range(self.min_number, self.max_number + 1))
        self.last_drawn_numbers = sorted(random.sample(available_numbers, self.numbers_to_draw))
        return self.last_drawn_numbers.copy()
    
    # 보너스 번호 추첨
    def draw_bonus(self) -> Optional[int]:
        logging.debug("보너스 번호 추첨")
        if not self.has_bonus:
            return None
        
        # 이미 추첨된 번호를 제외한 번호 중에서 선택
        logging.debug("이미 추첨된 번호를 제외한 번호 중에서 선택")
        available_numbers = [n for n in range(self.min_number, self.max_number + 1)
                           if n not in self.last_drawn_numbers]
        self.last_bonus_number = random.choice(available_numbers)
        return self.last_bonus_number
    
    # 추첨 기계 초기화
    def reset(self):
        logging.debug("추첨 기계 초기화")
        self.last_drawn_numbers = []
        self.last_bonus_number = None
    
    # 인스턴스의 출력 양식
    def __repr__(self):
        logging.debug("f"DrawingMachine({self.min_number}-{self.max_number}, draw {self.numbers_to_draw}, bonus: {self.has_bonus})")
        return (f"DrawingMachine({self.min_number}-{self.max_number}, draw {self.numbers_to_draw}, bonus: {self.has_bonus})")
