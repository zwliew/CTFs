# PHP Master [Web - 50 points]

## Description

> Another one of _those_ challenges.
>
> Target: http://challs.xmas.htsp.ro:3000/
> Author: yakuhito

## Solution

Navigating to the target site, we see the following PHP code:

```php
<?php

include('flag.php');

$p1 = $_GET['param1'];
$p2 = $_GET['param2'];

if(!isset($p1) || !isset($p2)) {
    highlight_file(__FILE__);
    die();
}

if(strpos($p1, 'e') === false && strpos($p2, 'e') === false  && strlen($p1) === strlen($p2) && $p1 !== $p2 && $p1[0] != '0' && $p1 == $p2) {
    die($flag);
}

?>
```

On a GET request, the server requires the existence of 2 query parameters: `param1` and `param2`. Note that in PHP,the parameters can only either be `strings` or `arrays`.

Based on the conditionals that follow, the query parameters must satisfy the following requirements:

1. Both parameters do not contain the character "e".
2. Both parameters _strictly_ have the same length outputted by `strlen()`. (Note that `strlen()` outputs `null` for `arrays`.)
3. Both parameters are not strictly equivalent.
4. The first element in the first parameter is not a "0".
5. Both parameters are equivalent after type juggling.

I realised that the parameters must either be both `arrays` or both `strings`. This is because `strlen()` would return `null` for `arrays` and a valid integer for `strings`. If 1 of the parameters is a `string` and the other is an `array`, the 2nd requirement would not be satisfied.

It turns out [numeric strings convert to integers](https://www.php.net/manual/en/language.types.type-juggling.php). Hence, if `param1 = "1."` and `param2 = "01"`, `param1 == param2` would be true since both would be converted to the integer `1` before comparison.

Therefore, the solution is `http://challs.xmas.htsp.ro:3000/?param1=1.&param2=01`.

The flag is `X-MAS{s0_php_m4ny_skillz-69acb43810ed4c42}`.
