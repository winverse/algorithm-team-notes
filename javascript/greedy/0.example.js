// 거스름돈 구하기

let n = 1260;
const coins = [500, 100, 50, 10];

let count = 0;

for (i in coins) {
  const coin = coins[i];
  count += parseInt(n / coin);
  n %= coin;
}

console.log(count);
