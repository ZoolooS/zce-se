ROOT_NODE = 'Mods'  # XML node where script find nods with mods info
NAME_ATTR = 'FriendlyName'  # XML attribute where name of mod is
ID_NODE_NAME = 'PublishedFileId'  # XML node where Steam ID is

PATH_IN = '_in'  # folder where script will look for sbc-files
PATH_OUT = '_out'  # folder where script will put modlist-files
SRC_FILES = (  # SE XML-files to search for
    'Sandbox_config.sbc',
    'Sandbox.sbc',
)
TARGET_SUFFIX = '_out'  # suffix for modlist-files
TARGET_EXT = '.txt'  # extension for modlist-files
