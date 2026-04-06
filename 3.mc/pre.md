In Minecraft JAVA we have three dimensions, Overworld, Nether, and the End. The End should be the one that surprise and astonish players most, where some of us have never seen the true structure of the End. Just as when people discovered the earth is a ball, I found it extremely unbelievable when I heard that blocks would disappear suddenly at some places and reappear again. It was still unreliable for me that until I double checked this circumstances in my worlds. The next question is: why does this happen? I mean, which line of the code let everything occurred? This video is made based on this thought, from the perspective of a freshman undergraduate who is not majoring in Computer Science and has never written Java code before. So to understand all of these easily for both you and me, lets begin with the basics of computers.

Binaries, used commonly in every computer, can represent numbers and values by the on and off of anything, e.g., lights, switches, etc.. The tower of Computer Science is built up on this logic, and by logic gates we can accomplish all kinds of manipulations on binaries, additions, subtractions, multiplications, and divisions. For additions, we can consider it as two binary numbers being added together, bit by bit, just like how we do it in decimal. Each bit can be either 0 or 1, and when we add them, we have the rules 0+0=0, 0+1=1, 1+0=1, and 1+1=0 with a carry of 1 to the next bit. The result of the addition is a new binary number that represents the sum of the two original numbers, which can use XOR gate to calculate the sum bit and AND gate to calculate the carry bit. 

When it turns to subtraction, we can use the same logic as addition, but with a twist. Still we can design gates to calculate the difference bit by bit, but we need to consider the borrow bit as well. The rules for subtraction are 0-0=0, 1-0=1, 1-1=0, and 0-1=1 with a borrow of 1. The result of the subtraction is a new binary number that represents the difference of the two original numbers. However, this is not as straightforward as addition, because we need to consider the borrow bit and how it affects the next bit. In order to simplify the circuits we use in computers, we can use a technique called complements.

There are two types of complements, the 1's complement and the 2's complement. The 1's complement is simply flipping all the bits of a binary number, while the 2's complement is flipping all the bits and adding 1 to the result. By using NOT gate, we can flip all 0 into 1 and all 1 into 0, which is pretty easy. And as you can see, the 2's complement is based on the 1's complement but with an additional step, thus it is also easy to implement.

Then some smart babies would ask, why do we need complements? The answer is simple, because it makes subtraction easier. Instead of having to deal with the borrow bit and the complexity of subtraction, we can just add the 2's complement of the number we want to subtract. This way, we can use the same addition circuits we have already designed, and it simplifies the design of computers. We can prove this by using the example of 5-3. In binary, 5 is 101 and 3 is 011. The 2's complement of 3 is flipping all numbers, 011 into 100, then add 1 become 101, so we can add 5 and the 2's complement of 3 to get the result. The addition is as follows:

```
101 + 101 = 1010
```

Reject the first carry, we get 010, which is 2 in decimal. The reason we reject it is that we are only interested in the last three bits, which represent the result of the subtraction. In this case, we can see that numbers are represented by three bits, so the first carry is not needed. This is how we can use complements to simplify subtraction in computers, by only additions we can achieve the same result as subtraction, and it makes the design of computers much simpler and more efficient. Thus, if we store the 2's complement of a number in memory, we can easily perform subtraction by adding the 2's complement of the number we want to subtract.

But how does this work? If we list out all the numbers in binary, then we get a list of complements as follows:
```
binary decimal 1s 2s
0000    0   0   0
0001    1   1   1
0010    2   2   2
0011    3   3   3
0100    4   4   4
0101    5   5   5
0110    6   6   6
0111    7   7   7
1000    8   -7  -8
1001    9   -6  -7
1010   10   -5  -6
1011   11   -4  -5
1100   12   -3  -4
1101   13   -2  -3
1110   14   -1  -2
1111   15   -0  -1
```
(We can see here flips for 1s complement, but we shifted to get 2s complement. And another rule is decimal-15=1s complement, decimal-16=2s complement)
As you can see, if we use 1's complement, we can represent both positive and negative numbers, but we have two representations for 0, which is not ideal. However, if add 1 to the 1's complement, which has only one representation for 0. This is why we use 2's complement in computers, because it simplifies the representation of numbers and makes it easier to perform arithmetic operations. And to proof that it really works, lets imagine a clock with 12 hours, we can represent the time as a number from 0 to 11. So the forward list can be exchanged into

