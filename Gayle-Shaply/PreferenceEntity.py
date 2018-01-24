class PreferenceEntity:
    def __init__(self, index, preference_list):
        self.index = index
        self.preference_list = preference_list
        self.is_matched = False
        self.matched_to = None

    def prefers(self, entities):
        for i in self.preference_list:
            if i in entities:
                return i
        return

    def match_to(self, entity):
        self.matched_to = entity
        self.is_matched = True

    def un_match(self):
        self.matched_to = None
        self.is_matched = False

    def __str__(self):
        return str(self.index) + ": " + str(self.preference_list)