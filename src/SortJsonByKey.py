import json
from sortedcontainers import SortedDict


def main():

    data_file = open('../resources/input.json')

    json_str = data_file.read()

    json_data = json.loads(json_str)

    sorted_json_data = sort_json_by_key(json_data)

    output_file = open('../resources/out.json', 'w')

    output_file.write(json.dumps(sorted_json_data, indent=2))

    output_file.close()

    print json.dumps(sorted_json_data, indent=2)
    print '\nDone!'


def sort_json_by_key(obj):
    """
    Iterate over all attributes to identify dictionary types and sort their attributes
    :param obj: Dictionary Object
    :return: Sorted Dictionary by Key
    """
    if type(obj) is dict:
        for a in obj.keys():
            if type(obj[a]) is dict:
                obj[a] = sort_json_by_key(obj[a])
            elif type(obj[a]) is list:
                for i in range(len(obj[a])):
                    if type(obj[a][i]) is dict:
                        obj[a][i] = sort_json_by_key(obj[a][i])
        return SortedDict(obj)
    elif type(obj) is list:
        for i in range(len(obj)):
            if type(obj[i]) is dict:
                obj[i] = sort_json_by_key(obj[i])
        return obj


if __name__ == "__main__":
    main()
