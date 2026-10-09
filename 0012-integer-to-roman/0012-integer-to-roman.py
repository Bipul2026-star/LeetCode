class Solution:
    def intToRoman(self, num: int) -> str:
        thousand=["","M","MM","MMM"]
        hundred=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        ten=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        one=["","I","II","III","IV","V","VI","VII","VIII","IX"]

        th_digit=num//1000
        h_digit=(num%1000)//100
        t_digit=(num%100)//10
        o_digit=(num%10)

        return thousand[th_digit]+hundred[h_digit]+ten[t_digit]+one[o_digit]