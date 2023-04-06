from yaml import load, SafeLoader
f = open("test.yml")
yml = load(stream=f, Loader=SafeLoader)
print(yml)


def find(d, tag):
    if tag in d:
        yield d[tag]
    for k, v in d.items():
        if isinstance(v, dict):
            for i in find(v, tag):
                yield i



for val in find(yml, 'tag_cl'):
    print(val)


