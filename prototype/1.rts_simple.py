# 星际争霸（RTS）
# 玩家控制一组游戏角色，修建建筑，生成作战单位
# 建模-类图：
# - 涉及定义一个Barracks类
# - 这个类有一个方法generate_knight
# - 她返回一个Knight对象
# Knight对象的基本属性
# - 生命
# - 速度
# - 攻击力
# - 攻击范围
# - 武器
class Knight(object):
    """ 士兵 """
    def __init__(self, life, speed, attack_power, attack_range, weapon):
        """
            士兵
        :param life: 生命值
        :param speed: 速度
        :param attack_power: 攻击力
        :param attack_range: 攻击范围
        :param weapon: 武器
        """
        self.unit_type = 'Knight'
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return f"Type: {self.unit_type}\n" \
            f"Life: {self.life}\n" \
            f"Speed: {self.speed}\n" \
            f"Attack Power: {self.attack_power}\n" \
            f"Attack Range: {self.attack_range}\n" \
            f"Weapon: {self.weapon}"


class Archer(object):
    """ 弓箭手 """
    def __init__(self, life, speed, attack_power, attack_range, weapon):
        self.unit_type = "Archer"
        self.life = life
        self.speed = speed
        self.attack_power = attack_power
        self.attack_range = attack_range
        self.weapon = weapon

    def __str__(self):
        return f"Type: {self.unit_type}\n" \
            f"Life: {self.life}\n" \
            f"Speed: {self.speed}\n" \
            f"Attack Power: {self.attack_power}\n" \
            f"Attack Range: {self.attack_range}\n" \
            f"Weapon: {self.weapon}"


class Barracks(object):
    """ 兵营 """
    def generate_knight(self):
        """ 制造士兵 """
        return Knight(400, 5, 3, 1, "短矛")

    def generate_archer(self):
        """ 制造弓箭手 """
        return Archer(200, 7, 1, 5, "短弓")


if __name__ == '__main__':
    barracks = Barracks()
    knight1 = barracks.generate_knight()
    archer1 = barracks.generate_archer()
    print(f"[knight1] {knight1}")
    print(f"[archer1] {archer1}")
