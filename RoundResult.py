# 라운드 진행 결과 클래스
from typing import List, Tuple, Dict
from tickets.Ticket import Ticket
import logging


# 복권 시뮬레이션을 한 라운드 진행한 결과
class RoundResult:

    def __init__(self, round_number: int, drawn_numbers: dict):
        # 로거 객체 직접 사용
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        
        if not self._logger.handlers:
            file_handler = logging.FileHandler(f"logs\\{__name__}.log", mode='w')
            #file_handler.setLevel(logging.INFO)

            log_formatter = logging.Formatter("%(funcname)s : %(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(log_formatter)
            self._logger.addHandler(file_handler)

        
        self._logger.info("RoundResult 객체 생성")
        self.round_number = round_number
        self.drawn_numbers = drawn_numbers
        self.tickets_purchased = 0
        self.total_spent = 0
        self.winning_tickets: List[Tuple[Ticket, int, int]] = []  # (티켓, 등급, 상금)
        self.total_won = 0
        self.net_profit = 0
        
    # 구매 정보 설정
    def set_purchase_info(self, ticket_count: int, total_cost: int):
        self._logger.info("구매 정보 설정하기")
        self.tickets_purchased = ticket_count
        self.total_spent = total_cost
    
    # 당첨 티켓 추가
    def add_winning_ticket(self, ticket: Ticket, rank: int, prize: int):
        self._logger.info("당첨 티켓 추가")
        self.winning_tickets.append((ticket, rank, prize))
        self.total_won += prize
        
    # 순이익 계산하기
    def calculate_net_profit(self):
        self._logger.info("순이익 계산하기")
        self.net_profit = self.total_won - self.total_spent
        
    # 등수별 당첨 횟수 계산하기
    def get_winning_count_by_rank(self) -> Dict[int, int]:
        self._logger.info("등수별로 당첨 횟수를 계산")
        rank_count = {}
        for _, rank, _ in self.winning_tickets:
            rank_count[rank] = rank_count.get(rank, 0) + 1
        return rank_count
    
    # 인스턴스의 출력 양식
    def __repr__(self):
        self._logger.debug(f"Round {self.round_number}: 구매 {self.tickets_purchased}장, 당첨 {len(self.winning_tickets)}장, 수익 {self.net_profit:+,}원")
        return (f"Round {self.round_number}: 구매 {self.tickets_purchased}장, 당첨 {len(self.winning_tickets)}장, 수익 {self.net_profit:+,}원")
