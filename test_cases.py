class TestCases:

    def test_cases():

        ts1= {
            'input':{
                'cards':[15, 13, 7,6,5,3,2,1],
                'query':5
            },
            'output': 4 
        }
        ts2= {
            'input':{
                'cards':[],
                'query':5
            },
            'output': -1 
        }
        ts3= {
            'input':{
                'cards':[15, 13, 7,6,5,5,5,5,5,5,2,1],
                'query':5
            },
            'output': 4 
        }

        ts4= {
            'input':{
                'cards':[20, 17, 15, 12, 9, 8, 7, 5, 1],
                'query':15
            },
            'output': 2 
        }

        ts5= {
            'input':{
                'cards':[20, 17, 15, 12, 9, 8, 7, 5, 1],
                'query':7
            },
            'output': 6 
        }

        large_testcase= {
            'input':{
                'cards':list(range(10000000,0,-1)),
                'query':2
            },
            'output': 9999998
        }
        
        tests = []
        
        tests.append(ts1)
        tests.append(ts2)
        tests.append(ts3)
        tests.append(ts4)
        tests.append(ts5)
        tests.append(large_testcase)

        return tests

    def first_last_postion_test_cases():

        ts1= {
            'input':{
                'cards':[1,1,1,1, 3,3,5,7,8,10],
                'query':1
            },
            'output': (0,3)
        }
        ts2= {
            'input':{
                'cards':[],
                'query':5
            },
            'output': (-1,-1)
        }
        ts3= {
            'input':{
                'cards':[15, 19, 20, 20, 20, 22, 22, 38],
                'query': 20
            },
            'output': (2,4)
        }

        ts4= {
            'input':{
                'cards':[20, 20, 21, 23, 29, 30, 30, 30, 1],
                'query':30
            },
            'output': (5,7)
        }

        ts5= {
            'input':{
                'cards':[20, 17, 15, 12, 9, 8, 7, 5, 1],
                'query':9
            },
            'output': (4,4)
        }

        tests = []
        
        tests.append(ts1)
        tests.append(ts2)
        tests.append(ts3)
        tests.append(ts4)
        tests.append(ts5)

        return tests

    def rotated_sorted_list_test_cases():

        ts1= {
            'input':{
                'num':[19,25,29,3,5,6,7,9,11,14],
            },
            'output': 3
        }
        ts2= {
            'input':{
                'num':[4,5,6,7,8,1,2,3],
            },
            'output': 5
        }
        ts3= {
            'input':{
                'num':[1,2,3,4,5,6,7,8],
            },
            'output': 0
        }
        

        tests = []
        
        tests.append(ts1)
        tests.append(ts2)
        tests.append(ts3)

        return tests