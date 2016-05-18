import re

HEADING_MARKERS = {
    1:"# ",
    2:"## ",
    3:"### ",
    4:"#### "
}

MARKDOWN_CELL_TEMPLATE = """
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "%s"
   ]
  },"""

EMPTY_CODE_CELL = """
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },"""

    
def create_ipynb_json_from_md(md_source, extra_code_cells=2):
    """
    Parses makdown syntax in `md_source` prepares JSON suitable 
    for copy pasting into an Jupyter notebook file.
    """

    output = ""

    leading_sp_re = re.compile(r"(?P<presp>\s*)(?P<rest>.*)")    
    list_item_re = re.compile(r"(?P<presp>\s*)[-|\*](?P<postsp>\s{1,4})(?P<rest>.*)")

    # STATE 
    level = 0       # list level
    indents = {
        1:0,        # indentation level for first-level lists (in spaces)
        2:0,        # indentation level for second-level lists (in spaces)
        3:0,        # indentation level for third-level lists (in spaces)
        4:0
    }
    
    for line in md_source.splitlines():
        if len(line.strip()) == 0:                     # skip blank lines
            continue
        list_item = list_item_re.match(line)
        leading_sp = leading_sp_re.match(line)
        if list_item:
            # match list item
            groups = list_item.groupdict()
            presp, postsp, rest = groups['presp'], groups['postsp'], groups['rest']
            rest_escaped = rest.replace("\\", "\\\\")
            line_indent = len(presp) + 1 + len(postsp)
            if level == 0:                           # A: start initial list
                level = 1
                indents[level] = line_indent
            elif level >= 1:                         # B: already in list
                if line_indent == indents[level]:    #   B1: continue list
                    pass
                elif line_indent > indents[level]:   #   B2: start deeper list
                    level += 1
                    indents[level] = line_indent
                elif line_indent < indents[level]:   #   B3: end list
                    if line_indent == indents[level-1]:
                        level = level - 1
                    elif line_indent == indents[level-2]:
                        level = level - 2
                    elif line_indent == indents[level-3]:
                        level = level - 3      
                    else:
                        pass
            # print actual json
            output += MARKDOWN_CELL_TEMPLATE % (HEADING_MARKERS[level] + rest_escaped)
            for i in range(0,extra_code_cells):
                output += EMPTY_CODE_CELL
        elif leading_sp:
            groups = leading_sp.groupdict()
            presp, rest = groups['presp'], groups['rest']
        else:
            pass

    return output

