import xml.etree.ElementTree as Et


class Parsexml(object):
    """用来解析xml文件，并返回解析数据"""

    def __init__(self, xml_file):
        self.__information = {}
        self.__module_list = []
        self.__xml_file = xml_file
        self.__root = None

    def __get_root_node(self, xml_file):
        """设置根节点对象"""
        tree = Et.parse(xml_file)
        root_node = tree.getroot()
        self.__root = root_node

    def parse(self):
        """遍历解析root节点对象"""

        self.__get_root_node(self.__xml_file)

        for child in self.__root:
            print(child.tag, child.text)
            if child.tag != 'moduleList':
                self.__information.update({child.tag: child.text})
            else:
                for sub_child in child:
                    for son in sub_child:
                        tmp_dic = {}
                        if son.tag != 'subMoList':
                            tmp_dic.update({son.tag: son.text})
                        else:
                            for sub in son:


def main():
    xml_path = './upgrade.xml'
    xml = Parsexml(xml_path)
    xml.parse()

if __name__ == '__main__':
    main()



