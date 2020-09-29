const doThirtyItrMincut = require('../divide-conquer/assignment4/mincut');

QUnit.module('mincut');

QUnit.test('test first case', assert => {
    var expected = 2;
    var graph = {1:[2,4], 2:[1,3,4], 3:[2,4], 4:[1,2,3]};
    var actual = doThirtyItrMincut(graph);
  assert.equal(actual, expected, 'should return 2');
});