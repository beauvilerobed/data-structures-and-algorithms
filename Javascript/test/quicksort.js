const quickSort = require('../divide-conquer/assignment3/quicksort');

QUnit.module('quickSort');

QUnit.test('test best case', assert => {
    var expected = [1];
    var actual = quickSort([1],1);
  assert.deepEqual(actual, expected, 'should return [1]');
});

QUnit.test('test array of length 2', assert => {
    var expected = [1, 2];
    var actual = quickSort([2, 1], 2);
  assert.deepEqual(actual, expected, 'should return [1, 2]');
});

QUnit.test('test array of length 3', assert => {
    var expected = [1, 2, 3];
    var actual = quickSort([2, 1, 3], 3);
  assert.deepEqual(actual, expected, 'should return [1, 2, 3]');
});

QUnit.test('test array of even length', assert => {
    var expected = [1, 2, 3, 4, 5, 6];
    var actual = quickSort([2, 5, 3, 6, 1, 4], 6);
  assert.deepEqual(actual, expected, 'should return [1, 2, 3, 4, 5, 6]')
});

QUnit.test('test array to help find issue', assert => {
    var expected = [45, 49, 26, 22, 87, 65, 72, 41, 25];
    expected = expected.sort(function(a, b){return a - b});
    var actual = quickSort([45, 49, 26, 22, 87, 65, 72, 41, 25], 9);
  assert.deepEqual(actual, expected, '22 and 25 should be in the proper location')
});


QUnit.test('test array of odd length', assert => {
    var expected = [45, 49, 26, 22, 87, 65, 72, 41, 25, 1, 59, 51, 69, 3, 47, 16, 93, 96, 32, 92, 83, 43, 86, 60, 75, 89, 39, 74, 81, 50, 77, 42, 97, 6, 62, 63, 36, 29, 52, 5, 14, 33, 55, 27, 57, 2, 82, 48, 40, 95, 7, 100, 15];
    expected = expected.sort(function(a, b){return a - b});
    var actual = quickSort([45, 49, 26, 22, 87, 65, 72, 41, 25, 1, 59, 51, 69, 3, 47, 16, 93, 96, 32, 92, 83, 43, 86, 60, 75, 89, 39, 74, 81, 50, 77, 42, 97, 6, 62, 63, 36, 29, 52, 5, 14, 33, 55, 27, 57, 2, 82, 48, 40, 95, 7, 100, 15], 53);
  assert.deepEqual(actual, expected, 'should return sorted array')
});