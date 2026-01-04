# 복권 티켓 클래스

from typing import List
from .Ticket import Ticket

# 복권 티켓의 기본 클래스
class LotteryTicket(Ticket):
    
    def __init__(self, numbers: List[int], game_type: str):
        super().__init__()
        self.numbers = numbers
        self.game_type = game_type
        self.winning_rank = 0
        
    # 티켓이 유효한지 검증하기
    def validate(self) -> bool:
        return len(self.numbers) > 0
    
    # 번호 반환하기
    def get_numbers(self) -> List[int]:
        return self.numbers
    
    # 당첨 순위 결정하기
    def set_winning_rank(self, rank: int):
        self.winning_rank = rank
        if rank > 0:
            self.is_winning = True
            
    # 당첨 순위 변환하기
    def get_winning_rank(self) -> int:
        return self.winning_rank
    
    # 티켓 정보를 문자열로 변환하기
    def to_string(self) -> str:
        numbers_str = ", ".join(map(str, sorted(self.numbers)))
        status = f"[{self.winning_rank}등 당첨!]" if self.is_winning else ""
        return f"{self.game_type} - [{numbers_str}] {status}"
