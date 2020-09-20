const countAndQuickSort = require('../divide-conquer/assignment3/countQuickSort');

QUnit.module('conutAndQuickSort');

QUnit.test('test base case', assert => {
    var expected = 0;
    var actual = countAndQuickSort([1])
  assert.equal(actual, expected, 'should return 0');
});

QUnit.test('test array of length 2', assert => {
    var expected = 1;
    var actual = countAndQuickSort([2, 1]);
  assert.equal(actual, expected, 'should return 1');
});

QUnit.test('test array of length 3', assert => {
    var expected = 2;
    var actual = countAndQuickSort([2, 1, 3]);
  assert.equal(actual, expected, 'should return 3');
});

QUnit.test('test array of length 5', assert => {
    var expected = 6;
    var actual = countAndQuickSort([3, 2, 1, 4, 5]);
  assert.equal(actual, expected, 'should return 6');
});