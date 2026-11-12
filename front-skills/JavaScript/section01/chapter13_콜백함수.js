// 콜백 함수 : 자신이 아닌 다른 함수에 파라미터로 전달된 함수

function main1(value) {

}

function sub1() {
    console.log("sub");
}


main1(sub1); // 콜백 함수 
// main 함수 파라미터로 value 전달 => value() 호출

// main이라는 다른 함수에 파라미터로 전달된 다른 함수를 콜백 함수라고 한다.

function main2(value2) {
    console.log(value2);
}
main2(1);

function sub2() {
    console.log("This is sub2");
}

main2(sub2); // sub 함수 코드 자체가 출력된다.

// sub2는 main2의 파라미터로 전달되어 main2가 실행될 때 sub2도 실행되기 때문에
// 이후에 실행된다는 의미로 'call back' 함수 라고 한다.  


// 함수 표현식, 익명 함수와 함께 사용하는 콜백 함수
// 콜백 함수 선언
function main(callback) {
    callback();
}

main(function () {
    console.log("This is sub3"); // function sub3 이름 생략
})
 
main(// 콜백
    () => { // 화살표
        console.log("This is sub4"); // 화살표 함수를 응용한 콜백 함수
    }
)

main( ()=> {} ) // 형태

// 콜백 함수의 활용
function repeat(count) {
    for (let idx = 1; idx <= count; idx++) {
        console.log(idx);
    }
}

repeat(5);

function repeatDouble(count) {
    for (let idx = 1; idx <= count; idx++) {
        console.log(idx * 2);
    }
}

repeatDouble(5);

// repeat, repeatDouble은 중복적인 코드가 많다 => 콜백 함수 사용으로 개선

function repeatCallBack (count, callback) { // callback 매개변수 추가 
    for (let idx = 1; idx <= count; idx++) {
        callback(idx); // 반복문 안에 callback 메서드 추가
    }
}


// 매개변수를 받아 그대로 출력하는 콜백 함수를 두 번째 파라미터로 전달
repeatCallBack(5, function (idx) {
    console.log(idx); // 1 2 3 4 5 출력 
})

repeatCallBack(5, function (idx) {
    console.log(idx * 2); //  2 4 6 8 10 출력, 중복 개선 
})