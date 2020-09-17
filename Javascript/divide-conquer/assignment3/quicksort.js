function quickSort(array, arrayLength) {
  if (arrayLength === 1) {
      return array;
  }

  var pivot = choosePivot(array);
  var partition = partitionAroundArray(array, pivot, arrayLength); 
  var partition1 = partition[0];
  var partition2 = partition[1];
  var firstPart = quickSort(partition1, partition1.length);
  var secondPart = quickSort(partition2, partition2.length);

  return firstPart.concat(secondPart);
}

function choosePivot(array) {
  return array[0];
}

function partitionAroundArray(array, pivot, arrayLength) {
  var i = 0;
  for (var j = 1; j < arrayLength; j++) {
      if (array[j] < pivot) {
          var temp = array[i];
          array[i] = array[j];
          array[j] = temp;
          i++;
      }
  }
  var temp = array[i-1];
  array[i-1] = array[0];
  array[0] = temp;

  return [array.slice(0,i), array.slice(i)];
}

module.exports = quickSort;