function sortAndCount(array, arrayLength) {
  if (arrayLength === 1) {
      return [array, 0];
  }
  var half = Math.floor(arrayLength / 2);
  var firstHalf = array.slice(0, half);
  var secondHalf = array.slice(half);

  var firstSortAndCount = sortAndCount(firstHalf, firstHalf.length);
  var secondSortAndCount = sortAndCount(secondHalf, secondHalf.length);
  var mergeAndCount = countSplitInv(firstSortAndCount[0], secondSortAndCount[0], arrayLength);

  return [mergeAndCount[0], mergeAndCount[1] + firstSortAndCount[1] + secondSortAndCount[1]];

}

function countSplitInv(array1, array2, sumLength) {
    var result = [];
    var count = 0;
    for (var k = 0; k < sumLength; k++) {
      if (array1.length === 0 || array2.length === 0) {
        result = result.concat(array1);
        result = result.concat(array2);
        break;
      }
      if (array1[0] < array2[0]) {
        result.push(array1.shift());
      } else {
        count += array1.length;
        result.push(array2.shift());
      }
    }
    return [result, count]
}

module.exports = sortAndCount;