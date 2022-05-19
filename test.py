import unittest, most_active_cookie

class MyTest(unittest.TestCase):
#TESTING getCookies()
    def test_getCookies_Empty(self):#empty array passed in
        self.assertEqual(most_active_cookie.getCookies([]),[]) 
        
        
#TESTING getCookies()
    def test_getCookies_Empty(self):#empty array passed in
        self.assertEqual(most_active_cookie.getCookies([]),[]) 
        
    def test_getCookies_NoTuples(self):#only heading passed in, no tuples in csv file
        self.assertEqual(most_active_cookie.getCookies(['cookie,timestamp']),[]) 
    
    def test_getCookies_Normal(self):#Normal Flow
        self.assertEqual(most_active_cookie.getCookies([]),[]) 
    
 #TESTING checkDate()
    def test_checkDate_empty(self):
        self.assertTrue(most_active_cookie.checkDate('', ''))
        
    def test_checkDate_False(self):
        self.assertFalse(most_active_cookie.checkDate('AtY0laUfhglK3lC7,2018-12-08T14:19:00+00:00', '2009-12-08'))
    
    def test_checkDate_False2(self):
        self.assertFalse(most_active_cookie.checkDate('4AtY0laUfhglK3lC7,2020-12-08T14:19:00+00:00', '2022-12-08'))
    
    def test_checkDate_False3(self):
        self.assertFalse(most_active_cookie.checkDate('afAtY0laUfhglK3lC7,2009-10-09T14:19:00+00:00', '2023-10-09'))
        
    def test_checkDate_True(self):
        self.assertTrue(most_active_cookie.checkDate('4567AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00', '2018-12-09'))
        
         
    def test_checkDate_True2(self):
        self.assertTrue(most_active_cookie.checkDate('SEDLFJ4567AtY0laUfhglK3lC7,2022-10-09T14:19:00+00:00', '2022-10-09'))
    
         
    def test_checkDate_True3(self):
        self.assertTrue(most_active_cookie.checkDate('asdf44567AtY0laUfhglK3lC7,2017-12-09T14:19:00+00:00', '2017-12-09'))
         
    def test_checkDate_True4(self):
        self.assertTrue(most_active_cookie.checkDate('4zvxcz567AtY0lagbUfhglK3lC7,2018-12-09T14:19:00+00:00', '2018-12-09'))
        
    def test_checkDate_Long(self):
        self.assertTrue(most_active_cookie.checkDate('joasdf98fasdhdsfkjh4r94uiahfdaso9874h9f8hsfihfihua9084fasfkjdha9f4 nh9awf49aw8yf9asfhas9fhf9saf94r98d4t45,2018-12-09T14:19:00+00:00', '2018-12-09'))
        
    def test_checkDate_OnlyDate(self):
        self.assertFalse(most_active_cookie.checkDate('2018-12-09', '2018-12-09')) #Should be False, no cookie given
        
#TESTING mostActive()
    def test_mostActive_Empty(self):#empty array passed in
        self.assertEqual(most_active_cookie.mostActive([]),set()) 
        
    def test_mostActive_OneValue(self):#Only One most frequent
        self.assertEqual(most_active_cookie.mostActive(['aaa']), {'aaa'})
    
    def test_mostActive_OneMostActive(self):#Only One most frequent
        self.assertEqual(most_active_cookie.mostActive(['aaa', 'bbb', 'aaa']), {'aaa'})  
        
    def test_mostActive_MultipleMostActive(self):#Multiple cookies have max_freq
        self.assertEqual(most_active_cookie.mostActive(['aaa', 'bbb', 'aaa', 'bbb', 'ccc']), {'aaa', 'bbb'})  
    
    def test_mostActive_Normal(self):
        self.assertEqual(most_active_cookie.mostActive(['9ASsdfa908h567[4t', '9ASsdfa908h567[4t', 'jafs9u80434af']), {'9ASsdfa908h567[4t'})  
        
    def test_mostActive_Large(self):#cookies not just alphanumerical, large number of values 
        self.assertEqual(most_active_cookie.mostActive(['OIHF*nas9dfn43rf', 'ahsd9f7ah4fasdfasf', 'jhas9fp8h4p', 'JP()F*of4'
                                                        ,'jasodifSDF(*', 'J)(*ojiF(*)E', 'J)(F*EJS)(*F', 'joid(*FDLKSDNF'
                                                        ,'JSDO)FoijdsfSDF*()LSJDFOSIDJF*90folSJDF0', 
                                                        'OIHF*nas9dfn43rf', 'ahsd9f7ah4fasdfasf', 'jhas9fp8h4p', 'JP()F*of4'
                                                        ,'jasodifSDF(*', 'J)(*ojiF(*)E', 'J)(F*EJS)(*F', 'joid(*FDLKSDNF'
                                                        ,'JSDO)FoijdsfSDF*()LSJDFOSIDJF*90folSJDF0',
                                                        'OIHF*nas9dfn43rf', 'ahsd9f7ah4fasdfasf', 'jhas9fp8h4p', 'JP()F*of4'
                                                        ,'jasodifSDF(*', 'J)(*ojiF(*)E', 'J)(F*EJS)(*F', 'joid(*FDLKSDNF'
                                                        ,'JSDO)FoijdsfSDF*()LSJDFOSIDJF*90folSJDF0',
                                                        'OIHF*nas9dfn43rf', 'ahsd9f7ah4fasdfasf', 'jhas9fp8h4p', 'JP()F*of4'
                                                        ,'jasodifSDF(*', 'J)(*ojiF(*)E', 'J)(F*EJS)(*F', 'joid(*FDLKSDNF'
                                                        ,'JSDO)FoijdsfSDF*()LSJDFOSIDJF*90folSJDF0',
                                                        'OIHF*nas9dfn43rf', 'ahsd9f7ah4fasdfasf', 'jhas9fp8h4p', 'JP()F*of4'
                                                        ,'jasodifSDF(*', 'J)(*ojiF(*)E', 'J)(F*EJS)(*F', 'joid(*FDLKSDNF'
                                                        ,'JSDO)FoijdsfSDF*()LSJDFOSIDJF*90folSJDF0','sdjfhS(DHFSPf', 'OSDFJH908d',
                                                        'SJODFIJS89hsef']), 
                         
                                                        {'OIHF*nas9dfn43rf', 'ahsd9f7ah4fasdfasf', 'jhas9fp8h4p', 'JP()F*of4'
                                                        ,'jasodifSDF(*', 'J)(*ojiF(*)E', 'J)(F*EJS)(*F', 'joid(*FDLKSDNF'
                                                        ,'JSDO)FoijdsfSDF*()LSJDFOSIDJF*90folSJDF0'})  
        
        
        
                   
if __name__ == '__main__':
    unittest.main()