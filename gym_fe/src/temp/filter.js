const empty = (arr) => {
  if (arr !== []) {
    for (const i = 0; i < arr.length; i++) {
      arr[i].pop();
      console.log(arr);
    }
  }
  
  return arr;
};

/**
 * listFilter : filters an array, to defined range
 * @param arr an array of size `n`
 * @param range limit
 * @returns a newly created filtered array
 **/
function listReducer(arr, range) {
  const filteredResults = [];
  let len = arr.length;

  range < len ? (len = range) : len;

  for (let i = 0; i < len; i++) {
    filteredResults.push(arr[i]);
  }

  return filteredResults;
}

export { listReducer, empty };
