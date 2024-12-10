class PageNotFoundError(Exception):
    pass


class ManualUpdate():
    def __init__(self, update_str: str):
        split_str = update_str.split(',')
        self.pages = [int(page) for page in split_str]
    
    def middlePageNum(self):
        return self.pages[len(self.pages) // 2]
    
    def pageIndex(self, page_num: int):
        try:
            return self.pages.index(page_num)
        except ValueError:
            raise PageNotFoundError()


class Rule():
    def __init__(self, rule_str: str):
        split_str = rule_str.split('|')
        self.prior = int(split_str[0])
        self.post = int(split_str[1])
    

class RuleSet():
    def __init__(self, rules_str_arr: list[str]):
        self.rules = []
        for rule in rules_str_arr:
            self.rules.append(Rule(rule))
        self.orderRules()
    
    def orderRules(self):
        self.rules.sort(key=lambda x: (x.prior, x.post))
    
    def testUpdate(self, update: ManualUpdate):
        for rule in self.rules:
            try:
                if update.pageIndex(rule.prior) > update.pageIndex(rule.post):
                    return False
            except PageNotFoundError:
                pass
        return True
    
    def fixUpdate(self, update: ManualUpdate):
        for rule in self.rules:
            try:
                priorIdx = update.pageIndex(rule.prior)
                postIdx = update.pageIndex(rule.post)
                if priorIdx > postIdx:
                    update.pages[priorIdx] = rule.post
                    update.pages[postIdx] = rule.prior
            except PageNotFoundError:
                pass
        return update

