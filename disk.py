class Disk:
    def __init__(self, total, used):
        self.__total = total
        self.__used = used
    
    def free(self):
        access_free = self.__total - self.__used
        return access_free
    
    def __repr__(self) -> str:
        result = f"Disk[total: {self.__total} GB, used: {self.__used} Gb]"
        return result
    
    def used_perc(self):
        percent = self.__used / self.__total
        return percent
    
    def __lt__(self, other):
        tri = self.used_perc() < other.used_perc()
        return tri

if __name__ == '__main__':
    disk = Disk(10,2)
    print(disk)
    
    
    disk1 = Disk(total = 10, used = 2)
    disk2 = Disk(total = 20, used = 5)
    disk3 = Disk(total = 15, used = 1)
    print(disk1.free()) # 8
    print(disk2.free()) # 15
    print(disk3.free()) 
    print(disk1.used_perc()) # 0.2
    print(disk2.used_perc()) # 0.25
    print(disk3.used_perc())
    disks = [disk1, disk2, disk3]
    disks_sorted = sorted(disks) # trié selon le pourcentage d'espace utilisé
    print(disks_sorted)
