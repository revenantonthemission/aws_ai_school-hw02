# 게임 제어 클래스

from typing import List, Optional
from games.LotteryGame import LotteryGame
from User import User
from RoundResult import RoundResult

# 게임 진행 컨트롤러 
class GameController:
    
    def __init__(self, game: LotteryGame, user: User):
        self.game = game
        self.user = user
        self.current_round = 0
        self.round_history: List[RoundResult] = []
    
    # 게임 초기화
    def initialize_game(self):
        self.current_round = 0
        self.round_history = []
        self.user.clear_tickets()
        
    # 티켓 구매 처리
    def process_ticket_purchase(self, count: int, strategy: str = 'auto', manual_numbers_list: Optional[List[List[int]]] = None) -> bool:
        total_cost = self.game.get_ticket_price() * count
        
        # 잔액 확인
        if not self.user.deduct_balance(total_cost):
            return False
        
        # 티켓 생성
        tickets = []
        for i in range(count):
            if strategy == 'manual' and manual_numbers_list and i < len(manual_numbers_list):
                # 수동 구매
                ticket = self.game.create_ticket(manual_numbers_list[i])
            else:
                # 자동 구매 (fallback)
                ticket = self.game.create_ticket()
            tickets.append(ticket)
        
        # 사용자에게 티켓 추가
        self.user.add_tickets(tickets)
        
        return True
    
    # 추첨 진행
    def conduct_draw(self) -> dict:
        return self.game.conduct_draw()
    
    # 당첨 확인 및 결산
    def check_and_settle_winnings(self, drawn_numbers: dict) -> RoundResult:
        self.current_round += 1
        round_result = RoundResult(self.current_round, drawn_numbers)
        
        # 구매 정보 설정
        ticket_count = len(self.user.owned_tickets)
        total_cost = self.game.get_ticket_price() * ticket_count
        round_result.set_purchase_info(ticket_count, total_cost)
        
        # 각 티켓 당첨 확인
        for ticket in self.user.owned_tickets:
            rank = self.game.check_winning(ticket, drawn_numbers)
            
            if rank > 0:
                # 상금 계산
                prize = self.game.prize_structure.get_prize(rank)
                
                # 사용자에게 상금 지급
                self.user.add_winnings(prize)
                
                # 라운드 결과에 기록
                round_result.add_winning_ticket(ticket, rank, prize)
        
        # 순이익 계산
        round_result.calculate_net_profit()
        
        # 히스토리에 추가
        self.round_history.append(round_result)
        
        # 다음 라운드를 위해 티켓 초기화
        self.user.clear_tickets()
        
        return round_result

    # 인스턴스의 출력 양식    
    def __repr__(self):
        return f"GameController(game={self.game.name}, round={self.current_round})"
