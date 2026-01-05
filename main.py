# 로또 게임의 메인 파일

from games.Lotto645 import Lotto645
from games.PowerballLottery import PowerballLottery
from base.GameManager import GameManager
from ui.UIManager import UIManager
from factory.GameFactory import GameFactory
from Logger import Logger
import logging
import asyncio
import os
import traceback

# 로또 어플리케이션
class LottoApp:
    
    def __init__(self):
        # 로거 객체 직접 사용
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        os.makedirs("logs", exist_ok=True)
        
        if not self._logger.handlers:
            file_handler = logging.FileHandler(f"logs/{__name__}.log", mode='w')
            #file_handler.setLevel(logging.INFO)

            log_formatter = logging.Formatter("%(funcName)s : %(asctime)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(log_formatter)
            self._logger.addHandler(file_handler)

        self._logger.info("객체 생성됨")
        self.ui_manager = UIManager()
        self.current_game = None
        self.game_manager = None
        
    # 어플리케이션 실행
    def run(self):

        # 환영 화면
        self._logger.info("환영 화면 출력")
        self.ui_manager.show_welcome_screen()
        
        # 게임 선택하기
        self._logger.info("게임 메뉴 출력")
        while True:
            self._logger.info("게임 메뉴 보여주기")
            game_choice = self.ui_manager.show_game_menu()
            
            # 게임 종료하기
            if game_choice == 0:
                self.exit_application()
                break
            
            # 로그 출력하기
            if game_choice == 3:
                self.show_logs()
                break

            self.current_game = GameFactory.create_game(game_choice)

            if self.current_game is None:
                self.ui_manager.show_error("올바르지 않은 선택입니다.")
                continue
            
            if not self.run_game_session():
                break
                
            if not self.confirm_continue():
                break

    def exit_application(self):
        self._logger.info("굿바이 메시지 출력")
        self.ui_manager.show_goodbye()
        self._logger.info("게임 종료됨")
    
    def show_logs(self):
        self._logger.info("로그 출력 진입")
        game_logger = Logger("logs")
        asyncio.run(game_logger.print_every_log())

    def run_game_session(self) -> bool:
        try:
            # 게임 정보 표시
            self._logger.info("현재 게임 정보 표시")
            self.ui_manager.show_game_info(self.current_game)

            # 초기 자금 설정
            self._logger.info("초기 자금 설정")
            budget = self.ui_manager.input_handler.get_initial_budget()

            # 게임 매니저 생성 및 실행
            self._logger.info("게임 매니저 생성 및 실행")
            self.game_manager = GameManager(
                game=self.current_game,
                initial_budget=budget,
                ui_manager=self.ui_manager
            )

            # 메인 루프 진입
            self._logger.info("게임 진입")
            self.game_manager.run_game_loop()

            return True

        except Exception as e:
            print(f"게임 실행 중 오류 발생: {e}")
            self._logger.error(f"게임 실행 중 오류: {e}")
            return False
        
    def confirm_continue(self) -> bool:
        # 계속 여부 확인
        self._logger.info("다른 게임을 계속할 건지 묻기")
        if not self.ui_manager.confirm("\n다른 게임을 하시겠습니까?"):
            self.exit_application()
            return False
        return True



# 메인 함수
def main():
    try:
        app = LottoApp()
        app.run()
    except KeyboardInterrupt:
        print("\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as e:
        print(f"\n예상치 못한 오류가 발생했습니다: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()
