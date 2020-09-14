function mergeSort(array, arrayLength) {
  if (arrayLength === 1) {
      return array;
  }

  var half = Math.floor(arrayLength / 2);
  var firstHalf = array.slice(0, half);
  var secondHalf = array.slice(half);

  var firstSorted = mergeSort(firstHalf, firstHalf.length)
  var secondSorted = mergeSort(secondHalf, secondHalf.length);
  var mergeHalfs = merge(firstSorted, secondSorted, arrayLength);

  return mergeHalfs
}

function merge(array1, array2, sumLength) {
  var result = []; 
  for (var k = 0; k < sumLength; k++) {
    if (array1.length === 0 || array2.length === 0) {
      result = result.concat(array1);
      result = result.concat(array2);
      break;
    }
    if (array1[0] < array2[0]) {
      result.push(array1.shift());
    } else {
      result.push(array2.shift());
    }
  }
  return result;
}

module.exports = mergeSort;