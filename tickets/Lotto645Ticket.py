# 6/45 로또 클래스
from typing import List
from .LotteryTicket import LotteryTicket
import logging

# 로또 6/45 티켓
class Lotto645Ticket(LotteryTicket):
    
    def __init__(self, numbers: List[int]):
        logging.basicConfig(filename="log/game_log.log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("6/45 로또 티켓 객체 생성")
        super().__init__(numbers, "로또 6/45")
        
    # 6/45 로또 티켓이 유효한지 검증하기
    def validate(self) -> bool:
        logging.debug("6/45 로또 티켓이 유효한지 검증하기")
        if len(self.numbers) != 6:
            return False
        if len(set(self.numbers)) != 6:  # 중복 확인
            return False
        if not all(1 <= num <= 45 for num in self.numbers):
            return False
        return True
