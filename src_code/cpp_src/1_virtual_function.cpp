#include <stdio.h>
#include <iostream>

using std::cout;
using std::endl;

class Ex2
{
	int var1;

public:
		virtual int sum(int x, int y){
			return x+y;
		}

		virtual void reset_values(){
			var1 = 0;
		}
};

int main(int argc, char ** argv, char **envp) {
	Ex2 *e = new Ex2();
	e->sum(1,2);
	e->reset_values();
	delete(e);
}
