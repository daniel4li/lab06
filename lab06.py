from Apartment import Apartment


def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2
        left = apartmentList[:mid]
        right = apartmentList[mid:]
        mergesort(left)
        mergesort(right)

        a = 0
        b= 0 
        c= 0 

        while a <len(left) and b < len(right):
            if left[a] < right[b] or left[a] == right[b] :
                apartmentList[c] = left[a]
                a = a + 1
            else:
                apartmentList[c] = right[b]
                b = b + 1
            c = c + 1
        while a < len(left):
            apartmentList[c] = left[a]
            a = a + 1
            c = c + 1
        while b < len(right):
            apartmentList[c] = right[b]
            b = b + 1
            c = c + 1

def ensureSortedAscending(apartmentList):
    for i in range(len(apartmentList) - 1):
        if apartmentList[i] > apartmentList[i + 1]:
            return False
    return True

def getTopThreeApartments(apartmentList):
    mergesort(apartmentList)
    apartmentList = apartmentList[0:3]

    m = ''
    for index, apartment in enumerate(apartmentList):
        m +=  apartment.getApartmentDetails()
        if index != len(apartmentList) - 1:
            m += "\n"
    return m

def getNthApartment(apartmentList, n):
    if n > len(apartmentList) - 1:
        return "(Apartment) DNE"
    return apartmentList[n].getApartmentDetails()

a0 = Apartment(1200, 200, "average")
a1 = Apartment(1200, 200, "excellent")
a2 = Apartment(1000, 100, "average")
a3 = Apartment(1000, 215, "excellent")
a4 = Apartment(700, 315, "bad")
a5 = Apartment(800, 250, "excellent")

apartmentList = [a0, a1, a2, a3, a4, a5]
print(getTopThreeApartments(apartmentList))