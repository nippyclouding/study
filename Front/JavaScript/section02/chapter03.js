// 구조 분해 할당 : 배열이나 객체에 저장된 여러 값들을 분해하여 각각 다른 변수에 할당
// let [] = 배열;
// let {} = 객체;

let arr = [1, 2, 3];

let one = arr[0];
let two = arr[1];
let three = arr[2];
// 반복이 많다. => 구조 분해 할당을 통해 반복 제거 가능


// 1. 배열의 구조 분해 할당
let [first, second, third, four, five = 5] = arr; 
// arr 배열의 값들이 순서대로 first, second, third에 할당된다.

console.log(first);
console.log(second);
console.log(third);
console.log(four); // undefined
console.log(five); // 구조 분해 할당 사용하며 초기화 => 5


// 2. 객체의 구조 분해 할당
let person = {
    name : "kim",
    age : 27,
    hobby : "listening music"
};

let {name, age, hobby, extra, height = 175} = person;
console.log(name, age, hobby);

console.log(extra); // undefined
console.log(height);// 175 출력

// 객체 내부 age 값을 myAge에 담는다.
let {age : myAge} = person;
console.log(myAge);

// 3. 객체 구조 분해 할당을 이용해 함수의 매개변수를 받는 방법

const func = ({name, age, hobby, extra}) => {
    console.log(name, age, hobby, extra);
}

func(person); // 파라미터로 객체나 배열을 전달해야 구조 분해 할당이 가능하다.