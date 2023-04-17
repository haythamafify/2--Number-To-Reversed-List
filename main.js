function convert(n) {
  let st = n.toString();
  let arr = st.split("");
  // arr = arr.map((m) => parseInt(m)).reverse();
  arr = arr.map((m) => +m);
  arr = arr.reverse();
  return arr;
}

console.log(convert(564987654)); // [4, 5, 6, 7, 8, 9, 4, 6, 5]
console.log(convert(529132)); // [2, 3, 1, 9, 2, 5]
