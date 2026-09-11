# My Testing Notes

**Tester:** [Bingyu Du]  
**Date:** 11 September 2026

I tested the two Python files with the files given for the assignment. I did not change any code while testing.

## Question 1 - Cipher

I used the supplied `raw_text.txt` and tried a few shift values.

| Shift values | What happened |
| --- | --- |
| `0, 0` | It worked. The program said `Decryption Successful` and the decrypted file matched the original file. |
| `1, 2` | It did not work. The program said `Unsuccessful, try again`. |
| `3, 5` | It also did not work. The decrypted file was different from the original. |
| `-1, 2` | The program still accepted the negative number instead of stopping it. |

Things I noticed:

- The program can make `encrypted_text.txt` and `decrypted_text.txt`.
- It only fully worked for the `0, 0` test I tried.
- The task says the shift numbers should not be negative, so that should probably be checked in the program.
- The task also asks for separate encrypt, decrypt, and verify functions. I could not find those as separate functions yet.

## Question 2 - Calculator

First I ran the file with an `input.txt` file in the same folder. It did run, but it only printed the built-in `7 ^ 2` example. It did not read my `input.txt` and it did not make `output.txt`.

Here are some expressions I tried:

| Expression | Result I got | Comment |
| --- | --- | --- |
| `3 + 5` | `8` | Worked |
| `2 + 3 * 4` | `14` | Worked |
| `-(3 + 4)` | `7` | Should be `-7`, so this did not work |
| `--5` | `5` | Got the right answer, but this should be checked again after fixing minus |
| `(10 - 2) * 3 + -4 / 2` | `26` | Should be `22`, so this did not work |
| `3 @ 5` | Error | Good - it saw that `@` is not allowed |
| `1 / 0` | Error | Good that it stopped, but it is not shown as `ERROR` in an output file yet |
| `1 / 3` | `0.3333` | Worked |
| `2 ^ 3 ^ 2` | `512` | Worked |
| `2(3 + 4)` | `14` | Worked |
| `2 3` | Error | Worked - this should not be allowed |
| `+5` | Error | Worked - unary plus should not be allowed |
| `2 ^ -2` | Error | This should be allowed because minus can come after an operator |

Things I noticed:

- Normal maths like addition, multiplication, brackets, decimals, powers, and `2(3+4)` mostly worked.
- The minus sign is showing in the tree, but it is not making the answer negative. This is why `-(3 + 4)` gave `7` instead of `-7`.
- The assignment asks for an `evaluate_file(input_path)` function. I could not find it in the file yet.
- The assignment also asks for an `output.txt` file with the Input, Tree, Tokens, and Result lines. That part is not there yet.

## Short conclusion

There are some parts that are working, especially the basic calculator operations. Before submitting, I think the group should fix the Cipher decryption for normal shift numbers, fix negative numbers in the calculator, and add the required input/output file part for Question 2.
