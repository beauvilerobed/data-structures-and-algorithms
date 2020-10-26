const karatsuba = require('../divide-conquer-sorting-searching-random-algs/assignment1/karatsuba');
const answers = require('../test/answers')

QUnit.module('karatsuba');

QUnit.test('karatsuba two positive integers', assert => {
    var expected = 123456789n * 987654321n;
    var actual = karatsuba('123456789', '987654321');
  assert.equal(actual, expected, '123456789 * 987654321');
});

QUnit.test('test assignment', assert => {
    var expected = answers.karatsuba;
    var actual = karatsuba('3141592653589793238462643383279502884197169399375105820974944592', '2718281828459045235360287471352662497757247093699959574966967627');
  assert.equal(actual, expected, '3141592653589793238462643383279502884197169399375105820974944592 * 2718281828459045235360287471352662497757247093699959574966967627');
})