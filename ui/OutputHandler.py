# 출력 처리 클래스

import os
import time
import logging, Logger
from typing import List, Dict
from tickets.Ticket import Ticket

# 출력을 처리하는 클래스
class OutputHandler:
    
    # 화면 지우기
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # 메시지 출력
    @staticmethod
    def print_message(message: str, style: str = 'normal'):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("메시지 출력")
        styles = {
            'normal': '',
            'success': '[성공] ',
            'error': '[오류] ',
            'warning': '[경고] ',
            'info': '[정보] '
        }
        
        prefix = styles.get(style, '')
        logging.debug(f"{prefix}{message}")
        print(f"{prefix}{message}")
    
    # 티켓 정보 출력
    @staticmethod
    def print_ticket(ticket: Ticket):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug(f"티켓 정보: {ticket.to_string()}")
        print(f"  {ticket.to_string()}")
    
    # 티켓 목록 출력
    @staticmethod
    def print_tickets(tickets: List[Ticket]):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("티켓 목록 출력")
        logging.debug(f"\n구매한 티켓 ({len(tickets)}장):")
        print(f"\n구매한 티켓 ({len(tickets)}장):")
        for i, ticket in enumerate(tickets, 1):
            logging.debug(f"  {i}. {ticket.to_string()}")
            print(f"  {i}. {ticket.to_string()}")
    
    # 추첨 결과 출력
    @staticmethod
    def print_draw_result(numbers: dict, game_name: str):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("티켓 결과 출력")
        print("\n추첨 결과:")
        
        if 'main' in numbers:
            main_str = ", ".join(map(str, sorted(numbers['main'])))
            print(f"  당첨 번호: [{main_str}]")
            
            if 'bonus' in numbers and numbers['bonus']:
                print(f"  보너스 번호: [{numbers['bonus']}]")
            
            if 'powerball' in numbers:
                print(f"  파워볼 번호: [{numbers['powerball']}]")
    
    # 테이블 형식 출력
    @staticmethod
    def print_table(data: List[List], headers: List[str]):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("테이블 형식 출력")

        # 각 열의 최대 너비 계산
        logging.debug("각 열의 최대 너비 계산")
        col_widths = [len(h) for h in headers]
        
        for row in data:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)))
        
        # 헤더 출력
        logging.debug("헤더 출력")
        header_line = " | ".join([h.ljust(col_widths[i]) for i, h in enumerate(headers)])
        print(header_line)
        print("-" * len(header_line))
        
        # 데이터 출력
        logging.debug("데이터 출력")
        for row in data:
            row_line = " | ".join([str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)])
            print(row_line)
    
    # 애니메이션 표시
    @staticmethod
    def show_animation(animation_type: str):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("애니메이션 표시")
        if animation_type == 'drawing':
            print("\n추첨 중", end="")
            for _ in range(3):
                time.sleep(0.3)
                print(".", end="", flush=True)
            print(" 완료!")
            time.sleep(0.3)
        
        elif animation_type == 'checking':
            print("\n당첨 확인 중", end="")
            for _ in range(3):
                time.sleep(0.2)
                print(".", end="", flush=True)
            print(" 완료!")
            time.sleep(0.2)
    

    # 위아래에 바(=) 출력
    @staticmethod
    def print_header(title: str):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("위아래에 바(=) 출력")
        width = 60
        try:
            print("\n" + "=" * width)
            print(title.center(width))
            print("=" * width + "\n")
        except Exception as e:
            print("\n" + "=" * width)
            print("NO GAME".center(width))
            print("=" * width + "\n")
    
    # 구분선 출력
    @staticmethod
    def print_separator(char: str = "-", length: int = 60):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("구분선 출력")
        print(char * length)
    
    # 당첨 결과 출력
    @staticmethod
    def print_winning_result(rank: int, prize: int):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("당첨 결과 출력")
        if rank > 0:
            print(f"  {rank}등 당첨! 상금: {prize:,}원")
        else:
            print("  아쉽게도 당첨되지 않았습니다.")
    
    # 잔액 출력
    @staticmethod
    def print_balance(balance: int):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("잔액 출력")
        print(f"\n현재 잔액: {balance:,}원")
    
    # 통계 출력
    @staticmethod
    def print_statistics(stats: Dict):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("통계 출력")
        print("\n" + "="*60)
        print("통계 정보")
        print("="*60)
        
        for key, value in stats.items():
            if isinstance(value, (int, float)):
                if isinstance(value, float):
                    print(f"  {key}: {value:.2f}")
                else:
                    print(f"  {key}: {value:,}")
            elif isinstance(value, dict):
                print(f"  {key}:")
                for sub_key, sub_value in value.items():
                    print(f"    {sub_key}: {sub_value}")
            else:
                print(f"  {key}: {value}")
    
    # 진행 바 출력
    @staticmethod
    def print_progress_bar(current: int, total: int, bar_length: int = 40):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("진행 바 출력")
        progress = current / total
        filled = int(bar_length * progress)
        bar = "#" * filled + "-" * (bar_length - filled)
        percentage = progress * 100
        
        print(f"\r진행: [{bar}] {percentage:.1f}% ({current}/{total})", end="", flush=True)
        
        if current == total:
            print()  # 완료 시 줄바꿈
    """
    @staticmethod
    def print_log(filename: str):
        game_logger = Logger("log/game_log.log")
        game_logger.get_log()
        game_logger.print_log()
    """