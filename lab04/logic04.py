class Family:
    def __init__(self, member_names, member_heights):
        self.members = member_names
        self.heights = member_heights
    
    def get_member_height(self, member_name):
        # Ищем соответствующую высоту члена семьи
        index = self.members.index(member_name)
        height = self.heights[index]
        return height
    
    def get_total_height(self):
        # Суммируем все значения в списке heights
        total_height = sum(self.heights)
        return total_height
