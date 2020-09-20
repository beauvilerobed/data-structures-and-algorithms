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

QUnit.test('test array of length 5 with leftMost rightMost and middle', assert => {
    var expected = 6;
    var actual = countAndQuickSort([3, 2, 1, 4, 5], 'leftMost');
  assert.equal(actual, expected, 'should return 6');

    var expected = 10;
    var actual = countAndQuickSort([3, 2, 1, 4, 5], 'rightMost');
  assert.equal(actual, expected, 'should return 10');

    var expected = 6;
    var actual = countAndQuickSort([3, 2, 1, 4, 5], 'middle');
  assert.equal(actual, expected, 'should return 6');
});


QUnit.test('test array of length 5 with leftMost rightMost and middle', assert => {
    var expected = 69;
    var actual = countAndQuickSort([2, 1, 12, 13, 16, 10, 9, 5, 18, 8, 17, 20, 19, 3, 4, 11, 14, 6, 7, 15], 'leftMost');
  assert.equal(actual, expected, 'should return 69');

    var expected = 65;
    var actual = countAndQuickSort([2, 1, 12, 13, 16, 10, 9, 5, 18, 8, 17, 20, 19, 3, 4, 11, 14, 6, 7, 15], 'rightMost');
  assert.equal(actual, expected, 'should return 65');

    var expected = 56;
    var actual = countAndQuickSort([2, 1, 12, 13, 16, 10, 9, 5, 18, 8, 17, 20, 19, 3, 4, 11, 14, 6, 7, 15], 'middle');
  assert.equal(actual, expected, 'should return 56');
});
