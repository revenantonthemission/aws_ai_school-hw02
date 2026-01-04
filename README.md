# AWS AI School 2주차 과제

## 프로젝트 구성

- base: 게임 관리를 위한 모듈
    - GameController.py: 게임 컨트롤러 클래스
    - GameManager.py: 게임 관리자 클래스
    - StatisticsAnalyzer.py: 게임 결과 분석 클래스
- games: 게임 클래스 모듈
    - LotteryGame.py: 로터리 게임 클래스
    - Lotto645.py: 6/45 로또 게임 클래스
    - NumberBasedLottery.py: 숫자 기반 로터리 게임 클래스
    - PowerballLottery.py: 파워볼 로터리 게임 클래스
- prize: 상금 관련 모듈
    - DrawingMachine.py: 추첨 기계 클래스
    - PrizeRank.py: 당첨 등수 클래스
    - PrizeStructure.py: 상금 구조 클래스
- tickets: 티켓 관련 모듈
    - LotteryTicket.py: 복권 티켓의 기본 클래스
    - Lotto645Ticket.py: 6/45 복권 티켓 클래스
    - PowerballTicket.py: 파워볼 로터리 티켓 클래스
- ui: 사용자 인터페이스 관련 모듈
    - InputHandler.py: 사용자 입력을 관리하는 클래스
    - OutputHandler.py: 출력을 관리하는 클래스
    - UIManager.py: UI 관리자 클래스
- main.py: 게임 실행을 위한 진입점
- RoundResult.py: 각 라운드별 결과에 대한 클래스
- User.py: 유저에 대한 클래스