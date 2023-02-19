# pip install compute_rhino3d and rhino3dm
import compute_rhino3d.Util
import compute_rhino3d.Grasshopper as gh
import rhino3dm
import json

compute_rhino3d.Util.url = 'http://35.157.191.153/'

# create DataTree for each input
input_trees = []
tree = gh.DataTree("Radius")
tree.Append([0], ["12.0"])
input_trees.append(tree)

tree = gh.DataTree("Count")
tree.Append([0], ["12.0"])
input_trees.append(tree)

output = gh.EvaluateDefinition('W:\\IAAC\\datamgmt\\repos\\bimsc21-datamgmt-session03\\example2\\rnd_node.gh', input_trees)
errors = output['errors']
if errors:
    print('ERRORS')
    for error in errors:
        print(error)
warnings = output['warnings']
if warnings:
    print('WARNINGS')
    for warning in warnings:
        print(warning)

values = output['values']
for value in values:
    name = value['ParamName']
    inner_tree = value['InnerTree']
    print(name)
    for path in inner_tree:
        print(path)
        values_at_path = inner_tree[path]
        for value_at_path in values_at_path:
            data = value_at_path['data']
            if isinstance(data, str) and 'archive3dm' in data:
                obj = rhino3dm.CommonObject.Decode(json.loads(data))
                print(obj)
            else:
                print(data)
