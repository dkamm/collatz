
import json
import uuid

import collatz

def defaultname(x):
    return '{}, {}'.format(x % 3, collatz.base2(x))

def build_tree_helper(x, n, d, max_d, name=defaultname):
    """Builds the collatz subtree rooted at x.

    Args:
        x (int): current node.
        n (int): number of children.
        d (int): current depth.
        max_d (int): max depth
        name (calleable): naming function. base10 int -> string.
    Returns:
        dict with 2 keys representing subtree rooted at x.
        'name' is the name for the node.
        'children' is a list of child dicts.
    """
    ret = {}
    ret['name'] = name(x)
    if d == max_d:
        return ret
    children = collatz.children(x, n)
    if x == 1:
        children = children[1:]
    if children:
        ret['children'] = [build_tree_helper(x, n, d + 1, max_d, name) for x in children]
    return ret

def build_tree(n, d, name=defaultname):
    """Builds a collatz tree.

    Args:
        n (int): number or of nodes
        d (int): depth of tree to render.
        name (calleable): function of base10 int -> string which names
            the node.
    Returns:
        dict with 2 keys representing tree rooted at 1.
        'name' is the name for the node.
        'children' is a list of child dicts.
    """
    return build_tree_helper(1, n, 1, d, name)


def get_html(tree, width=2000, height=500):
    """Generates html for an interactive collatz tree for use
    in jupyter notebook.

    See https://bl.ocks.org/mbostock/4339083.

    Args:
        tree (dict): dict representing collatz tree.
        width (int): width of plot in px.
        height (int): height of plot in px.
    """
    with open('collatz.json', 'w') as fh:
        fh.write(json.dumps(tree))

    def replace(_tmpl, **kwargs):
        for k, v in kwargs.items():
            _tmpl = _tmpl.replace('{{{{{}}}}}'.format(k), str(v))
        return _tmpl

    chartid = 'chart' + str(uuid.uuid4())[-6:]

    with open('tree.js.tmpl') as fh:
        tmpl = ''.join(fh.readlines())
        js_src = replace(tmpl, width=width, height=height, filename='collatz.json', chartid=chartid)

    with open('tree.html') as fh:
        html_src = ''.join(fh.readlines())
    html_src = replace(html_src, width=width, chartid=chartid)

    html = html_src + '<script>' + js_src + '</script>'
    return html
