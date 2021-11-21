def to_camel_case(s):
    if s.find("-") < 0:
        return s
    temp = s.split("-")
    res = temp[0] + "".join(ele.title() for ele in temp[1:])
    return res


def process(data):

    if isinstance(data, dict):
        # return  {(to_camel_case(k), process(v)) for (k,v) in data.items()}
        data2 = {}
        for k in data.keys():
            data2[to_camel_case(k)] = process(data[k])
        return data2
    elif isinstance(data, list):
        return [process(e) for e in data]
    else:
        return data
