# UI 관리자 클래스

from ui.InputHandler import InputHandler
from ui.OutputHandler import OutputHandler
from RoundResult import RoundResult
import logging

# UI를 관리하는 클래스
class UIManager:
    
    def __init__(self):
        logging.basicConfig(filename="log/game_log.log", filemode="at", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("UI 관리자 객체 생성")
        self.input_handler = InputHandler()
        self.output_handler = OutputHandler()
    
    # 환영 화면
    def show_welcome_screen(self):
        logging.debug("환영 화면 출력")
        self.output_handler.clear_screen()
        self.output_handler.print_header("로또 시뮬레이션 프로그램")
        
        print("이 프로그램은 로또/복권 시뮬레이션을 실행합니다.\n다양한 게임과 설정으로 시뮬레이션을 진행하고\n통계를 확인할 수 있습니다.")
        
        self.input_handler.wait_for_enter()
    
    # 게임 선택 메뉴
    def show_game_menu(self) -> int:
        logging.debug("게임 선택 메뉴")
        self.output_handler.clear_screen()
        self.output_handler.print_header("게임 선택")
        
        return self.input_handler.get_game_selection()
    
    # 게임 정보 표시하기
    def show_game_info(self, game):
        logging.debug("게임 정보 표시하기")
        self.output_handler.clear_screen()
        self.output_handler.print_header(f"{game.name}")
        print(game.get_game_rules())
        self.input_handler.wait_for_enter()
    
    # 라운드 진행 상황을 표시
    def show_round_progress(self, current_round: int, total_rounds: int):
        logging.debug("라운드 진행 상황 표시")
        self.output_handler.print_progress_bar(current_round, total_rounds)
    
    # 라운드 결과 표시
    def show_round_result(self, result: RoundResult):
        logging.debug("라운드 결과 표시")
        print(f"\n{'='*60}")
        print(f"라운드 {result.round_number} 결과")
        print(f"{'='*60}")
        
        # 추첨 번호
        logging.debug("추첨 번호 출력")
        self.output_handler.print_draw_result(result.drawn_numbers, "")
        
        # 구매 정보
        logging.debug(f"구매정보: 구매: {result.tickets_purchased}장 ({result.total_spent:,}원)")
        print(f"\n구매: {result.tickets_purchased}장 ({result.total_spent:,}원)")
        
        # 당첨 정보
        if result.winning_tickets:
            logging.debug("당첨 정보 출력")
            print(f"\n당첨: {len(result.winning_tickets)}장")
            
            winning_by_rank = result.get_winning_count_by_rank()
            for rank in sorted(winning_by_rank.keys()):
                count = winning_by_rank[rank]
                print(f"  - {rank}등: {count}장")
            
            print(f"\n당첨금: {result.total_won:,}원")
        else:
            print("\n당첨 없음")
        
        # 수익
        logging.debug("수익 계산")
        profit_indicator = "이익" if result.net_profit >= 0 else "손실"
        print(f"\n수익: {result.net_profit:+,}원 ({profit_indicator})")
        print(f"{'='*60}\n")
    
    # 최종 통계 표시
    def show_final_statistics(self, stats: dict, report: str):
        logging.debug("최종 통계 표시")
        self.output_handler.clear_screen()
        self.output_handler.print_header("최종 결과")
        
        print(report)
        
        self.input_handler.wait_for_enter()
    
    # 에러 메시지 표시
    def show_error(self, message: str):
        logging.debug("에러 메시지 표시")
        self.output_handler.print_message(message, 'error')
    
    # 일반적인 메시지 표시
    def show_message(self, message: str, style: str = 'normal'):
        logging.debug("일반적인 메시지 표시")
        self.output_handler.print_message(message, style)
    
    # 정보에 대한 메시지 표시
    def show_info(self, message: str):
        logging.debug("정보에 대한 메시지 표시")
        self.output_handler.print_message(message, 'info')
    
    # 성공 메시지 표시
    def show_success(self, message: str):
        logging.debug("성공 메시지 표시")
        self.output_handler.print_message(message, 'success')
    
    # 경고 메시지 표시
    def show_warning(self, message: str):
        logging.debug("경고 메시지 표시")
        self.output_handler.print_message(message, 'warning')
    
    # 입력 확인 요청하기
    def confirm(self, message: str) -> bool:
        logging.debug("입력 확인 요청하기")
        return self.input_handler.confirm_action(message)
    
    # 종료 메시지
    def show_goodbye(self):
        logging.debug("종료 메시지")
        self.output_handler.clear_screen()
        self.output_handler.print_header("프로그램 종료")
        print("\n감사합니다! 다음에 또 만나요~\n")