```
clock 1s 2s
0   0   0
1   1   1
2   2   2
3   3   3
4   4   4
5   5   5
6   -5  -6
7   -4  -5
8   -3  -4
9   -2  -3
10  -1  -2
11  -0  -1
```
where the mid-point is 6 o'clock, and the numbers after 6 are negative numbers. Thus we have clockwised to 3 to represent 3 o'clock later, and counterclockwised to 9 to represent 3 o'clock earlier (if we work as computers in two's complement). In this way, if I want to calculate what time it is 2 hours earlier than 5 o'clock, I can just take 10 for 2 hours earlier, and 5 for 5 hours later, then add them together, which is 15. But we only have 12 hours on the clock, so you would directly take the 3 o'clock, which is 15-12=3. This is how we can use complements to simplify subtraction in computers, by only additions we can achieve the same result as subtraction, and it makes the design of computers much simpler and more efficient.

For different number of bits, by using 2's complement, we can represent both positive and negative numbers. For 4 bits system , we can represent numbers from -8 to 7. So as to 8 bits system from -128 to 127, 16 bits system from -32768 to 32767, and so on. The range of numbers we can represent is `2^n` (from `-2^(n-1)` to `2^(n-1)-1`), and basically it would be decided by the capacity of the memory of a computer, which is usually a power of 2.

Some may ask, what if we add another one to the maximum value? This causes overflow error, which is the error occured when the value exceeds the maximum value can be expressed by the number of bits. If the maximum value is exceeded, it will wrap around to a negative value due to integer overflow.

Lets see an example. For decimal number `2147483646`, its binary representation is `01111111111111111111111111111110`. Here we have the first bit and the last bit as 0, and the other 30 bits are 1. If we add 1 to it, it will become `01111111111111111111111111111111`. These two numbers share the fisrt bit as 0, which means they are both positive numbers. However, if we again add 1, it will become `10000000000000000000000000000000`, which is a negative number `-2147483648` in 32-bit signed integer representation.

While in Minecraft Java Editions, the integer numbers are represented by 32 bits, which means we can represent numbers from `-2147483648` to `2147483647`. This is a very large range of numbers, and it allows us to represent all kinds of values in the game, such as player positions, block states, and so on. However, there are some limitations to this system. For example, if we try to represent a number that is larger than 2147483647, we will get an overflow error. This can cause unexpected behavior in the game, and in this case problems occured in the end dimension.

In the original code, we have
```java
// Original problematic code
private static float getHeightValue(SimplexNoise noise, int x, int z) {
    int chX = x / 2;
    int chZ = z / 2;
    int secX = x % 2;
    int secZ = z % 2;

    float errorWithNaN = 100 - Mth.sqrt(x * x + z * z) * 8;
    errorWithNaN = Mth.clamp(errorWithNaN, -100, 80);

    for (int iX = -12; iX <= 12; iX++) {
        for (int iZ = -12; iZ <= 12; iZ++) {
            long nX = (chX + iX);
            long nZ = (chZ + iZ);

            if (nX * nX + nZ * nZ > 4096 && noise.getValue(nX, nZ) < -0.9F) {
                float rnd = (Mth.abs(nX) * 3439 + Mth.abs(nZ) * 147) % 13 + 9;
                float gx = (secX - iX * 2);
                float gy = (secZ - iZ * 2);
                float islandDensity = 100 - Mth.sqrt(gx * gx + gy * gy) * rnd;
                islandDensity = Mth.clamp(islandDensity, -100, 80);
                errorWithNaN = Math.max(errorWithNaN, islandDensity);
            }
        }
    }
    return errorWithNaN;
}
```

This code is used to generate the height value of the End dimension, and it works well for most cases. `errorWithNaN = Mth.clamp(errorWithNaN, -100, 80);` is used to ensure that the height value is within the range from -100 to 80, and the name `errorWithNaN` is only a temporary variable to hold the error value (although it really goes wrong somtimes!). The two nested loops iterate over a range of values to calculate the island density based on the noise value, and errorWithNaNis updated accordingly to become the final height value. The `Mth.sqrt(x * x + z * z)`is used to calculate the distance from (0, 0), and the result is multiplied by 8 to get the final coordinate you see in Minecraft. This means that each chunk (which is 16 blocks * 16 blocks in size) is conceptually divided into four parts (each 8 blocks * 8 blocks in size) for generation purposes.

