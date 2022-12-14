


from abc import ABC, abstractmethod
class song(ABC):
    def recordProducer(self, prod):
        print("The song's producer is: ",prod)
    #creating my abstract method
    @abstractmethod
    def priceCategory(self, prod):
        pass

class SongStream(song):
    #Here is the same priceCategory function as the parent song class, but we now define it in the SongStream child:
    def priceCategory(self, prod):
        if prod == "Brandi Carlile":
            print("This Brandi Carlile record is priced at $25.00")
        else:
            print("This producer is not in our system")

#creating an object that uses both the parent and child methods     
obj = SongStream()
obj.recordProducer("Brandi Carlile")
obj.priceCategory("Brandi Carlile")
