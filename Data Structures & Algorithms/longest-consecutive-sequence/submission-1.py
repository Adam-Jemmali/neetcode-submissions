class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set((nums))
        maxlength=0

        for num in sett:
            #what is the FIRST START OF SEQUENCE
            #ex if num = 2 and num-1 =1 not in set THUS 2 SEQUENCESTART
            if (num-1) not in sett:
                current=num
                currentlen=1
                while(current+1 )  in sett:
                    current=current+1

                    ## find the longest sequence after add +1 to num
                    currentlen +=1
                   
                maxlength=max(maxlength,currentlen)
        return maxlength
                



    
        