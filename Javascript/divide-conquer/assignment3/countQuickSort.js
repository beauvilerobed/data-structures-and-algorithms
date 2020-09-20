// for the first question in assignment #3
var globalCount = 0;

function countAndQuickSort(inputArray) {
  partitionAroundArray(inputArray, 0, inputArray.length - 1);
  var count = globalCount;
  globalCount = 0;
  return count;
}

function partitionAroundArray(inputArray, leftMost, rightMost) {
  console.log(globalCount)
  globalCount += Math.max(rightMost - leftMost, 0);
  if (rightMost - leftMost < 1) {
    return; 
  }
//   var pivot = choosePivot(inputArray);
  var i = leftMost + 1;
  for (var j = leftMost + 1; j < rightMost + 1; j++) {
    if (inputArray[j] < inputArray[leftMost]) {
    var temp = inputArray[i];
    inputArray[i] = inputArray[j];
    inputArray[j] = temp;
    i++;
    }
  }
  var temp2 = inputArray[i-1];
  inputArray[i-1] = inputArray[leftMost];
  inputArray[leftMost] = temp2;

  if (i !== leftMost + 1) {
    partitionAroundArray(inputArray, leftMost, i - 2)
  }
  partitionAroundArray(inputArray, i , rightMost)
}

module.exports = countAndQuickSort;