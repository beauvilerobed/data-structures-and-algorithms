const quickSort = require('../divide-conquer-sorting-searching-random-algs/assignment3/quicksort');

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
