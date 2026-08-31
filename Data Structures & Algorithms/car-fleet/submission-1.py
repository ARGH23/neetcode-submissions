class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        cars = sorted(cars)


        fleets = 0

        while cars:
            x = True

            mfspeed = None
            mfpos = None

            while x:
                x = False
                last = cars.pop()

                if mfspeed == None:
                    mfspeed = last[1]
                    mfpos = last[0]

                if cars:
                    cl = cars[-1]

                    if cl[1] > mfspeed:
                        time = (mfpos - cl[0])/(cl[1] - mfspeed)

                        distance = time * mfspeed + mfpos

                        if distance <= target:
                            x = True
            
            fleets += 1
        
        return fleets
                



