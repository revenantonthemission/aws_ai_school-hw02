# 6/45 로또 클래스
from typing import List
from .LotteryTicket import LotteryTicket
import logging

# 로또 6/45 티켓
class Lotto645Ticket(LotteryTicket):
    
    def __init__(self, numbers: List[int]):
        # 로거 객체 직접 사용
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        
        if not self._logger.handlers:
            file_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
            #file_handler.setLevel(logging.INFO)

            log_formatter = logging.Formatter("%(funcName)s : %(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(log_formatter)
            self._logger.addHandler(file_handler)

        super().__init__(numbers, "로또 6/45")
        
    # 6/45 로또 티켓이 유효한지 검증하기
    def validate(self) -> bool:
        self._logger.info("6/45 로또 티켓이 유효한지 검증하기")
        if len(self.numbers) != 6:
            return False
        if len(set(self.numbers)) != 6:  # 중복 확인
            return False
        if not all(1 <= num <= 45 for num in self.numbers):
            return False
        return True
