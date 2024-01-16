class Phone:
    __is_5g_enable = False
    def __check_5g(self):
        if self.__is_5g_enable == True:
            print("5G开启")
        else:
            print("5g关闭,使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone =  Phone()
# phone.__keep_single_core()
phone.call_by_5g()