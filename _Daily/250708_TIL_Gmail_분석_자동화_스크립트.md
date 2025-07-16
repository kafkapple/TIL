# 250708_TIL_Gmail_분석_자동화_스크립트 (Tuesday)

## What I Learned
- Google Apps Script를 이용하여 Gmail 받은편지함의 발신자 통계를 자동으로 분석하고, 그 결과를 Google Sheets에 정리하는 프로세스를 구축하는 방법을 학습했습니다.

### 과정 요약
1.  **Google Sheets 생성 및 스크립트 편집기 열기**
2.  **스크립트 코드 작성 및 붙여넣기**
3.  **스크립트 저장, 실행 및 권한 승인**

### 스크립트 코드
```javascript
/**
 * @OnlyCurrentDoc
 *
 * Gmail 받은편지함을 분석하여 발신자별 이메일 수를 집계하고,
 * 현재 활성화된 Google Sheet에 결과를 내림차순으로 정리합니다.
 */
function analyzeGmailSenders() {
  // 1. 시트 준비
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  const sheetName = "발신자 분석 리포트";
  let sheet = spreadsheet.getSheetByName(sheetName);
  if (sheet) {
    sheet.clear(); // 기존 데이터가 있으면 삭제
  } else {
    sheet = spreadsheet.insertSheet(sheetName);
  }

// 헤더(제목) 추가
  sheet.appendRow(["순위", "발신자 이름", "이메일 주소", "수신 횟수"]);
  sheet.setFrozenRows(1); // 제목 행 고정

// 2. Gmail 데이터 가져오기 (최근 500개 스레드 대상)
  const threads = GmailApp.getInboxThreads(0, 500);
  const senderData = {}; // 발신자 정보를 저장할 객체

// 3. 발신자 정보 추출 및 집계
  for (const thread of threads) {
    const messages = thread.getMessages();
    for (const message of messages) {
      const from = message.getFrom();
      let email = from.match(/<(.+)>/);
      if (!email) {
        email = from;
      } else {
        email = email[1];
      }
      const name = from.replace(/<.+>/, "").trim().replace(/"/g, '');

if (senderData[email]) {
        senderData[email].count++;
      } else {
        senderData[email] = { name: name, count: 1 };
      }
    }
  }

// 4. 집계 결과를 배열로 변환 및 정렬
  const sortedSenders = Object.keys(senderData).map(email => {
    return [senderData[email].name, email, senderData[email].count];
  });

sortedSenders.sort((a, b) => b[2] - a[2]);

// 5. 시트에 데이터 작성
  if (sortedSenders.length > 0) {
    const dataToWrite = sortedSenders.map((sender, index) => {
      return [index + 1, sender[0], sender[1], sender[2]];
    });
    sheet.getRange(2, 1, dataToWrite.length, 4).setValues(dataToWrite);
  }

SpreadsheetApp.getUi().alert("Gmail 발신자 분석이 완료되었습니다!");
}

/**
 * 메뉴에 'Gmail 분석' 기능을 추가하는 함수
 */
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('🚀 Gmail 분석 도구')
    .addItem('발신자 분석 실행', 'analyzeGmailSenders')
    .addToUi();
}
```

### 결과 및 활용
- **결과:** Google Sheets에 '발신자 분석 리포트' 시트가 생성되고, 발신자 통계가 자동으로 정리됩니다.
- **활용:** 시트 상단 메뉴 또는 Apps Script 트리거를 통해 주기적으로 분석을 자동화할 수 있습니다.

- **Created Date**: 2025-07-08
- **Category**: TIL
- **ID**: N_gmail_script_250708