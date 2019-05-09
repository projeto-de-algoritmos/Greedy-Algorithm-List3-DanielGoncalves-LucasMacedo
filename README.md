# <p align="center">Telegram Bot to encode text using Greedy Algorithm Huffman Code</p>

## Autors

| Name  | University Registration  | GitHub | Email |
|---|---|---|---|
| Daniel Maike Mendes Gonçalves  | 16/0117003  | [DanMke](https://github.com/DanMke) | danmke@hotmail.com |
| Lucas Pereira de Andrade Macêdo  | 15/0137397  | [lukassxp](https://github.com/lukassxp) | lpalucas.10@gmail.com |

## Using Bot

### Telegram Bot Link

Redirects to the conversation with the bot, a telegram account is needed
* http://t.me/huffman_encoding_bot

### Bot Commands

> * ``` /start ``` 
Initial message to bot and the bot shows the accepted commands

> * ``` /help ```
Bot shows the accepted commands

> * ``` /encode <text> ```
(enter text after the command /encode)
The bot shows the coded, decoded text and number of bits saved with the compression
 
### Bot Limitations

The telegram only allows messages of up to 4096 characters in size, so it is possible to encode texts up to 4096 characters (command /encode + text).
For the code it is possible to encode larger sized text, it is a limitation only for the bot.

## Huffman Code

In computer science and information theory, 
a Huffman code is a particular type of optimal prefix code that is commonly 
used for lossless data compression. The process of finding or using such a code proceeds by means of Huffman coding, 
an algorithm developed by David A. Huffman while he was a Sc.D. student at MIT, and published in the 1952 paper 
"A Method for the Construction of Minimum-Redundancy Codes".
The output from Huffman's algorithm can be viewed as a variable-length code 
table for encoding a source symbol (such as a character in a file). 
The algorithm derives this table from the estimated probability or frequency of occurrence (weight) 
for each possible value of the source symbol. As in other entropy encoding methods, more common 
symbols are generally represented using fewer bits than less common symbols. Huffman's method can be 
efficiently implemented, finding a code in time linear to the number of input weights if these weights are sorted. 
However, although optimal among methods encoding symbols separately, Huffman coding is not always optimal among 
all compression methods.

## References
 
> * https://core.telegram.org/bots/api <br>
> * https://en.wikipedia.org/wiki/Huffman_coding
