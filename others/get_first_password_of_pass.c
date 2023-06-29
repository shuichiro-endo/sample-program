/*
 * Title:  get first password of pass (hackmyvm casino)
 * Author: Shuichiro Endo
 */

/*
undefined8 checkPasswd(char *param_1)

{
  size_t sVar1;
  undefined8 uVar2;
  
  sVar1 = strlen(param_1);
  if (sVar1 == 0x1a) {
    if ((int)*param_1 - (int)param_1[0x14] == -10) {
      if ((int)param_1[6] + (int)param_1[1] == 0xd0) {
        if ((int)param_1[2] - (int)param_1[4] == 10) {
          if ((int)param_1[3] - (int)param_1[0xe] == -2) {
            if ((int)param_1[0x19] * (int)param_1[4] == 0x2774) {
              if ((int)param_1[0x11] + (int)param_1[5] == 0xdb) {
                if ((int)param_1[6] - (int)param_1[10] == -0xb) {
                  if ((int)param_1[7] - (int)param_1[0x14] == -10) {
                    if ((int)param_1[0x11] * (int)param_1[8] == 0x2e45) {
                      if ((int)param_1[9] - (int)param_1[0x12] == -7) {
                        if ((int)param_1[10] - (int)param_1[0x18] == 1) {
                          if ((int)param_1[4] * (int)param_1[0xb] == 0x2645) {
                            if ((int)param_1[0xc] - (int)param_1[3] == 3) {
                              if ((int)param_1[0xb] * (int)param_1[0xd] == 0x2bf4) {
                                if ((int)param_1[0xe] - (int)param_1[0xd] == -2) {
                                  if (param_1[0xf] == param_1[0x17]) {
                                    if ((int)param_1[0x10] - (int)param_1[8] == -5) {
                                      if ((int)param_1[7] * (int)param_1[0x11] == 0x2a3f) {
                                        if ((int)param_1[0x12] - (int)param_1[0xe] == -2) {
                                          if ((int)param_1[0x13] - (int)*param_1 == -8) {
                                            if ((int)param_1[0x14] - (int)param_1[0x17] == 4) {
                                              if ((int)param_1[7] + (int)param_1[0x15] == 0xdc) {
                                                if ((int)param_1[0x16] - (int)param_1[1] == 0xf) {
                                                  if (param_1[0x17] == param_1[0xf]) {
                                                    if ((int)param_1[2] * (int)param_1[0x18] == 0x316e) {
                                                      if ((int)param_1[0x19] - (int)param_1[0xc] == -0xf) {
                                                        puts("Correct pass");
                                                        uVar2 = 1;
                                                      }
                                                      
                                                      ...
 */


#include <stdio.h>

int main()
{
	
	char password[0x1a + 1] = {0};
	int check = 0;
	
	for(char i=0x20; i<0x7e; i++){
		password[0] = i;
		
		password[0x13] = -8 + (int)*password;
		password[0x14] = 10 + (int)*password;
		password[0x17] = -4 + (int)password[0x14];
		password[0xf] = password[0x17];
		password[7] = -10 + (int)password[0x14];
		password[0x15] = 0xdc - (int)password[7];
		
		if(0x2a3f % (int)password[7] != 0){
			continue;
		}
		password[0x11] = 0x2a3f / (int)password[7];
		
		password[5] = 0xdb - (int)password[0x11];
		
		if(0x2e45 % (int)password[0x11] != 0){
			continue;
		}
		password[8] = 0x2e45 / (int)password[0x11];
		
		password[0x10] = -5 + (int)password[8];
		
		for(int k=0; k<0x1a; k++){
			if(password[k]!=0x0 && (password[k]<0x20 || password[k]>0x7e)){
				check = 1;
				break;
			}
		}
		
		if(check == 1){
			check = 0;
			continue;
		}
		
		for(char j=0x20; j<0x7e; j++){
			password[1] = j;
			
			password[0x16] = 0xf + (int)password[1];
			password[6] = 0xd0 - (int)password[1];
			password[10] = 0xb + (int)password[6];
			password[0x18] = -1 + (int)password[10];
			
			if(0x316e % (int)password[0x18] != 0){
				continue;
			}
			password[2] = 0x316e / (int)password[0x18];
			
			password[4] = -10 + (int)password[2];
			
			if(0x2645 % (int)password[0x4] != 0){
				continue;
			}
			password[0xb] = 0x2645 / (int)password[4];
			
			if(0x2bf4 % (int)password[0xb] != 0){
				continue;
			}
			password[0xd] = 0x2bf4 / (int)password[0xb];
			
			password[0xe] = -2 + (int)password[0xd];
			password[0x12] = -2 + (int)password[0xe];
			password[9] = -7 + (int)password[0x12];
			
			if(0x2774 % (int)password[4] != 0){
				continue;
			}
			password[0x19] = 0x2774 / (int)password[4];
			
			password[0xc] = 0xf + (int)password[0x19];
			password[3] = -3 + (int)password[0xc];
			
			if((int)password[3] - (int)password[0xe] != -2){
				continue;
			}
			
			for(int k=0; k<0x1a; k++){
				if(password[k]!=0x0 && (password[k]<0x20 || password[k]>0x7e)){
					check = 1;
					break;
				}
			}
			
			if(check == 1){
				check = 0;
				continue;
			}else{
				printf("password:%s\n", password);
			}
		}
	}

	return 0;
}


