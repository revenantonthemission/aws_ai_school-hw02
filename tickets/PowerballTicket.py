# 파워볼(Powerball) 티켓 클래스

from typing import List
from .LotteryTicket import LotteryTicket
import logging

# 파워볼 티켓
class PowerballTicket(LotteryTicket):
    
    def __init__(self, main_numbers: List[int], powerball_number: int):
        logging.basicConfig(filename="log/game_log.log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("파워볼 티켓 객체 생성")

        # 메인 번호와 파워볼 번호를 하나의 리스트로 결합
        logging.debug("기본 번호와 파워볼 번호를 하나의 리스트로 결합")
        super().__init__(main_numbers, "파워볼")
        self.main_numbers = main_numbers
        self.powerball_number = powerball_number
        
    # 파워볼 티켓이 유효한지 검증하기
    def validate(self) -> bool:
        logging.debug("파워볼 티켓이 유효한지 검증하기")
        if len(self.main_numbers) != 5:
            return False
        if len(set(self.main_numbers)) != 5:  # 중복 확인
            return False
        if not all(1 <= num <= 28 for num in self.main_numbers):
            return False
        if not (1 <= self.powerball_number <= 10):
            return False
        return True
    
    # 메인 번호와 파워볼 번호(보너스 번호)를 딕셔너리로 변환
    def get_all_numbers(self) -> dict:
        logging.debug("기본 번호와 파워볼 번호(보너스 번호)를 딕셔너리로 변환")
        return {
            'main': self.main_numbers,
            'powerball': self.powerball_number
        }
    
    # 티켓 정보를 문자열로 변환
    def to_string(self) -> str:
        logging.debug("티켓 정보를 문자열로 변환")
        main_str = ", ".join(map(str, sorted(self.main_numbers)))
        status = f"[{self.winning_rank}등 당첨!]" if self.is_winning else ""
        return f"{self.game_type} - 일반: [{main_str}] + 파워볼: [{self.powerball_number}] {status}"
