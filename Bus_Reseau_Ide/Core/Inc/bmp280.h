/*
 * bmp280.h
 *
 *  Created on: Oct 19, 2022
 *      Author: arthurpellegrin
 */
#include "main.h"
#include "i2c.h"
#include "usart.h"

#ifndef SRC_BMP280_H_
#define SRC_BMP280_H_

#endif /* SRC_BMP280_H_ */

#define BMP_280_ADDR 0x77 << 1
#define BMP_280_REGISTER_ID 0xD0
#define BMP_280_Init_Value 0x58

int init_bmp280(void);
