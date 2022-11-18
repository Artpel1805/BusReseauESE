/*
 * BMP280.h
 *
 *  Created on: Oct 3, 2020
 *      Author: cbares
 */

#ifndef SRC_BMP280_SIMPLE_H_
#define SRC_BMP280_SIMPLE_H_

typedef uint32_t BMP280_U32_t;
typedef int32_t BMP280_S32_t;
typedef int64_t BMP280_S64_t;

static const uint8_t BMP280_ADDR = 0x77 << 1; // Use 8-bit address
// static const uint8_t BMP280_ADDR = 0x76 << 1; // Use 8-bit address

static const uint8_t BMP280_ID_REG = 0xD0;
static const uint8_t BMP280_ID_LEN = 1;
static const uint8_t BMP280_ID_VAL = 0x58;

static const uint8_t BMP280_CTRL_MEAS_REG = 0xF4;

static const uint8_t BMP280_PRES_REG_MSB = 0xF7;
static const uint8_t BMP280_PRES_LEN = 3;

static const uint8_t BMP280_TEMP_REG_MSB = 0xFA;
static const uint8_t BMP280_TEMP_LEN = 3;

static const uint8_t BMP280_TRIM_REG_MSB = 0x88;
static const uint8_t BMP280_TRIM_LEN = 12 * 2;



int BMP280_check();
int BMP280_init();
BMP280_S32_t BMP280_get_temperature();
int BMP280_get_pressure();
uint8_t* BMP280_Read_Reg(uint8_t reg, uint8_t value);
int BMP280_Write_Reg(uint8_t reg, uint8_t value);


#endif /* SRC_BMP280_H_ */
