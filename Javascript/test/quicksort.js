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