# 6/45 로또 게임 클래스

from typing import List, Optional
from .NumberBasedLottery import NumberBasedLottery
from tickets.Lotto645Ticket import Lotto645Ticket
from prize.PrizeStructure import PrizeStructure
from prize.PrizeRank import PrizeRank
from prize.DrawingMachine import DrawingMachine
import logging

# 6/45 로또 게임
class Lotto645(NumberBasedLottery):
    
    def __init__(self):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("6/45 로또 게임 객체 생성")
        super().__init__(
            name="로또 6/45",
            ticket_price=1000,
            min_number=1,
            max_number=45,
            numbers_to_pick=6,
            has_bonus=True
        )
        self._setup_prize_structure()
        self._setup_drawing_machine()
    
    # 상금 구조 초기화
    def _setup_prize_structure(self):
        logging.debug("상금 구조 초기화")
        self.prize_structure = PrizeStructure()
        
        # 실제 로또 6/45 상금 구조 (평균값)
        logging.debug("실제 6/45 로또 상금 구조 설정하기") 
        self.prize_structure.add_rank(PrizeRank(1, 6, False, 2_000_000_000))  # 1등: 6개
        self.prize_structure.add_rank(PrizeRank(2, 5, True, 50_000_000))      # 2등: 5개+보너스
        self.prize_structure.add_rank(PrizeRank(3, 5, False, 1_500_000))      # 3등: 5개
        self.prize_structure.add_rank(PrizeRank(4, 4, False, 50_000))         # 4등: 4개
        self.prize_structure.add_rank(PrizeRank(5, 3, False, 5_000))          # 5등: 3개
    
    # 추첨 기계 초기화
    def _setup_drawing_machine(self):
        logging.debug("추첨 기계 초기화")
        self.drawing_machine = DrawingMachine(
            min_number=1,
            max_number=45,
            numbers_to_draw=6,
            has_bonus=True
        )
        
    # 6/45 로또 티켓 만들기
    def create_ticket(self, numbers: Optional[List[int]] = None) -> Lotto645Ticket:
        logging.debug("6/45 로또 티켓 만들기")
        if numbers is None:
            logging.debug("숫자가 없으므로 난수 생성")
            numbers = self.generate_random_numbers()
        
        ticket = Lotto645Ticket(numbers)
        if not ticket.validate():
            logging.debug("유효하지 않은 번호, ValueError 발생")
            raise ValueError("유효하지 않은 번호입니다.")
        
        return ticket
    
    # 추첨 진행하기
    def conduct_draw(self) -> dict:
        logging.debug("추첨 진행하기")
        main_numbers = self.drawing_machine.draw_numbers()
        bonus_number = self.drawing_machine.draw_bonus()
        
        return {
            'main': main_numbers,
            'bonus': bonus_number
        }
    
    # 당첨 확인
    def check_winning(self, ticket: Lotto645Ticket, drawn_numbers: dict) -> int:
        logging.debug("당첨 확인")
        user_numbers = ticket.get_numbers()
        main_numbers = drawn_numbers['main']
        bonus_number = drawn_numbers['bonus']
        
        # 일치 개수 계산
        logging.debug("일치 개수 계산")
        match_count = self.count_matches(user_numbers, main_numbers)
        
        # 보너스 번호 일치 여부
        logging.debug("보너스 번호 일치 여부 확인")
        has_bonus = bonus_number in user_numbers
        
        # 당첨 등급 확인
        logging.debug("당첨 등수 확인")
        rank = self.prize_structure.find_rank(match_count, has_bonus)
        
        if rank:
            ticket.set_winning_rank(rank)
            return rank
        
        return 0
    
    # 게임 규칙 설명하기
    def get_game_rules(self) -> str:
        logging.debug("게임 규칙 설명하기")
        rules = f"{self.name} 게임 규칙:\n- 1~45 중 6개 번호 선택\n- 티켓 가격: {self.ticket_price:,}원\n- 추첨: 6개 + 보너스 1개\n\n당첨 기준:\n- 1등: 6개 일치\n- 2등: 5개 일치 + 보너스\n- 3등: 5개 일치\n- 4등: 4개 일치\n- 5등: 3개 일치\n"
        return rules
