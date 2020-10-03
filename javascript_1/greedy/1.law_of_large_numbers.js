const n = 5;
let m = 8;
const k = 3;

const data = [2, 4, 5, 4, 6];

data.sort();
const leng = data.length;

const max = data[leng - 1];
const subMax = data[leng - 2];

let result = 0;

while (true) {
  for (let i = 0; i < k; i++) {
    if (m === 0) break;
    result += max;
    m -= 1;
  }
  if (m === 0) break;
  result += subMax;
  m -= 1;
}

console.log(result);
