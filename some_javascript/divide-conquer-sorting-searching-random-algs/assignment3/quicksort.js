function quickSort(inputArray, arrayLength) {
  if (arrayLength === 1) {
      return inputArray;
  }

  var pivot = choosePivot(inputArray);
  var partition = partitionAroundArray(inputArray, pivot); 
  var partition1 = partition[0];
  var partition2 = partition[1];

  var firstPart = quickSort(partition1, partition1.length);
  var secondPart = quickSort(partition2, partition2.length);

  return firstPart.concat(secondPart);
}

function choosePivot(inputArray) {
  return inputArray[0];
}

function partitionAroundArray(inputArray, pivot) {
  var i = 1;
  for (var j = 1; j < inputArray.length; j++) {
    if (inputArray[j] < pivot) {
      var temp = inputArray[i];
      inputArray[i] = inputArray[j];
      inputArray[j] = temp;
      i++;
    }
  }
  var temp2 = inputArray[i-1];
  inputArray[i-1] = inputArray[0];
  inputArray[0] = temp2;
 
  // if input array is already sorted let i be 2 so the array is slice properly
  if (i === 1) {
    i = 2;
  }
  return [inputArray.slice(0, i-1), inputArray.slice(i-1)];
}

module.exports = quickSort;