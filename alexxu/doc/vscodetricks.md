1. Add Extension (Markdown PDF, PDF Preview, Python)
2. Save file
3. Open Terminal
4. Add Terminal
5. Create a Python file
6. Run Python file
1. Create title
2. Create bulletin list
3. Display image
4. Display web link
5. Create DOS command block
6. Create python program block
7. Convert markdown to PDF
8. Create file link 


## Create shortcut for complex code block
right-click in Editor window ⟹ command palettes ⟹ Configure user snipittes ⟹ python.json

Rigth-click in editor window ⟹ command palettes ⟹ configure user snippets ⟹ markdown.json.
```mermaid
graph TB
START((start))
END[end]
B[Hi]
A-->B
classDef html fill:#F46624,stroke:#F46624,stroke-width:4px,color:white;
classDef js fill:yellow,stroke:#DE9E1F,stroke-width:2px;
classDef start fill:green,stroke:#DE9E1F,stroke-width:2px;
classDef end1 fill:red,stroke:#DE9E1F,stroke-width:2px;
class START start
class B,C,D html
class END end1
```

```mermaid
classDiagram
class classname {
    variable:type
    function():returntype
}
```