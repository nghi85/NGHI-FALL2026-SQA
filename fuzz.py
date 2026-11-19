import parser
import graphtaint

# bad inputs used for fuzzing
bad_inputs = [None, 0, -1, 3.14, "", "abc", "github/workflows/", [], [[]], {}, {"a": None}, (1, 2), True]


def getValuesRecursively(x):
    # getValuesRecursively is a generator, so list() is needed to run it
    return list(parser.getValuesRecursively(x))


def fuzz(method, *args):
    try:
        method(*args)
    except Exception as error:
        message = method.__name__ + str(args) + " -> " + type(error).__name__ + ": " + str(error)
        print(message)
        report = open("fuzz_report.txt", "a")
        report.write(message + "\n")
        report.close()


if __name__ == '__main__':
    open("fuzz_report.txt", "w").close()

    for x in bad_inputs:
        fuzz(parser.checkIfWeirdYAML, x)                 # 1
        fuzz(parser.keyMiner, x, x)                      # 2
        fuzz(parser.getKeyRecursively, x, x)             # 3
        fuzz(getValuesRecursively, x)                    # 4
        fuzz(parser.getValsFromKey, x, x, x)             # 5
        fuzz(parser.checkIfValidHelm, x)                 # 6
        fuzz(parser.update_json_paths, x)                # 7
        fuzz(parser.getSingleDict4MultiDocs, x)          # 8
        fuzz(graphtaint.constructHelmString, x)          # 9
        fuzz(graphtaint.getValidTaints, x)               # 10

    print("Fuzzing done. See fuzz_report.txt")
