class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu * self.__memory

    def __str__(self):
        return f"Memory: {self.__memory}, Cpu: {self.__cpu}"


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f"Идет звонок на номер {call_to_number} "
              f"с сим-карты-{sim_card_number} - {self.__sim_cards_list[sim_card_number]}")

    def __str__(self):
        return f"Sim cards list: {self.__sim_cards_list}"


class Smartphone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        self.sim_cards_list = sim_cards_list

    def use_gps(self, location):
        print(f"Маршрут до локации {location} был построен")

    def __str__(self):
        return super().__str__() + f", Sim cards list: {self.sim_cards_list}"


computer = Computer(5, 512)
phone = Phone(sim_cards_list=["Beeline", "Megacom"])
smartphone1 = Smartphone(3, 64, sim_cards_list=["O!", "Beeline"])
smartphone2 = Smartphone(6, 128, sim_cards_list=["Megacom", "O!"])
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

smartphone1.use_gps("Tsum")
print(smartphone2.make_computations())
smartphone1.call(0, "+996 505 05 05 55")
phone.call(1, "+996 707 06 32 56")
print(f"computer has a larger memory than smartphone1: {computer > smartphone1}")
print(f"computer has a smaller memory than smartphone1: {computer < smartphone1}")
print(f"computer and smartphone2 have the same volume of memory: {computer == smartphone2}")
print(f"computer`s memory is not equal to smartphone2`s: {computer != smartphone2}")
print(f"computer >= smartphone2: {computer >= smartphone2}")
print(f"computer <= smartphone2: {computer <= smartphone2}")
