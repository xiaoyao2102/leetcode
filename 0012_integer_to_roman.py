class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        raw_1 = {
            0: '',
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
        }

        raw_10 = {
            0: '',
            1: 'X',
            2: 'XX',
            3: 'XXX',
            4: 'XL',
            5: 'L',
            6: 'LX',
            7: 'LXX',
            8: 'LXXX',
            9: 'XC'
        }

        raw_100 = {
            0: '',
            1: 'C',
            2: 'CC',
            3: 'CCC',
            4: 'CD',
            5: 'D',
            6: 'DC',
            7: 'DCC',
            8: 'DCCC',
            9: 'CM'
        }

        raw_1000 = {
            0: '',
            1: 'M',
            2: 'MM',
            3: 'MMM'
        }
        return raw_1000[num / 1000] + raw_100[num / 100 % 10] + raw_10[num / 10 % 10] + raw_1[num % 10]
