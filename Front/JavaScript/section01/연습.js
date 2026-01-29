// 함수 표현식 = 변수에 함수를 담을 수 있다. 

let testVar1 = function func1() {
    console.log("hello");
}
testVar1();
console.log(testVar1);

let testVar2 = function () {
    console.log("hello2");
}
testVar2();
console.log(testVar2);

let testVar3 = () => {
    console.log("hello3");
}
testVar3();
console.log(testVar3);

let testVar4 = () => console.log("hello4");
testVar4();
console.log(testVar4);

let testVar5 = (min, sec) => 60 * min + sec;
testVar5(4, 2); // 함수 리턴값이 출력되지 않는다. 
console.log(testVar5(4, 2)); // 출력
console.log(testVar5);

let testVar6 = testVar5(3, 2);
console.log(testVar6);


// 콜백 : 함수를 호출할 때 파라미터로 다른 함수를 호출하는 경우
function funcA () {
    console.log("this is CallBack a");
}
function funcB(varation1) {
    return varation1;
}
funcB(funcA());


function repeatCallBack (cnt, funcTest) {
    for (i = 0; i < cnt; i++) {
        funcTest(i + 1);
    }
}


repeatCallBack(7, function aaa(i) {
    console.log(i);
});

repeatCallBack(8, function (i) {
    if (i % 2 == 0) return;
    else console.log(i);
})

repeatCallBack(9, (i) => {
    if (i % 2 == 0) return;
    else console.log(i);
})

repeatCallBack(10, (i) => {
    console.log(i);
})