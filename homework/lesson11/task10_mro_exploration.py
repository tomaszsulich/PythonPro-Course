class A:
    ...

class B(A):
    ...

class C(A):
    ...

class D(B):
    ...

class E(C):
    ...

class F(D, E):
    pass


def main()-> None:
    print("Moja przewidywana kolejność MRO dla klasy F:")
    print("F -> D -> E -> B -> C -> A -> object")
    
    print("\nRzeczywista kolejność MRO według Pythona:")
    print(F.mro())
    
    # Początkowo można błędnie założyć, że po D Python przejdzie od razu do E.
    # W rzeczywistości MRO zachowuje kolejność wynikającą z dziedziczenia klas bazowych,
    # dlatego B pojawia się przed E.
    

if __name__ == "__main__":
    main()