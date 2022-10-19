
#include "bmp280.h"


int init_bmp280() {
	uint8_t pData[1];
	pData[0] = BMP_280_REGISTER_ID;
	uint8_t res[10];
	HAL_I2C_Master_Transmit(&hi2c1, BMP_280_ADDR , pData , 1, HAL_MAX_DELAY);
	HAL_I2C_Master_Receive(&hi2c1, BMP_280_ADDR, res , 1, HAL_MAX_DELAY);

	if (res[0] == BMP_280_Init_Value){
		return 1;
	}
	else {
		return 0;
	}
}


int write_configuration(uint8_t register, ){
	}

