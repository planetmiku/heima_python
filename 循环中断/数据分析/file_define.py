from data_define import Record
import json
class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件的数据，读到的每一条数据都转换为Record对象，将他们封装到list内返回即可"""
        pass

class TextFileReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_data(self) -> list[Record]:
        with open(self.path,'r',encoding='UTF-8') as f:
            record_list: list[Record] = []
            for line in f.readlines():
                line = line.strip()
                data_list = line.split(',')
                record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
                record_list.append(record)
            return record_list

class JsonfileReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_data(self) -> list[Record]:
        with open(self.path,'r',encoding='UTF-8') as f:
            record_list: list[Record] = []
            data = json.loads(f.read())
            for data_dict in data:
                record = Record(str(data_dict["date"]),data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
                record_list.append(record)
            return record_list

if __name__=='__main__':
    text_file_reader = TextFileReader('1月.txt')
    json_file_reader = JsonfileReader('2月.json')
    text_file_reader.read_data()
