# 로또 게임의 메인 파일

from games.Lotto645 import Lotto645
from games.PowerballLottery import PowerballLottery
from base.GameManager import GameManager
from ui.UIManager import UIManager
import logging
from Logger import Logger

# 로또 어플리케이션
class LottoApp:
    
    def __init__(self):
        logging.basicConfig(filename="log/game_log.log", filemode="wt", format="%(asctime)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("UI 매니저 객체 생성됨")
        self.ui_manager = UIManager()
        logging.debug("현재 게임 없음")
        self.current_game = None
        logging.debug("현재 게임 매니저 없음")
        self.game_manager = None
        
    # 어플리케이션 실행
    def run(self):

        # 환영 화면
        logging.debug("환영 화면 출력")
        self.ui_manager.show_welcome_screen()
        
        # 게임 선택하기
        logging.debug("게임 메뉴 출력")
        while True:
            logging.debug("게임 메뉴 보여주기")
            game_choice = self.ui_manager.show_game_menu()
            
            # 게임 종료하기
            if game_choice == 0:
                logging.debug("굿바이 메시지 출력")
                self.ui_manager.show_goodbye()
                logging.debug("게임 종료됨")
                break
            
            # 게임 초기화하기
            if game_choice == 1:
                logging.debug("6/45 로또 게임 진입")
                self.current_game = Lotto645()
            elif game_choice == 2:
                logging.debug("파워볼 로터리 진입")
                self.current_game = PowerballLottery()
            elif game_choice == 3:
                logging.debug("로그 출력 진입")
                game_logger = Logger("log/game_log.log")
                game_logger.get_log()
                game_logger.print_log()
                break
            else:
                self.ui_manager.show_error("올바르지 않은 선택입니다.")
                continue
            
            # 게임 정보 표시
            logging.debug("현재 게임 정보 표시")
            try:
                self.ui_manager.show_game_info(self.current_game)
            except Exception as e:
                print(f"There is no game: {e}")
                break
            
            # 초기 자금 설정
            logging.debug("초기 자금 설정")
            budget = self.ui_manager.input_handler.get_initial_budget()
            
            # 게임 매니저 생성 및 실행
            logging.debug("게임 매니저 생성 및 실행")
            self.game_manager = GameManager(
                game=self.current_game,
                initial_budget=budget,
                ui_manager=self.ui_manager
            )
            
            logging.debug("게임 진입")
            self.game_manager.run_game_loop()
            
            # 계속 여부 확인
            logging.debug("다른 게임을 계속할 건지 묻기")
            if not self.ui_manager.confirm("\n다른 게임을 하시겠습니까?"):
                logging.debug("굿바이 메시지 출력")
                self.ui_manager.show_goodbye()
                logging.debug("게임 종료됨")
                break


# 메인 함수
def main():
    try:
        app = LottoApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n프로그램이 사용자에 의해 중단되었습니다.")
    except Exception as e:
        print(f"\n예상치 못한 오류가 발생했습니다: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
