#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC; // Note: 0x21DD09EC == 568134124
unsigned long check_password(const char* p){ // Note: char == 1 byte
	int* ip = (int*)p; // Note: int == 4 bytes
	int i;
	int res=0;
	for(i=0; i<5; i++){ // Note: reads 4 * 5 == 20 bytes == 20 chars.
		res += ip[i];
	}
	return res;
}

int main(int argc, char* argv[]){
	if(argc<2){
		printf("usage : %s [passcode]\n", argv[0]);
		return 0;
	}
	if(strlen(argv[1]) != 20){
		printf("passcode length should be 20 bytes\n");
		return 0;
	}

	if(hashcode == check_password( argv[1] )){
		system("/bin/cat flag");
		return 0;
	}
	else
		printf("wrong passcode.\n");
	return 0;
}
	