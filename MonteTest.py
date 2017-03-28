from itertools import permutations as perm
from collections import Counter
#List = ['A','B','C','D','E','F','G','H','I']
#List2 = ['B','C','D','F','G','H']
KL = ['A','B','C','D','E','F']
def Monte(ListOfItems, XMoves,OMoves):
    global XRoutes
    global ORoutes
    XRoutes = []
    ORoutes = []
    ListTypes = []
    for i in ListOfItems:
        exec('%s = []' % i)
        
    L = list(perm(ListOfItems))
    for i in L:
        X = []
        O = []
        Count = 0
        CountMoves = 0
        for x in i:
            CountMoves+=1
            if Count == 0:
                Count = 1
                X.append(x)
                Checked = Check(XMoves+X)
                if Checked == True:
                    XRoutes.append(X[0])
                    exec('%s.append("W")' % X[0])
                    if CountMoves == 1:
                        for i in range(40): XRoutes.append(str(X[0]))
                    break
                
                elif Checked == 'Tie':
                    exec('%s.append("T")' % X[0])
            else:
                Count = 0
                O.append(x)
                if Check(OMoves+O):
                    ORoutes.append(O[0])
                    exec('%s.append("L")' % O[0])
                    break
                elif Checked == 'Tie':
                    exec('%s.append("T")' % X[0])

    print(len(XRoutes))
    print(len(ORoutes))
    global XCounts
    global OCounts
    xSet = set(XRoutes)
    oSet = set(ORoutes)
    #print(xSet)
    x = []
    o = []
    for i in xSet:
        x.append(i)
    for i in oSet:
        o.append(i)
    x.sort()
    o.sort()
    XMaxChar = ''
    XMaxCount = 0
    OMaxChar = ''
    OMaxCount = 0
    ListXScore = []
    ListOScore = []
    HighScore = 0
    HighScoreChar = ''
    ActiveScore = 0
    PassThrough = False
    print('********X*******')
    for i in x:
        #exec('print(%s)'% i)
        exec('ListXScore.append(%s)'% i)
    for i in o:
        exec('ListOScore.append(%s)' % i)
    for i,y in zip(ListOScore, o):
        #print(i)
        
        
        """try:
            ActiveScore = i.count('W')-(i.count('L'))
        except:
            if i.count('L') == 0:
                print('@@@@@@@@@@@@ L+T = 0')
                PassThrough = True
        if ActiveScore > HighScore or PassThrough:
            HighScore = 0
            HighScore += ActiveScore
            HighScoreChar = y
            print('#####'+str(HighScore))
        if i.count('L') == 0 and i.count('W') > 0:
            HighScoreChar = y
            break"""
        if i.count('L')+i.count('T') == 0:
            HighScoreChar = y
            PassThrough = True
            print('^^^^^^^^^^^^^^^^^^^^')
            print(y)
            print(i)
            print('^^^^^^^^^^^^^^^^^^^^')
            break
    print(str(HighScoreChar)+': '+str(HighScore))
            
    print('X')
    for i in x:
        if XRoutes.count(i) > XMaxCount:
            XMaxCount = XRoutes.count(i)
            XMaxChar = ''
            XMaxChar += i
            
        print(str(i)+': '+str(XRoutes.count(i)))
        """if str(i)+'W' in x:
            XMaxChar = i
            print('Found One-Move Win!')
            break"""
    print('\n'+str(XMaxChar)+': '+str(XMaxCount)+'\n')
    print('O')
    OMaxCount = 0
    for i in o:
        if ORoutes.count(i) > OMaxCount:
            OMaxCount = ORoutes.count(i)
            OMaxChar = ''
            OMaxChar += i
        print(str(i)+': '+str(ORoutes.count(i)))
    print('\n'+str(OMaxChar)+': '+str(OMaxCount)+'\n')
    if PassThrough:
        return HighScoreChar #XMaxChar
    else:
        return XMaxChar
        
"ABC, ADG, AEI, BEH, CEG, CFI, DEF, GHI"
def Check(List):
    if 'A' in List and 'B' in List and 'C' in List: return True
    if 'A' in List and 'D' in List and 'G' in List: return True
    if 'A' in List and 'E' in List and 'I' in List: return True
    if 'B' in List and 'E' in List and 'H' in List: return True
    if 'C' in List and 'E' in List and 'G' in List: return True
    if 'C' in List and 'F' in List and 'I' in List: return True
    if 'D' in List and 'E' in List and 'F' in List: return True
    if 'G' in List and 'H' in List and 'I' in List: return True
    elif len(List) == 5:
        return 'Tie'
    else: return False
#Monte(List)
#Monte(KL)
