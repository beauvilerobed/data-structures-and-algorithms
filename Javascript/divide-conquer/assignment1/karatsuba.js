function karatsuba(strnum1, strnum2) {
  var num1 = BigInt(strnum1);
  var num2 = BigInt(strnum2);
  if (num1 < 10n || num2 < 10n) {
    return num1 * num2;
  }
  var strnum1len = (strnum1.toString()).length;
  var strnum2len = (strnum2.toString()).length;

  var len = strnum1len > strnum2len ? strnum1len : strnum2len
  var maxstrlen = BigInt(len) / 2n; 
  var base = 10n ** maxstrlen;

  var a = num1 / base;
  var b = num1 % base;
  var c = num2 / base;
  var d = num2 % base;

  var first = karatsuba(a, c);
  var second = karatsuba(b, d);
  var third = karatsuba(a + b, c + d);
  var fourth = karatsuba(a, d) + karatsuba(c, b)

  return BigInt(first) * (base ** 2n) + BigInt(second) + base * BigInt(fourth);

}

module.exports = karatsuba;