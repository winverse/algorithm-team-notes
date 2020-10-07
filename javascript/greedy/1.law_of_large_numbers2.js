const m = 8;
const k = 3;

const data = [2, 4, 5, 4, 6, 6];

const n = data.length;

const uniqueData = [];

data.forEach((k) => {
  if (!uniqueData.includes(k)) {
    uniqueData.push(k);
  }
});

uniqueData.sort();

const dataLeng = uniqueData.length;

const maxNum = uniqueData[dataLeng - 1];
const nextMaxNum = uniqueData[dataLeng - 2];

let count = parseInt(m / (k + 1)) * k;
count += m % (k + 1);

let result = 0;

result += maxNum * count;
result += nextMaxNum * (m - count);

console.log(result);
