from lab06 import *
from Apartment import Apartment

def test_mergeSort():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")

    apartmentList = [a0, a1, a2, a3, a4, a5]
    length = len(apartmentList)
    assert (getNthApartment(apartmentList, 0)) == "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"
    assert (getNthApartment(apartmentList, length-1)) == "(Apartment) Rent: $800, Distance From UCSB: 250m, Condition: excellent"
    mergesort(apartmentList)
    assert (getNthApartment(apartmentList, 0)) == "(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad"
    assert (getNthApartment(apartmentList, length-1)) == "(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average"

    
     
"""def test_topThree():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")

    apartmentList = [a0, a1, a2, a3, a4, a5]"""
  