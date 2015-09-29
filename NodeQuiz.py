def flag(node):
    if isinstance(node, dict):
        if 'children' in node.keys():
            # list comprehension over generator expression: for efficiency
            [flag(t) for t in (i for i in (node['children']))]
        if node['weight'] > 5:
            node['flagged'] = True


def reset(node):
    if isinstance(node, dict):
        if 'children' in node.keys():
            # list comprehension over generator expression: for efficiency
            [reset(t) for t in (i for i in (node['children']))]
        if 'flagged' in node.keys():
            node['weight'] = 0


def destroy_flags(node):
    if isinstance(node, dict):
        if 'children' in node.keys():
            # list comprehension over generator expression: for efficiency
            [destroy_flags(t) for t in (i for i in (node['children']))]
        node.pop('flagged', None)


a = {"id": 1, "weight": 0, "children": [
    {"id": 3, "weight": 7, "children": [
        {"id": 4, "weight": 5, "children": [
            {"id": 6, "weight": 8, "children": [
                {"id": 10, "weight": 6, "children": []}
            ]},
            {"id": 7, "weight": 3, "children": [
                {"id": 8, "weight": 7, "children": []}
            ]}
        ]},
    ]},
]}

