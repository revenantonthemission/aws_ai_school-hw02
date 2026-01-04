# 6/45 로또 클래스
from typing import List
from .LotteryTicket import LotteryTicket


# 로또 6/45 티켓
class Lotto645Ticket(LotteryTicket):
    
    def __init__(self, numbers: List[int]):
        super().__init__(numbers, "로또 6/45")
        
    # 6/45 로또 티켓이 유효한지 검증하기
    def validate(self) -> bool:
        if len(self.numbers) != 6:
            return False
        if len(set(self.numbers)) != 6:  # 중복 확인
            return False
        if not all(1 <= num <= 45 for num in self.numbers):
            return False
        return True
