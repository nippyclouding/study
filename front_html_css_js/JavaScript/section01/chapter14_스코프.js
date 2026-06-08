// 스코프 : 전역 스코프, 지역 스코프

let a = 1; // 전역 

function funcA() {
    console.log(a); //전역 스코프 - 정상 출력 
    let b = 2; // 지역 스코프
}

// console.log(b); // 지역 스코프 - 출력 불가 

if (true) {
    let c = 1; // 지역 스코프
}

for (let i = 0; i < 10; i++) {
    function funcB() {
    
    }
}

funcB(); // 특별한 상황 : 전역으로 사용 가능 (함수 선언식)