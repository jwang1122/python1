## Useful Icons

β‘οΈππβοΈβββοΈππ¨π‘βοΈππβοΈππππΎπππβ οΈππ’β»οΈπ₯π ππ―βοΈβοΈ

## Sample File Structure:

```output
<project root>
    βββ πdoc/
    |    βββ mistakes.md 
    |    βββ vscodeTrics.md 
    |    βββ python.md 
    βββ π¨homeworks/
    |       βββ <filenameXX.md>
    βββ π₯src/
    |      βββ hello.py 
    βββ πReadMe.md
```

## Colors

[color picker](https://www.webfx.com/web-design/color-picker/)

## Sample Mermaid Diagram

```mermaid
graph TB
START((start))
B[code block]
END[end]
IF{condition<br> block}
DB[(database)]

START-->IF
IF--True-->DB-->END
IF--False-->B-->END

classDef html fill:#F46624,stroke:#F46624,stroke-width:4px,color:white;
classDef js fill:yellow,stroke:black,stroke-width:2px;
classDef if fill:#EBCD6F,stroke:black,stroke-width:2px;
classDef db fill:#BEBDB7,stroke:black,stroke-width:2px;
classDef start fill:green,stroke:#DE9E1F,stroke-width:2px,color:white;
classDef end1 fill:red,stroke:#DE9E1F,stroke-width:2px,color:white;

class START start
class B,D,E js
class IF if
class DB db
class END end1
```