# 유저 클래스

from typing import List
from tickets.Ticket import Ticket
import logging


# 유저 정보 및 상태 관리
class User:
    
    def __init__(self, name: str, initial_balance: int):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("유저 객체 생성")
        self.name = name
        self.balance = initial_balance
        self.initial_balance = initial_balance
        self.owned_tickets: List[Ticket] = []
        self.total_winnings = 0
        self.total_spent = 0
        
    # 티켓 구매하기
    def add_tickets(self, tickets: List[Ticket]):
        logging.debug("티켓 생성")
        self.owned_tickets.extend(tickets)
        
    # 복권을 구매할 때 잔액 차감하기
    def deduct_balance(self, amount: int) -> bool:
        logging.debug("복권 구매")
        if self.balance >= amount:
            self.balance -= amount
            self.total_spent += amount
            return True
        return False
    
    # 당첨되면 당첨금 추가하기
    def add_winnings(self, amount: int):
        logging.debug("당첨금 추가")
        self.balance += amount
        self.total_winnings += amount
        
    # 현재 잔액을 반환함
    def get_balance(self) -> int:
        logging.debug("현재 잔액 반환")
        return self.balance
    
    # 보유한 티켓 초기화
    def clear_tickets(self):
        logging.debug("티켓 초기화")
        self.owned_tickets = []
        
    # 순이익 계산하기
    def get_net_profit(self) -> int:
        logging.debug("순이익 계산")
        return self.total_winnings - self.total_spent
    
    # 인스턴스의 출력 양식
    def __repr__(self):
        logging.debug(f"User(name={self.name}, balance={self.balance:,}원, tickets={len(self.owned_tickets)})")
        return (f"User(name={self.name}, balance={self.balance:,}원, tickets={len(self.owned_tickets)})")
