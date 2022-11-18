from fastapi import FastAPI, Path
from uart import *
app = FastAPI(title="BUS_RESEAU_PELLEGRIN_RAMI", version="1.0.0")

temperatures = []
pressures = []

## TEMPERATURE

@app.get("/temp", tags=["TEMPERATURE"])
async def get_temperatures():
    return temperatures

@app.get("/temp/{x}", tags=["TEMPERATURE"])
async def get_temperature(x: int = Path(None,title="The index of the temperature", lt=len(temperatures), ge=-len(temperatures))):
    return temperatures[x]

@app.post("/temp", tags=["TEMPERATURE"])
async def add_temperature_mesure():
    temperature = fetch_temperature()
    temperatures.append(temperature)
    return 

@app.delete("/temp/{x}", tags=["TEMPERATURE"])
async def delete_temperature(x: int = Path(None,title="The index of the temperature", lt=len(temperatures), ge=-len(temperatures))):
    del temperatures[x]
    return

## PRESSURE
@app.get("/pressure", tags=["PRESSURE"])
async def get_pressures():
    return pressures

@app.get("/pressure/{x}", tags=["PRESSURE"])
async def get_pressure(x: int = Path(None,title="The index of the pressure", lt=len(pressures), ge=-len(pressures))):
    return pressures[x]

@app.post("/pressure", tags=["PRESSURE"])
async def add_pressure_mesure():
    pressure = fetch_pressure()
    pressures.append(pressure)
    return 

@app.delete("/pressure/{x}", tags=["PRESSURE"])
async def delete_pressure(x: int = Path(None,title="The index of the pressure", lt=len(pressures), ge=-len(pressures))):
    del pressures[x]
    return

##Scale

@app.get("/scale", tags=["SCALE"])
async def get_scale():
    scale = fetch_scale()
    return scale

@app.patch("/scale/x", tags=["SCALE"])
async def patch_scale(x: int):
    scale = update_scale(x)
    return scale

##Angle

@app.get("/angle", tags=["ANGLE"])
async def get_scale():
    angle = fetch_angle()
    return angle
