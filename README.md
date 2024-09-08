# KTV 聊天機器人

這是一個基於 Telegram 的聊天機器人專案，提供多種功能，包括：
依據歌名搜尋完整歌詞
依據歌詞片段搜尋對應的歌曲
YouTube 影片搜尋
將音樂檔案拆分為伴奏和人聲

## 功能介紹
指令列表
/start or /help：顯示指令說明
/lyrics [歌名]：搜尋特定歌曲的完整歌詞
/name [歌詞片段]：根據提供的歌詞片段，搜尋可能的歌曲名稱
/youtube [關鍵字]：在 YouTube 上搜尋對應關鍵字的第一個結果
/mp3 [YouTube 影片名稱]：下載該 YouTube 影片的音檔，並分離出伴奏與人聲

## 安裝與設定
請確認已安裝以下工具：
Python 3.8 以上版本
Poetry 依賴管理工具
poetry install(即可安裝所有套件)
你需要擁有自己的tg bot api 和 gemini api
export AI_API_KEY="Your gemini api key"


