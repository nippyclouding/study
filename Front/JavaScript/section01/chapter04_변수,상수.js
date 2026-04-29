// 1. 변수
let age;
age = 30; 

/*
var 변수는 제약이 좋은 편이 아니다.
var age = 10;
var age = 20; => 컴파일 오류 x 
*/

// 2. 상수
const birth = "1997.02.21";
// birth = "hello"; 
/* 상수는 값을 변경 불가
Uncaught TypeError: 
Assignment to constant variable.
at chapter04_변수,상수.js:7:7
*/

// 변수 작성 규칙 : $, _를 제외한 기호는 사용 불가, 숫자로 시작 불가
let $_name = "kim";

let salesCount = 1;
let refundCount = 1;
let totalSalesCount = salesCount - refundCount;