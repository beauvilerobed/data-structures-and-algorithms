var globalCount = 0;

function countQuickSort(inputArray, choosePivot) {
  partitionAroundArray(inputArray, 0, inputArray.length - 1, choosePivot);
  var count = globalCount;
  globalCount = 0;
  return count; 
}

function partitionAroundArray(inputArray, leftMost, rightMost, choosePivot) {
  globalCount += Math.max(rightMost - leftMost, 0)
  if (rightMost - leftMost < 1) {
    return;
  }
  
  var pivotIndex = selectFirst(leftMost, rightMost);
  if (choosePivot === 'rightMost') {
    pivotIndex = selectSecond(leftMost, rightMost);
  } else if (choosePivot === 'middle') {
    pivotIndex = selectThreepointMedian(inputArray, leftMost, rightMost)
  }

  var temp = inputArray[leftMost];
  inputArray[leftMost] = inputArray[pivotIndex];
  inputArray[pivotIndex] = temp;

  var i = leftMost + 1;
  for (var j = leftMost + 1; j < rightMost + 1; j++){
    if (inputArray[j] < inputArray[leftMost]) {
      var temp2 = inputArray[i];
      inputArray[i] = inputArray[j];
      inputArray[j] = temp2;
      i++
    }
  }

  var temp3 = inputArray[leftMost];
  inputArray[leftMost] = inputArray[i-1];
  inputArray[i-1] = temp3;

  if (i !== leftMost + 1) {
    partitionAroundArray(inputArray, leftMost, i - 2, choosePivot);
  }
  partitionAroundArray(inputArray, i, rightMost, choosePivot);

}

function selectFirst(leftIndex, rightIndex) {
  return leftIndex;
}

function selectSecond(leftIndex, rightIndex) {
  return rightIndex;
}

function selectThreepointMedian(inputArray, left, right) {
  var middle = left + Math.floor((right - left) / 2);
  var median = medianValue([inputArray[left], inputArray[right], inputArray[middle]]);
  var middleIndex = inputArray.indexOf(median);
  return middleIndex;
}

function medianValue(inputArray) {
  if (inputArray.length === 0) {
    return 0;
  }

  inputArray.sort(function(a, b) {return a - b;});
  var middleIndex = Math.floor(inputArray.length / 2);
  if (inputArray.length % 2) {
    return inputArray[middleIndex];
  }
  return (inputArray[middleIndex - 1] + inputArray[middleIndex]) / 2.0;
}

module.exports = countQuickSort;