# 파워볼 게임 클래스

import random
from typing import List, Optional
from .NumberBasedLottery import NumberBasedLottery
from tickets.PowerballTicket import PowerballTicket
from prize.PrizeStructure import PrizeStructure
from prize.PrizeRank import PrizeRank
from prize.DrawingMachine import DrawingMachine
import logging
from Logger import Logger

# 파워볼 게임
class PowerballLottery(NumberBasedLottery):
    
    def __init__(self):
        # 로거 객체 직접 사용
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        
        if not self._logger.handlers:
            file_handler = logging.FileHandler(f"logs\\{__name__}.log", mode='w')
            #file_handler.setLevel(logging.INFO)

            log_formatter = logging.Formatter("%(funcname)s : %(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(log_formatter)
            self._logger.addHandler(file_handler)
        
        self._logger.info("파워볼 로터리 게임 객체 생성")
        super().__init__(
            name="파워볼",
            ticket_price=1000,
            min_number=1,
            max_number=28,
            numbers_to_pick=5,
            has_bonus=False
        )
        self.powerball_min = 1
        self.powerball_max = 10
        self._setup_prize_structure()
        self._setup_drawing_machine()
        
    # 상금 구조 초기화
    def _setup_prize_structure(self):
        self._logger.info("상금 구조 초기화")
        self.prize_structure = PrizeStructure()
        
        # 파워볼 상금 구조 (간소화)
        # 실제로는 더 복잡한 구조이지만, 시뮬레이션을 위해 단순화
        self._logger.debug("파워볼 상금 구조 만들기")
        self.prize_structure.add_rank(PrizeRank(1, 5, False, 500_000_000))   # 1등: 5개 + 파워볼
        self.prize_structure.add_rank(PrizeRank(2, 5, False, 10_000_000))    # 2등: 5개
        self.prize_structure.add_rank(PrizeRank(3, 4, False, 500_000))       # 3등: 4개 + 파워볼
        self.prize_structure.add_rank(PrizeRank(4, 4, False, 50_000))        # 4등: 4개
        self.prize_structure.add_rank(PrizeRank(5, 3, False, 5_000))         # 5등: 3개 + 파워볼
        
    # 추첨 기계 초기화
    def _setup_drawing_machine(self):
        self._logger.info("추첨 기계 초기화")
        self.drawing_machine = DrawingMachine(
            min_number=1,
            max_number=28,
            numbers_to_draw=5,
            has_bonus=False
        )
        
    # 파워볼 티켓 생성하기
    def create_ticket(self, numbers: Optional[List[int]] = None) -> PowerballTicket:
        self._logger.info("파워볼 티켓 생성하기")
        if numbers is None:
            main_numbers = self.generate_random_numbers()
            powerball_number = random.randint(self.powerball_min, self.powerball_max)
        else:
            # numbers는 [main1, main2, main3, main4, main5, powerball] 형식
            if len(numbers) != 6:
                self._logger.error("숫자가 덜 입력됨, ValueError 발생")
                raise ValueError("파워볼은 6개의 숫자가 필요합니다 (메인 5개 + 파워볼 1개)")
            main_numbers = numbers[:5]
            powerball_number = numbers[5]
        
        ticket = PowerballTicket(main_numbers, powerball_number)
        if not ticket.validate():
            self._logger.error("유효하지 않은 번호, ValueError 발생")
            raise ValueError("유효하지 않은 번호입니다.")
        
        return ticket
    
    # 추첨 진행하기
    def conduct_draw(self) -> dict:
        self._logger.info("추첨 진행하기")
        main_numbers = self.drawing_machine.draw_numbers()
        powerball_number = random.randint(self.powerball_min, self.powerball_max)
        
        return {
            'main': main_numbers,
            'powerball': powerball_number
        }
    
    # 당첨 확인하기
    def check_winning(self, ticket: PowerballTicket, drawn_numbers: dict) -> int:
        self._logger.info("당첨 확인하기")
        ticket_numbers = ticket.get_all_numbers()
        user_main = ticket_numbers['main']
        user_powerball = ticket_numbers['powerball']
        
        drawn_main = drawn_numbers['main']
        drawn_powerball = drawn_numbers['powerball']
        
        # 메인 번호 일치 개수
        self._logger.debug("기본 번호 일치 개수 확인하기")
        main_matches = self.count_matches(user_main, drawn_main)
        
        # 파워볼 일치 여부
        self._logger.debug("파워볼 번호 일치 여부 확인하기")
        powerball_match = (user_powerball == drawn_powerball)
        
        # 당첨 등수 결정 (간소화된 규칙)
        self._logger.debug("당첨 등수 결정")
        rank = 0
        if main_matches == 5 and powerball_match:
            rank = 1  # 1등
        elif main_matches == 5:
            rank = 2  # 2등
        elif main_matches == 4 and powerball_match:
            rank = 3  # 3등
        elif main_matches == 4:
            rank = 4  # 4등
        elif main_matches == 3 and powerball_match:
            rank = 5  # 5등
        
        if rank > 0:
            ticket.set_winning_rank(rank)
        
        return rank
    
    # 게임 설명하기
    def get_game_rules(self) -> str:
        self._logger.info("게임 설명하기")
        rules = f"{self.name} 게임 규칙:\n- 일반볼: 1~28 중 5개 선택\n- 파워볼: 1~10 중 1개 선택\n- 티켓 가격: {self.ticket_price:,}원\n\n당첨 기준:\n- 1등: 일반 5개 + 파워볼 일치\n- 2등: 일반 5개 일치\n- 3등: 일반 4개 + 파워볼 일치\n- 4등: 일반 4개 일치\n- 5등: 일반 3개 + 파워볼 일치\n"
        return rules
