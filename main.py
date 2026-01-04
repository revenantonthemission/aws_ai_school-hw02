# 로또 게임의 메인 파일

from games.Lotto645 import Lotto645
from games.PowerballLottery import PowerballLottery
from base.GameManager import GameManager
from ui.UIManager import UIManager

# 로또 어플리케이션
class LottoApp:
    
    def __init__(self):
        self.ui_manager = UIManager()
        self.current_game = None
        self.game_manager = None
        
    # 어플리케이션 실행
    def run(self):

        # 환영 화면
        self.ui_manager.show_welcome_screen()
        
        # 게임 선택하기
        while True:
            game_choice = self.ui_manager.show_game_menu()
            
            # 게임 종료하기
            if game_choice == 0:
                self.ui_manager.show_goodbye()
                break
            
            # 게임 초기화하기
            if game_choice == 1:
                self.current_game = Lotto645()
            elif game_choice == 2:
                self.current_game = PowerballLottery()
            else:
                self.ui_manager.show_error("올바르지 않은 선택입니다.")
                continue
            
            # 게임 정보 표시
            self.ui_manager.show_game_info(self.current_game)
            
            # 초기 자금 설정
            budget = self.ui_manager.input_handler.get_initial_budget()
            
            # 게임 매니저 생성 및 실행
            self.game_manager = GameManager(
                game=self.current_game,
                initial_budget=budget,
                ui_manager=self.ui_manager
            )
            
            self.game_manager.run_game_loop()
            
            # 계속 여부 확인
            if not self.ui_manager.confirm("\n다른 게임을 하시겠습니까?"):
                self.ui_manager.show_goodbye()
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
