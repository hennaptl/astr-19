#here we create a class for the animal so we can describe it later
class Favorite_Animal:
	def __init__(self, name, arm_length, leg_length, num_eyes, has_tail, furry):
		self.name = name
		self.arm_length = arm_length
		self.leg_length = leg_length
		self.num_eyes = num_eyes
		self.has_tail = has_tail
		self.furry = furry
#now that we have the catagories we can tell python to print the answers
	def describe(self):
		print(f'Animal Name:{self.name}')
		print(f'Arm Length:{self.arm_length} ft')
		print(f'Leg Length: {self.leg_length} ft')
		print(f'Number of Eyes: {self.num_eyes}')
		print(f'Has Tail: {self.has_tail}')
		print(f'Furry: {self.furry}')

#here we answer the catagories with name, integer, floats, and bools (more convienent with lists of animals)
def main():
	giraffe = Favorite_Animal("Giraffe", 0.0, 6.0, 2, True, True)
	giraffe.describe()

#always close with this
if __name__ == "__main__":
	main()
