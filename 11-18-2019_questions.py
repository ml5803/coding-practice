# First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = dict()
        for elem in s:
            if seen.get(elem):
                seen[elem] += 1
            else:
                seen[elem] = 1

        uniques = set()
        for item in seen.keys():
            if seen[item] == 1:
                uniques.add(item)

        for ind, elem in enumerate(s):
            if elem in uniques:
                return ind

        return -1

#Most Common Word
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuation = set([char for char in "'!@#$%^&*()_+<>?:.,;"])

        cleaned = paragraph.lower()
        for elem in cleaned:
            if elem in punctuation:
                cleaned = cleaned.replace(elem, " ")
        print(cleaned)
        cleaned = cleaned.split(" ")
        banned_set = set(banned)
        banned_set.add("")

        words = {}
        for word in cleaned:
            if word not in banned_set:
                if words.get(word):
                    words[word] += 1
                else:
                    words[word] = 1
        print(words)

        max_occ = 0
        to_return = ""
        for word in words:
            if max_occ < words[word]:
                to_return = word
                max_occ = words[word]

        print(max_occ, to_return)
        return to_return

#longest substring w/ no repeats
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        curr = set()
        start, end = 0 , 0
        while start < len(s) and end < len(s):
            if s[end] not in curr:
                curr.add(s[end])
                end += 1
                ans = max(ans, end - start)
            else:
                curr.remove(s[start])
                start += 1

        return ans

#two sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #map each integer to an ind
        lookup = {}
        for ind, elem in enumerate(nums):
            if elem in lookup:
                lookup[elem].append(ind)
            else:
                lookup[elem] = [ind]

        #if we can find the target in our map and the ind isn't matching, it is a possible solution.
        #told that we had to have at least 1 solution.
        for ind,elem in enumerate(nums):
            to_look = target - elem
            if to_look in lookup:
                for item in lookup[to_look]:
                    if item == ind:
                        continue
                    else:
                        return [ind,item]

#group anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            string = "".join(sorted(s))
            if string in groups:
                groups[string].append(s)
            else:
                groups[string] = [s]

        return [groups[key] for key in groups.keys()]