So, how does this strange phenomenon of blocks disappearing and reappearing actually happen in the game? To understand this, we need to take a look the line
```java
float errorWithNaN = 100 - Mth.sqrt(x * x + z * z) * 8;
```
has a problem when the x and z coordinates are too large. For the `Math.sqrt()` function, it calculates the square root of the sum of the squares of x and z. But in Java, since Mojang did not protect against overflow, when `x * x + z * z` exceeds the maximum value, i.e. `2147483647`, it wraps around to a negative value due to integer overflow. This causes `Mth.sqrt(x * x + z * z)` to return `NaN` (Not a Number) or a negative value, which leads to  blocks disappearing or reappearing unexpectedly.

Lets take an example. Suppose we have `x = 46340, z = 0`. Please remember that x here is not the coordinate you see in Minecraft, but only the number of halved chunk index. Then `x * x + z * z` will be `2,147,395,600`. At this point, since
```
2,147,395,600 < 2,147,483,647
```
, it will not overflow yet, so we can still see blocks at the point scaled by 8: `(370720, ~, 0)`. But if we increase `x` to `46341`, then `x * x + z * z` will be `2,147,488,281`, which exceeds the maximum value. This causes an overflow, and the result wraps around to a negative value. Specifically, 
```
2,147,488,281 - 4,294,967,296 = -2,147,479,015
```
. When we take the square root of this negative value using `Mth.sqrt()`, it returns `NaN`. Thus after scaled by 8 at point `(370728, ~, 0)`, there are no blocks generated. 

However, things do not end here. When we still increase `x` and `z` to larger values, then `x * x + z * z` will eventually become larger and larger, since the distance is simply increasing. But if we keep increasing `x` and `z`, the value will wrap around again and again, it can led a fake positive value, and thus `Mth.sqrt()` will return a valid positive number again. This is why blocks reappear again at some places far away.

Lets see another example. Suppose we have `x = 65536, z = 0`, then `x * x + z * z` will be `4,294,967,296`. Since
```
4,294,967,296 - 4,294,967,296 = 0
```
You say, what? WHY 4,294,967,296 not 2,147,483,647? This is because an entire 'turn' of 32 bits is `2^32 = 4,294,967,296`, which is the maximum value of a 32-bit signed integer. So exactly at `x = 65536` it will wrap around to `0`. When we take the square root of this value using `Mth.sqrt()`, it returns `0`, which is valid. Thus after scaled by 8 at point `(524,288, ~, 0)`, blocks reappear again.

The disappearing and reappearing loops continue as we increase `x` and `z` further. But the distance between the disappearing and reappearing points will become smaller and smaller. And we can derive some formulas to calculate the exact points where blocks disappear and reappear. Denote distance from `(0,0)` as `r`. For `r^2` it is always increasing, but we want to find the points where it wraps around. And do not forget Minecraft generate the end in terms of 8. i.e. We seek for 
```
(r/8)^2 = n (mod 2^32)
```
where `0 <= n <= 2^31`. On the graph it obeys the region like this: ... To further locate some exact points, lets consider an sinusoidal onscillation, and for the positive part, we have blocks, while for the negative part, we have no blocks. Thus we should have a period of `2^32 * 8^2`, such that `omega=2pi/(2^32*64)`, and the function should be `f(r) = sin(omega*r^2)`. We choose sine instead of cosine as sine is even and symmetric about the origin, same as that in Minecraft.
```
omega=2pi/(2^32*64)=2.2858094988549370016427153192341e-11
```
In this way, the formula is 
```
y=sin(2.2858094988549370016427153192341e-11*r^2)
```
where `y` is the height value, and `r` is the distance from `(0,0)`. To make it visible on graphing software, we can multiply `y` by `25000`. And this is why you may have seen this formula before
```
250000\sin\left(\left(x^{2}\right)\cdot0.0000000000228580929\right)
```
And I also wrote a Python script to visualise the phenomenon, which you can find in the description below.
...

看情况做其他内容。