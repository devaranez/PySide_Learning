## Design

1. 使用Designer製作畫面*.ui
2. VS Code有自己的workspace，而不是依據打開的.py檔案的目錄，因此在程式中使用相對路徑import檔案時pylance解析可能會失敗(但執行沒有問題)，要做的是先open folder或者其它設定workspace，pylance才能成功解析相對路徑
3. 
