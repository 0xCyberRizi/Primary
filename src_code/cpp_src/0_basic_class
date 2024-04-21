#include <stdio.h>
#include <iostream>

using std::cout;
using std::endl;

class ZooAnimal
{
	int cageNumber;

public:
	int ageInYears = 2;
	int weightInKg = 100;

	ZooAnimal() {
		cageNumber = 1;
		cout << "ZooAnimal Constructor" << endl;
	}
	int getCageNumber() {
		return cageNumber;
	}
};

int main(int argc, char ** argv, char **envp) {
	
	int result = 0;
	ZooAnimal *lion = new ZooAnimal();
	result = lion->getCageNumber();
	lion->ageInYears = 5; // Lions can live up to 15 years in the wild
	lion->weightInKg = 200; // Lions can weigh up to 250 kg
	delete(lion);
    
    return 0;
}
