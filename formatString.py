def getValues(formatStr, inpString):
    formatInd = 0
    stringInd = 0
    result = []
    paramType = 's'

    while(formatInd < len(formatStr) and formatInd >= 0):
        if(formatStr[formatInd] == '{'):
            newformatInd = formatStr.find('}', formatInd)
            paramType = formatStr[formatInd + 1:newformatInd]
            formatInd = newformatInd
        elif(formatStr[formatInd] == '}'):
            formatInd = formatInd + 1
        else:
            newformatInd = formatStr.find('{', formatInd)
            delem = formatStr[formatInd:newformatInd]
            newStrInd = inpString.find(delem, stringInd)
            if(newStrInd > stringInd):
                print str(stringInd) + " " + str(newStrInd) + " '" + delem + "'"
                result.append(processParam(paramType, inpString[stringInd:newStrInd]))
                stringInd = newStrInd + len(delem)
            formatInd = newformatInd

    result.append(processParam(paramType, inpString[stringInd:]))
    return result


def processParam(paramType, paramStr):
    if(paramType == 's'):
        return paramStr
    elif(paramType == 'd'):
        return int(paramStr)
    elif(paramType == 'f'):
        return float(paramStr)
    elif(paramType == 'd/m/y'):
        idx = 0
        nIdx = paramStr.find('/', idx)
        dd = int(paramStr[idx:nIdx])
        idx = nIdx + 1
        nIdx = paramStr.find('/', idx)
        mm = int(paramStr[idx:nIdx])
        yy = int(paramStr[nIdx + 1:])
        return [dd, mm, yy]
    elif(paramType == 'h:m'):
        idx = paramStr.find(':')
        hh = int(paramStr[0:idx])
        mm = int(paramStr[idx + 1:])
        return [hh, mm]
    else:
        return paramStr


res = getValues('{d} : : {d} : {d} : {f} : {s} : {d/m/y} , {h:m}', '1 : : 2 : 3 : 4.5 : 5,7 : 03/07/1997 , 12:10')
print res
