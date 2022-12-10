# 当我们控制的角色，有等级切换时，按照之前的设计，兵工厂制造角色的方法就会成倍增加。
# 进一步封装

class Knight(object):
    def __init__(self, level):
        """
            士兵
        :param level: 等级
        """
        self.unit_type = "Knight"
        if level == 1:
            self.life = 400
            self.speed = 5
            self.attack_power = 3
            self.attack_range = 1
            self.weapon = "短矛"
        elif level == 2:
            self.life = 400
            self.speed = 5
            self.attack_power = 6
            self.attack_range = 2
            self.weapon = "长矛"

    def __str__(self):
        return f"Type: {self.unit_type}\n" \
            f"Life: {self.life}\n" \
            f"Speed: {self.speed}\n" \
            f"Attack Power: {self.attack_power}\n" \
            f"Attack Range: {self.attack_range}\n" \
            f"Weapon: {self.weapon}"


class Archer(object):
    def __init__(self, level):
        self.unit_type = "Archer"
        if level == 1:
            self.life = 200
            self.speed = 7
            self.attack_power = 1
            self.attack_range = 5
            self.weapon = "短弓"
        elif level == 2:
            self.life = 200
            self.speed = 7
            self.attack_power = 3
            self.attack_range = 10
            self.weapon = "长弓"

    def __str__(self):
        return f"Type: {self.unit_type}\n" \
            f"Life: {self.life}\n" \
            f"Speed: {self.speed}\n" \
            f"Attack Power: {self.attack_power}\n" \
            f"Attack Range: {self.attack_range}\n" \
            f"Weapon: {self.weapon}"


class Barracks(object):
    def build_unit(self, unit_type, level):
        if unit_type == "Knight":
            return Knight(level)
        elif unit_type == "Archer":
            return Archer(level)


if __name__ == '__main__':
    barracks = Barracks()
    knight1 = barracks.build_unit("Knight", 1)
    archer1 = barracks.build_unit("Archer", 2)
    print(f"[knight1] {knight1}")
    print(f"[archer1] {archer1}")
