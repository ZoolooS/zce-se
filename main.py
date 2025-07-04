from lxml import etree
from pathlib import Path

from settings import (
    ROOT_NODE,
    ID_NODE_NAME,
    NAME_ATTR,
    SRC_FILES,
    PATH_IN,
    PATH_OUT,
    TARGET_SUFFIX,
    TARGET_EXT,
    MODLIST_LINE,  # have {mod_name}, {mod_id} vars
)


MSG = {
    'ERR_FILE': 'Something wrong with file {filename}.',
    'ERR_XML': 'Invalid XML format in {filename}.',
    'ERR_IN_PATH': 'Can\'t read from {filename}. Check path.',
    'ERR_OUT_PATH': 'Can\'t write to {filename}. Check path.',
    'ERR_UNKNOWN': 'Something went wrong.',
    'GOOD': 'You can check {filename}.',
    'END': 'All processes has ended.'
}


def get_mods_data(filename):
    try:
        tree = etree.parse(filename)
    except IOError:
        print(MSG['ERR_FILE'].format(filename=filename))
        return
    except (FileNotFoundError, UnboundLocalError):
        print(MSG['ERR_IN_PATH'].format(filename=filename))
        return
    except etree.XMLSyntaxError:
        print(MSG['ERR_XML'].format(filename=filename))
    except Exception:
        print(MSG['ERR_UNKNOWN'])

    root = tree.getroot()
    cur_root = root.find(ROOT_NODE)

    for el in cur_root:
        id_node = el.find(ID_NODE_NAME)
        yield MODLIST_LINE.format(mod_name=el.attrib[NAME_ATTR], mod_id=id_node.text)


def put_to_txt(filename, payload, mode='w'):
    try:
        with open(filename, mode, encoding='utf-8') as f:
            f.write(payload)
    except FileNotFoundError:
        print(MSG['ERR_OUT_PATH'].format(filename=filename))
        raise


def main():
    for f in SRC_FILES:
        if not Path(PATH_IN).is_dir():
            print(MSG['ERR_IN_PATH'].format(filename=PATH_IN))
            break

        curr_f_path_in = Path(PATH_IN, f)
        if not curr_f_path_in.is_file():
            print(MSG['ERR_IN_PATH'].format(filename=f))
            continue

        if not Path(PATH_OUT).is_dir():
            Path(PATH_OUT).mkdir()

        curr_f_path_out = Path(PATH_OUT, f[:-4] + TARGET_SUFFIX + TARGET_EXT)

        try:
            put_to_txt(curr_f_path_out, '')  # clear file if exists or create empty file
        except FileNotFoundError:
            return

        for line in get_mods_data(curr_f_path_in):
            put_to_txt(curr_f_path_out, line, mode='a')

        print(MSG['GOOD'].format(filename=curr_f_path_out))

    print(MSG['END'])


if __name__ == '__main__':
    main()
