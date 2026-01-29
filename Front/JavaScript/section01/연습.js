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