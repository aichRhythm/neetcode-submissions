class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        # temp = []
        # for i in range(len(strs)):            
        #     string = sorted(list(strs[i]))
        #     temp.append(string)
        # print(temp)
        # for j in range(len(temp)):
        #     tempout = []
        #     for k in range(len(temp)):
        #         if temp[j] == sorted(list(strs[k])):
        #             if strs[k] not in tempout:
        #                 tempout.append(strs[k])
        #     output.append(tempout)
        for string in strs:
            key = "".join(sorted(string))
            if key not in output:
                output[key] = []
            output[key].append(string)

        print(output)

        return list(output.values())