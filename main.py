from lxml import etree
from settings import (
    ROOT_NODE,
    ID_NODE_NAME,
    NAME_ATTR,
    SRC_FILES,
    PATH_IN,
    PATH_OUT,
    TARGET_SUFFIX,
    TARGET_EXT,
)


def get_mods_data(filename):
    try:
        tree = etree.parse(filename)
    except IOError:
        print(f'Something wrong with file {filename}.')
        return
    except etree.XMLSyntaxError:
        print(f'Invalid XML format in {filename}.')
        return

    root = tree.getroot()
    cur_root = root.find(ROOT_NODE)

    for el in cur_root:
        id_node = el.find(ID_NODE_NAME)
        yield f'-:|: {el.attrib[NAME_ATTR]} :|: {id_node.text}\n'


def put_to_txt(filename, payload, mode='w'):
    try:
        with open(filename, mode, encoding='utf-8') as f:
            f.write(payload)
    except FileNotFoundError:
        print(f"Can't write to {filename}. Check path.")
        raise


def main():
    for f in SRC_FILES:
        path_out = f'{PATH_OUT}/{f[:-4]}{TARGET_SUFFIX}{TARGET_EXT}'
        try:
            put_to_txt(path_out, '')
        except FileNotFoundError:
            return
        for line in get_mods_data(f'{PATH_IN}/{f}'):
            put_to_txt(path_out, line, 'a')

    print('You cat check result')


if __name__ == '__main__':
    main()
