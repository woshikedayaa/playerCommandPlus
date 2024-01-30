# playerCommandPlus

通过mcdr来加强player指令的功能

## 使用例

```text
!pcp help 显示帮助页面  
!!pcp hello spawn 召唤hello假人  
!!pcp hello[0-10] spawn  
召唤hello0,hello1...hello10假人  
carpet:/player hello0 spawn,/player hello1 spawn...  
!!pcp hello[0-10] kill  
将hello0,hello1...hello10假人退出  
carpet:/player hello0 kill,/player hello1 kill...  
!!pcp hello[0-10] jump.interval.10  
让hello0,hello1...hello10假人每10gt跳跃一次  
carpet:/player hello0 jump interval 10,/player hello0 jump interval 10  
```

## config
```js
{
    // 前缀 #none 代表没有
    "prefix":"#none",
    // 后缀 #none 代表没有
    "suffix":"#none"
}

```

## 作者

woshikedayaa  

## LICENSE

```text
MIT License

Copyright (c) 2023 woshikedayaa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
