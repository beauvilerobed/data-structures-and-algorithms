// Only for testing purposes. window is not defined
var globalCount = 0;

function countAndQuickSort(inputArray, choosePivot) {
  partitionAroundArray(inputArray, 0, inputArray.length - 1, choosePivot);
  var count = globalCount;
  globalCount = 0;
  return count;
}

function partitionAroundArray(inputArray, leftMost, rightMost, choosePivot) {
  globalCount += Math.max(rightMost - leftMost, 0);
  if (rightMost - leftMost < 1) {
    return; 
  }
  
  // choose the pivot index
  var pivotIndex = selectFirst(leftMost, rightMost);;
  if (choosePivot === 'rightMost') {
    pivotIndex = selectLast(leftMost, rightMost);
  } 
  if (choosePivot === 'middle') {
    pivotIndex = selectThreepointMedian(inputArray, leftMost, rightMost, choosePivot)
  }

  var tempSwap = inputArray[leftMost];
  inputArray[leftMost] = inputArray[pivotIndex];
  inputArray[pivotIndex] = tempSwap;

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
    partitionAroundArray(inputArray, leftMost, i - 2, choosePivot)
  }
  partitionAroundArray(inputArray, i , rightMost, choosePivot)
}

function selectFirst(leftMost, rightMost) {
  return leftMost;
}

function selectLast(leftMost, rightMost) {
  return rightMost;
}

function selectThreepointMedian(inputArray, leftMost, rightMost) {
  var middle = leftMost + Math.floor((rightMost - leftMost) / 2);
  var medianValue = median([inputArray[leftMost], inputArray[rightMost], inputArray[middle]]);
  return inputArray.indexOf(medianValue);
}

function median(values){
  if(values.length === 0) return 0;

  values.sort(function(a,b){return a-b;});
  var half = Math.floor(values.length / 2);
  if (values.length % 2)
    return values[half];
  return (values[half - 1] + values[half]) / 2.0;
}

module.exports = countAndQuickSort;