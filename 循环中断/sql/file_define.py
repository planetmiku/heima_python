from data_define import Record
class FileReader():
    def read_data(self):
        """"读取数据"""
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_data(self) -> list[Record] :
        with open(self.path,'r',encoding='utf-8') as f:
            record_list: list[Record] = []
            for line in f.readlines():
                 data_list = line.strip().split(',')
                 record = Record(data_list[0],data_list[1],data_list[2],data_list[3])
                 record_list.append(record)
            return record_list

if __name__ == '__main__':
    path = 'txt数据.txt'
    text_file_reader = TextFileReader(path)
    text_file_reader.read_data()
