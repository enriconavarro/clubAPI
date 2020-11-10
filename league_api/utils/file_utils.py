def _write_file(filename, json_string):
    with open(filename, 'w') as tfile:
        tfile.write(json_string)

def write_export(exports):
    for export in exports:
        # export[0] = file name
        # export[1] = json_string
        _write_file(export[0], export[1])