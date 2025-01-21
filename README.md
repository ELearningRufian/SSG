# SSG

A static site generator that takes raw content files (like Markdown and images) and turns them into a static website (a mix of HTML, images and CSS files).

Limitations and Known issues:

* The only markdown tags supported are:
    * Inline
        * Bold, text surrounded by double asterisks (**)
        * Italic, text surrounded by single asterisks (*)
        * Code, text surrounded by single backticks (`)
        * Images, `![alt text](image url, e.g., "local/path/image.jpg"`
        * Links, `[link text](link url, e.g., https://boot.dev)`
    * Blocks
        * Headers (1 to 6), blocks starting with 1 to 6 consecutive hash marks (#) followed by a space
        * Code, blocks surrounded by triple backticks (```)
        * Blockquote, blocks where all lines start with a greater than (>) optionally followed by spaces
        * Unordered Lists, blocks where all lines start with an asterisk (*) or a hyphen (-)
        * Ordered Lists, blocks where lines start with consecutive numbers, followed by a period and a space
* Blocks are separated by empty lines and are processed first. They can contain inline elements, but support for nesting inline elements is not implemented.
* Multi-level support for lists is not implemented.
* Conversion of line breaks is not implemented (e.g., a code block with newlines will not get converted appropriately).
* Conversion of HTML entities (characters that would need &amp;code; representation) is not implemented.
