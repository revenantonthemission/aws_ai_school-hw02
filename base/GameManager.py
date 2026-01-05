# 게임 관리자 클래스

from base.GameController import GameController
from base.StatisticsAnalyzer import StatisticsAnalyzer
from games.LotteryGame import LotteryGame
from User import User
import logging

# 게임 진행을 관리하는 클래스
class GameManager:
    
    def __init__(self, game: LotteryGame, initial_budget: int, ui_manager):
        # 로거 객체 직접 사용
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        
        if not self._logger.handlers:
            file_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
            #file_handler.setLevel(logging.INFO)

            log_formatter = logging.Formatter("%(funcName)s : %(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(log_formatter)
            self._logger.addHandler(file_handler)
        
        self._logger.info("게임 매니저 객체 생성")
        self.game = game
        self.ui_manager = ui_manager
        
        # 사용자 및 컨트롤러 설정
        self._logger.debug("사용자 및 컨트롤러 설정")
        self.user = User("Player", initial_budget)
        self.game_controller = GameController(game, self.user)
        self.statistics_analyzer = StatisticsAnalyzer()
    
    # 게임의 주요 루프
    def run_game_loop(self):
        self._logger.info("주요 루프 진입")
        self.game_controller.initialize_game()
        self.statistics_analyzer.reset()
        
        self.ui_manager.show_message(f"\n{'='*60}")
        self.ui_manager.show_message(f"{self.game.name} 게임 시작!")
        self.ui_manager.show_message(f"시작 자금: {self.user.get_balance():,}원")
        self.ui_manager.show_message(f"{'='*60}\n")
        
        while True:
            # 메뉴 표시 및 선택
            self._logger.info("메뉴 표시 및 선택")
            action = self.ui_manager.input_handler.get_main_menu_action()
            
            if action == 0:  # 종료
                self._logger.debug("메뉴 종료")
                break
                
            elif action == 1:  # 티켓 구매
                self._logger.debug("티켓 구매")
                self._handle_purchase_round()
                
            elif action == 2:  # 통계 확인
                self._logger.debug("통계 확인")
                self._show_current_stats()
        
        # 최종 통계 표시
        self._logger.debug("최종 통계 표시")
        self._show_final_report()
    
    # 구매부터 추첨까지 한 라운드 진행하기
    def _handle_purchase_round(self):
        self._logger.info("한 라운드 진행하기")

        # 구매 방식 선택 (자동/수동)
        self._logger.debug("구매 방식 선택")
        purchase_type = self.ui_manager.input_handler.get_purchase_type()
        
        # 티켓 수 입력
        self._logger.debug("티켓 수 입력")
        count = self.ui_manager.input_handler.get_ticket_count()
        
        # 수동 번호 입력 (필요 시)
        manual_numbers = []
        if purchase_type == 'manual':
            self._logger.debug("수동으로 번호 입력")
            self.ui_manager.show_message(f"\n{count}장의 티켓 번호를 입력해주세요.")
            
            for i in range(count):
                logging.debug(f"\n티켓 #{i+1} 작성")
                self.ui_manager.show_message(f"\n티켓 #{i+1} 작성")
                
                # Powerball 처리
                if self.game.name == "파워볼":
                    self._logger.debug("파워볼 게임 처리")
                    main = self.ui_manager.input_handler.get_numbers(
                        count=5, 
                        min_num=1, 
                        max_num=28, 
                        manual=True,
                        prompt_msg="일반볼 5개 번호를 입력하세요 (1-28)"
                    )
                    power = self.ui_manager.input_handler.get_numbers(
                        count=1,
                        min_num=1,
                        max_num=10,
                        manual=True,
                        prompt_msg="파워볼 1개 번호를 입력하세요 (1-10)"
                    )
                    if main and power:
                        manual_numbers.append(main + power)
                else:
                    # 일반 로또
                    self._logger.debug("6/45 로또 게임 처리")
                    numbers = self.ui_manager.input_handler.get_numbers(
                        count=self.game.numbers_to_pick,
                        min_num=getattr(self.game, 'min_number', 1),
                        max_num=getattr(self.game, 'max_number', 45),
                        manual=True
                    )
                    if numbers:
                        manual_numbers.append(numbers)
        
        # 티켓 구매 처리
        self._logger.debug("티켓 구매 처리")
        success = self.game_controller.process_ticket_purchase(
            count=count,
            strategy=purchase_type,
            manual_numbers_list=manual_numbers if manual_numbers else None
        )
        
        if not success:
            self._logger.debug("잔액 부족")
            self.ui_manager.show_error("잔액이 부족합니다!")
            return
            
        # 추첨 및 결과 표시
        self._logger.debug("추첨 중...")
        self.ui_manager.output_handler.show_animation('drawing')
        drawn_numbers = self.game_controller.conduct_draw()
        
        self._logger.debug("확인 중...")
        self.ui_manager.output_handler.show_animation('checking')
        round_result = self.game_controller.check_and_settle_winnings(drawn_numbers)
        
        # 통계 기록
        self._logger.debug("통계 기록")
        self.statistics_analyzer.record_round(round_result)
        
        # 결과 표시
        self._logger.debug("결과 표시")
        self.ui_manager.show_round_result(round_result)
        self.ui_manager.input_handler.wait_for_enter()
        
    # 현재 상태 및 통계 표시
    def _show_current_stats(self):
        self._logger.debug("현재 상태 및 통계 표시")
        self.ui_manager.output_handler.clear_screen()
        stats = self.statistics_analyzer.get_winning_statistics()
        
        print("\n" + "="*40)
        print("현재 상태")
        print("="*40)
        print(f"잔액: {self.user.get_balance():,}원")
        print(f"순손익: {self.user.get_net_profit():+,}원")
        print(f"총 구매: {stats['total_tickets']}장")
        print(f"총 당첨: {stats['total_winning_tickets']}장")
        print("="*40)
        
        self.ui_manager.input_handler.wait_for_enter()
    
    # 게임 종료 시 통계 출력하기
    def _show_final_report(self):
        self._logger.info("게임 종료 시 통계 출력하기")
        report = self.statistics_analyzer.generate_summary_report()
        user_info = f"게임 종료 결과:\n- 최종 잔액: {self.user.get_balance():,}원\n- 순손익: {self.user.get_net_profit():+,}원\n"
        self.ui_manager.show_final_statistics({}, user_info + report)
