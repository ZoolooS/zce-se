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

MSG = {
    'ERR_FILE': 'Something wrong with file {filename}.',
    'ERR_XML': 'Invalid XML format in {filename}.',
    'ERR_PATH': 'Can\'t write to {filename}. Check path.',
    'ERR_UNKNOWN': 'Something went wrong.',
    'GOOD': 'You can check result'
}

def get_mods_data(filename):
    try:
        tree = etree.parse(filename)
    except IOError:
        print(MSG['ERR_FILE'].format(filename=filename))
    except etree.XMLSyntaxError:
        print(MSG['ERR_XML'].format(filename=filename))
    except Exception:
        print(MSG['ERR_UNKNOWN'])

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
        print(MSG['ERR_PATH'].format(filename=filename))
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

    print(MSG['GOOD'])


if __name__ == '__main__':
    main()
