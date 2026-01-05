# 추상 티켓 클래스
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
import uuid

# 모든 종류의 티켓이 상속하는 클래스
class Ticket(ABC):
    
    def __init__(self):
        self.ticket_id = str(uuid.uuid4())
        self.purchase_date = datetime.now()
        self.is_winning = False
        
    # 티켓이 유효한지 검증하기
    @abstractmethod
    def validate(self) -> bool:
        pass
    
    # 티켓 번호 반환하기
    @abstractmethod
    def get_numbers(self) -> List[int]:
        pass
    
    # 티켓에 대한 정보를 문자열로 변환하기
    def to_string(self) -> str:
        return f"Ticket ID: {self.ticket_id[:8]}..."
