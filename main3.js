function convert(n) {
  let st = String(n);
  let emptyArray = [];
  for (let index = 0; index < st.length; index++) {
    emptyArray.push(+st[index]);
  }

  // return emptyArray.reverse();

  let result = emptyArray.reverse();
  return result;
}

console.log(convert(564987654)); // [4, 5, 6, 7, 8, 9, 4, 6, 5]
console.log(convert(529132)); // [2, 3, 1, 9, 2, 5]
