class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ana_map={}
        for s in strs:
            sorted_key="".join(sorted(s))
            ana_map[sorted_key]=ana_map.get(sorted_key,[])+[s]
        return list(ana_map.values())       