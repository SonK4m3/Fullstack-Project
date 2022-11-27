async function loadJson(url){
    return fetch(url)
        .then(response=>{
            if(response.status == 200)
                return response.json();
            else{
                throw new Error(response.status);
            }
        });
}
let url = 'https://javascript.info/user.json';
loadJson(url).catch(console.log);



// class Waiter{
//     constructor(phrase){
//         this.phrase = phrase;
//     }

//     async f(){
//         let promise = new Promise((resolve, reject)=>{
//             setTimeout(()=>resolve(this.phrase), 3000)
//         });
        
//         let result = await promise;
//         console.log(result);
//     }

//     async e(){

//         await Promise.reject(new Error("Whoopppps!"));
//         // throw new Error("Whoopsss!");
//     }
// }
// let counter = setInterval(()=>{console.log(1);}, 1000);
// new Waiter("son").e();
// clearInterval(counter);

// function partial(func, ...argsBound){
//     return function(...args){
//         return func.call(this, ...argsBound, ...args);
//     }
// }

// let user = {
//     name: "Son",
//     say(time, phrase){
//         console.log(`[${time}] ${this.name} : ${phrase}!`);
//     }
// }

// sayNow = partial(user.say, new Date().getHours() + ":" + new Date().getMinutes()).bind(user);

// setTimeout(sayNow, 1000, "hahaha");

// user.sayNow("hahaaaaa");
// function mul(a, b){
//     return a * b;
// }

// let triple = mul.bind(null, 3);

// console.log(triple(3));

// let user = {
//     name: "son",
//     age: 20
// };

// function func(phrase){
//     console.log(phrase + " " + this.name + " " + this.age);
// }

// let funcUser = func.bind(user);

// funcUser("hello");




// let worker = {
//     slow(min, max) {
//       console.log(`Called with ${min},${max}`);
//       return min + max;
//     }
//   };
  
//   function cachingDecorator(func, hash) {
//     let cache = new Map();
//     return function() {
//       let key = hash(arguments); // (*)
//       if (cache.has(key)) {
//         return cache.get(key);
//       }
  
//       let result = func.call(this, ...arguments); // (**)
  
//       cache.set(key, result);
//       return result;
//     };
//   }
  
//   function hash(args) {
//     return args[0] + ',' + args[1];
//   }
  
//   worker.slow = cachingDecorator(worker.slow, hash);
  
//   console.log( worker.slow(3, 5) ); // works
//   console.log( "Again " + worker.slow(3, 5) ); // same (cached)




// let intervalTime = setInterval(()=>{
//     console.log(1);
// }, 1000);


// let timeOut = setTimeout(() => {
//     clearInterval(intervalTime);
//     console.log(2);
// }, 6000);


var x = 10;

function slice(str, start, end){
    x -= 1;
    return Array.from(str).slice(start, end).join('');
}

let str_test = "abcdef";

// console.log(slice(str_test, 2, 4));

function manyArg(first, last, ...args){
    console.log(first + " " + last);
    for(let arg of args){
        console.log(arg);
    }
}

// manyArg('son', 'nguyen', 'mot', 'hai', 'ba', 'zo');

let newArray = [1, 2, 3, 4];

let copyArray = [...newArray];

// console.log(JSON.stringify(newArray) === JSON.stringify(copyArray));

// console.log(x);
// iterables
let range = {
    from: 1,
    to: 5,

    [Symbol.iterator]() {
        this.current = this.from;
        return this;
    },

    next() {
        if (this.current <= this.to) {
            return { done: false, value: this.current++ };
        } else {
            return { done: true };
        }
    }
};

// for (let i of range) {
    // console.log(i);
// }


let str = "Son123";

let ite = str[Symbol.iterator]();

// while(true){
//     let res = ite.next();
//     if(res.done) break;
//     console.log(res.value);
// }

// let arrayLike = {
//     0: 1,
//     1: 3,
//     length: 2
// };

// arrayLike = Array.from(arrayLike, num => num * 2);

// for(let x of arrayLike){
//     console.log(x);
// }
